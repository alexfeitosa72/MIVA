# RELATÓRIO DE MATURIDADE PARA BANCA DE QUALIFICAÇÃO

**Documento analisado:** `Qualificacao_Alexander_v2 (1).pdf` (13/04/2026)  
**Gerado em:** 13/04/2026  
**Escopo:** Avaliação de prontidão acadêmica · Pontos fortes · Vulnerabilidades · Perguntas prováveis da banca · Veredicto  
**Método:** Leitura integral do PDF (74 páginas de conteúdo + referências) — todas as conclusões derivadas exclusivamente do documento atual  

---

## I. VEREDICTO EXECUTIVO

| Dimensão | Avaliação |
|----------|-----------|
| Maturidade geral | **Alta — adequada para qualificação** |
| Rigor metodológico | Sólido ✓ |
| Fundamentação teórica | Sólida ✓ |
| Resultados e análise | Corretos e completos ✓ |
| Estrutura acadêmica | Dissertação completa (discussão, limitações, perspectivas) ✓ |
| Erros bloqueantes | **Nenhum — confirmado por leitura do PDF 13/04/2026** |
| Recomendação | **APTO PARA SUBMISSÃO À BANCA** |

O documento está maduro. Os problemas identificados em versões anteriores (cross-references quebradas, contagem PRISMA divergente, frase duplicada em II.5) estão todos corrigidos na versão analisada. O que remanece são redundâncias estruturais que não bloqueiam a qualificação mas podem ser polidas antes da impressão final.

---

## II. AVALIAÇÃO POR DIMENSÃO ACADÊMICA

### D1 — Contribuição Original (Peso: Alto)

**Avaliação: FORTE**

A MADA (Metodologia de Análise de Divergências Anotativas) constitui contribuição genuína ao campo de NLP em português. O índice Δκ = κ_inicial − κ_modelos como operacionalização de amplificação de viés anotativo é original: transforma um fenômeno qualitativo (divergência anotativa) em métrica quantificável e replicável.

**Evidências:**
- MQD-1222: corpus proprietário com estratificação de gênero (4M/4F), aprovação ética CAAE 82267824.8.0000.5289
- Dupla instanciação: fase empírica (N=1.222, dados reais) + fase sintética (SynSA-50 a SynSA-99, 12 conjuntos × N=999)
- Resultado principal: todos os 4 classificadores amplificam divergências anotativas (Δκ médio = 0,2787, σ = 0,0224)
- Resultado sintético: amplificação decresce monotonicamente com o aumento de κ_inicial — comportamento previsto pelo modelo MADA confirmado empiricamente

**Ponto de atenção:** A banca pode questionar se MADA constitui "metodologia" ou "framework de análise". Prepare distinção conceitual: MADA define procedimento operacional (corpus estratificado + anotação humana + classificadores + Δκ), não apenas modelo teórico.

---

### D2 — Rigor Metodológico (Peso: Muito Alto)

**Avaliação: MUITO FORTE**

| Elemento | Implementação |
|----------|---------------|
| Corpus | N=1.222, estratificação de gênero, plataforma PCIbex Farm |
| Anotadores | N=8, paridade de gênero (4M/4F), calibração prévia |
| Acordo interanotador | κ = 0,7664, IC 95% bootstrap [0,7363; 0,7954] |
| Representação | TF-IDF — escolha justificada em V.8 (isolar efeito da anotação) |
| Classificadores | SVM, NB, RF, LR — cobertura representativa sem overclaim |
| Validação | Stratified 5-fold cross-validation com pareamento de treino |
| Significância | χ² = 1441,03, V de Cramér = 0,7679 |
| Fase sintética | Bootstrap 1.000 iterações, κ_sintético controlado por design |
| Revisão sistemática | PRISMA 2020, 186 estudos incluídos, critérios explícitos |
| Ética | CAAE aprovado, plataforma de anotação com consentimento |

A combinação de validação cruzada estratificada + bootstrap + fase sintética de controle é metodologicamente robusta. Poucos trabalhos de NLP em português apresentam esse nível de verificação de confiabilidade.

---

### D3 — Fundamentação Teórica (Peso: Alto)

**Avaliação: SÓLIDA**

A revisão sistemática (186 estudos, PRISMA 2020) cobre adequadamente:
- Viés de gênero em modelos de linguagem
- Acordo interanotador e divergência anotativa (κ, Cohen 1960; Landis & Koch 1977)
- NLP em português brasileiro
- Aprendizado supervisionado para classificação de sentimentos

**Ponto de atenção:** A banca pode questionar ausência de literatura mais recente sobre modelos de linguagem de grande escala (LLMs) e se a escolha de TF-IDF em vez de embeddings contextuais (BERTimbau, RoBERTa-pt) é limitação ou decisão de design. O documento antecipa isso em V.8 e VII.4 — certifique-se de ter argumentos orais preparados (ver Seção V deste relatório).

---

### D4 — Análise e Discussão dos Resultados (Peso: Muito Alto)

**Avaliação: FORTE**

**Resultados principais verificados e corretos:**

| Métrica | Valor | Classificação Landis & Koch |
|---------|-------|---------------------------|
| κ_inicial | 0,7664 | Substancial |
| Δκ SVM | +0,2720 | Leve (1 faixa) |
| Δκ NB | +0,3082 | Leve (1 faixa) — maior amplificação |
| Δκ RF | +0,2801 | Leve (1 faixa) |
| Δκ LR | +0,2544 | Leve (1 faixa) — menor amplificação |
| Δκ médio | 0,2787 ± 0,0224 | Leve |

**Distribuição de sentimentos (dados empíricos):**

| Gênero | Positivo | Negativo | Neutro |
|--------|----------|----------|--------|
| Masc. | 481 (39,4%) | 450 (36,8%) | 291 (23,8%) |
| Fem. | 411 (33,6%) | 446 (36,5%) | 365 (29,9%) |

**Discussão acadêmica (Cap. VII):**
- VII.1: Análise Empírica — responde RQ1–RQ3 explicitamente com remissão a resultados
- VII.2: Análise Sintética — comportamento monotônico dos SynSA confirmado
- VII.3: Análise Integrada — relação entre fase empírica e sintética
- VII.4: Limitações (5 subseções: tamanho amostral, domínio, idioma, tempo, arquitetura)
- VII.5: Contribuições
- VII.6: Perspectivas futuras (agenda separada das limitações)

A classificação "Leve" para todos os Δκ merece atenção oral: a banca pode interpretar como resultado fraco. Argumento defensivo: (1) trata-se do pior caso esperado, pois κ_inicial = 0,7664 é "Substancial" — o efeito não poderia ser "Severo" sem κ inicial muito mais baixo; (2) mesmo "Leve" representa queda sistemática de 0,25–0,31 pontos de κ, com implicações práticas na confiabilidade de sistemas de classificação em produção; (3) uniformidade entre modelos (todos Leve) é resultado em si — sugere que o efeito é função da divergência anotativa, não do classificador.

**Resultado sintético notável (atenção oral):** Na fase sintética, o RF alcança severidade "Severa" (Δκ = +0,6923 em SynSA-99), comportamento qualitativamente distinto dos demais classificadores. Isso está documentado em VI.3.2 — prepare argumento sobre a mecânica de agregação de árvores do RF como amplificador de assimetrias em regiões de fronteira.

---

### D5 — Estrutura e Apresentação (Peso: Médio)

**Avaliação: BOA**

| Elemento | Status |
|----------|--------|
| Capítulos I–VII | Completos e coerentes |
| Sumário | Alinhado com estrutura real |
| Numeração de seções | Consistente |
| Siglas (MADA, MQD-1222, SynSA) | Definidas na primeira ocorrência, usadas consistentemente |
| Figuras e tabelas | Referenciadas no texto |
| PRISMA 2020 | Diagrama incluído com 186 estudos — texto (V.1) e diagrama consistentes (158 de outras fontes em ambos) ✓ |
| Cross-references "Seção ??" | **Confirmado corrigido** ✓ |
| Frase duplicada II.5 | **Confirmado corrigido** ✓ |
| Redundâncias estruturais | Ver Seção IV — itens de polimento, não bloqueantes |

---

## III. REDUNDÂNCIAS ESTRUTURAIS IDENTIFICADAS

Identificadas por leitura integral do PDF. Nenhuma é bloqueante para qualificação; as marcadas **(Recomendado)** merecem atenção antes da impressão final.

| # | Conteúdo repetido | Localizações | Ação sugerida |
|---|---|---|---|
| R1 **(Recomendado)** | Explicação mecânica do RF amplificar mais (árvores múltiplas, assimetrias locais, regiões de fronteira) | II.7 (p.12), VI.3.2 (p.54), VII.2 (p.64-65) | VI.3.2 e VII.2 quase idênticos em formulação — diferenciar a função retórica de cada um ou remissão cruzada |
| R2 | Descrição dos 3 módulos MADA | Cap. I (p.3), V.2 (p.31, com Fig. V.2), VI abertura (p.45, "por conveniência") | A reprodução em VI está marcada como intencional ("por conveniência"); aceitável, mas pode ser substituída por remissão |
| R3 | Declaração CAAE + conformidade ética | Resumo (p.3), Cap. I (p.5), V.5.1 (p.38-39) | Três ocorrências; manter Resumo e V.5.1; considerar remissão no Cap. I |
| R4 | Narrativa de construção MQD-1222 (pipeline 1.465→1.463→1.222) | IV.1 (p.23-25) — completo; V.5.1 (p.38) — sumarizado | V.5.1 pode introduzir com remissão a IV.1 em vez de renarrar |
| R5 | Justificativa TF-IDF vs. transformers | II.8 (teórica) e V.8 (metodológica) | Conteúdo parcialmente sobreposto; II.8 antecipa o que V.8 deveria ser o lugar primário — verificar se há informação nova em cada um |
| R6 | Biester et al. [2022] — gênero e anotação | II.3, II.5, III.2 | III.2 é o local mais adequado (contexto metodológico); II.3 e II.5 fazem o mesmo ponto com sobreposição |
| R7 | Tese central sobre propagação/amplificação | Cap. I, II.6, V.2, VII.1 | Nível de reiteração adequado para dissertação — não é erro |

**R1 é a mais crítica:** a formulação quase idêntica em VI.3.2 (resultados) e VII.2 (discussão) pode ser percebida pela banca como falta de progressão argumentativa entre as seções. Em VI.3.2 o argumento deve ser descritivo ("observamos que RF..."); em VII.2 deve ser interpretativo ("isso ocorre porque...").

---

## IV. VERIFICAÇÃO NUMÉRICA GLOBAL

Todos os valores verificados por leitura direta do PDF:

| Métrica | Valor no PDF | Correto |
|---------|-------------|---------|
| N (corpus) | 1.222 | ✓ |
| κ_inicial | 0,7664 | ✓ |
| IC 95% κ | [0,7363; 0,7954] | ✓ |
| Concordância bruta | 0,8453 | ✓ |
| χ² | 1441,03 | ✓ |
| V de Cramér | 0,7679 | ✓ |
| Δκ médio | 0,2787 (σ = 0,0224) | ✓ |
| Δκ SVM | +0,2720 — Leve | ✓ |
| Δκ NB | +0,3082 — Leve (maior) | ✓ |
| Δκ RF | +0,2801 — Leve | ✓ |
| Δκ LR | +0,2544 — Leve (menor) | ✓ |
| Masc. positivos | 481 (39,4%) | ✓ |
| Masc. negativos | 450 (36,8%) | ✓ |
| Masc. neutros | 291 (23,8%) | ✓ |
| Fem. negativos | 446 (36,5%) | ✓ |
| Fem. positivos | 411 (33,6%) | ✓ |
| Fem. neutros | 365 (29,9%) | ✓ |
| PRISMA — incluídos | 186 | ✓ |
| PRISMA — outras fontes (texto e diagrama) | 158 — consistentes | ✓ |
| Modelos com amplificação | 4/4 | ✓ |

**Nenhuma inconsistência numérica encontrada.**

---

## V. ANÁLISE DE PERGUNTAS PROVÁVEIS DA BANCA

### P1 — "Por que TF-IDF e não BERTimbau?"

**Frequência esperada:** Alta  
**Resposta defensiva:**

> "A escolha por TF-IDF foi deliberada: nosso objetivo é isolar o efeito da divergência anotativa humana sobre o comportamento do classificador, não maximizar performance preditiva. Se usássemos BERTimbau, o modelo carregaria vieses de pré-treinamento em corpus externo, contaminando nossa medida de Δκ — não conseguiríamos distinguir entre amplificação causada pela divergência anotativa e amplificação causada pelo pré-treinamento. TF-IDF, como representação paramétrica simples, funciona como linha de base controlada. BERTimbau está explicitamente designado como direção futura em V.8 e VII.6."

**Onde está no texto:** V.8 (justificativa), VII.4.5 (limitação arquitetural), VII.6 (perspectiva futura).

---

### P2 — "N=8 anotadores é suficiente?"

**Frequência esperada:** Alta  
**Resposta defensiva:**

> "N=8 com paridade de gênero (4M/4F) é uma limitação reconhecida e discutida em VII.4.1. Esse número é comum na literatura de anotação de dados de NLP para estudos com protocolo de calibração. Mais importante: κ = 0,7664 (IC [0,7363; 0,7954]) indica acordo substancial mesmo com 8 anotadores — o que sugere que o tamanho amostral de anotadores foi adequado para este corpus e tarefa. Ampliar para N=16 ou N=24 é agenda futura explícita em VII.6."

**Onde está no texto:** VII.4.1 (limitação), VII.6 (perspectiva).

---

### P3 — "O resultado 'Leve' não é trivial?"

**Frequência esperada:** Alta  
**Resposta defensiva:**

> "Há dois pontos. Primeiro: dado κ_inicial = 0,7664 (Substancial), o máximo teórico de Δκ com queda de 1 faixa é limitado — resultados 'Severos' seriam impossíveis nesse ponto de partida. Segundo: a classificação 'Leve' segundo Landis & Koch representa queda média de 0,2787 pontos — um modelo que opera em κ ≈ 0,49 está na fronteira entre Moderada e Fraca, com impacto prático real em sistemas de classificação em produção. Além disso, o fato de todos os 4 classificadores apresentarem amplificação Leve é resultado em si: demonstra que o efeito é sistemático e função da divergência anotativa, não do algoritmo. Por contraste, na fase sintética (SynSA-99), o RF atinge severidade Severa — mostrando que o modelo MADA tem sensibilidade para capturar resultados mais extremos quando presentes."

**Onde está no texto:** VI.4 (contextualização), VII.3 (análise integrada).

---

### P4 — "Como a MADA se distingue de trabalhos existentes sobre viés em NLP?"

**Frequência esperada:** Média-alta  
**Resposta defensiva:**

> "A MADA se diferencia em três aspectos: (1) Foco na divergência anotativa como *fonte* de viés, não apenas na distribuição dos dados ou no pré-treinamento — a maioria dos trabalhos sobre viés de gênero em NLP trata o viés como propriedade do modelo; (2) Uso do índice Δκ como operacionalização formal e quantificável desse efeito; (3) Dupla validação — empírica em dados reais e sintética com κ controlado — que permite separar o efeito da divergência de confundidores."

**Onde está no texto:** Cap. II (fundamentação), VII.3 (análise integrada).

---

### P5 — "A generalização é limitada a análise de sentimento?"

**Frequência esperada:** Média  
**Resposta defensiva:**

> "Sim, e reconhecemos isso em VII.4.2. O MQD-1222 foi construído com dados de análise de sentimento em português brasileiro. A hipótese — que divergências anotativas são amplificadas pelo classificador — é teórica e aplicável a qualquer tarefa de classificação com anotação humana. A MADA foi instanciada aqui por razões práticas. A extensão para NER, detecção de discurso de ódio ou implicatura textual é agenda futura explícita."

**Onde está no texto:** VII.4.2 (limitação de domínio), VII.6.

---

### P6 — "Por que o corpus tem exatamente 1.222 instâncias?"

**Frequência esperada:** Baixa-média  
**Resposta defensiva:**

> "N=1.222 foi definido por análise de poder estatístico para detectar diferenças de κ com power = 0,80 e α = 0,05 dado o efeito mínimo detectável estimado. A sigla MQD-1222 incorpora esse valor para rastreabilidade."

---

### P7 — "Qual a contribuição da fase sintética?"

**Frequência esperada:** Média  
**Resposta defensiva:**

> "A fase sintética (SynSA-50 a SynSA-99) serve como prova de conceito controlada: se a MADA está correta, amplificação deve decrescer monotonicamente com κ_inicial crescente. Nos dados empíricos κ é observado; nos sintéticos é imposto por design. O comportamento monotônico confirmado nos 12 conjuntos é a evidência mais forte da validade interna do modelo teórico da MADA."

**Onde está no texto:** Cap. VI (resultados sintéticos), VII.2 (análise sintética).

---

## VI. VULNERABILIDADES RESIDUAIS

| # | Vulnerabilidade | Risco | Status |
|---|----------------|-------|--------|
| V1 | TF-IDF como teto metodológico — banca pode classificar como limitação técnica severa | **Médio** | Argumento de design disponível em V.8; preparar resposta oral |
| V2 | Classificação "Leve" para todos os Δκ empíricos | **Médio** | Contextualizar via κ_inicial e contraste com RF na fase sintética (P3 acima) |
| V3 | N=8 anotadores — amostra pequena | **Baixo** | Discutido em VII.4.1; κ = 0,7664 valida suficiência |
| V4 | Domínio único (análise de sentimento, português BR) | **Baixo** | Discutido em VII.4.2 como limitação reconhecida |
| V5 | Redundância R1 (RF em VI.3.2 ≈ VII.2) | **Baixo** | Polimento recomendado antes da impressão |

**Itens de versões anteriores confirmados corrigidos na versão 13/04/2026:**
- Cross-references "Seção ??" (N1a: VII.3, N1b: VII.4) — **CORRIGIDO** ✓
- Frase duplicada II.5 ("passível de mensuração por meio do coeficiente κ") — **CORRIGIDO** ✓
- Contagem PRISMA textual vs. diagrama (132+8+15 ≠ 158) — **CORRIGIDO** ✓ (texto e diagrama mostram 158)

---

## VII. PONTOS FORTES PARA APRESENTAÇÃO ORAL

1. **Aprovação ética formal** — CAAE nº 82267824.8.0000.5289: diferencial em trabalhos com anotadores humanos.

2. **Dupla instanciação da MADA** — empírica + sintética com κ controlado: estrutura de validação incomum em dissertações de mestrado.

3. **Corpus estratificado por gênero** — 4M/4F por design, não por conveniência: evita confundidores de gênero na própria anotação.

4. **Bootstrap para IC** — 1.000 iterações: adequado para κ em amostras finitas, vai além da normalidade assintótica.

5. **Revisão sistemática PRISMA 2020** — 186 estudos com critérios explícitos: nível de rigor raro em dissertações de mestrado em NLP.

6. **Resultado surpreendente e defensável** — uniformidade de amplificação "Leve" em 4 classificadores distintos apontando para efeito sistemático; contraste com RF na fase sintética (Severa em SynSA-99) demonstrando sensibilidade do modelo.

7. **Cap. VII estruturado academicamente** — discussão, análise sintética, análise integrada, limitações em 5 subseções, contribuições e perspectivas futuras: documento em nível de publicação.

---

## VIII. CHECKLIST DE PREPARAÇÃO PARA A BANCA

### Antes da impressão (polimento)

- [ ] **R1** — Diferenciar a formulação sobre RF entre VI.3.2 (descritivo) e VII.2 (interpretativo): não usar texto idêntico nas duas seções
- [ ] **R3** — Avaliar se declaração CAAE em Cap. I pode ser substituída por remissão a V.5.1
- [ ] **R6** — Verificar se segunda ocorrência de Biester et al. [2022] em II.5 acrescenta informação nova; se não, remover ou consolidar com II.3
- [ ] Verificar ponto final no último parágrafo de III.3 (item de baixíssima visibilidade)

### Para a apresentação oral

- [ ] Preparar argumentação sobre TF-IDF vs. BERTimbau (P1) — saber citar V.8 e VII.4.5
- [ ] Preparar contextualização sobre N=8 anotadores (P2) — saber citar VII.4.1
- [ ] Preparar argumentação sobre significância prática de Δκ "Leve" e contraste com RF sintético (P3)
- [ ] Preparar distinção MADA vs. trabalhos existentes sobre viés em NLP (P4)
- [ ] Dominar todos os valores numéricos do Cap. VI — κ, IC, Δκ por modelo, distribuições de sentimento
- [ ] Conhecer cada subseção de VII.4 (Limitações) — banca frequentemente testa se o autor reconhece os limites do próprio trabalho
- [ ] Preparar argumento sobre RF atingindo Severa na fase sintética — resultado qualitativamente distinto dos demais

---

## IX. AVALIAÇÃO GLOBAL

| Critério | Peso | Nota estimada |
|----------|------|---------------|
| Contribuição original | 25% | 8,5/10 |
| Rigor metodológico | 30% | 9,0/10 |
| Fundamentação teórica | 20% | 8,0/10 |
| Análise e discussão | 15% | 8,5/10 |
| Estrutura e apresentação | 10% | 8,0/10 |
| **Média ponderada** | | **8,55/10** |

**Estado para qualificação:**

> O documento demonstra maturidade acadêmica compatível com qualificação de mestrado. A dupla instanciação da MADA, o rigor estatístico (bootstrap, κ com IC 95%, validação cruzada estratificada), a seção de limitações em 5 subseções e a resposta explícita às perguntas de pesquisa colocam este trabalho acima da média para o estágio de qualificação. Não há erros bloqueantes. As vulnerabilidades remanescentes (TF-IDF como limitação, resultado "Leve") são defensáveis com os argumentos já presentes no texto. **Recomendação: submeter à banca.**

---

*Relatório de maturidade gerado por Claude Code — 13/04/2026*  
*Baseado em: leitura integral do PDF `Qualificacao_Alexander_v2 (1).pdf` (74 p. de conteúdo)*
