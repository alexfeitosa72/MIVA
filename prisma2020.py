"""
PRISMA 2020 Flow Diagram Generator
===================================
Gera o fluxograma PRISMA 2020 pronto para dissertacao em LaTeX.

Uso:
    python prisma2020.py                    modo interativo (prompt no terminal)
    python prisma2020.py --config vals.json carrega valores de um arquivo JSON
    python prisma2020.py --demo             roda com valores de exemplo

Saida:
    prisma_flow.svg   vetor para includegraphics no LaTeX
    prisma_flow.pdf   alternativa direta para pdflatex

Citacao sugerida (adicionar como nota na figura no LaTeX):
    Adaptado de Page et al. (2021). BMJ, 372, n71.
    https://doi.org/10.1136/bmj.n71. Licenca CC BY 4.0.
"""

import argparse
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


# ── Paleta ────────────────────────────────────────────────────────────────────
TEAL       = "#01696F"
TEAL_LIGHT = "#E6F3F3"
TEAL_MID   = "#B3D9DA"
TEAL_DARK  = "#004D52"
RED_LIGHT  = "#FDECEA"
RED_BORDER = "#C0392B"
GRAY_LIGHT = "#F7F6F2"
GRAY_MID   = "#D4D1CA"
GRAY_TEXT  = "#7A7974"
DARK       = "#28251D"
WHITE      = "#FFFFFF"


# ── Coleta interativa dos valores ─────────────────────────────────────────────
FIELDS = [
    # (chave, rótulo amigável, descrição)
    ("db_acl",           "ACL Anthology",            "Registros identificados — ACL Anthology (0 se não usou)"),
    ("db_scopus",        "Scopus",                   "Registros identificados — Scopus (0 se não usou)"),
    ("db_wos",           "Web of Science",           "Registros identificados — Web of Science (0 se não usou)"),
    ("db_sol",           "SOL",                      "Registros identificados — SOL (0 se não usou)"),
    ("db_acm-dl",        "ACM Digital Library",      "Registros identificados — ACM Digital Library (0 se não usou)"),
    ("db_other",         "Outras bases",             "Registros identificados — outras bases (soma; 0 se nenhuma)"),
    ("other_sources",    "Outras fontes",            "Registros via outras fontes (literatura cinza, listas de referências; 0 se nenhum)"),
    ("duplicates",       "Duplicatas removidas",     "Registros removidos como duplicatas"),
    ("auto_excluded",    "Excluídos por automação",  "Registros excluídos antes da triagem por ferramentas de automação (0 se não usou)"),
    ("screened",         "Triados (título/resumo)",  "Registros triados na etapa de título e resumo"),
    ("excluded_screen",  "Excluídos na triagem",     "Registros excluídos na triagem de título/resumo"),
    ("sought",           "Textos completos buscados","Relatórios buscados para recuperação (texto completo)"),
    ("not_retrieved",    "Não recuperados",          "Textos completos não recuperados"),
    ("assessed",         "Avaliados (elegibilidade)","Textos completos elegíveis"),
    ("excluded_ft",      "Excluídos (texto completo)","Textos completos excluídos (com motivo)"),
    ("included",         "INCLUÍDOS",                "Estudos incluídos no estudo"),
]

# Motivos de exclusão no texto completo (lista aberta)
EXCLUSION_REASONS_PROMPT = (
    "\nMotivos de exclusão no texto completo\n"
    "  (ex.: 'Não atende critérios PICO: 12' — deixe em branco para terminar)\n"
)


def ask_int(prompt: str, default: int = 0) -> int:
    while True:
        raw = input(f"  {prompt} [{default}]: ").strip()
        if raw == "":
            return default
        try:
            v = int(raw)
            if v < 0:
                print("    ⚠  Digite um número ≥ 0.")
                continue
            return v
        except ValueError:
            print("    ⚠  Digite um número inteiro.")


def collect_interactive() -> dict:
    print("\n" + "═" * 60)
    print("  PRISMA 2020 — Preenchimento do fluxograma")
    print("  (Enter = aceitar valor padrão [0])")
    print("═" * 60)

    data: dict = {}

    print("\n▶  IDENTIFICAÇÃO — Registros por base de dados")
    for key, label, desc in FIELDS[:6]:
        data[key] = ask_int(f"{label:30s}  ({desc})")

    print("\n▶  IDENTIFICAÇÃO — Outras fontes")
    for key, label, desc in FIELDS[6:7]:
        data[key] = ask_int(f"{label:30s}  ({desc})")

    print("\n▶  TRIAGEM")
    for key, label, desc in FIELDS[7:11]:
        data[key] = ask_int(f"{label:30s}  ({desc})")

    print("\n▶  ELEGIBILIDADE (texto completo)")
    for key, label, desc in FIELDS[11:15]:
        data[key] = ask_int(f"{label:30s}  ({desc})")

    # Motivos de exclusão
    print(EXCLUSION_REASONS_PROMPT)
    reasons = []
    while True:
        r = input("    Motivo (ou Enter para terminar): ").strip()
        if not r:
            break
        reasons.append(r)
    data["exclusion_reasons"] = reasons if reasons else ["Não atende critérios de elegibilidade"]

    print("\n▶  INCLUÍDOS")
    data["included"] = ask_int(
        f"{'INCLUÍDOS no estudo':30s}  (Estudos incluídos no estudo)"
    )

    # Bases usadas (para o rótulo do box de identificação)
    data["db_labels"] = _build_db_labels(data)
    return data


def _build_db_labels(data: dict) -> list[str]:
    mapping = [
        ("db_acl",  "ACL Anthology"),
        ("db_scopus",  "Scopus"),
        ("db_wos",     "Web of Science"),
        ("db_sol",  "SOL"),
        ("db_acm-dl",  "ACM Digital Library"),
        ("db_other",   "Outras"),
    ]
    lines = []
    for key, name in mapping:
        v = data.get(key, 0)
        if v > 0:
            lines.append(f"{name} (n = {v:,})")
    return lines


def demo_data() -> dict:
    """Valores de exemplo para testes."""
    d = {
        "db_acl":       423,
        "db_scopus":       318,
        "db_wos":          207,
        "db_sol":         0,
        "db_acm-dl":        89,
        "db_other":         41,
        "other_sources":    15,
        "duplicates":      312,
        "auto_excluded":     0,
        "screened":        781,
        "excluded_screen": 698,
        "sought":           83,
        "not_retrieved":     4,
        "assessed":         79,
        "excluded_ft":      51,
        "exclusion_reasons": [
            "Não atende critérios PICO (n = 23)",
            "Tipo de estudo inadequado (n = 14)",
            "Texto duplicado / extensão de outro (n = 9)",
            "Dados insuficientes para extração (n = 5)",
        ],
        "included":         28,
    }
    d["db_labels"] = _build_db_labels(d)
    return d


# ── Funções de desenho ────────────────────────────────────────────────────────

def _fancy_box(ax, x, y, w, h,
               text: str,
               facecolor: str = TEAL_LIGHT,
               edgecolor: str = TEAL,
               textcolor: str = DARK,
               fontsize: float = 8.5,
               bold: bool = False,
               linewidth: float = 1.2,
               radius: float = 0.015) -> None:
    box = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        facecolor=facecolor, edgecolor=edgecolor,
        linewidth=linewidth, zorder=3,
    )
    ax.add_patch(box)
    ax.text(
        x, y, text,
        ha="center", va="center",
        fontsize=fontsize,
        fontweight="bold" if bold else "normal",
        color=textcolor,
        wrap=True,
        multialignment="center",
        zorder=4,
    )


def _arrow(ax, x1, y1, x2, y2,
           color: str = GRAY_TEXT,
           lw: float = 1.0) -> None:
    ax.annotate(
        "",
        xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=lw,
            mutation_scale=10,
        ),
        zorder=2,
    )


def _horiz_arrow(ax, x1, y1, x2, y2,
                 color: str = GRAY_TEXT) -> None:
    ax.annotate(
        "",
        xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=0.9,
            mutation_scale=9,
            connectionstyle="arc3,rad=0.0",
        ),
        zorder=2,
    )


def _section_label(ax, x, y, text: str, fontsize: float = 7.5) -> None:
    ax.text(
        x, y, text,
        ha="center", va="center",
        fontsize=fontsize,
        fontweight="bold",
        color=WHITE,
        rotation=90,
        bbox=dict(
            boxstyle="round,pad=0.3",
            facecolor=TEAL_DARK,
            edgecolor="none",
            zorder=5,
        ),
        zorder=5,
    )


def _total_identified(data: dict) -> int:
    keys = ["db_acl", "db_scopus", "db_wos", "db_sol", "db_acm-dl", "db_other"]
    return sum(data.get(k, 0) for k in keys)


def _records_after_dedup(data: dict) -> int:
    total_identified = _total_identified(data) + data.get("other_sources", 0)
    removed = data.get("duplicates", 0) + data.get("auto_excluded", 0)
    return max(0, total_identified - removed)


def _records_screened(data: dict) -> int:
    return _records_after_dedup(data)


def _reports_sought(data: dict) -> int:
    screened = _records_screened(data)
    excluded_screen = data.get("excluded_screen", 0)
    return max(0, screened - excluded_screen)


def _reports_assessed(data: dict) -> int:
    sought = _reports_sought(data)
    not_retrieved = data.get("not_retrieved", 0)
    return max(0, sought - not_retrieved)


def _studies_included(data: dict) -> int:
    assessed = _reports_assessed(data)
    excluded_ft = data.get("excluded_ft", 0)
    return max(0, assessed - excluded_ft)


def build_diagram(data: dict, output_stem: str = "prisma_flow") -> list[Path]:
    """Renderiza o fluxograma e salva SVG + PDF. Retorna lista de paths."""

    total_db      = _total_identified(data)
    after_dedup   = _records_after_dedup(data)
    other_src     = data.get("other_sources", 0)
    duplicates    = data.get("duplicates", 0)
    auto_excl     = data.get("auto_excluded", 0)
    screened      = _records_screened(data)
    excl_screen   = data.get("excluded_screen", 0)
    sought        = _reports_sought(data)
    not_retr      = data.get("not_retrieved", 0)
    assessed      = _reports_assessed(data)
    excl_ft       = data.get("excluded_ft", 0)
    included      = _studies_included(data)
    reasons       = data.get("exclusion_reasons", [])
    db_labels     = data.get("db_labels", [])

    # ── Canvas ────────────────────────────────────────────────────────────────
    fig_w, fig_h = 7.4, 10.2
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.patch.set_facecolor(WHITE)

    # ── Geometria ─────────────────────────────────────────────────────────────
    # Colunas (centros x)
    SEC_X   = 0.070   # rótulo de seção (rotacionado)
    LEFT_X  = 0.365   # coluna principal
    RIGHT_X = 0.825   # coluna de exclusões

    # Larguras
    BOX_W_MAIN = 0.360
    BOX_W_EXCL = 0.275

    # Alturas (variáveis por conteúdo)
    H_STD   = 0.064
    H_STD_EXCL = 0.082
    H_TALL  = 0.078
    H_EXCL  = 0.050

    # Posições Y (de cima para baixo) — usa ~85% do canvas
    Y = {
        "title":       0.958,
        "id_db":       0.875,
        "id_other":    0.875,
        "dedup":       0.770,
        "dedup_excl":  0.770,
        "screen":      0.668,
        "screen_excl": 0.668,
        "sought":      0.565,
        "not_retr":    0.565,
        "assessed":    0.462,
        "ft_excl":     0.445,
        "included":    0.305,
    }

    # ── Título ────────────────────────────────────────────────────────────────
    ax.text(
        0.5, Y["title"],
        "Fluxograma de Seleção dos Estudos — PRISMA 2020",
        ha="center", va="center",
        fontsize=11, fontweight="bold", color=TEAL_DARK,
        zorder=5,
    )
    ax.plot([0.04, 0.96], [Y["title"] - 0.025, Y["title"] - 0.025],
            color=TEAL_MID, lw=0.8, zorder=2)

    # ── SEÇÃO: IDENTIFICAÇÃO ──────────────────────────────────────────────────
    _section_label(ax, SEC_X, 0.825, "IDENTIFICAÇÃO", fontsize=7)

    # Box bases de dados
    db_text_lines = [f"Registros identificados nas bases de dados"]
    if db_labels:
        db_text_lines += [f"  {l}" for l in db_labels]
    db_text_lines.append(f"Total: n = {total_db:,}")
    db_text = "\n".join(db_text_lines)
    h_db = H_STD + 0.012 * max(0, len(db_labels) - 1)
    _fancy_box(ax, LEFT_X, Y["id_db"], BOX_W_MAIN, h_db + 0.02,
               db_text, facecolor=TEAL_LIGHT, edgecolor=TEAL,
               fontsize=7.8)

    # Box outras fontes
    if other_src > 0:
        _fancy_box(ax, RIGHT_X, Y["id_other"], BOX_W_EXCL, H_STD_EXCL,
                   f"Identificados via outras fontes\n(literatura cinza, ref. manuais)\nn = {other_src:,}",
                   facecolor=TEAL_LIGHT, edgecolor=TEAL_MID,
               fontsize=7.0)
    else:
        ax.text(RIGHT_X, Y["id_other"], "(sem outras fontes)",
                ha="center", va="center", fontsize=7, color=GRAY_TEXT,
                style="italic")

    # Seta vertical: id_db → dedup
    _arrow(ax, LEFT_X, Y["id_db"] - (h_db + 0.02) / 2,
               LEFT_X, Y["dedup"]  + H_TALL / 2 + 0.005,
           color=TEAL)

    # ── SEÇÃO: TRIAGEM ────────────────────────────────────────────────────────
    _section_label(ax, SEC_X, 0.718, "TRIAGEM", fontsize=7)

    # Box remoção de duplicatas + automação
    dedup_lines = [f"Registros após remoção de duplicatas",
                   f"n = {after_dedup:,}"]
    rem_lines   = [f"Duplicatas removidas: n = {duplicates:,}"]
    if auto_excl > 0:
        rem_lines.append(f"Excluídos por automação: n = {auto_excl:,}")
    _fancy_box(ax, LEFT_X, Y["dedup"], BOX_W_MAIN, H_TALL,
               "\n".join(dedup_lines),
               facecolor=GRAY_LIGHT, edgecolor=GRAY_MID,
               fontsize=7.8)
    _fancy_box(ax, RIGHT_X, Y["dedup_excl"], BOX_W_EXCL, H_STD_EXCL,
               "\n".join(rem_lines),
               facecolor=RED_LIGHT, edgecolor=RED_BORDER,
               fontsize=7.2)
    _horiz_arrow(ax, LEFT_X + BOX_W_MAIN / 2, Y["dedup"],
                     RIGHT_X - BOX_W_EXCL / 2 - 0.005, Y["dedup_excl"])

    # Seta vertical: dedup → screen
    _arrow(ax, LEFT_X, Y["dedup"] - H_TALL / 2,
               LEFT_X, Y["screen"] + H_STD / 2 + 0.005,
           color=TEAL)

    # Box triagem título/resumo
    _fancy_box(ax, LEFT_X, Y["screen"], BOX_W_MAIN, H_STD,
               f"Registros triados (título e resumo)\nn = {screened:,}",
               facecolor=GRAY_LIGHT, edgecolor=GRAY_MID,
               fontsize=7.8)
    _fancy_box(ax, RIGHT_X, Y["screen_excl"], BOX_W_EXCL, H_STD_EXCL,
               f"Excluídos na triagem\nn = {excl_screen:,}",
               facecolor=RED_LIGHT, edgecolor=RED_BORDER,
               fontsize=7.2)
    _horiz_arrow(ax, LEFT_X + BOX_W_MAIN / 2, Y["screen"],
                     RIGHT_X - BOX_W_EXCL / 2 - 0.005, Y["screen_excl"])

    # Seta vertical: screen → sought
    _arrow(ax, LEFT_X, Y["screen"] - H_STD / 2,
               LEFT_X, Y["sought"] + H_STD / 2 + 0.005,
           color=TEAL)

    # ── SEÇÃO: ELEGIBILIDADE ──────────────────────────────────────────────────
    _section_label(ax, SEC_X, 0.513, "ELEGIBILIDADE", fontsize=7)

    # Box textos buscados
    _fancy_box(ax, LEFT_X, Y["sought"], BOX_W_MAIN, H_STD,
               f"Textos completos para recuperação\nn = {sought:,}",
               facecolor=GRAY_LIGHT, edgecolor=GRAY_MID,
               fontsize=7.8)

    if not_retr > 0:
        _fancy_box(ax, RIGHT_X, Y["not_retr"], BOX_W_EXCL, H_STD_EXCL,
                   f"Não recuperados\nn = {not_retr:,}",
                   facecolor=RED_LIGHT, edgecolor=RED_BORDER,
               fontsize=7.2)
        _horiz_arrow(ax, LEFT_X + BOX_W_MAIN / 2, Y["sought"],
                         RIGHT_X - BOX_W_EXCL / 2 - 0.005, Y["not_retr"])

    # Seta vertical: sought → assessed
    _arrow(ax, LEFT_X, Y["sought"] - H_STD / 2,
               LEFT_X, Y["assessed"] + H_STD / 2 + 0.005,
           color=TEAL)

    # Box avaliados
    _fancy_box(ax, LEFT_X, Y["assessed"], BOX_W_MAIN, H_STD,
               f"Textos completos elegíveis\nn = {assessed:,}",
               facecolor=GRAY_LIGHT, edgecolor=GRAY_MID,
               fontsize=7.8)

    # Box excluídos texto completo + motivos
    show_reasons = excl_ft > 0 and len(reasons) > 0
    reasons_str = "\n".join(f"  • {r}" for r in reasons) if show_reasons else ""
    ft_excl_text = f"Excluídos (texto completo)\nn = {excl_ft:,}"
    if show_reasons:
        ft_excl_text += f"\n{reasons_str}"
    n_reason_lines = len(reasons) if show_reasons else 0
    h_excl = H_STD_EXCL + 0.018 * max(0, n_reason_lines)
    excl_center_y = Y["assessed"]

    _fancy_box(ax, RIGHT_X, excl_center_y, BOX_W_EXCL, h_excl,
               ft_excl_text,
               facecolor=RED_LIGHT, edgecolor=RED_BORDER,
               fontsize=7.0)
    _horiz_arrow(ax, LEFT_X + BOX_W_MAIN / 2, Y["assessed"],
                     RIGHT_X - BOX_W_EXCL / 2 - 0.005, excl_center_y)

    # Seta vertical: assessed → included
    _arrow(ax, LEFT_X, Y["assessed"] - H_STD / 2,
               LEFT_X, Y["included"] + H_TALL / 2 + 0.005,
           color=TEAL)

    # ── SEÇÃO: INCLUÍDOS ──────────────────────────────────────────────────────
    _section_label(ax, SEC_X, 0.305, "INCLUÍDOS", fontsize=7)

    _fancy_box(ax, LEFT_X, Y["included"], BOX_W_MAIN + 0.02, H_TALL,
               f"Estudos incluídos no estudo\n\nn = {included:,}",
               facecolor=TEAL, edgecolor=TEAL_DARK,
               textcolor=WHITE,
               fontsize=9.5, bold=True,
               linewidth=2.0)

    # ── Nota de rodapé / citação ──────────────────────────────────────────────
    citation = (
        "Adaptado de: Page MJ, et al. PRISMA 2020 statement. BMJ 2021;372:n71. "
        "https://doi.org/10.1136/bmj.n71 · Licença CC BY 4.0"
    )
    ax.text(
        0.5, 0.018, citation,
        ha="center", va="bottom",
        fontsize=6.0, color=GRAY_TEXT,
        style="italic",
        zorder=4,
    )
    ax.plot([0.04, 0.96], [0.032, 0.032], color=GRAY_MID, lw=0.5, zorder=2)

    fig.subplots_adjust(left=0.08, right=0.98, top=0.975, bottom=0.08)

    # ── Exportação ────────────────────────────────────────────────────────────
    out_svg = Path(output_stem).with_suffix(".svg")
    out_pdf = Path(output_stem).with_suffix(".pdf")

    fig.savefig(out_svg, format="svg", bbox_inches="tight", dpi=300)
    fig.savefig(out_pdf, format="pdf", bbox_inches="tight", dpi=300)
    plt.close(fig)

    return [out_svg, out_pdf]


# ── Verificação de consistência aritmética ────────────────────────────────────

def _check_consistency(data: dict) -> list[str]:
    total_db    = _total_identified(data)
    other_src   = data.get("other_sources", 0)
    duplicates  = data.get("duplicates", 0)
    auto_excl   = data.get("auto_excluded", 0)
    screened    = data.get("screened", 0)
    excl_screen = data.get("excluded_screen", 0)
    sought      = data.get("sought", 0)
    not_retr    = data.get("not_retrieved", 0)
    assessed    = data.get("assessed", 0)
    excl_ft     = data.get("excluded_ft", 0)
    included    = data.get("included", 0)

    warns = []

    total_identified = total_db + other_src
    expected_screened = _records_screened(data)
    if screened != expected_screened:
        warns.append(
            f"Triagem informada ({screened}) difere do valor derivado "
            f"({expected_screened}) a partir de Identificados ({total_identified}) "
            f"− Removidos ({duplicates + auto_excl})"
        )

    expected_sought = _reports_sought(data)
    if sought != expected_sought:
        warns.append(
            f"Buscados informados ({sought}) difere do valor derivado "
            f"({expected_sought}) a partir de Triados ({expected_screened}) "
            f"− Excluídos triagem ({excl_screen})"
        )

    expected_assessed = _reports_assessed(data)
    if assessed != expected_assessed:
        warns.append(
            f"Avaliados informados ({assessed}) difere do valor derivado ({expected_assessed}) "
            f"a partir de Buscados derivados ({expected_sought}) − Não recuperados "
            f"({not_retr}) = {expected_assessed}"
        )

    expected_included = _studies_included(data)
    if included != expected_included:
        warns.append(
            f"Incluídos informados ({included}) difere do valor derivado ({expected_included}) "
            f"a partir de Avaliados derivados ({expected_assessed}) − Excluídos FT "
            f"({excl_ft}) = {expected_included}"
        )

    return warns


def print_consistency_report(data: dict) -> None:
    warns = _check_consistency(data)
    print("\n" + "═" * 60)
    if warns:
        print("  ⚠  ATENÇÃO — inconsistências detectadas:")
        for w in warns:
            print(f"      • {w}")
    else:
        print("  ✓  Consistência aritmética OK — todos os n's fecham.")
    print("═" * 60)


# ── Entrada via JSON ──────────────────────────────────────────────────────────

def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    data["db_labels"] = _build_db_labels(data)
    return data


def save_json(data: dict, path: str) -> None:
    """Salva os valores preenchidos para reutilização."""
    out = {k: v for k, v in data.items() if k != "db_labels"}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"  💾  Valores salvos em: {path}")


# ── Bloco de snippet LaTeX ─────────────────────────────────────────────────────

LATEX_SNIPPET = r"""
% ─────────────────────────────────────────────────────────────────────────────
% Insira no preâmbulo do seu .tex (se ainda não tiver):
%   \usepackage{graphicx}
%   \usepackage[hidelinks]{hyperref}
%
% Coloque prisma_flow.pdf (ou .svg compilado) na mesma pasta do .tex.
% ─────────────────────────────────────────────────────────────────────────────

\begin{figure}[htbp]
  \centering
  \includegraphics[width=\textwidth]{prisma_flow}   % sem extensão: pdflatex usa .pdf
  \caption{Fluxograma de seleção dos estudos segundo o PRISMA~2020.}
  \label{fig:prisma-flow}
  \footnotesize\textit{Adaptado de: Page MJ, McKenzie JE, Bossuyt PM et al.
    The PRISMA~2020 statement: an updated guideline for reporting systematic reviews.
    \textit{BMJ} 2021;372:n71.
    \href{https://doi.org/10.1136/bmj.n71}{https://doi.org/10.1136/bmj.n71}.
    Licença CC~BY~4.0.}
\end{figure}

% No texto, referencie com:
%   conforme apresentado na Figura~\ref{fig:prisma-flow}
"""


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gerador de fluxograma PRISMA 2020 — dissertação em LaTeX"
    )
    parser.add_argument("--demo",   action="store_true", help="Usa valores de demonstração")
    parser.add_argument("--config", metavar="JSON", help="Carrega valores de um .json")
    parser.add_argument("--output", default="prisma_flow", help="Prefixo do arquivo de saída")
    args = parser.parse_args()

    if args.demo:
        data = demo_data()
        print("\n  Modo DEMO — usando valores de exemplo.")
    elif args.config:
        data = load_json(args.config)
        print(f"\n  Valores carregados de: {args.config}")
    else:
        data = collect_interactive()
        save_path = Path(args.output).parent / "prisma_values.json"
        save_json(data, str(save_path))

    print_consistency_report(data)

    print("\n  Gerando diagrama…")
    paths = build_diagram(data, output_stem=args.output)

    print("\n" + "═" * 60)
    print("  ✓  Arquivos gerados:")
    for p in paths:
        print(f"      {p.resolve()}")
    print("\n  📋  Snippet LaTeX para incluir na dissertação:")
    print(LATEX_SNIPPET)
    print("═" * 60)


if __name__ == "__main__":
    main()
