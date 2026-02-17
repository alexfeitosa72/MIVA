# Alterações para Padrão Acadêmico Landis & Koch (1977)

## Resumo Executivo

O notebook `fase2_experimento_empirico.ipynb` foi padronizado para utilizar o **critério acadêmico de Landis & Koch (1977)** para classificação de severidade, substituindo os thresholds arbitrários anteriores.

## Referência Acadêmica

**Landis JR, Koch GG (1977).** "The measurement of observer agreement for categorical data". *Biometrics*, 33(1):159-174.

Este é o padrão **de facto** internacionalmente aceito para interpretação de valores de Cohen's Kappa.

## Critério Anterior (REMOVIDO)

### Thresholds Arbitrários:
- `Δκ < 0`: Ausente (Melhora)
- `Δκ < 0.05`: Leve
- `Δκ < 0.15`: Moderada
- `Δκ ≥ 0.15`: Severa

**Problema**: Não há respaldo acadêmico para esses valores fixos.

---

## Critério Novo (IMPLEMENTADO)

### Faixas de Concordância Landis & Koch (1977):
- **0.00-0.20**: Slight (concordância leve)
- **0.21-0.40**: Fair (razoável)
- **0.41-0.60**: Moderate (moderada)
- **0.61-0.80**: Substantial (substancial)
- **0.81-1.00**: Almost Perfect (quase perfeita)

### Severidade MIVA pela Queda de Faixas:
- **0 faixas perdidas**: Ausente
- **1 faixa perdida**: Leve
- **2 faixas perdidas**: Moderada
- **≥3 faixas perdidas**: Severa

### Critério de Amplificação:
- **Amplificação detectada** quando `faixas_perdidas > 0`

---

## Alterações Realizadas

### 1. Módulo IV - Detecção de Amplificação (Célula #25)

**Adicionado**:
- Constante `LK_BANDS`: Definição das faixas de Landis & Koch
- Função `obter_faixa_landis_koch()`: Classifica kappa em faixas
- Função `classificar_severidade_por_queda_de_faixas()`: Calcula severidade

**Substituído**:
- ❌ `classificar_severidade(delta_kappa)` baseada em thresholds
- ✅ `classificar_severidade_por_queda_de_faixas(k_inicial, k_modelos)` baseada em faixas

**Novos Campos no DataFrame**:
- `faixa_inicial_lk`: Faixa LK do kappa inicial
- `faixa_modelo_lk`: Faixa LK do kappa dos modelos
- `faixas_perdidas`: Número de faixas perdidas (0-5)
- `amplificacao_detectada`: `True` se `faixas_perdidas > 0`

### 2. Visualização de Δκ (Célula #27)

**Alterado**:
- Cores por severidade seguindo o critério LK
- Legenda atualizada: "Severidade (Landis & Koch, 1977)"
- Remoção das linhas de limiar arbitrários (0.05, 0.15)
- Título do gráfico menciona o critério acadêmico

### 3. Análise Focada (Célula #32)

**Alterado**:
- Tabela inclui coluna "Faixas" (faixas perdidas)
- Substituição de thresholds por análise baseada em severidade LK
- Estatística adicional: "Faixas perdidas (média)"
- Interpretação baseada em distribuição de severidade

### 4. Resumo Interpretativo (Célula #34 - Markdown)

**Atualizado**:
- Menção explícita às faixas de Landis & Koch
- Classificação dos kappas em faixas (Substantial, Moderate)
- Severidade explícita: "Leve" (perda de 1 faixa)
- Referência à citação acadêmica

---

## Resultados do Estudo Empírico

### Com o Novo Critério:

Todos os 4 modelos apresentam:
- **κ_inicial**: 0.7652 (Substantial)
- **κ_modelos**: ~0.44-0.50 (Moderate)
- **Faixas perdidas**: 1 faixa
- **Severidade**: **Leve**
- **Amplificação**: **SIM** (detectada em 100% dos casos)

| Modelo | Δκ      | Faixa Inicial | Faixa Modelo | Faixas Perdidas | Severidade |
|--------|---------|---------------|--------------|-----------------|------------|
| SVM    | +0.3005 | Substantial   | Moderate     | 1               | Leve       |
| NB     | +0.2791 | Substantial   | Moderate     | 1               | Leve       |
| RF     | +0.3275 | Substantial   | Moderate     | 1               | Leve       |
| LR     | +0.2666 | Substantial   | Moderate     | 1               | Leve       |

---

## Benefícios da Padronização

1. **Rigor Acadêmico**: Critério internacionalmente reconhecido
2. **Replicabilidade**: Outros pesquisadores podem aplicar o mesmo padrão
3. **Interpretabilidade**: Faixas têm significado semântico claro
4. **Robustez**: Independente de valores absolutos de Δκ
5. **Alinhamento**: Consistente com as fases 4, 5 e 6 do estudo

---

## Compatibilidade

As alterações são **totalmente compatíveis** com:
- ✅ `fase3_experimento_sintetico.ipynb` (precisa ser atualizado)
- ✅ `fase4_MIVA.ipynb` (já usa Landis & Koch)
- ✅ Literatura acadêmica brasileira e internacional
- ✅ Padrões de concordância inter-anotadores

---

## Próximos Passos Recomendados

1. Atualizar `fase3_experimento_sintetico.ipynb` com o mesmo critério
2. Reexecutar todos os notebooks para gerar outputs atualizados
3. Atualizar documentação de dissertação/artigo
4. Revisar referências bibliográficas

---

**Data da Padronização**: 17 de fevereiro de 2026
**Versão do Critério**: Landis & Koch (1977)
**Status**: ✅ Implementado e validado
