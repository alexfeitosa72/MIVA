"""
Verificação independente dos resultados do Random Forest nos datasets sintéticos.
Replica exatamente os parâmetros do fase3_dados_sinteticos.ipynb:
  - TF-IDF: max_features=10000, ngram_range=(1,3), min_df=3
  - RF: n_estimators=100, random_state=42, n_jobs=-1
  - CV: StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
  - Dois modelos independentes por fold (masculino / feminino), κ entre predições
"""

import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import cohen_kappa_score

SEED = 42
N_FOLDS = 5
DATA_DIR = r"b:\TechLab\MIVA\data\sinteticos"
RESULTADOS_ORIGINAIS = r"b:\TechLab\MIVA\data\resultados_sinteticos\kappa_todos_classificadores.csv"

DATASETS = [
    ("SynSA-99",  99),
    ("SynSA-97",  97),
    ("SynSA-95",  95),
    ("SynSA-90",  90),
    ("SynSA-85",  85),
    ("SynSA-80",  80),
    ("SynSA-75",  75),
    ("SynSA-70",  70),
    ("SynSA-65",  65),
    ("SynSA-60",  60),
    ("SynSA-55",  55),
    ("SynSA-50",  50),
]

LANDIS_KOCH = [
    (0.00, "Slight"),
    (0.20, "Fair"),
    (0.40, "Moderate"),
    (0.60, "Substantial"),
    (0.80, "Almost Perfect"),
]

def faixa_lk(kappa):
    faixa = "Slight"
    for limiar, nome in LANDIS_KOCH:
        if kappa > limiar:
            faixa = nome
    return faixa

def n_faixas_queda(kappa_orig, kappa_modelo):
    ordem = ["Slight", "Fair", "Moderate", "Substantial", "Almost Perfect"]
    fi = ordem.index(faixa_lk(kappa_orig))
    fm = ordem.index(faixa_lk(kappa_modelo))
    return max(0, fi - fm)

def severidade(n_faixas):
    if n_faixas == 0: return "Ausente"
    if n_faixas == 1: return "Leve"
    if n_faixas == 2: return "Moderada"
    return "Severa"

def rodar_rf(df):
    tfidf = TfidfVectorizer(max_features=10000, ngram_range=(1, 3), min_df=3)
    X = tfidf.fit_transform(df["texto"]).toarray()

    y_masc = df["rotulo_masculino"].values
    y_fem  = df["rotulo_feminino"].values
    kappa_orig = cohen_kappa_score(y_masc, y_fem)

    cv = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
    all_pred_masc = np.empty(len(df), dtype=object)
    all_pred_fem  = np.empty(len(df), dtype=object)
    kappas_folds  = []

    for train_idx, test_idx in cv.split(X, y_masc):
        rf_masc = RandomForestClassifier(n_estimators=100, random_state=SEED, n_jobs=-1)
        rf_fem  = RandomForestClassifier(n_estimators=100, random_state=SEED, n_jobs=-1)

        rf_masc.fit(X[train_idx], y_masc[train_idx])
        rf_fem.fit(X[train_idx],  y_fem[train_idx])

        pred_masc = rf_masc.predict(X[test_idx])
        pred_fem  = rf_fem.predict(X[test_idx])

        all_pred_masc[test_idx] = pred_masc
        all_pred_fem[test_idx]  = pred_fem
        kappas_folds.append(cohen_kappa_score(pred_masc, pred_fem))

    kappa_modelo = float(np.mean(kappas_folds))
    kappa_global = cohen_kappa_score(all_pred_masc, all_pred_fem)
    delta = kappa_orig - kappa_modelo
    n_q   = n_faixas_queda(kappa_orig, kappa_modelo)
    sev   = severidade(n_q)

    return {
        "kappa_orig":    round(kappa_orig, 4),
        "kappa_rf_fold": round(kappa_modelo, 4),
        "kappa_rf_glob": round(kappa_global, 4),
        "delta_kappa":   round(delta, 4),
        "faixa_orig":    faixa_lk(kappa_orig),
        "faixa_rf":      faixa_lk(kappa_modelo),
        "n_faixas":      n_q,
        "severidade":    sev,
    }

# ── Carrega originais para comparação ──────────────────────────────────────────
orig = pd.read_csv(RESULTADOS_ORIGINAIS, index_col=0)

print("=" * 90)
print(f"{'Dataset':<12} {'k_orig':>8} {'k_RF_orig':>11} {'k_RF_novo':>11} {'Dk_orig':>9} "
      f"{'Dk_novo':>9} {'Sev_orig':>10} {'Sev_nova':>10} {'OK?':>5}")
print("-" * 90)

resultados = []
for nome, nivel in DATASETS:
    path = os.path.join(DATA_DIR, f"{nome}.csv")
    df = pd.read_csv(path)

    res = rodar_rf(df)

    # Valores originais da tabela salva
    row_orig = orig.loc[nome]
    kappa_rf_orig  = round(float(row_orig["RF κ"]), 4)
    kappa_base     = round(float(row_orig["Originais κ"]), 4)

    delta_orig = round(kappa_base - kappa_rf_orig, 4)
    delta_novo = res["delta_kappa"]
    bate = abs(res["kappa_rf_fold"] - kappa_rf_orig) < 0.005

    print(f"{nome:<12} {kappa_base:>8.4f} {kappa_rf_orig:>11.4f} {res['kappa_rf_fold']:>11.4f} "
          f"{delta_orig:>9.4f} {delta_novo:>9.4f} {row_orig['RF Faixa']:>10} "
          f"{res['faixa_rf']:>10} {'OK' if bate else 'DIFF':>5}")

    resultados.append({
        "dataset":           nome,
        "concordancia_alvo": nivel,
        "kappa_orig":        res["kappa_orig"],
        "kappa_rf_orig":     kappa_rf_orig,
        "kappa_rf_novo":     res["kappa_rf_fold"],
        "kappa_rf_global":   res["kappa_rf_glob"],
        "delta_orig":        delta_orig,
        "delta_novo":        delta_novo,
        "n_faixas_queda":    res["n_faixas"],
        "severidade":        res["severidade"],
        "bate": bate,
    })

print("=" * 90)

df_res = pd.DataFrame(resultados)
confirmados = df_res["bate"].sum()
print(f"\nResultados confirmados: {confirmados}/{len(df_res)}")

desvio_medio = (df_res["delta_orig"] - df_res["delta_novo"]).abs().mean()
print(f"Desvio medio |dk_orig - dk_novo|: {desvio_medio:.4f}")

df_res.to_csv(r"b:\TechLab\MIVA\data\resultados_sinteticos\verificacao_rf_independente.csv", index=False)
print("\nTabela salva em data/resultados_sinteticos/verificacao_rf_independente.csv")
