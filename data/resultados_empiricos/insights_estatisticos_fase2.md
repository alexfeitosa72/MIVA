# Principais Insights Estatísticos — MADA Fase 2

**Data de geração:** 12/07/2026 11:01:32

## 1) Baseline entre anotadores
- **Cohen's Kappa inicial:** `0.7664`
- **IC 95% do Kappa (bootstrap):** `[0.7363, 0.7954]`
- **Concordância observada:** `0.8453` (84.53%)
- **Cramér's V:** `0.7679`

> Interpretação: há concordância inicial relativamente alta entre os grupos de anotadores.

## 2) Concordância entre modelos pareados
- **Média de κ_pred (4 classificadores):** `0.4904`
- **Melhor κ_pred:** `LR` com `0.5140`
- **Pior κ_pred:** `NB` com `0.4680`

## 3) Amplificação de viés (Δκ = κ_anot - κ_pred)
- **Δκ médio:** `+0.2760`
- **Maior amplificação:** `NB` com `Δκ=+0.2984`
- **Menor amplificação:** `LR` com `Δκ=+0.2524`
- **Modelos com amplificação detectada:** `4/4`

### Severidade (Landis & Koch, 1977)
- **Nulo:** 0 modelo(s)
- **Restrito:** 4 modelo(s)
- **Amplo:** 0 modelo(s)
- **Acentuado:** 0 modelo(s)

## 4) Significância estatística (bootstrap de Δκ)
- **Modelos com Δκ estatisticamente significativo:** `4/4`
  - SVM: Δκ observado `+0.2888`, IC95% `[+0.2476, +0.3248]`, direção: **AMPLIFICA**
  - NB: Δκ observado `+0.2984`, IC95% `[+0.2638, +0.3373]`, direção: **AMPLIFICA**
  - RF: Δκ observado `+0.2645`, IC95% `[+0.2232, +0.3029]`, direção: **AMPLIFICA**
  - LR: Δκ observado `+0.2524`, IC95% `[+0.2159, +0.2903]`, direção: **AMPLIFICA**

## 5) Conclusão executiva
- Os classificadores reproduzem padrões com **menor concordância inter-grupos** do que a observada entre anotadores humanos.
- Houve **amplificação de viés em todos os modelos testados** nesta configuração experimental.
- A queda de faixa de concordância foi predominantemente **Restrito** (1 faixa em Landis & Koch), mas consistente.

---
Arquivo gerado automaticamente em: `data\resultados_empiricos\insights_estatisticos_fase2.md`