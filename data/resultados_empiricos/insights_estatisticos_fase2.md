# Principais Insights Estatísticos — MADA Fase 2

**Data de geração:** 08/04/2026 13:44:34

## 1) Baseline entre anotadores
- **Cohen's Kappa inicial:** `0.7664`
- **IC 95% do Kappa (bootstrap):** `[0.7363, 0.7954]`
- **Concordância observada:** `0.8453` (84.53%)
- **Cramér's V:** `0.7679`

> Interpretação: há concordância inicial relativamente alta entre os grupos de anotadores.

## 2) Concordância entre modelos pareados
- **Média de κ_modelos (4 classificadores):** `0.4877`
- **Melhor κ_modelos:** `LR` com `0.5120`
- **Pior κ_modelos:** `NB` com `0.4582`

## 3) Amplificação de viés (Δκ = κ_inicial - κ_modelos)
- **Δκ médio:** `+0.2787`
- **Maior amplificação:** `NB` com `Δκ=+0.3082`
- **Menor amplificação:** `LR` com `Δκ=+0.2544`
- **Modelos com amplificação detectada:** `4/4`

### Severidade (Landis & Koch, 1977)
- **Ausente:** 0 modelo(s)
- **Leve:** 4 modelo(s)
- **Moderada:** 0 modelo(s)
- **Severa:** 0 modelo(s)

## 4) Significância estatística (bootstrap de Δκ)
- **Modelos com Δκ estatisticamente significativo:** `4/4`
  - SVM: Δκ observado `+0.2720`, IC95% `[+0.2335, +0.3095]`, direção: **AMPLIFICA**
  - NB: Δκ observado `+0.3082`, IC95% `[+0.2710, +0.3436]`, direção: **AMPLIFICA**
  - RF: Δκ observado `+0.2801`, IC95% `[+0.2375, +0.3179]`, direção: **AMPLIFICA**
  - LR: Δκ observado `+0.2544`, IC95% `[+0.2175, +0.2900]`, direção: **AMPLIFICA**

## 5) Conclusão executiva
- Os classificadores reproduzem padrões com **menor concordância inter-grupos** do que a observada entre anotadores humanos.
- Houve **amplificação de viés em todos os modelos testados** nesta configuração experimental.
- A queda de faixa de concordância foi predominantemente **leve** (1 faixa em Landis & Koch), mas consistente.

---
Arquivo gerado automaticamente em: `data\resultados_empiricos\insights_estatisticos_fase2.md`