import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import textwrap

# =========================
# DADOS DO ESTUDO
# =========================
dados = {
    "bases": 96,
    "outras_fontes": 66,
    "duplicados": 2,
    "outros_removidos": 0,
    "triados": 160,
    "excluidos_titulo_resumo": 62,
    "buscados": 98,
    "nao_recuperados": 0,
    "avaliados": 98,
    "excluidos_elegibilidade": {
        "Fora do escopo": 19,
        "Sem relação direta com viés/anotação": 11,
        "Sem experimento empírico": 0,
        "Duplicidade temática": 10,
    },
    "incluidos": 58
}

# =========================
# CONFIGURAÇÃO VISUAL
# =========================
plt.rcParams["font.family"] = "DejaVu Serif"
plt.rcParams["font.size"] = 8.5

fig, ax = plt.subplots(figsize=(7.2, 10.2))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")

BOX_FACE = "#F8F8F8"
BOX_EDGE = "#1F1F1F"
HEADER_FACE = "#EDEDED"
PHASE_FACE = "#E6E6E6"

# =========================
# FUNÇÕES AUXILIARES
# =========================
def wrap_text(texto, width=44):
    linhas = []
    for linha in texto.split("\n"):
        if linha.strip():
            linhas.extend(textwrap.wrap(linha, width=width))
        else:
            linhas.append("")
    return "\n".join(linhas)


def caixa(x, y, w, h, texto, fontsize=8.2, face=BOX_FACE, bold=False, wrap=44):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.35,rounding_size=0.8",
        linewidth=0.9,
        edgecolor=BOX_EDGE,
        facecolor=face
    )
    ax.add_patch(patch)

    ax.text(
        x + w / 2,
        y + h / 2,
        wrap_text(texto, wrap),
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight="bold" if bold else "normal",
        linespacing=1.18
    )


def fase_lateral(y, h, texto):
    patch = FancyBboxPatch(
        (4, y), 17, h,
        boxstyle="round,pad=0.18,rounding_size=0.5",
        linewidth=0.8,
        edgecolor=BOX_EDGE,
        facecolor=PHASE_FACE
    )
    ax.add_patch(patch)

    ax.text(
        12.5,
        y + h / 2,
        texto,
        ha="center",
        va="center",
        fontsize=7.2,
        fontweight="bold"
    )


def seta(x1, y1, x2, y2):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="-|>",
            mutation_scale=10,
            linewidth=0.9,
            color=BOX_EDGE
        )
    )

# =========================
# TÍTULO
# =========================
ax.text(
    58,
    97,
    "Diagrama de fluxo PRISMA 2020",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold"
)

ax.text(
    58,
    94.5,
    "Processo de identificação, triagem, elegibilidade e inclusão dos estudos",
    ha="center",
    va="center",
    fontsize=8.2
)

# =========================
# POSIÇÃO DAS CAIXAS
# =========================
x_main = 27
w_main = 60
x_center = x_main + w_main / 2

# =========================
# FASES LATERAIS
# =========================
fase_lateral(76, 17, "Identificação")
fase_lateral(54, 17.5, "Triagem")
fase_lateral(33, 17.5, "Recuperação")
fase_lateral(8, 21, "Elegibilidade")
fase_lateral(0.5, 5.5, "Inclusão")

# =========================
# IDENTIFICAÇÃO
# =========================
total_identificados = dados["bases"] + dados["outras_fontes"]

caixa(
    x_main,
    86,
    w_main,
    7,
    f"Registros identificados em bases de dados e outras fontes "
    f"(n = {total_identificados})",
    bold=True
)

caixa(
    x_main,
    76,
    w_main,
    8.5,
    "Registros removidos antes da triagem:\n"
    f"Duplicados removidos (n = {dados['duplicados']})\n"
    f"Outros registros removidos (n = {dados['outros_removidos']})"
)

# =========================
# TRIAGEM
# =========================
caixa(
    x_main,
    64,
    w_main,
    7.5,
    f"Registros triados por título e resumo (n = {dados['triados']})",
    bold=True
)

caixa(
    x_main,
    54,
    w_main,
    7.5,
    f"Registros excluídos após leitura de título e resumo "
    f"(n = {dados['excluidos_titulo_resumo']})"
)

# =========================
# RECUPERAÇÃO
# =========================
caixa(
    x_main,
    43,
    w_main,
    7.5,
    f"Artigos buscados para recuperação do texto completo "
    f"(n = {dados['buscados']})",
    bold=True
)

caixa(
    x_main,
    33,
    w_main,
    7.5,
    f"Artigos não recuperados "
    f"(n = {dados['nao_recuperados']})"
)

# =========================
# ELEGIBILIDADE
# =========================
caixa(
    x_main,
    22,
    w_main,
    7.5,
    f"Artigos avaliados para elegibilidade "
    f"(n = {dados['avaliados']})",
    bold=True
)

motivos = "\n".join(
    [f"{motivo} (n = {valor})"
     for motivo, valor in dados["excluidos_elegibilidade"].items()]
)

caixa(
    x_main,
    8,
    w_main,
    11,
    "Artigos excluídos, com justificativa:\n" + motivos,
    fontsize=7.6,
    wrap=50
)

# =========================
# INCLUSÃO
# =========================
caixa(
    x_main,
    0.5,
    w_main,
    5.5,
    f"Estudos incluídos na revisão (n = {dados['incluidos']})",
    face=HEADER_FACE,
    bold=True
)

# =========================
# SETAS
# =========================
seta(x_center, 86, x_center, 84.5)
seta(x_center, 76, x_center, 71.5)

seta(x_center, 64, x_center, 61.5)
seta(x_center, 54, x_center, 50.5)

seta(x_center, 43, x_center, 40.5)
seta(x_center, 33, x_center, 29.5)

seta(x_center, 22, x_center, 19)
seta(x_center, 8, x_center, 6)

# =========================
# EXPORTAÇÃO
# =========================
plt.savefig("prisma_2020_dissertacao.pdf", bbox_inches="tight")
plt.savefig("prisma_2020_dissertacao.png", dpi=300, bbox_inches="tight")
plt.savefig("prisma_2020_dissertacao.svg", bbox_inches="tight")

plt.show()