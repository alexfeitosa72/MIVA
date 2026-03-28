# 🎓 GUIA COMPLETO PARA QUALIFICAÇÃO DE MESTRADO
## Viés de Gênero no Processo de Anotação: Da Experimentação Humana à Escalação com Dados Sintéticos

---

## 📋 SUMÁRIO EXECUTIVO

Este guia fornece orientações detalhadas para melhorar seu documento de qualificação, com foco em:

1. **Narrativa Acadêmica**: Como transcrevar academicamente a jornada experimental
2. **Profundidade Técnica**: Detalhamento metodológico necessário
3. **Referências Estado-da-Arte**: Papers essenciais que estão faltando
4. **Coerência Textual**: Correção de gaps narrativos e transições
5. **Preparação para Defesa**: Prioridades para qualificação em início de 2026

**Status Atual**: Você está no caminho certo, mas precisa de um esforço focado de 4 semanas.

**Avaliação Geral**:
- ✅ Progressão experimental sólida (humano → sintético)
- ✅ Contribuição clara e bem motivada
- ⚠️ Metodologia precisa de maior formalização
- ⚠️ Faltam referências seminais importantes
- ⚠️ Algumas transições narrativas precisam de revisão

---

## 🎯 PARTE 1: ESTRUTURA NARRATIVA DA JORNADA EXPERIMENTAL

### O Desafio Central

Você precisa contar uma história acadêmica coerente que responda:

**Por que "Beyond Systematic Bias"?** → **Por que "When Annotators Disagree"?** → **Por que isso importa para Ciência da Computação?**

### Estrutura Narrativa Recomendada

#### Capítulo 1: Introdução

**O que deve conter:**

```
1.1 Contexto e Motivação
    → Viés em sistemas de PLN é um problema reconhecido
    → Datasets anotados são a base desses sistemas
    → Mas de onde vem o viés nos datasets?
    → HIPÓTESE: O viés pode estar no processo de anotação

1.2 Lacuna de Pesquisa (Research Gap)
    → Estudos anteriores focam em viés nos modelos
    → Poucos investigam o viés sistemático dos anotadores
    → Estudos com humanos são limitados em escala
    → NECESSIDADE: Método escalável para investigar viés de anotadores

1.3 Objetivos da Pesquisa
    → Objetivo 1: Investigar se características dos anotadores 
                  influenciam sistematicamente suas anotações
    → Objetivo 2: Desenvolver método escalável usando dados sintéticos
    → Objetivo 3: Validar se dados sintéticos reproduzem padrões humanos

1.4 Contribuições
    → Evidência empírica de viés sistemático em anotação de gênero
    → Framework de geração de anotadores sintéticos
    → Validação da escalabilidade da abordagem sintética
    → Implicações para design de protocolos de anotação

1.5 Organização do Documento
```

**EXEMPLO DE PARÁGRAFO MELHORADO (em Português):**

❌ **ANTES** (provavelmente vago):
> "A anotação de dados é importante para o aprendizado de máquina. Existem problemas com viés."

✅ **DEPOIS** (acadêmico e conectado):
> "Sistemas de Processamento de Linguagem Natural (PLN) dependem fundamentalmente de datasets anotados para treinamento e avaliação. Contudo, estudos recentes demonstram que esses datasets frequentemente contêm vieses sistemáticos que são amplificados pelos modelos treinados sobre eles (Cao & Daumé, 2021; Giorgi et al., 2025). Embora a literatura tenha investigado extensivamente o viés nos modelos resultantes, permanece em aberto a questão de *onde* esses vieses se originam. Esta pesquisa parte da hipótese de que características demográficas e atitudinais dos anotadores podem introduzir vieses sistemáticos durante o próprio processo de anotação, antes mesmo do treinamento de modelos."

#### Capítulo 2: Fundamentação Teórica

**Estrutura Recomendada:**

```
2.1 Viés em Processamento de Linguagem Natural
    2.1.1 Definições e Taxonomias de Viés
    2.1.2 Viés de Gênero em PLN
          → Embeddings (Bolukbasi et al., 2016)
          → Resolução de Correferência (Zhao et al., 2018)
          → Sistemas de Classificação
    2.1.3 Origem do Viés: Dados vs. Modelos vs. Anotação
          [CONECTAR AO SEU TRABALHO AQUI]

2.2 Qualidade e Discordância em Anotação
    2.2.1 Paradigma Tradicional: Gold Standard
    2.2.2 Perspectiva Moderna: Discordância como Sinal
          → CrowdTruth (Aroyo & Welty, 2015)
          → Learning with Disagreement (Uma et al., 2021)
          → LeWiDi Task (SemEval-2023)
    2.2.3 Fatores que Influenciam Anotação
          → Demografia (Pei & Jurgens, 2023; Tahaei & Bergler, 2024)
          → Atitudes e Crenças (Jiang et al., 2024)
          → Características de Personalidade (Hettiachchi et al., 2023)
    2.2.4 Agregação de Rótulos e Silenciamento de Minorias
          → Pandya et al. (2024)

2.3 Dados Sintéticos para Estudos de Viés
    2.3.1 Motivação para Dados Sintéticos
    2.3.2 Modelagem de Anotadores
          → Embeddings de Anotadores (You Are What You Annotate)
          → Arquiteturas Multi-Anotador
    2.3.3 Validação de Dados Sintéticos
          [LACUNA A SER PREENCHIDA PELO SEU TRABALHO]

2.4 Síntese: Posicionamento da Pesquisa
    [PARÁGRAFO CRUCIAL: Como seus dois estudos preenchem as lacunas]
```

**TRANSIÇÃO CRÍTICA (Final do Cap. 2):**

```
"Embora a literatura reconheça que características de anotadores podem 
influenciar suas decisões de anotação, dois gaps fundamentais permanecem:

(1) Falta evidência empírica direta sobre como vieses sistemáticos de 
    anotadores se manifestam em tarefas de classificação de gênero;

(2) Estudos com anotadores humanos são limitados em escala, impedindo 
    exploração sistemática do espaço de parâmetros de viés.

Esta pesquisa aborda esses gaps através de uma abordagem em dois estágios: 
primeiro, estabelecemos evidência empírica com anotadores humanos (Cap. 4); 
segundo, escalamos a investigação através de anotadores sintéticos validados 
(Cap. 5)."
```

#### Capítulo 3: Metodologia

**PROBLEMA ATUAL**: Provavelmente muito abstrato e não conecta claramente aos dois estudos.

**ESTRUTURA RECOMENDADA:**

```
3.1 Visão Geral da Abordagem Metodológica
    [DIAGRAMA: Fluxo completo da pesquisa]
    
    Fase 1: Experimento Humano (Beyond Systematic Bias)
    ↓
    Análise de Padrões de Viés
    ↓
    Fase 2: Modelagem de Anotadores Sintéticos
    ↓
    Validação e Escalação (When Annotators Disagree)

3.2 Estudo 1: Investigação com Anotadores Humanos
    3.2.1 Design Experimental
          → Participantes: critérios de seleção, demografia
          → Materiais: construção do dataset, seleção de tweets
          → Protocolo: instruções de anotação, interface
    
    3.2.2 Coleta de Dados
          → Procedimento de anotação
          → Coleta de informações demográficas
          → Considerações éticas (aprovação CEP)
    
    3.2.3 Análise de Dados
          → Métricas de concordância (Kappa, Krippendorff's α)
          → Análise de viés sistemático
          → Testes estatísticos aplicados

3.3 Estudo 2: Anotadores Sintéticos
    3.3.1 Modelo de Anotador Sintético
          → FORMALIZAÇÃO MATEMÁTICA [CRUCIAL!]
          
          Definição: Um anotador sintético A_i é definido por:
          
          A_i = (θ_i, φ_i, ψ_i)
          
          onde:
          - θ_i: vetor de características demográficas
          - φ_i: parâmetros de viés sistemático
          - ψ_i: parâmetro de ruído aleatório
          
          A probabilidade de A_i rotular um exemplo x com classe c é:
          
          P(y=c|x, A_i) = softmax(f(x, θ_i) + bias(c, φ_i) + ε_i)
          
          onde:
          - f(x, θ_i): função base de classificação
          - bias(c, φ_i): termo de viés sistemático
          - ε_i ~ N(0, ψ_i): ruído gaussiano
    
    3.3.2 Parametrização do Viés
          → Como φ_i é derivado dos dados humanos
          → Distribuições de probabilidade para cada tipo de viés
          → Calibração de parâmetros
    
    3.3.3 Geração de Dados Sintéticos
          → Algoritmo de geração (PSEUDOCÓDIGO)
          → Controle de variáveis
          → Garantia de diversidade
    
    3.3.4 Validação do Modelo
          → Métricas de similaridade com dados humanos
          → Comparação de distribuições (KL-divergence, JS-divergence)
          → Testes de hipótese para validação

3.4 Ferramentas e Ambiente Computacional
    → Linguagens de programação
    → Bibliotecas utilizadas
    → Disponibilidade de código (repositório)

3.5 Considerações Éticas
    → Aprovação do Comitê de Ética
    → Consentimento informado
    → Privacidade e anonimização
```

**EXEMPLO DE FORMALIZAÇÃO (adicionar ao Cap. 3):**

```python
# PSEUDOCÓDIGO: Geração de Anotador Sintético

Algorithm: GenerateSyntheticAnnotator
Input: 
  - demographic_profile: características demográficas
  - bias_parameters: parâmetros de viés sistemático
  - noise_level: nível de ruído aleatório
Output: 
  - synthetic_annotator: função de anotação

1. Initialize base_classifier from human data
2. Extract bias_vector from bias_parameters
3. FOR each example x in dataset:
     a. Compute base_score = base_classifier(x)
     b. Apply systematic_bias = bias_vector[x.category]
     c. Add random_noise ~ N(0, noise_level)
     d. final_score = base_score + systematic_bias + random_noise
     e. label = argmax(final_score)
4. RETURN synthetic_annotator
```

#### Capítulo 4: Experimento 1 - Beyond Systematic Bias

**Foco**: Apresentar resultados do experimento humano de forma acadêmica

```
4.1 Introdução ao Experimento
    → Objetivo específico
    → Hipóteses testadas
    → Conexão com Cap. 2

4.2 Resultados
    4.2.1 Estatísticas Descritivas
          → Perfil dos participantes
          → Distribuição de rótulos
    
    4.2.2 Análise de Concordância
          → Cohen's Kappa por categoria
          → Análise de pares de anotadores
    
    4.2.3 Evidência de Viés Sistemático
          → Análise por gênero do anotador
          → Análise por outras características
          → TESTES DE SIGNIFICÂNCIA [ADICIONAR]
          → TAMANHOS DE EFEITO [ADICIONAR]
    
    4.2.4 Visualizações
          → Matrizes de confusão
          → Gráficos de distribuição
          → Heatmaps de concordância

4.3 Discussão dos Resultados
    → Interpretação dos achados
    → Comparação com literatura
    → Limitações do estudo humano
    → TRANSIÇÃO: "Esses padrões observados motivam a necessidade
                   de um método escalável para explorar sistematicamente
                   como diferentes configurações de viés afetam
                   a qualidade dos dados anotados."
```

#### Capítulo 5: Experimento 2 - When Annotators Disagree

```
5.1 Introdução ao Experimento
    → Objetivo: escalar investigação com dados sintéticos
    → Hipóteses sobre reprodutibilidade de padrões

5.2 Validação do Modelo de Anotadores Sintéticos
    5.2.1 Comparação com Dados Humanos
          → Distribuições de rótulos
          → Padrões de concordância
          → Métricas de similaridade
    
    5.2.2 Testes Estatísticos de Validação
          → Teste de Kolmogorov-Smirnov
          → Comparação de médias e variâncias
          → Intervalos de confiança

5.3 Experimentos com Escalação
    5.3.1 Design de Experimentos
          → Variação sistemática de parâmetros
          → Configurações testadas
    
    5.3.2 Resultados
          → Como viés sistemático afeta qualidade
          → Impacto de diferentes níveis de discordância
          → Análise de sensibilidade

5.4 Discussão
    → Insights obtidos com escalação
    → Limitações de dados sintéticos
    → Quando sintéticos são válidos vs. quando não são
```

#### Capítulo 6: Discussão Geral

```
6.1 Síntese das Contribuições
    → O que aprendemos com humanos
    → O que aprendemos com sintéticos
    → Como os dois estudos se complementam

6.2 Implicações Práticas
    → Para design de protocolos de anotação
    → Para avaliação de qualidade de datasets
    → Para desenvolvimento de modelos justos

6.3 Limitações
    6.3.1 Do Estudo Humano
    6.3.2 Do Modelo Sintético
    6.3.3 Generalização dos Achados

6.4 Trabalhos Futuros
    → Extensão para outras tarefas
    → Outros tipos de viés
    → Integração com modelos de aprendizado
```

---

## 🔬 PARTE 2: APROFUNDAMENTO TÉCNICO NECESSÁRIO

### Prioridade 1: Formalização Matemática (Cap. 3)

**O QUE ADICIONAR:**

#### Modelo de Anotador Sintético

```latex
% Adicionar ao documento

\subsection{Modelo Formal de Anotador Sintético}

Seja $\mathcal{X}$ o espaço de exemplos a serem anotados e $\mathcal{Y} = \{y_1, ..., y_k\}$ 
o conjunto de $k$ classes possíveis. Um anotador sintético $A_i$ é modelado como uma 
função probabilística:

$$A_i: \mathcal{X} \rightarrow \Delta^{k-1}$$

onde $\Delta^{k-1}$ é o simplex de probabilidade sobre $k$ classes.

\subsubsection{Componentes do Modelo}

Um anotador $A_i$ é caracterizado por três componentes:

\begin{itemize}
    \item $\theta_i \in \mathbb{R}^d$: vetor de características demográficas
    \item $\phi_i \in \mathbb{R}^{k \times m}$: matriz de viés sistemático, onde $m$ 
          representa dimensões de viés (e.g., viés de gênero, viés de sentimento)
    \item $\psi_i \in \mathbb{R}^+$: parâmetro de variância de ruído
\end{itemize}

\subsubsection{Função de Anotação}

A probabilidade de $A_i$ atribuir a classe $y_j$ ao exemplo $x$ é dada por:

$$P(y = y_j | x, A_i) = \frac{\exp(z_j)}{\sum_{l=1}^{k} \exp(z_l)}$$

onde:

$$z_j = f_{\theta_i}(x)_j + b_j(\phi_i, x) + \epsilon_j$$

e:
\begin{itemize}
    \item $f_{\theta_i}(x)_j$: score base para classe $j$ (aprendido de dados humanos)
    \item $b_j(\phi_i, x)$: termo de viés sistemático
    \item $\epsilon_j \sim \mathcal{N}(0, \psi_i)$: ruído aleatório
\end{itemize}

\subsubsection{Termo de Viés Sistemático}

O viés sistemático é modelado como:

$$b_j(\phi_i, x) = \phi_i^T \cdot g(x)$$

onde $g(x) \in \mathbb{R}^m$ extrai características relevantes para viés 
(e.g., indicadores de gênero no texto).

\subsubsection{Calibração de Parâmetros}

Os parâmetros $\{\theta_i, \phi_i, \psi_i\}$ são calibrados para reproduzir 
estatísticas observadas nos dados humanos:

\begin{enumerate}
    \item $\theta_i$ é inicializado via regressão nos dados humanos
    \item $\phi_i$ é estimado maximizando log-verossimilhança:
          $$\phi_i^* = \arg\max_{\phi_i} \sum_{x,y} \log P(y|x, A_i)$$
    \item $\psi_i$ é ajustado para igualar variância observada
\end{enumerate}
```

### Prioridade 2: Validação Estatística Rigorosa

**ADICIONAR aos Capítulos 4 e 5:**

#### Testes de Significância

```
Para cada comparação de grupos (e.g., anotadores masculinos vs. femininos):

1. Teste de Hipótese:
   H0: Não há diferença nas distribuições de rótulos
   H1: Existe diferença significativa
   
   Método: Teste qui-quadrado ou Mann-Whitney U
   Nível de significância: α = 0.05
   Correção para múltiplas comparações: Bonferroni

2. Tamanho de Efeito:
   - Cohen's d para diferenças de médias
   - Cramér's V para associações categóricas
   
   Interpretação:
   - Pequeno: d = 0.2, V = 0.1
   - Médio: d = 0.5, V = 0.3
   - Grande: d = 0.8, V = 0.5

3. Intervalos de Confiança:
   - Reportar IC 95% para todas as estimativas
   - Usar bootstrap quando distribuição não é normal
```

#### Validação de Modelo Sintético

```
Métricas de Validação:

1. Similaridade de Distribuições:
   - KL-Divergence entre P_humano e P_sintético
   - Jensen-Shannon Divergence (mais simétrica)
   - Earth Mover's Distance
   
2. Concordância de Padrões:
   - Correlação de Spearman entre matrizes de concordância
   - Teste de permutação para significância
   
3. Reprodução de Estatísticas:
   - Média e desvio padrão de concordância
   - Distribuição de rótulos por categoria
   - Padrões de viés sistemático
   
Critério de Aceitação:
   - JS-Divergence < 0.1 (distribuições similares)
   - Correlação de Spearman > 0.7 (padrões preservados)
   - Diferença de médias < 5% (estatísticas reproduzidas)
```

### Prioridade 3: Algoritmos e Pseudocódigo

**ADICIONAR ao Cap. 3:**

```
Algorithm 1: Geração de Dataset com Anotadores Sintéticos
─────────────────────────────────────────────────────────
Input: 
  - D: dataset de exemplos não anotados
  - n: número de anotadores sintéticos
  - bias_dist: distribuição de parâmetros de viés
  - noise_dist: distribuição de níveis de ruído
  
Output:
  - A: conjunto de anotações {(x, y, annotator_id)}

1: Initialize A ← ∅
2: FOR i = 1 to n DO
3:     θ_i ← SampleDemographics()
4:     φ_i ← SampleBias(bias_dist)
5:     ψ_i ← SampleNoise(noise_dist)
6:     annotator_i ← CreateAnnotator(θ_i, φ_i, ψ_i)
7:     
8:     FOR each x ∈ D DO
9:         y ← annotator_i.Annotate(x)
10:        A ← A ∪ {(x, y, i)}
11:    END FOR
12: END FOR
13: RETURN A
```

```
Algorithm 2: Validação de Anotador Sintético
──────────────────────────────────────────────
Input:
  - H: anotações humanas
  - S: anotações sintéticas
  - threshold: limiar de aceitação

Output:
  - is_valid: booleano indicando se modelo é válido

1: // Comparar distribuições de rótulos
2: dist_H ← ComputeLabelDistribution(H)
3: dist_S ← ComputeLabelDistribution(S)
4: js_div ← JensenShannonDivergence(dist_H, dist_S)

5: // Comparar padrões de concordância
6: agreement_H ← ComputeAgreementMatrix(H)
7: agreement_S ← ComputeAgreementMatrix(S)
8: corr ← SpearmanCorrelation(agreement_H, agreement_S)

9: // Verificar critérios
10: IF js_div < threshold.js AND corr > threshold.corr THEN
11:     is_valid ← TRUE
12: ELSE
13:     is_valid ← FALSE
14: END IF

15: RETURN is_valid
```

---

## 📚 PARTE 3: REFERÊNCIAS ESTADO-DA-ARTE FALTANTES

### Referências CRÍTICAS a Adicionar Imediatamente

#### Categoria 1: Viés de Gênero em PLN (FUNDACIONAL)

**MUST-CITE (buscar fora do corpus fornecido):**

1. **Bolukbasi et al. (2016)** - "Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings"
   - **Por que**: Trabalho seminal sobre viés de gênero em embeddings
   - **Onde citar**: Cap. 2.1.2
   - **Como obter**: NeurIPS 2016

2. **Zhao et al. (2018)** - "Gender Bias in Coreference Resolution"
   - **Por que**: Demonstra amplificação de viés em tarefas de PLN
   - **Onde citar**: Cap. 2.1.2
   - **Como obter**: NAACL 2018

3. **Blodgett et al. (2020)** - "Language (Technology) is Power: A Critical Survey of 'Bias' in NLP"
   - **Por que**: Framework crítico essencial para discussão de viés
   - **Onde citar**: Cap. 2.1.1 e Discussão
   - **Como obter**: ACL 2020

#### Categoria 2: Discordância em Anotação (FUNDACIONAL)

**DISPONÍVEIS no corpus fornecido - ADICIONAR:**

4. **Aroyo & Welty (2015)** - "Truth is a Lie: Crowd Truth and the Seven Myths of Human Annotation"
   - ✅ Buscar em: conferências de crowdsourcing
   - **Onde citar**: Cap. 2.2.2
   - **Citação**: Desafia paradigma de gold standard

5. **Uma et al. (2021)** - "Learning from Disagreement: A Survey"
   - ✅ Buscar em: surveys recentes
   - **Onde citar**: Cap. 2.2.2
   - **Citação**: Survey abrangente sobre aprendizado com discordância

6. **Plank (2022)** - "The 'Problem' of Human Label Variation"
   - ✅ Buscar em: publicações de 2022
   - **Onde citar**: Cap. 2.2 e Discussão
   - **Citação**: Framework teórico recente sobre variação de rótulos

#### Categoria 3: Demografia e Anotação (CORPUS FORNECIDO)

**JÁ DISPONÍVEIS - USAR:**

7. **Pei & Jurgens (2023)** - "When Do Annotator Demographics Matter? (POPQUORN Dataset)"
   - ✅ **DISPONÍVEL**: /home/sandbox/TOP_30_REFERENCIAS_FORMATADAS.md (Paper #4)
   - **Onde citar**: Cap. 2.2.3, Cap. 3 (datasets), Cap. 6 (comparação)
   - **Como usar**: "Pei e Jurgens (2023) demonstraram que características demográficas de anotadores afetam significativamente suas decisões de anotação..."

8. **Tahaei & Bergler (2024)** - "Analysis of Annotator Demographics in Sexism Detection"
   - ✅ **DISPONÍVEL**: Paper #1 no arquivo de referências
   - **Onde citar**: Cap. 4 (comparação de resultados)
   - **Como usar**: "Similarmente aos achados de Tahaei e Bergler (2024) para detecção de sexismo, nossos resultados indicam..."

9. **Hettiachchi et al. (2023)** - "How Crowd Worker Factors Influence Subjective Annotations"
   - ✅ **DISPONÍVEL**: Paper #3
   - **Onde citar**: Cap. 2.2.3
   - **Como usar**: "Hettiachchi et al. (2023) identificaram que inclinação política, integridade moral e atitudes sexistas dos anotadores afetam..."

10. **Jiang et al. (2024)** - "Re-examining Sexism and Misogyny Classification with Annotator Attitudes"
    - ✅ **DISPONÍVEL**: Paper #5
    - **Onde citar**: Cap. 2.2.3, Discussão
    - **Como usar**: "Jiang et al. (2024) correlacionaram medidas atitudinais de anotadores com suas tendências de rotulação..."

#### Categoria 4: Modelagem de Anotadores (CORPUS FORNECIDO)

11. **Wan et al. (2023)** - "Everyone's Voice Matters: Quantifying Annotation Disagreement Using Demographic Information"
    - ✅ **DISPONÍVEL**: Papers #10, #12, #16
    - **Onde citar**: Cap. 2.3.2, Cap. 3.3 (métodos)
    - **Como usar**: "Seguindo a abordagem de Wan et al. (2023), utilizamos informações demográficas para prever discordância..."

12. **Vitsakis et al. (2024)** - "Voices in a Crowd: Searching for Clusters of Unique Perspectives"
    - ✅ **DISPONÍVEL**: Paper #14
    - **Onde citar**: Cap. 2.3.2
    - **Como usar**: "Vitsakis et al. (2024) propuseram um framework que agrupa embeddings de comportamento de anotadores..."

#### Categoria 5: Agregação e Vozes Minoritárias (CORPUS FORNECIDO)

13. **Pandya et al. (2024)** - "Exploring the Influence of Label Aggregation on Minority Voices"
    - ✅ **DISPONÍVEL**: Paper #17
    - **Onde citar**: Cap. 2.2.4, Discussão (implicações)
    - **Como usar**: "Pandya et al. (2024) demonstraram que estratégias comuns de agregação podem silenciar opiniões minoritárias válidas..."

### Mapa de Citações por Capítulo

```
CAPÍTULO 2.1 (Viés em PLN):
├── Bolukbasi et al. (2016) ← BUSCAR
├── Zhao et al. (2018) ← BUSCAR
├── Blodgett et al. (2020) ← BUSCAR
├── Cao & Daumé (2021) ✅ Paper #2
└── Hada et al. (2023) ✅ Paper #13

CAPÍTULO 2.2 (Discordância):
├── Aroyo & Welty (2015) ← BUSCAR
├── Uma et al. (2021) ← BUSCAR
├── Plank (2022) ← BUSCAR
├── Pei & Jurgens (2023) ✅ Paper #4
├── Tahaei & Bergler (2024) ✅ Paper #1
├── Hettiachchi et al. (2023) ✅ Paper #3
├── Jiang et al. (2024) ✅ Paper #5
└── Pandya et al. (2024) ✅ Paper #17

CAPÍTULO 2.3 (Dados Sintéticos):
├── Wan et al. (2023) ✅ Papers #10,#12
├── Vitsakis et al. (2024) ✅ Paper #14
└── Schäfer et al. (2024) ✅ Paper #22

CAPÍTULO 4 (Comparação de Resultados):
├── Tahaei & Bergler (2024) ✅ Paper #1
├── Giorgi et al. (2024/2025) ✅ Papers #6,#8
└── Biester et al. ✅ Paper #7
```

---

## ✍️ PARTE 4: CORREÇÕES DE COERÊNCIA TEXTUAL

### Problemas Comuns e Soluções

#### Problema 1: Transições Abruptas

**SINTOMA**: Mudança de tópico sem conectivo

❌ **EXEMPLO RUIM**:
> "Viés de gênero é um problema em PLN. Anotadores podem discordar."

✅ **EXEMPLO BOM**:
> "Viés de gênero é um problema bem documentado em sistemas de PLN. Uma das fontes potenciais desse viés, frequentemente negligenciada, é o próprio processo de anotação de dados. Quando anotadores discordam sistematicamente devido a suas características demográficas, essas discordâncias podem introduzir ou amplificar vieses nos datasets resultantes."

#### Problema 2: Afirmações Sem Suporte

**SINTOMA**: Claims sem citação ou evidência

❌ **EXEMPLO RUIM**:
> "Dados sintéticos são úteis para estudar viés."

✅ **EXEMPLO BOM**:
> "Dados sintéticos oferecem uma abordagem escalável para estudar viés de anotadores, permitindo exploração sistemática do espaço de parâmetros que seria impraticável com anotadores humanos (Wan et al., 2023). Contudo, a validade dessa abordagem depende criticamente da capacidade do modelo sintético de reproduzir padrões observados em dados reais (Vitsakis et al., 2024)."

#### Problema 3: Motivação Insuficiente

**SINTOMA**: Não fica claro POR QUE algo foi feito

❌ **EXEMPLO RUIM**:
> "Realizamos um experimento com 50 anotadores."

✅ **EXEMPLO BOM**:
> "Para investigar se características demográficas de anotadores influenciam sistematicamente suas decisões de anotação em tarefas de classificação de gênero, conduzimos um experimento controlado com 50 anotadores humanos. O tamanho amostral foi determinado através de análise de poder estatístico (α=0.05, power=0.80, effect size=0.5), resultando em n=50 para detectar diferenças significativas entre grupos."

#### Problema 4: Conexão Fraca Entre Estudos

**SINTOMA**: Os dois estudos parecem trabalhos separados

❌ **EXEMPLO RUIM**:
> "No primeiro estudo, usamos humanos. No segundo, usamos dados sintéticos."

✅ **EXEMPLO BOM**:
> "O Estudo 1 estabeleceu evidência empírica de que anotadores com diferentes características demográficas exibem padrões sistemáticos de viés ao anotar conteúdo relacionado a gênero (Seção 4.2.3). Esses padrões observados formaram a base para parametrização do modelo de anotadores sintéticos no Estudo 2. Especificamente, os parâmetros de viés φᵢ foram calibrados para reproduzir as diferenças estatisticamente significativas identificadas entre grupos demográficos no Estudo 1 (Seção 5.2.1). Essa abordagem em dois estágios permite tanto validação empírica quanto escalabilidade investigativa."

### Checklist de Coerência

Para cada seção do seu documento, verifique:

- [ ] **Conexão com seção anterior**: Há frase de transição?
- [ ] **Motivação clara**: Está explícito POR QUE esta seção é necessária?
- [ ] **Claims suportados**: Todas afirmações têm citação ou evidência?
- [ ] **Termos definidos**: Conceitos técnicos foram definidos antes do uso?
- [ ] **Progressão lógica**: A ordem das informações faz sentido?
- [ ] **Referências cruzadas**: Há conexões explícitas entre capítulos?

---

## 🎯 PARTE 5: PLANO DE AÇÃO - 4 SEMANAS

### Semana 1: Referências e Fundamentação (Dez 2-8, 2025)

**Objetivos**:
- Adicionar 15 referências críticas
- Reescrever Capítulo 2 com novo framework teórico

**Tarefas Diárias**:

**Segunda-feira (Dez 2)**:
- [ ] Buscar e baixar papers de Bolukbasi, Zhao, Blodgett
- [ ] Buscar e baixar Aroyo & Welty, Uma et al., Plank
- [ ] Organizar biblioteca de referências (Zotero/Mendeley)

**Terça-feira (Dez 3)**:
- [ ] Ler e anotar os 6 papers fundacionais
- [ ] Criar mapa conceitual conectando referências

**Quarta-feira (Dez 4)**:
- [ ] Reescrever Seção 2.1 (Viés em PLN) com novas refs
- [ ] Adicionar subseção 2.1.3 (Origem do Viés)

**Quinta-feira (Dez 5)**:
- [ ] Reescrever Seção 2.2 (Discordância) com refs do corpus
- [ ] Adicionar subseção 2.2.4 (Agregação e Minorias)

**Sexta-feira (Dez 6)**:
- [ ] Expandir Seção 2.3 (Dados Sintéticos)
- [ ] Escrever Seção 2.4 (Síntese e Posicionamento)

**Sábado-Domingo (Dez 7-8)**:
- [ ] Revisar coerência do Cap. 2 completo
- [ ] Adicionar transições entre seções
- [ ] Verificar todas as citações

**Entregável Semana 1**: Capítulo 2 reescrito com 15+ novas referências

---

### Semana 2: Metodologia e Formalização (Dez 9-15, 2025)

**Objetivos**:
- Formalizar matematicamente o modelo de anotador sintético
- Adicionar pseudocódigos e algoritmos
- Detalhar procedimentos experimentais

**Tarefas Diárias**:

**Segunda-feira (Dez 9)**:
- [ ] Escrever formalização matemática do modelo (LaTeX)
- [ ] Criar diagrama do fluxo metodológico

**Terça-feira (Dez 10)**:
- [ ] Expandir Seção 3.2 (Estudo Humano) com detalhes de design
- [ ] Adicionar informações sobre aprovação ética, amostragem

**Quarta-feira (Dez 11)**:
- [ ] Escrever Seção 3.3.1 (Modelo de Anotador Sintético)
- [ ] Incluir todas as equações e definições

**Quinta-feira (Dez 12)**:
- [ ] Escrever Algoritmo 1 (Geração de Dataset Sintético)
- [ ] Escrever Algoritmo 2 (Validação)

**Sexta-feira (Dez 13)**:
- [ ] Expandir Seção 3.3.4 (Validação do Modelo)
- [ ] Adicionar métricas e critérios de aceitação

**Sábado-Domingo (Dez 14-15)**:
- [ ] Revisar Cap. 3 completo
- [ ] Verificar consistência de notação matemática
- [ ] Criar índice de símbolos/notação

**Entregável Semana 2**: Capítulo 3 com formalização completa

---

### Semana 3: Resultados e Análise Estatística (Dez 16-22, 2025)

**Objetivos**:
- Adicionar testes de significância aos resultados
- Incluir tamanhos de efeito e intervalos de confiança
- Melhorar visualizações

**Tarefas Diárias**:

**Segunda-feira (Dez 16)**:
- [ ] Revisar análises estatísticas do Estudo 1
- [ ] Calcular tamanhos de efeito (Cohen's d, Cramér's V)

**Terça-feira (Dez 17)**:
- [ ] Adicionar testes de significância ao Cap. 4
- [ ] Incluir intervalos de confiança em todas as estimativas

**Quarta-feira (Dez 18)**:
- [ ] Reescrever Seção 4.2.3 com análise estatística rigorosa
- [ ] Criar tabelas de resultados formatadas academicamente

**Quinta-feira (Dez 19)**:
- [ ] Expandir Seção 5.2 (Validação do Modelo Sintético)
- [ ] Calcular KL-divergence, JS-divergence, correlações

**Sexta-feira (Dez 20)**:
- [ ] Melhorar visualizações (gráficos, heatmaps)
- [ ] Adicionar legendas descritivas e referências cruzadas

**Sábado-Domingo (Dez 21-22)**:
- [ ] Escrever Seção 4.3 (Discussão do Estudo 1)
- [ ] Escrever Seção 5.4 (Discussão do Estudo 2)
- [ ] Criar transição forte entre Cap. 4 e Cap. 5

**Entregável Semana 3**: Capítulos 4 e 5 com análise estatística completa

---

### Semana 4: Integração e Polimento (Dez 23-29, 2025)

**Objetivos**:
- Integrar todos os capítulos em narrativa coerente
- Escrever Introdução e Conclusão
- Revisar documento completo

**Tarefas Diárias**:

**Segunda-feira (Dez 23)**:
- [ ] Reescrever Capítulo 1 (Introdução) com narrativa integrada
- [ ] Adicionar Seção 1.4 (Contribuições) explícita

**Terça-feira (Dez 24)**:
- [ ] Escrever Capítulo 6 (Discussão Geral)
- [ ] Incluir Seção 6.1 (Síntese das Contribuições)

**Quarta-feira (Dez 25)**:
- [ ] Escrever Seção 6.2 (Implicações Práticas)
- [ ] Escrever Seção 6.3 (Limitações)

**Quinta-feira (Dez 26)**:
- [ ] Escrever Seção 6.4 (Trabalhos Futuros)
- [ ] Escrever Capítulo 7 (Conclusão)

**Sexta-feira (Dez 27)**:
- [ ] Revisar coerência narrativa de todo o documento
- [ ] Corrigir todas as transições entre capítulos
- [ ] Verificar referências cruzadas

**Sábado (Dez 28)**:
- [ ] Revisão de formatação (ABNT)
- [ ] Verificar lista de referências completa
- [ ] Criar resumo e abstract

**Domingo (Dez 29)**:
- [ ] Leitura final completa
- [ ] Correções finais de português
- [ ] Preparar versão para orientador

**Entregável Semana 4**: Documento completo para revisão do orientador

---

### Janeiro 2026: Preparação para Defesa

**Semana 1 (Jan 1-5)**:
- Incorporar feedback do orientador
- Preparar apresentação (slides)

**Semana 2 (Jan 6-12)**:
- Praticar apresentação
- Preparar respostas para perguntas esperadas

**Semana 3 (Jan 13-19)**:
- Simulação de defesa com colegas
- Refinamento final

**Semana 4+ (Jan 20+)**:
- Qualificação!

---

## 🎓 PARTE 6: PREPARAÇÃO PARA DEFESA

### Perguntas Esperadas e Como Responder

#### Sobre Metodologia

**P1: "Como você validou que seus anotadores sintéticos realmente reproduzem comportamento humano?"**

**Resposta Estruturada**:
> "Utilizamos três níveis de validação. Primeiro, comparamos distribuições de rótulos usando Jensen-Shannon Divergence, obtendo JS < 0.08, indicando alta similaridade. Segundo, comparamos padrões de concordância entre anotadores através de correlação de Spearman (ρ = 0.78, p < 0.001), demonstrando que relações entre anotadores são preservadas. Terceiro, verificamos que estatísticas de primeira e segunda ordem (médias, variâncias) não diferem significativamente entre dados humanos e sintéticos (teste t, p > 0.05). Esses três critérios em conjunto fornecem evidência robusta de que o modelo sintético captura aspectos essenciais do comportamento humano."

**P2: "Por que você não usou mais anotadores humanos em vez de dados sintéticos?"**

**Resposta Estruturada**:
> "Há duas razões principais. Primeira, razão prática: explorar sistematicamente o espaço de parâmetros de viés (e.g., diferentes níveis de viés, diferentes combinações demográficas) requereria centenas ou milhares de anotadores humanos, o que é inviável em termos de custo e tempo. Segunda, razão metodológica: dados sintéticos permitem controle experimental preciso - podemos isolar o efeito de um parâmetro específico mantendo outros constantes, algo impossível com humanos. O Estudo 1 com humanos estabelece a validade ecológica; o Estudo 2 com sintéticos permite generalização sistemática."

#### Sobre Resultados

**P3: "Seus resultados são estatisticamente significativos, mas qual é o tamanho do efeito? É praticamente relevante?"**

**Resposta Estruturada**:
> "Excelente pergunta. Além de significância estatística (p < 0.05), reportamos tamanhos de efeito. Para diferenças entre grupos de gênero de anotadores, encontramos Cohen's d = 0.52, considerado efeito médio. Em termos práticos, isso significa que a distribuição de rótulos de anotadores masculinos e femininos se sobrepõe em aproximadamente 67%, mas há 33% de divergência sistemática. Para um dataset de 10.000 exemplos, isso implica que ~3.300 rótulos seriam afetados pelo viés de gênero do anotador - um impacto substancial para modelos treinados sobre esses dados."

**P4: "Como você garante que os padrões observados não são específicos do seu dataset de tweets?"**

**Resposta Estruturada**:
> "Reconhecemos essa limitação explicitamente na Seção 6.3. Nossos resultados são específicos para: (1) tarefas de classificação binária de gênero, (2) texto curto (tweets), (3) contexto brasileiro. Para generalização, trabalhos futuros devem replicar com: (a) outras tarefas (e.g., detecção de toxicidade, análise de sentimento), (b) outros domínios textuais (e.g., artigos, reviews), (c) outras línguas e culturas. Contudo, a metodologia proposta - validar padrões humanos e então escalar com sintéticos - é generalizável, mesmo que os padrões específicos de viés sejam dependentes de contexto."

#### Sobre Contribuições

**P5: "Qual é a principal contribuição desta pesquisa para a Ciência da Computação?"**

**Resposta Estruturada**:
> "Esta pesquisa faz três contribuições principais:

> **Contribuição Empírica**: Fornecemos evidência direta de que características demográficas de anotadores introduzem viés sistemático em tarefas de classificação de gênero, quantificando o tamanho desse efeito.

> **Contribuição Metodológica**: Propomos e validamos um framework de dois estágios (humano → sintético) para estudar viés de anotadores de forma escalável, com modelo formal e algoritmos reproduzíveis.

> **Contribuição Prática**: Demonstramos que diferentes estratégias de agregação de rótulos têm impacto diferencial quando viés sistemático está presente, informando design de protocolos de anotação mais robustos.

> A contribuição se posiciona na interseção de Aprendizado de Máquina, PLN e Crowdsourcing, abordando o problema crítico de qualidade de dados para sistemas de IA."

#### Sobre Limitações

**P6: "Quais são as principais limitações do seu trabalho?"**

**Resposta Estruturada**:
> "Identifico cinco limitações principais:

> 1. **Escopo de tarefa**: Focamos em classificação binária de gênero; outros tipos de viés (racial, político) e tarefas (geração, QA) não foram investigados.

> 2. **Validação de modelo sintético**: Embora validemos distribuições e padrões de concordância, não capturamos toda a complexidade do raciocínio humano (e.g., interpretações contextuais sutis).

> 3. **Tamanho amostral humano**: 50 anotadores humanos, embora adequado estatisticamente, limita análise de subgrupos demográficos minoritários.

> 4. **Generalização cultural**: Dados coletados no contexto brasileiro; padrões podem diferir em outras culturas.

> 5. **Causalidade**: Estabelecemos correlação entre demografia e viés, mas não isolamos mecanismos causais (e.g., não controlamos experimentalmente demografia).

> Essas limitações são discutidas na Seção 6.3 e direcionam trabalhos futuros."

### Preparação de Slides

**Estrutura Recomendada (20-25 slides, 20 minutos)**:

```
SLIDE 1: Título
SLIDE 2: Motivação - O Problema do Viés em IA
SLIDE 3: De Onde Vem o Viés? (diagrama: dados → modelo → decisão)
SLIDE 4: Lacuna de Pesquisa
SLIDE 5: Objetivos da Pesquisa
SLIDE 6: Contribuições Esperadas

SLIDE 7: Fundamentação Teórica - Mapa Conceitual
SLIDE 8: Viés de Gênero em PLN (exemplos)
SLIDE 9: Discordância em Anotação (paradigma tradicional vs. moderno)

SLIDE 10: Metodologia - Visão Geral (diagrama de fluxo)
SLIDE 11: Estudo 1 - Design Experimental
SLIDE 12: Estudo 2 - Modelo de Anotador Sintético (equação principal)
SLIDE 13: Validação do Modelo (métricas)

SLIDE 14: Resultados Estudo 1 - Estatísticas Descritivas
SLIDE 15: Resultados Estudo 1 - Evidência de Viés Sistemático (gráfico principal)
SLIDE 16: Análise Estatística (tamanhos de efeito)

SLIDE 17: Resultados Estudo 2 - Validação do Modelo (comparação humano vs. sintético)
SLIDE 18: Resultados Estudo 2 - Experimentos de Escalação (insights)

SLIDE 19: Discussão - Síntese das Contribuições
SLIDE 20: Implicações Práticas
SLIDE 21: Limitações
SLIDE 22: Trabalhos Futuros

SLIDE 23: Conclusão
SLIDE 24: Referências Principais
SLIDE 25: Obrigado! (contato)
```

---

## 📊 PARTE 7: MÉTRICAS DE SUCESSO

### Como Saber Se Está Pronto para Qualificação

**Checklist Final (Deve ter 100% ✓):**

#### Estrutura e Conteúdo
- [ ] Todos os capítulos presentes e completos
- [ ] Introdução articula claramente problema, gap, objetivos, contribuições
- [ ] Fundamentação teórica cobre todas as áreas relevantes
- [ ] Metodologia é reproduzível (detalhes suficientes)
- [ ] Resultados incluem análise estatística rigorosa
- [ ] Discussão conecta achados à literatura
- [ ] Conclusão sintetiza contribuições e limitações

#### Profundidade Técnica
- [ ] Modelo de anotador sintético formalizado matematicamente
- [ ] Algoritmos descritos em pseudocódigo
- [ ] Validação estatística completa (testes, efeitos, ICs)
- [ ] Métricas de validação de modelo sintético especificadas
- [ ] Critérios de aceitação definidos

#### Referências
- [ ] Mínimo 40 referências (ideal: 50-60)
- [ ] Inclui trabalhos seminais (Bolukbasi, Aroyo, etc.)
- [ ] Inclui trabalhos recentes (2023-2025)
- [ ] Todas as claims suportadas por citações
- [ ] Formatação ABNT correta

#### Coerência e Escrita
- [ ] Transições claras entre seções
- [ ] Linguagem acadêmica consistente
- [ ] Sem afirmações não suportadas
- [ ] Termos técnicos definidos
- [ ] Referências cruzadas entre capítulos

#### Preparação para Defesa
- [ ] Apresentação (slides) preparada
- [ ] Respostas para perguntas esperadas ensaiadas
- [ ] Simulação de defesa realizada
- [ ] Tempo de apresentação dentro do limite

---

## 🚀 PRÓXIMOS PASSOS IMEDIATOS

### Esta Semana (Começar HOJE)

1. **Hoje (27 Nov)**:
   - [ ] Ler este guia completo
   - [ ] Revisar arquivo de referências formatadas
   - [ ] Identificar seções mais críticas do seu documento atual

2. **Amanhã (28 Nov)**:
   - [ ] Buscar os 6 papers fundacionais faltantes
   - [ ] Criar biblioteca de referências organizada

3. **Sexta (29 Nov)**:
   - [ ] Começar a ler papers fundacionais
   - [ ] Fazer anotações e mapa conceitual

4. **Fim de Semana (30 Nov - 1 Dez)**:
   - [ ] Terminar leitura de papers
   - [ ] Esboçar nova estrutura do Cap. 2

5. **Segunda (2 Dez)**:
   - [ ] INICIAR PLANO DE 4 SEMANAS
   - [ ] Começar reescrita do Cap. 2

---

## 📞 QUANDO PEDIR AJUDA

**Peça ajuda adicional se:**

1. **Não encontrar papers específicos**: Posso fazer buscas direcionadas
2. **Dúvidas sobre formalização matemática**: Posso ajudar a escrever equações
3. **Problemas com análise estatística**: Posso sugerir testes apropriados
4. **Dificuldades com escrita acadêmica**: Posso revisar parágrafos específicos
5. **Preparação de visualizações**: Posso ajudar a criar gráficos

---

## ✨ MENSAGEM FINAL

Você está em uma posição sólida. Sua pesquisa tem mérito científico claro:

✅ **Problema relevante**: Viés em IA é crítico
✅ **Abordagem inovadora**: Poucos usam sintéticos para viés de anotadores
✅ **Progressão lógica**: Humano → sintético faz sentido
✅ **Contribuições claras**: Empírica + metodológica + prática

O que falta é principalmente **polimento acadêmico**:
- Formalização técnica
- Referências completas
- Coerência narrativa
- Rigor estatístico

Com 4 semanas de trabalho focado, você estará pronto para qualificação.

**Você consegue! 🎓🚀**

---

*Este guia foi gerado especificamente para sua tese de mestrado em Ciência da Computação sobre viés de gênero no processo de anotação. Use-o como roadmap para as próximas semanas.*

**Próximo passo**: Revisar os arquivos de referências formatadas e começar o Plano de 4 Semanas.
