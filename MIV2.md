# Saídas do Claude Code — Sessão de 07/04/2026 (manhã)

> Arquivo gerado automaticamente para continuidade no VSCode.

---

## Review Completo da Dissertação

I now have a complete picture of the dissertation. Here is the full multi-perspective review following the academic-paper-reviewer protocol.

---

## Phase 0: Reviewer Configuration Card

**Paper:** "Da Anotação ao Modelo: Amplificação de Viés de Gênero em Aprendizado Supervisionado para Análise de Sentimentos"
**Field:** NLP Fairness / Computational Linguistics
**Paradigm:** Quantitative experimental — dual instantiation (empirical + synthetic)
**Maturity:** V0 draft — PRISMA review incomplete, Section III.2 struck through
**Recommended venue tier:** ACL/EMNLP workshop (GeBNLP), TALLIP (ACM), or JMLR

| # | Role | Configured Identity |
|---|------|---------------------|
| EIC | Editor-in-Chief | Senior editor of a venue focused on NLP fairness (e.g., GeBNLP@ACL); expertise in bias measurement and dataset science |
| R1 | Methodology Reviewer | Specialist in inter-annotator agreement, experimental design for text classification, and statistical inference |
| R2 | Domain Reviewer | Expert in NLP bias research, sentiment analysis, and annotation science for low-resource languages |
| R3 | Perspective Reviewer | Social computing / HCI researcher focused on sociotechnical consequences of AI fairness |
| DA | Devil's Advocate | Challenges core causal claims, tests logical consistency, identifies alternative explanations |

---

## Phase 1: Independent Review Reports

---

### EIC Review

**Journal Fit:** Good fit for GeBNLP workshop (ACL/EMNLP), TALLIP (ACM), or a Portuguese-language venue with an international track. With significant revision, potentially suitable for a main venue short paper.

**Originality:** The MIVA framework is a genuine contribution. The dual-instantiation design (real + synthetic) is creative and well-motivated. Focus on Brazilian Portuguese annotation bias is genuinely understudied — the positioning gap shown in Table III.4 is convincing.

**Overall quality:** The paper is clearly structured and well-written. However, as a V0, it has several incomplete elements that must be resolved before submission: the PRISMA flowchart is explicitly marked *"até o momento"* (in progress), Section III.2 is struck through, and the practical guidelines promised in Section I.4.4 are never delivered in the conclusions.

**Recommendation: MAJOR REVISION**

---

### Reviewer 1 (Methodology) — Research Design and Statistical Validity

**Strengths:**
- The paired comparison design (identical experimental conditions, only label source varies) is internally sound and allows clean causal attribution
- Bootstrap-based CIs for Δκ are appropriate; preserving pairing during resampling is correct
- Stratified K-fold with shared splits eliminates partitioning as a confound
- Synthetic study with parameterized γ is elegant and provides structural insight
- The choice of N=999 (divisible by 3) to ensure perfect class balance without rounding is well-motivated

**Weaknesses:**

**[CRITICAL] W1.1 — Only 4 annotators per group**
This is the most serious methodological limitation. With 4 annotators per group, no statistical test can confirm that the observed inter-group difference (κ_inicial = 0.7652) reflects gender rather than individual variation. A single idiosyncratic annotator could drive group majority labels for many instances. Within-group κ (κ_mm and κ_ff) is never reported, making it impossible to assess intragroup consistency. The paper's claims about gender-based patterns cannot be supported at this sample size.

*Required fix:* Report within-group κ for male and female annotators. Perform sensitivity analysis removing one annotator at a time. Reframe conclusions from "gender bias" to "divergence between two annotation groups stratified by gender."

**[CRITICAL] W1.2 — No null amplification baseline**
The paper does not demonstrate that Δκ > 0 exceeds what would be expected by construction. If two classifiers are trained on two different label sets (κ_inicial < 1), some reduction in κ_modelos is mathematically expected — even for perfectly calibrated classifiers. The paper needs a theoretical or empirical lower bound showing that the observed Δκ is larger than this mathematical baseline.

*Required fix:* Add a "trivial baseline": compute the expected κ_modelos if each classifier simply replicates its training labels (without any generalization). Compare empirical κ_modelos to this bound.

**[CRITICAL] W1.3 — No classifier performance metrics**
The paper argues that accuracy is not the goal, but provides zero information about how well classifiers perform on the sentiment task. A classifier barely above chance may show artificial Δκ patterns driven by random label fluctuation rather than systematic learned behavior.

*Required fix:* Report macro-F1 and per-class precision/recall for all four classifiers on the MQD-1209 task. Examine whether Δκ correlates with classifier performance.

**[MAJOR] W1.4 — TF-IDF scope**
The deliberate choice of TF-IDF over pre-trained representations is methodologically justified for causal attribution. However, the claim that results generalize to modern NLP is significantly weakened, since transformer-based models dominate practice. The amplification mechanism in architectures with pre-trained representations (BERT, BERTimbau) may differ substantially.

**[MAJOR] W1.5 — Single dataset and single domain**
The entire empirical study rests on 1,209 instances from a single blog (*Meu Querido Diário*) in a single domain (informal personal diary). Generalization claims are unsupported.

**[MINOR] W1.6 — κ_modelos averaging**
The paper reports κ_modelos as the arithmetic mean of five fold-level κ values. While the paper also computes κ on concatenated out-of-fold predictions for Cramér's V, the relationship between these two estimates is not always clearly distinguished in the notation.

---

### Reviewer 2 (Domain) — Literature Coverage and Theoretical Contribution

**Strengths:**
- Related work comprehensively covers annotator bias, gender bias in NLP, and amplification through to 2024
- Table III.4 is a well-constructed comparison that clearly maps the gap this work fills
- Bilingual search strategy is explicitly justified and appropriate

**Weaknesses:**

**[MAJOR] W2.1 — Missing engagement with "learning from disagreement" literature**
The paper's core premise — that disagreement is legitimate interpretive variation, not noise — is the defining claim of the *perspectivist NLP* movement (Uma et al. 2021, Plank 2022, Leonardelli et al. 2021). These works are not cited. The MIVA's majority vote aggregation is a specific design choice with theoretical implications (aggregating discards the very signal the paper claims to study). The paper should engage with this literature and justify why majority vote was chosen over soft labeling or individual label preservation.

**[MAJOR] W2.2 — Binary gender framing undertheorized**
Devinney et al. [2022] is cited but not substantively engaged. The binary treatment of gender is operationally necessary but theoretically problematic — the paper should explicitly discuss what is lost by framing gender as binary, and acknowledge that the annotator pool's homogeneity (in terms of other sociodemographic variables) limits the interpretation.

**[MAJOR] W2.3 — "Bias amplification" terminology conflation**
The paper uses "amplificação de viés" but Δκ measures *divergence between two model groups*, not bias in the fairness sense (differential treatment of protected attributes in input text). The connection to standard fairness metrics (demographic parity, equalized odds, calibration across groups) is never made. Reviewers at fairness venues will flag this disconnect.

*Required fix:* Either connect Δκ to input-level fairness metrics (do models trained on M vs. F labels make systematically different predictions for texts with gender-marked content?), or reposition MIVA explicitly as measuring "annotator divergence propagation" distinct from standard bias metrics.

**[MAJOR] W2.4 — Section III.2 deletion weakens Portuguese motivation**
If the section on Portuguese linguistic patterns is removed, the paper loses its language-specific rationale. The introduction claims that Portuguese grammatical gender marking may intensify bias effects, but this is never empirically tested and the section supporting it is struck through.

**[MINOR] W2.5 — Missing: Uma et al. (2021), Plank (2022)**
These are foundational references for the paper's theoretical premise and must be included.

---

### Reviewer 3 (Perspective) — Cross-Disciplinary Implications

**Strengths:**
- IRB approval and ethics handling are exemplary
- The framing of disagreement as legitimate variation aligns with important trends in responsible AI
- The practical implication — that classifier choice is not bias-neutral — is actionable and well-articulated

**Weaknesses:**

**[MAJOR] W3.1 — Practical harm chain is absent**
The paper demonstrates Δκ > 0 but never shows *who is harmed* by this, or *how*. A sentiment system deployed in the real world uses a single model trained on a single label set — not two competing models. Under what conditions does the amplification of annotator divergence produce disparate real-world outcomes for users of different genders? This practical harm chain is the most important missing piece for a sociotechnical contribution.

**[MAJOR] W3.2 — Promised practical guidelines not delivered**
Section I.4.4 promises "diretrizes para design de protocolos de anotação que considerem divergências interpretativas" and "recomendações para mitigação de amplificação de viés em sistemas de PLN." These are absent from the conclusions.

**[MINOR] W3.3 — Annotator compensation not discussed**
The paper notes voluntary participation but says nothing about compensation. Given that the paper itself cites MIT Technology Review Brasil (2023) on the labor conditions of data annotation, this omission is notable.

**[MINOR] W3.4 — Female annotators' "neutral label" pattern underanalyzed**
The finding that the female group uses the neutral label 25% more often (363 vs. 290 instances) is interesting. Is this a gender effect, a label calibration style effect, or a response to the specific text selection? The paper describes this but does not analyze it deeply enough.

---

### Devil's Advocate Report

**Strongest Counter-Argument (200 words):**

The central claim — that supervised learning *amplifies* gender-based annotator divergence — rests on an operationalization that may produce Δκ > 0 as a mathematical artifact rather than as evidence of amplification. Here is the core argument: if two annotation groups disagree with each other at level κ_inicial < 1, and two separate classifiers are trained to predict each group's majority label, then those classifiers will necessarily disagree in their predictions — because they are optimized toward different targets. The degree of that disagreement (κ_modelos) depends on how well each classifier generalizes. If classifiers are perfectly accurate, κ_modelos approaches κ_inicial (no amplification). If classifiers are poor, they introduce prediction noise that *reduces* inter-model agreement below κ_inicial regardless of any amplification mechanism. The paper does not establish what κ_modelos *should be* under a null hypothesis of "no amplification beyond what is structurally expected," making it impossible to determine whether Δκ = 0.29 represents genuine amplification or classifier imperfection. The burden of proof requires a theoretical baseline or a "faithful replication" experiment demonstrating that Δκ exceeds the expected value under the null.

**Issue List:**

| Severity | # | Issue | Location |
|----------|---|-------|---------|
| CRITICAL | DA1 | Null hypothesis may be trivially satisfied by construction — no baseline for expected Δκ under null amplification | Ch. IV–V |
| CRITICAL | DA2 | Classifier performance not reported — cannot distinguish amplification from random prediction noise | Ch. V |
| CRITICAL | DA3 | 4 annotators per group cannot support between-group attribution — individual variation is uncontrolled | Ch. IV |
| MAJOR | DA4 | "Amplification" framing conflates divergence between models with input-level fairness bias | Ch. I, VI |
| MAJOR | DA5 | Synthetic study uses semantically null text — finding that label disagreement propagates through classifiers with random input is structurally trivial, not evidence of semantic amplification | Ch. IV.6 |
| MAJOR | DA6 | Cross-instantiation comparison (SynSA-85 as anchor) is post-hoc — κ_inicial is not the only relevant variable | Ch. V.3 |
| MINOR | DA7 | Section III.2 struck through — weakens Portuguese linguistic motivation | Ch. III.2 |
| MINOR | DA8 | Practical guidelines promised in I.4.4 not delivered | Ch. I, VI |
| MINOR | DA9 | 256 instances excluded due to ties — could introduce systematic selection bias | Ch. IV.5.1 |

**Ignored Alternative Explanations:**
- Classifiers trained on noisy labels may learn smoother decision boundaries (regularization effect), making their predictions more concentrated in majority classes, which reduces κ_modelos independently of amplification
- κ is sensitive to marginal class distributions; if classifiers trained on M vs. F labels learn different class priors, κ_modelos will decrease for distributional reasons unrelated to bias propagation
- The 25% difference in neutral label usage between groups could reflect a task calibration artifact (one group was annotated first or with slightly different instructions) rather than a gender effect

**Missing Stakeholder Perspectives:**
- The perspective of a system developer who needs to know *which* annotation group to use, and how to detect amplification prospectively, is not addressed
- Users of the deployed sentiment system are never considered

**"So What?" Test:**
A sentiment analysis system is typically trained once on one set of labels and deployed to all users. The MIVA measures divergence between *two hypothetical parallel deployments* trained on different gendered annotation sources. The practical scenario in which this matters — and which the paper never specifies — is either: (a) a system is retrained with a new annotation group and the old model is compared to the new, or (b) multiple models are aggregated and their inter-model disagreement harms users. Without specifying this scenario, the practical contribution remains abstract.

---

## Phase 2: Editorial Synthesis and Decision

### Consensus Issues (all or majority of reviewers agree)

| Issue | Reviewers | Priority |
|-------|-----------|----------|
| 4 annotators per group is insufficient | R1, DA (CRITICAL), EIC | P1 |
| No null amplification baseline | DA (CRITICAL), R1 (CRITICAL) | P1 |
| No classifier performance metrics | R1 (CRITICAL), DA (CRITICAL) | P1 |
| "Bias amplification" terminology conflicts with standard fairness definitions | R2, DA, R3 | P2 |
| PRISMA review incomplete / draft status | EIC, R2 | P2 |
| Practical guidelines promised but not delivered | R3, DA, EIC | P2 |
| Missing "learning from disagreement" / perspectivist NLP literature | R2 | P3 |
| Synthetic study's semantic limitations underacknowledged | DA, R1 | P3 |
| Practical harm chain absent | R3, DA | P3 |

### Divergent Opinions

- R1 and R3 disagree on whether the ethics handling is sufficient (R1 finds it adequate; R3 flags the compensation omission)
- EIC is more optimistic about venue fit than R2, who notes the terminology problem could be fatal at fairness venues

### Editorial Decision: **MAJOR REVISION**

---

## Editorial Decision Letter

Dear Alexander Ramos Feitosa,

Thank you for submitting "Da Anotação ao Modelo: Amplificação de Viés de Gênero em Aprendizado Supervisionado para Análise de Sentimentos." After review by five independent referees, the decision is **Major Revision**.

The MIVA framework is a genuine methodological contribution, and the dual-instantiation design is creative and well-motivated. The focus on Brazilian Portuguese is important and the gap identified in Table III.4 is convincing. However, the reviewers have identified several concerns — three of them critical — that must be addressed before the work can be recommended for acceptance.

---

### Revision Roadmap

**P1 (Critical) — Establish a null amplification baseline**
Demonstrate theoretically or empirically that the observed Δκ ≈ 0.29 exceeds what is expected by mathematical construction when classifiers are trained on divergent label sets. At minimum, compute the expected κ_modelos if each classifier perfectly reproduces its training labels (a "trivial replication" baseline) and show your empirical values exceed it. Without this, the amplification claim is not falsifiable.

**P2 (Critical) — Report classifier performance and its relationship to Δκ**
Report macro-F1, per-class precision/recall, and accuracy for all four classifiers on MQD-1209. Examine whether Δκ correlates with classifier accuracy. This is necessary to distinguish genuine amplification from prediction noise in low-performing classifiers.

**P3 (Critical) — Address the 4-annotators-per-group limitation**
- Report within-group κ for male (κ_mm) and female (κ_ff) annotators
- Perform a jackknife sensitivity analysis (leave-one-annotator-out) to show results are not driven by a single individual
- Reframe all claims from "gender bias" to "divergence between two annotation groups stratified by gender"
- Add explicit caveats about generalizability

**P4 (Major) — Clarify the relationship to standard fairness metrics**
Either: (a) connect Δκ to input-level fairness metrics by showing that models trained on male vs. female labels make systematically different predictions for texts with gender-marked content; or (b) reposition MIVA explicitly as measuring "annotator divergence propagation" and clearly distinguish this from bias in the standard algorithmic fairness sense.

**P5 (Major) — Complete the draft**
- Finalize the PRISMA review and update all "(até o momento)" annotations
- Decide on Section III.2 and, if removed, address the Portuguese linguistic motivation elsewhere
- Deliver the practical guidelines promised in Section I.4.4 in the conclusions

**P6 (Major) — Engage with perspectivist NLP literature**
Cite and engage with Uma et al. (2021) "Learning from Disagreement: A Survey" and Plank (2022) on perspectivist NLP. Justify the majority vote aggregation in light of alternatives (soft labels, per-annotator models).

**P7 (Major) — Acknowledge the synthetic study's semantic limits**
The synthetic placeholder text study demonstrates *structural* propagation of label disagreement through classifiers, not *semantic* amplification of gender-related language patterns. This distinction must be made explicit in the discussion. The synthetic study validates the structural model; it does not demonstrate the same mechanism in real NLP tasks.

**P8 (Minor) — Add practical harm chain**
Specify at least one concrete deployment scenario where Δκ > 0 produces demonstrably different outcomes for real users — this is the "so what?" the contribution requires.

**P9 (Minor) — Deepen the neutral label analysis**
The finding that the female group uses the neutral label 25% more often is one of the most interesting empirical results. Add qualitative or statistical analysis of which types of instances drive this pattern.

---

### Scores

| Dimension | Score (0–100) |
|-----------|--------------|
| Originality | 72 |
| Methodology rigor | 52 |
| Domain contribution | 66 |
| Writing clarity | 76 |
| Statistical validity | 58 |
| Practical impact | 48 |
| **Overall** | **62** |

---

## Phase 2.5: Revision Coaching

Since the decision is Major Revision, I'd like to guide you through the most impactful revisions before you write.

**Step 1 — What surprised you most?**
My expectation is the Devil's Advocate's point surprised you most: "Δκ > 0 may be a mathematical artifact." Before dismissing it, ask yourself: if each of your four classifiers *perfectly* reproduced its training labels (zero generalization error), what would κ_modelos equal? It would equal κ_inicial. So perfect classifiers produce zero amplification. Your classifiers are *not* perfect — they generalize. How does imperfect generalization interact with label disagreement to produce Δκ? This is the null baseline you need.

**Step 2 — The 4-annotator constraint**
You can't collect more annotations now. But you *can* reframe. The key move: stop claiming the study measures gender bias in the population and instead claim it measures "the behavior of MIVA when applied to two balanced annotation groups stratified by self-declared gender in the MQD-1209 context." This is honest, defensible, and still publishable. The within-group κ analysis is essential — if κ_mm and κ_ff are high, you can argue that group-level majority labels are stable; if they're low, you have a problem.

**Step 3 — If you could change only three things:**
I suggest: (1) add the null baseline experiment — this addresses the most fundamental objection; (2) add within-group κ and jackknife analysis — this addresses the small-N concern without new data collection; (3) report classifier performance and correlate with Δκ — this adds a missing dimension that will satisfy most methodological reviewers.

**Step 4 — Responding to the DA's "so what?" challenge**
Think of a concrete scenario: *your institution deploys a sentiment classifier trained on annotations from Group A. One year later, Group B annotates an update. The two models now serve different user populations.* Can you show — even on MQD-1209 — that instances where the two models disagree are not random, but systematically relate to specific semantic features? That would make the practical implication concrete.

---

*Review conducted using the academic-paper-reviewer skill (v1.7). Output is a separate review document — the manuscript has not been modified.*

---

## Análise e Proposta de Estrutura — Fundamentação Teórica

Antes de propor a estrutura, deixa eu mapear o problema do Capítulo II atual.

**O que a versão atual tem:**
II.1 PLN → II.2 Análise de Sentimentos → II.3 Aprendizado de máquina → II.4 Rotulagem e anotação → II.5 Divergência e viés

**O problema:** a sequência vai do geral para o específico, mas não constrói a *cadeia lógica* que sustenta a MIVA. O leitor chega ao Capítulo IV sem entender *por que* a amplificação deveria ocorrer — apenas sabe que foi observada.

---

## Diagnóstico: o que está faltando

A dissertação faz três afirmações que precisam de sustentação teórica, e a versão atual só ampara parcialmente a terceira:

| Afirmação | Fundamento necessário | Status atual |
|-----------|----------------------|--------------|
| Discordância entre anotadores não é ruído — é variação interpretativa legítima | Epistemologia da anotação / NLP perspectivista | Apenas mencionado (p.9) |
| Gênero afeta sistematicamente a interpretação em tarefas subjetivas | Sociolinguística + literatura de viés de anotador | Parcialmente na seção III |
| Aprendizado supervisionado *amplifica* (não apenas preserva) divergências | Teoria de generalização indutiva + amplificação em ML | **Ausente do cap. II** |

---

## Estrutura proposta para o Capítulo II

A lógica que recomendo é a de um *pipeline causal* — a mesma ordem em que o fenômeno acontece na prática:

```
Texto → Anotação → Rótulo → Treinamento → Modelo → Viés amplificado
```

Cada seção deve responder a uma pergunta, e a resposta da última deve ser: *"é exatamente isso que a MIVA mede."*

---

### II.1 — Classificação de Textos e Análise de Sentimentos
**Pergunta:** *Qual é a tarefa que estudamos e por que ela é subjetiva?*

Foco estreito — não é uma introdução geral ao PLN. Apresentar:
- Classificação de textos como tarefa supervisionada de mapeamento texto → categoria
- Análise de sentimentos como subtarefa cuja natureza é **inerentemente subjetiva**: não há um rótulo objetivamente correto, há múltiplas leituras plausíveis
- Isso distingue AS de tarefas objetivas (ex: reconhecimento de entidades nomeadas) — e é essa subjetividade que torna o problema da anotação relevante

> **Por que essa ordem:** estabelece a motivação para todo o restante. Sem subjetividade, discordância entre anotadores é erro puro; com subjetividade, é informação.

---

### II.2 — Aprendizado Supervisionado e o Papel dos Rótulos
**Pergunta:** *O que o modelo aprende, e qual é o papel central dos rótulos?*

Apresentar:
- O processo de aprendizado supervisionado como **ajuste de uma função de mapeamento** a partir de pares (texto, rótulo)
- O pressuposto implícito: o rótulo é uma *proxy* da verdade — o modelo aprende o que os rótulos dizem, não o que o texto "realmente" é
- O mecanismo de generalização indutiva: o modelo extrapola padrões do treino para dados não vistos
- Consequência crítica: **se os rótulos carregam uma perspectiva particular, o modelo generalizará essa perspectiva**

> **Por que aqui:** essa seção faz a ponte entre "o que o modelo faz" e "por que a fonte dos rótulos importa." Sem isso, a motivação da MIVA parece arbitrária.

---

### II.3 — Anotação Humana como Prática Interpretativa
**Pergunta:** *De onde vêm os rótulos, e por que o processo é social — não técnico?*

Esta é a seção mais importante do capítulo. Apresentar:

**II.3.1 — O processo de anotação**
- Anotação como tradução de um julgamento humano para uma categoria discreta
- Fontes de variação: ambiguidade linguística, contexto cultural, experiência prévia, identidade social do anotador

**II.3.2 — A virada epistemológica: da discordância como erro à discordância como informação**
- Paradigma clássico: discordância = ruído a minimizar (maximizar IAA)
- Paradigma perspectivista (Uma et al. 2021; Plank 2022; Havens et al. 2022): discordância entre anotadores pode refletir variação interpretativa genuína — especialmente em tarefas subjetivas
- Esta dissertação adota a visão perspectivista: **divergência anotativa é o objeto de análise, não um artefato a eliminar**

**II.3.3 — Identidade social e anotação**
- Evidência empírica de que características demográficas afetam sistematicamente os rótulos atribuídos (Ding et al. 2022; Geva et al. 2019; Biester et al. 2022)
- Gênero como eixo de diferenciação: padrão de maior uso da classe neutra por anotadoras femininas em contextos de ambiguidade semântica

> **Por que aqui:** coloca a fonte da divergência antes da métrica que a mede. O leitor entende *de onde* vem a divergência antes de ver como ela é quantificada.

---

### II.4 — Mensuração de Divergência Anotativa
**Pergunta:** *Como quantificamos a discordância entre fontes de rotulagem?*

Apresentar:
- O coeficiente κ de Cohen como métrica central: fórmula, interpretação, por que desconta o acaso
- As faixas de Landis & Koch como escala qualitativa
- Limitações do κ (sensibilidade a distribuições marginais, pressuposto de independência dos julgadores) — e por que isso importa para a MIVA
- Métricas complementares: V de Cramér, estatística χ²
- A distinção entre **concordância intra-grupo** (κ_mm, κ_ff) e **concordância inter-grupo** (κ_inicial) — chave para interpretar os resultados do Cap. V

> **Por que aqui:** o κ é o instrumento de medida central da MIVA. Apresentá-lo antes da metodologia permite que o leitor entenda o Cap. IV sem interrupções explicativas.

---

### II.5 — Viés em Sistemas de PLN: Conceitos e Taxonomia
**Pergunta:** *O que é viés em PLN e de onde ele vem?*

Apresentar:
- Definições de viés: distinção entre viés como *representação distorcida nos dados* vs. viés como *comportamento diferenciado do modelo em relação a atributos protegidos*
- Fontes de viés no pipeline de AM: dados de entrada, processo de anotação, arquitetura do modelo, métricas de avaliação (Hovy & Prabhumoye 2021; Shah et al. 2020)
- Viés de gênero especificamente: evidências de que sistemas de AS classificam diferentemente sentenças com marcadores femininos (EEC; Gupta et al. 2024)
- A limitação conceitual da abordagem binária de gênero (Devinney et al. 2022) — **esta seção deve reconhecer explicitamente o que a operacionalização binária não captura**

> **Por que aqui:** o viés é o *consequente* — o que emerge do processo descrito nas seções anteriores. Colocá-lo antes da amplificação cria a lógica "viés existe → e pode ser intensificado."

---

### II.6 — Amplificação de Divergência no Aprendizado Supervisionado
**Pergunta:** *Por que o aprendizado supervisionado não apenas preserva, mas intensifica divergências anotativas?*

Esta seção é a que está **completamente ausente** do capítulo atual — e é a que mais diretamente sustenta a MIVA.

Apresentar:
- O conceito de **amplificação de viés** em ML: modelos treinados em dados tendenciosos tendem a exacerar as associações presentes além do que os dados brutos indicam (Zhao et al. 2017; Minatel et al. 2023)
- O mecanismo teórico: generalização indutiva amplifica padrões sistemáticos e atenua ruído aleatório — e divergências interpretativas entre grupos são, do ponto de vista do modelo, padrões sistemáticos
- A distinção entre três regimes: **atenuação** (κ_modelos > κ_inicial), **preservação** (κ_modelos ≈ κ_inicial) e **amplificação** (κ_modelos < κ_inicial)
- Por que arquiteturas de conjunto (Random Forest) tendem a amplificar mais que modelos lineares — teoria de agregação de votos e fronteiras de decisão

> **Por que aqui, por último:** fecha o ciclo teórico. Após entender a tarefa (II.1), os rótulos (II.2), a anotação (II.3), como medir divergência (II.4) e o que é viés (II.5), o leitor está pronto para entender *por que a amplificação é esperada* — o que torna a MIVA não apenas uma observação empírica, mas uma investigação teoricamente fundamentada.

---

## Estrutura final resumida

```
II.1  Classificação de Textos e Análise de Sentimentos
      └─ Por que subjetividade importa

II.2  Aprendizado Supervisionado e o Papel dos Rótulos
      └─ O modelo aprende a perspectiva de quem rotulou

II.3  Anotação Humana como Prática Interpretativa
      ├─ II.3.1  O processo de anotação
      ├─ II.3.2  Discordância como informação (virada perspectivista)
      └─ II.3.3  Identidade social e padrões de anotação

II.4  Mensuração de Divergência Anotativa
      └─ Cohen's κ, Landis & Koch, V de Cramér

II.5  Viés em Sistemas de PLN
      └─ Definições, fontes, viés de gênero, limitação binária

II.6  Amplificação de Divergência no Aprendizado Supervisionado
      └─ Por que modelos intensificam o que anotadores insinuam
```

---

## Três referências que precisam entrar no cap. II

| Referência | Onde usar |
|-----------|-----------|
| Uma et al. (2021) — *Learning from Disagreement* survey | II.3.2 — fundação da virada perspectivista |
| Plank (2022) — *The "Problem" of Human Label Variation* | II.3.2 — argumento principal contra minimização de IAA |
| Zhao et al. (2017) — *Men Also Like Shopping* | II.6 — mecanismo de amplificação com evidência empírica |

---

Quer que eu comece a redigir uma das seções específicas?

---

## Capítulo II — Fundamentação Teórica (texto gerado)

## Capítulo II — Fundamentação Teórica

Este capítulo apresenta os fundamentos conceituais que sustentam a investigação proposta, organizados segundo uma cadeia lógica que acompanha o próprio percurso do fenômeno estudado: da tarefa que motiva a pesquisa, passando pelo processo que produz os dados, até o mecanismo pelo qual divergências interpretativas se propagam e se intensificam ao longo do aprendizado supervisionado. Cada conceito introduzido prepara o terreno para o seguinte, de modo que a metodologia apresentada no Capítulo IV possa ser compreendida não apenas como um protocolo experimental, mas como uma resposta direta às questões teóricas aqui levantadas.

O ponto de partida é a natureza da tarefa investigada. A análise de sentimentos consiste em atribuir polaridade afetiva — tipicamente classificada como positiva, negativa ou neutra — a unidades textuais que expressam opiniões, avaliações ou relatos experienciais. Diferentemente de tarefas de classificação mais objetivas, como o reconhecimento de entidades nomeadas ou a detecção de idioma, a análise de sentimentos opera sobre um terreno inerentemente subjetivo: um mesmo texto pode admitir múltiplas leituras igualmente defensáveis, a depender do contexto pragmático, da sensibilidade semântica do leitor e de sua experiência sociocultural acumulada. Essa característica não é uma imperfeição do processo de anotação, mas uma propriedade constitutiva da linguagem natural. Como observam Kenyon-Dean et al. [2018], aproximadamente um terço dos itens em corpora de análise de sentimentos apresenta alta discordância entre anotadores humanos — não porque os anotadores errem, mas porque o texto genuinamente suporta interpretações divergentes. É precisamente essa multiplicidade de leituras legítimas que confere relevância teórica ao estudo da etapa de anotação.

A relevância da anotação decorre do funcionamento do aprendizado supervisionado. Nesse paradigma, um modelo é ajustado a partir de exemplos rotulados, aprendendo a generalizar a relação entre representações textuais e categorias semânticas para instâncias não vistas durante o treinamento. O mecanismo de generalização indutiva é, por construção, sensível à estrutura dos rótulos: o modelo extrai padrões estatísticos dos dados de supervisão e os projeta sobre o espaço de entrada. Isso implica uma consequência frequentemente subestimada na literatura aplicada — os rótulos não são uma janela neutra para a realidade; são uma mediação interpretativa que carrega as perspectivas, os valores e as categorias cognitivas de quem os atribuiu. Quando essa mediação é sistematicamente influenciada por características de quem anota, o modelo não aprende "o sentimento do texto": aprende "o sentimento do texto conforme interpretado por esse grupo particular de anotadores." A fonte dos rótulos de supervisão é, portanto, uma variável estrutural do pipeline de aprendizado — e não um detalhe operacional.

Compreender por que anotadores diferentes produzem rótulos diferentes exige reconhecer que a anotação humana é uma prática interpretativa, não um procedimento técnico neutro. Quando um indivíduo lê um texto e atribui uma categoria, ele mobiliza simultaneamente o conteúdo explícito do texto, sua familiaridade com o domínio, sua sensibilidade a nuances pragmáticas e sua identidade social — incluindo gênero, faixa etária, origem regional e capital cultural. Ainda que diretrizes de anotação possam padronizar critérios formais, não é possível neutralizar completamente a subjetividade interpretativa em tarefas que envolvem julgamento de polaridade afetiva. O resultado observável dessa subjetividade é a divergência anotativa: a variabilidade nos rótulos atribuídos por anotadores distintos a um mesmo conjunto de instâncias.

Durante muito tempo, a literatura de processamento de linguagem natural tratou essa divergência predominantemente como ruído a ser minimizado. O objetivo implícito dos protocolos de anotação era maximizar a concordância interanotadores, e instâncias de alta discordância eram frequentemente descartadas ou resolvidas por voto majoritário antes de qualquer análise. Essa abordagem repousa sobre um pressuposto ontológico específico: existe um rótulo correto para cada instância, e a discordância entre anotadores é desvio em relação a esse padrão ideal. Trabalhos recentes têm questionado esse pressuposto de forma sistemática. Uma et al. [2021], em uma revisão abrangente sobre aprendizado a partir da discordância, argumentam que tratar anotações divergentes como ruído implica descartar informação genuína sobre a estrutura subjetiva da tarefa. Plank [2022] vai além ao propor que a variabilidade dos rótulos humanos não é um problema a resolver, mas uma característica informativa que os modelos deveriam ser capazes de representar. Havens et al. [2022] formalizam essa perspectiva no âmbito específico do viés de gênero em anotação, desenvolvendo taxonomias que distinguem incerteza legítima de inconsistência operacional. Em consonância com essa linha de pesquisa, o presente estudo adota uma posição perspectivista: a divergência entre anotadores de grupos distintos não é tratada como imperfeição do processo, mas como o próprio objeto de investigação.

Essa reorientação epistemológica é especialmente relevante quando a divergência anotativa está associada a características demográficas dos anotadores. Há evidência crescente de que variáveis como gênero, idade e origem cultural afetam sistematicamente os padrões de rotulagem em tarefas subjetivas. Ding et al. [2022] demonstraram que essas características influenciam a percepção de polaridade e intensidade emocional em análise de sentimentos. Biester et al. [2022], em um estudo comparativo cobrindo quatro tarefas de PLN, identificaram diferenças consistentes de anotação associadas ao gênero — em particular, uma tendência de anotadores masculinos a atribuir rótulos mais polarizados em contextos de ambiguidade semântica moderada. Geva et al. [2019] mostraram que características do anotador individual podem ser tão determinantes para o rótulo resultante quanto o próprio conteúdo do texto. Esses achados indicam que, em tarefas subjetivas, a divergência entre grupos anotadores estratificados por gênero não é aleatória: ela reflete padrões interpretativos coletivos que emergem da interação entre a tarefa, o texto e a identidade social de quem anota.

Para que esses padrões possam ser investigados empiricamente, é necessário dispor de métricas que quantifiquem a concordância entre fontes de rotulagem de forma rigorosa. A medida mais amplamente utilizada para esse fim é o coeficiente κ de Cohen [Cohen, 1960], definido como

$$\kappa = \frac{p_o - p_e}{1 - p_e},$$

onde $p_o$ representa a proporção de concordância observada entre duas fontes e $p_e$ representa a concordância esperada ao acaso, estimada a partir das distribuições marginais das categorias. Ao descontar a concordância que seria obtida aleatoriamente, o coeficiente κ produz uma estimativa mais conservadora e interpretável do alinhamento efetivo entre duas fontes de rotulagem do que a simples taxa de concordância bruta. Valores próximos de 1 indicam concordância quase perfeita; valores próximos de 0, concordância equivalente ao acaso; valores negativos, concordância inferior à esperada por acaso. Landis e Koch [1977] propuseram uma escala interpretativa que organiza o coeficiente em seis faixas qualitativas — de *poor* ($\kappa < 0{,}00$) a *almost perfect* ($0{,}81 \leq \kappa \leq 1{,}00$) — amplamente adotada como referência na literatura de concordância interavaliadores. Complementarmente, o coeficiente V de Cramér e a estatística $\chi^2$ de independência fornecem medidas da magnitude e da significância da associação estatística entre duas distribuições de rótulos, independentemente das distribuições marginais. Essas métricas compõem o instrumental quantitativo central desta pesquisa: permitem estimar, em bases comparáveis, o grau de divergência interpretativa antes e depois do processo de modelagem supervisionada.

A existência de divergências sistemáticas associadas ao gênero dos anotadores insere-se em um problema mais amplo, extensamente documentado na literatura: o viés em sistemas de processamento de linguagem natural. Blodgett et al. [2020], em uma revisão crítica da literatura sobre viés em PLN, argumentam que o conceito é utilizado de forma heterogênea — ora referindo-se a representações distorcidas nos dados de treinamento, ora a comportamentos diferenciados dos modelos em relação a grupos sociais, ora a danos concretos produzidos por sistemas implantados. Para os fins desta pesquisa, adota-se uma definição processual: viés é compreendido como um efeito emergente do processo de construção, interpretação e uso dos dados, e não como atributo individual de anotadores ou de algoritmos isoladamente. Essa perspectiva é coerente com a proposta de Shah et al. [2020], que enquadra o viés preditivo como resultado sistemático da interação entre arquiteturas de modelos e recursos latentes presentes nos conjuntos de dados. Hovy e Prabhumoye [2021] identificam cinco fontes principais de viés em PLN — incluindo explicitamente o viés dos anotadores —, reforçando que a etapa de rotulagem não é anterior ou exterior ao problema do viés: ela é uma de suas origens constitutivas.

No contexto específico do viés de gênero, sistemas de análise de sentimentos têm demonstrado comportamento diferenciado em função de marcadores linguísticos associados ao feminino e ao masculino. Gupta et al. [2024] documentam, em ampla pesquisa sobre viés sociodemográfico em modelos de linguagem, que sistemas de análise de sentimentos exibem viés sistemático de gênero, classificando sentenças com marcadores femininos de forma consistentemente distinta. É importante reconhecer, contudo, que a operacionalização do gênero como variável binária — como a adotada neste estudo por razões metodológicas — apresenta limitações conceituais documentadas. Devinney et al. [2022] demonstram que, mesmo em pesquisas que reconhecem a multidimensionalidade do gênero, ele é consistentemente tratado como caso binário na prática experimental. Essa simplificação implica a invisibilização de identidades não binárias e pode mascarar a heterogeneidade interna de cada grupo. A adoção do recorte binário neste trabalho é, portanto, uma decisão instrumental justificada pela disponibilidade de anotadores e pela necessidade de controle experimental — e não uma afirmação ontológica sobre a natureza do gênero.

O problema central que esta pesquisa investiga não é, porém, a mera existência de divergências anotativas associadas ao gênero — fenômeno já documentado na literatura. O problema é o que acontece com essas divergências ao longo do pipeline de aprendizado supervisionado. Há razões teóricas para suspeitar que o processo de modelagem não apenas preserve as divergências presentes nos rótulos de treinamento, mas as intensifique. O mecanismo pode ser compreendido a partir das propriedades da generalização indutiva: ao ajustar seus parâmetros para minimizar o erro sobre o conjunto de treinamento, um classificador aprende a identificar e a explorar padrões estatísticos nos dados — incluindo padrões latentes de divergência interpretativa entre as fontes de supervisão. Quando dois modelos são treinados sobre os mesmos textos, mas com rótulos provenientes de grupos com perfis interpretativos distintos, cada um generaliza a partir de um sinal de supervisão diferente. As fronteiras de decisão aprendidas por cada modelo refletem as assimetrias estruturais presentes nos rótulos de seus respectivos grupos — e, ao generalizarem para instâncias não vistas, essas assimetrias podem se manifestar com magnitude superior à observada entre os próprios anotadores. Zhao et al. [2017] demonstraram empiricamente esse fenômeno em tarefas de PLN: modelos treinados com dados tendenciosos tenderam a exagerar as associações demográficas presentes no corpus original. Minatel et al. [2023] corroboraram esse padrão em tarefas de classificação binária, mostrando que efeitos discriminatórios nos rótulos se propagam e se intensificam ao longo do aprendizado supervisionado.

A propensão à amplificação não é, ademais, uniforme entre algoritmos. Modelos baseados em estruturas de conjunto — como o Random Forest, que agrega predições de múltiplas árvores de decisão por voto majoritário — tendem a reforçar padrões sistemáticos presentes nos rótulos de treinamento, amplificando inclusive pequenas assimetrias distribucionais que, em contextos de alta concordância entre as fontes, se concentram em regiões de fronteira de decisão e exercem impacto desproporcional sobre o comportamento preditivo. Modelos lineares, por operarem sobre projeções globais do espaço de atributos, são estruturalmente menos sensíveis a assimetrias locais e, consequentemente, tendem a exibir amplificação de menor magnitude. Essa diferença entre arquiteturas não é meramente empírica: ela decorre das propriedades indutivas de cada classe de algoritmos e constitui, por si mesma, uma dimensão analítica relevante para a compreensão do fenômeno.

É a partir desse conjunto articulado de conceitos — a subjetividade constitutiva da análise de sentimentos, a dependência do aprendizado supervisionado em relação à fonte dos rótulos, a anotação como prática interpretativa socialmente situada, a divergência anotativa como fenômeno mensurável por métricas de concordância, as origens e manifestações do viés de gênero em PLN e o mecanismo de amplificação de divergências pelo processo de modelagem — que a Metodologia de Identificação de Viés Amplificado, apresentada no Capítulo IV, encontra sua fundamentação. A MIVA não é, portanto, uma proposta arbitrária: é uma resposta metodológica direta à estrutura teórica aqui delineada, concebida para tornar o fenômeno da amplificação observável, mensurável e atribuível à sua origem.

---

## Capítulo III — Trabalhos Relacionados (texto gerado)

## Capítulo III — Trabalhos Relacionados

A investigação proposta nesta dissertação situa-se na interseção de três linhas de pesquisa que, embora distintas em seu desenvolvimento histórico, convergem para uma mesma questão: como as escolhas feitas durante a construção de dados rotulados se propagam e se transformam ao longo do pipeline de aprendizado supervisionado. Mapear esse território é condição necessária para identificar com precisão o que já foi estabelecido, o que permanece em aberto e de que forma a Metodologia de Identificação de Viés Amplificado responde a lacunas concretas do estado da arte.

---

### III.1 — A Anotação como Fonte Estrutural de Viés

O ponto de partida desta revisão é uma transformação epistemológica ainda em curso na literatura de PLN: a revisão do estatuto teórico da discordância entre anotadores. Durante décadas, o pressuposto dominante nos protocolos de anotação foi o de que existe um rótulo correto para cada instância — uma verdade de referência (*gold standard*) em relação à qual a discordância constitui desvio a ser minimizado ou eliminado. Aroyo e Welty [2015] foram dos primeiros a desafiar sistematicamente esse pressuposto, argumentando que a busca por um único rótulo consensual encobre sete mitos sobre a anotação humana — entre eles, o de que a discordância é sempre produto de ambiguidade ou incompetência. Em tarefas cognitivamente complexas e interpretativas, demonstram os autores, múltiplos rótulos conflitantes podem ser todos defensáveis, e o consenso artificial produzido pela agregação mascara informação valiosa sobre a estrutura subjetiva da tarefa.

Esse argumento ganhou substância empírica e sistemática com a revisão de Uma et al. [2021], que examina dezenas de estudos sobre aprendizado a partir da discordância (*learning from disagreement*) e demonstra que tratar anotações divergentes como ruído implica descartar exatamente o sinal que diferencia tarefas subjetivas de tarefas objetivas. Em vez de eliminar a variabilidade interanotadores, os autores propõem que modelos sejam treinados para capturá-la — seja por meio de distribuições suaves sobre rótulos, seja pela preservação de anotações individuais em vez de agregações majoritárias. Na mesma direção, Plank [2022] argumenta que o chamado "problema da variação de rótulos humanos" não é, em rigor, um problema: é uma característica informativa da linguagem natural que os sistemas de PLN deveriam ser capazes de representar, em vez de suprimir. A consequência prática dessa virada perspectivista é direta: se a discordância carrega informação, então a *fonte* dessa discordância — quem anota, com que identidade, a partir de que perspectiva — torna-se uma variável de primeira ordem na análise.

A cadeia de implicações entre anotação e viés foi formalizada por Blodgett et al. [2020] em uma revisão crítica da literatura sobre viés em PLN que permanece referência fundamental na área. Os autores demonstram que anotações tendenciosas podem ser incorporadas em conjuntos de dados desde seu início, e que sistemas treinados nesses dados herdam e frequentemente ampliam tais tendenciosidades. O argumento central é que tecnologia de linguagem é poder: as escolhas sobre o que anotar, quem anota e como os rótulos são consolidados não são decisões neutras — são decisões que inscrevem perspectivas particulares nas representações que os modelos irão aprender. Hovy e Prabhumoye [2021] complementam essa análise identificando cinco fontes estruturais de viés em sistemas de PLN — incluindo o viés do anotador como uma categoria autônoma, distinta do viés nos dados brutos e do viés algorítmico —, e argumentam que a negligência de qualquer uma dessas fontes compromete a validade dos modelos resultantes.

A resposta mais direta a esse diagnóstico tem sido a demanda por maior transparência no processo de anotação. Prabhakaran et al. [2021] defendem a publicação de rótulos ao nível do anotador individual, e não apenas de agregações, como condição necessária para compreender e mitigar vieses de anotação. Davani et al. [2022] demonstram empiricamente que ir além do voto majoritário — considerando a distribuição completa de rótulos individuais — melhora substancialmente a qualidade dos modelos em tarefas com alta variabilidade interpretativa. Paullada et al. [2021], em uma crítica mais ampla às práticas de construção de conjuntos de dados em aprendizado de máquina, argumentam que os dados são produtos culturais cujos conteúdos e lacunas refletem as condições sociais de sua produção — e que ignorar essas condições é uma forma de validar acriticamente as perspectivas dos grupos que participaram de sua construção. Raji et al. [2021] estendem essa crítica aos próprios *benchmarks* de avaliação, mostrando que as escolhas normativas neles incorporadas moldam silenciosamente o que conta como sucesso em PLN.

Esse conjunto de trabalhos estabelece com solidez o terreno conceitual sobre o qual a presente pesquisa se apoia: a anotação humana é uma prática interpretativa socialmente situada, a discordância entre anotadores é frequentemente legítima e informativa, e a fonte dos rótulos de supervisão é uma variável estrutural do pipeline de aprendizado — não um detalhe operacional. O que permanece menos explorado, e que as próximas seções abordam, é o papel específico do gênero como eixo de divergência anotativa e o que ocorre com essas divergências ao longo do processo de modelagem supervisionada.

---

### III.2 — Gênero como Eixo de Divergência Interpretativa

Se a literatura revisada na seção anterior estabelece que a identidade dos anotadores importa para os rótulos produzidos, uma segunda linha de pesquisa investiga de forma específica como o gênero — enquanto eixo de diferenciação social — estrutura padrões sistemáticos de divergência interpretativa em tarefas de classificação textual.

Um estudo fundamental nessa direção é o de Geva et al. [2019], que demonstraram que características do anotador individual — incluindo gênero, background educacional e estilo pessoal de anotação — podem ser tão determinantes para o rótulo atribuído quanto o próprio conteúdo do texto em tarefas de compreensão de linguagem natural. Os autores concluem que, em muitos casos, os modelos treinados nesses dados aprendem a simular o comportamento do anotador médio, não a compreender a tarefa — o que torna a composição demográfica do grupo anotador uma variável latente de primeira importância. Resultados convergentes foram obtidos por Ding et al. [2022] especificamente no domínio da análise de sentimentos: em um estudo sistemático sobre o impacto de características demográficas na rotulagem de dados de sentimento, os autores mostraram que gênero, idade e origem cultural afetam de forma mensurável e consistente a percepção de polaridade e intensidade emocional dos textos avaliados.

Biester et al. [2022] aprofundam essa evidência em escopo mais amplo, analisando o efeito do gênero dos anotadores em quatro tarefas distintas de PLN — incluindo análise de sentimentos — e identificando diferenças sistemáticas nos padrões de rotulagem, com tendência dos anotadores masculinos a atribuir rótulos mais polarizados em contextos de ambiguidade semântica moderada. Kumar et al. [2020], por sua vez, compararam o desempenho de modelos de análise de sentimentos treinados por grupos estratificados segundo critérios de idade e gênero, encontrando que a acurácia dos modelos femininos superava consistentemente a dos masculinos em uma tarefa de classificação de *ebooks* — resultado que os autores interpretam como evidência de diferenças nos padrões de expressão linguística e interpretação afetiva entre os grupos.

Essas diferenças não são necessariamente atribuíveis ao gênero como categoria biológica, mas ao gênero como posição social que molda trajetórias de socialização, acesso à linguagem e sensibilidades interpretativas — uma distinção que a literatura tem progressivamente incorporado. Stańczak e Augenstein [2021], em uma revisão abrangente sobre viés de gênero em PLN, documentam as limitações persistentes dos estudos na área, entre as quais se destacam a suposição binária de gênero e a escassez de estudos multilíngues. Devinney et al. [2022] examinam criticamente as teorias de gênero implícitas nas pesquisas sobre viés em PLN e demonstram que o gênero é consistentemente operacionalizado como variável binária mesmo quando os autores reconhecem sua natureza multidimensional — uma tensão que esta dissertação herda e explicita como limitação metodológica necessária.

No que diz respeito às consequências dessas diferenças para os sistemas implantados, a evidência é igualmente robusta. Kiritchenko e Mohammad [2018] desenvolveram o *Equity Evaluation Corpus* (EEC) — um conjunto de 8.640 sentenças em inglês especificamente construído para medir vieses em relação a raça e gênero em sistemas de análise de sentimentos — e encontraram que a análise de 219 sistemas comerciais e de pesquisa revelou viés estatisticamente significativo na grande maioria deles, com intensidades de sentimento sistematicamente distintas para sentenças com marcadores femininos e masculinos. Gupta et al. [2024], em uma revisão ainda mais abrangente sobre viés sociodemográfico em modelos de linguagem, documentam que sistemas de análise de sentimentos exibem viés sistemático de gênero de forma robusta e transversal a diferentes arquiteturas e idiomas, classificando sentenças com marcadores femininos de forma diferenciada — frequentemente associando-as a maior intensidade emocional negativa ou a menor assertividade.

Waseem [2016], em um contexto relacionado — o da detecção de discurso de ódio —, demonstrou que a identidade do anotador é determinante para os rótulos produzidos em tarefas subjetivas envolvendo linguagem ofensiva, e que a omissão dessa informação nos conjuntos de dados introduz vieses ocultos nos classificadores resultantes. O trabalho constitui um precedente metodológico importante para a presente pesquisa: ao tornar a identidade do anotador uma variável explícita de análise, em vez de uma fonte de variabilidade a ser controlada, abre-se espaço para investigar sistematicamente como essas diferenças se propagam no pipeline de aprendizado.

É precisamente nesse ponto que a segunda lacuna relevante se configura. Embora a literatura estabeleça com consistência que o gênero dos anotadores afeta os rótulos produzidos em tarefas subjetivas, a maioria dos estudos analisa esse efeito no plano dos dados — comparando as distribuições de rótulos entre grupos — sem investigar o que ocorre com essas diferenças quando os dados são utilizados como supervisão para treinar modelos. A pergunta sobre se as divergências interpretativas associadas ao gênero são preservadas, atenuadas ou amplificadas ao longo do processo de aprendizado supervisionado permanece, até o presente, sistematicamente inexplorada.

---

### III.3 — Amplificação, Propostas Recentes e o Caso do Português

A terceira linha de pesquisa relevante para esta dissertação é a que investiga especificamente o fenômeno de amplificação de viés em modelos supervisionados — isto é, a tendência de que assimetrias presentes nos dados de treinamento se manifestem nos modelos resultantes com magnitude superior à observada nos dados brutos.

O trabalho seminal nessa direção é o de Zhao et al. [2017], que demonstraram empiricamente que modelos de PLN treinados em dados tendenciosos tendem a exagerar as associações demográficas presentes no corpus original: em seu estudo sobre captioning de imagens, os modelos treinados em dados com viés de gênero amplificaram esse viés nas predições — associando atividades domésticas ao feminino com frequência ainda maior do que os dados de treinamento indicavam. A contribuição teórica central do trabalho é a distinção entre o viés presente nos dados e o viés amplificado pelo modelo: mesmo que os dados de entrada exibam assimetrias moderadas, o processo de generalização indutiva pode intensificá-las de forma substancial. Shah et al. [2020] situam esse fenômeno em um quadro conceitual mais amplo, propondo que vieses preditivos em PLN são resultado sistemático da interação entre a arquitetura dos modelos e recursos latentes presentes nos conjuntos de dados — o que implica que a amplificação não é um artefato acidental, mas uma propriedade emergente do processo de modelagem.

Minatel et al. [2023], em contexto mais próximo ao presente estudo, investigaram a propagação de efeitos discriminatórios em tarefas de classificação binária no contexto brasileiro, analisando como estratificações dos conjuntos de dados e distribuições de rótulos contribuem para a perpetuação e intensificação de padrões discriminatórios. Seus resultados corroboram a hipótese de que o aprendizado supervisionado não é um filtro que atenua o viés dos dados de entrada, mas um amplificador que pode reforçar padrões sistemáticos latentes. Lim et al. [2024] avançam nessa direção ao propor a análise de mediação causal como instrumento para identificar e mitigar o viés de anotação em tarefas de compreensão de linguagem natural — uma abordagem que trata a fase de anotação como variável mediadora entre o texto e o comportamento do modelo, e não como uma fonte de variabilidade residual. Essa reorientação metodológica é conceitualmente próxima à proposta da MIVA, embora opte por ferramentas de inferência causal em vez de métricas de concordância.

Propostas mais recentes têm explorado estratégias de mitigação do viés de anotação por duas vias principais. A primeira, representada por Toker et al. [2024], consiste na calibração inteligente dos anotadores: ajustes no processo de seleção e composição dos grupos anotadores, baseados em perfis demográficos, podem reduzir divergências sistemáticas sem comprometer a qualidade geral das anotações. A segunda, exemplificada por Sobhani e Delany [2024], aposta em técnicas de aumento de dados contrafactuais como mecanismo de mitigação: ao gerar variações dos textos originais com substituições controladas de marcadores de gênero, é possível reduzir a dependência dos classificadores em relação a esses marcadores sem sacrificar o desempenho na tarefa principal. Jiang et al. [2024], em contexto adjacente — a classificação de sexismo e misoginia — demonstram que os *datasets* existentes frequentemente falham em capturar a pluralidade de perspectivas dos anotadores, e que a incorporação explícita das atitudes e dos perfis dos anotadores no processo de treinamento produz modelos mais robustos e interpretativamente responsáveis. Zhu et al. [2024], por sua vez, investigam se modelos de linguagem pré-treinados compartilham o mesmo viés de gênero de seus anotadores, concluindo que há correspondência parcial e que o contexto em que as sentenças são avaliadas modula significativamente a manifestação do viés — o que sugere que a relação entre viés de anotação e viés de modelo é mediada por propriedades das representações aprendidas durante o pré-treinamento.

Em paralelo a essa agenda internacional, um conjunto emergente de estudos tem voltado atenção para as especificidades do português e do contexto brasileiro. Taso et al. [2023] investigaram a discriminação algorítmica de gênero em sistemas de PLN no Brasil, documentando viés sistemático e estatisticamente significativo em tarefas de análise de sentimento em português — o que estabelece evidência direta da relevância do problema no contexto nacional. Moreira et al. [2024], no desenvolvimento do FairPIVARA, demonstraram que características morfossintáticas do português brasileiro, incluindo o gênero gramatical pervasivo na língua, influenciam os padrões de viés em modelos de linguagem pré-treinados de forma distinta do que se observa em inglês — reforçando a necessidade de investigações linguisticamente situadas. Firmino et al. [2024] identificaram, em letras de músicas brasileiras, que o gênero feminino é frequentemente descrito por predicativos ligados à aparência física, enquanto o masculino é caracterizado por traços de personalidade — padrões que os modelos de AM podem aprender e perpetuar. Silva e Moro [2024], em contexto de literatura portuguesa, desenvolveram um *pipeline* de PLN para detecção de viés de gênero que evidencia como marcas linguísticas de gênero gramatical podem servir como proxies para estereótipos sociais internalizados pelos modelos.

O exame sistemático desse conjunto de trabalhos revela o ponto preciso em que a presente pesquisa se insere. A existência de viés de gênero em sistemas de análise de sentimentos está bem documentada. A influência do gênero dos anotadores sobre os rótulos produzidos é empiricamente estabelecida. O fenômeno de amplificação de viés pelo aprendizado supervisionado tem precedentes sólidos. E o contexto do português brasileiro tem recebido atenção crescente, ainda que incipiente. O que nenhum dos trabalhos revisados faz, porém, é combinar simultaneamente esses quatro elementos: investigar as divergências anotativas associadas ao gênero em português brasileiro, medir empiricamente se e em que grau essas divergências são amplificadas ao longo do pipeline de aprendizado supervisionado, e validar esse fenômeno tanto em dados reais quanto em um ambiente sintético controlado que permita isolar o efeito da fonte de anotação de todos os demais fatores experimentais. É exatamente essa lacuna que a Metodologia de Identificação de Viés Amplificado, descrita no capítulo seguinte, se propõe a preencher.

---

## Capítulo I — Introdução (texto gerado)

## Capítulo I — Introdução

O desenvolvimento de sistemas de processamento de linguagem natural baseados em aprendizado supervisionado repousa sobre uma dependência fundamental: a existência de dados rotulados de qualidade suficiente para que os modelos possam extrair padrões linguísticos generalizáveis. Essa dependência é tão constitutiva do paradigma que frequentemente passa despercebida como pressuposto — os rótulos são tratados, implicitamente, como representações neutras de uma realidade semântica objetiva, e o processo que os produz, como um estágio técnico anterior e exterior ao aprendizado propriamente dito. A pesquisa das últimas décadas tem, contudo, acumulado evidência robusta de que esse pressuposto é falso, com consequências que se estendem muito além do laboratório. Sistemas de análise de sentimentos classificam sentenças com marcadores femininos de forma sistematicamente distinta das que contêm marcadores masculinos. Modelos de linguagem treinados em corpora construídos por grupos demograficamente homogêneos reproduzem e frequentemente amplificam as perspectivas implícitas nesses grupos. A etapa de anotação — o momento em que seres humanos atribuem categorias a textos — não é o ponto de partida neutro de um pipeline objetivo: é o lugar onde perspectivas, identidades e estruturas sociais são inscritas nos dados que os modelos irão aprender a generalizar.

Esta dissertação parte dessa constatação e avança sobre uma questão que a literatura tem abordado de forma fragmentada: o que acontece, ao longo do aprendizado supervisionado, com as divergências interpretativas produzidas por grupos de anotadores com perfis distintos? Não se trata apenas de perguntar se grupos diferentes produzem rótulos diferentes — evidência que já existe — mas de investigar se o processo de modelagem preserva, atenua ou *intensifica* essas divergências quando as incorpora como supervisão. A distinção é analiticamente importante: um sistema que reproduz fielmente a divergência presente em seus dados de treinamento é distinto, em natureza e em implicações práticas, de um sistema que amplifica essa divergência além do que os próprios anotadores exibiam. No segundo caso, o pipeline de aprendizado não é um espelho dos dados — é um amplificador de assimetrias latentes.

O eixo social escolhido para investigar esse fenômeno é o gênero dos anotadores, operacionalizado como critério de estratificação em uma tarefa de análise de sentimentos em português brasileiro. A escolha é motivada por duas ordens de razões. A primeira é empírica: há evidência consistente na literatura de que o gênero afeta sistematicamente os padrões de rotulagem em tarefas subjetivas, com anotadoras femininas tendendo a maior cautela interpretativa diante de conteúdos de polaridade atenuada e anotadores masculinos tendendo a rótulos mais polarizados em contextos de ambiguidade semântica. A segunda é linguística: o português brasileiro, ao contrário do inglês, possui um sistema gramatical fortemente marcado por gênero, o que torna potencialmente mais visíveis os efeitos de diferenças interpretativas associadas a essa variável sobre modelos treinados na língua. A escassez de estudos sobre viés de anotação por gênero em português — documentada pela busca sistemática conduzida neste trabalho — confere ao recorte relevância empírica adicional.

Para investigar essa questão de forma rigorosa, esta dissertação propõe a Metodologia de Identificação de Viés Amplificado (MIVA), um protocolo analítico modular que opera sobre uma configuração experimental de paridade estrita: dois conjuntos de rótulos, provenientes de grupos anotadores distintos, são aplicados ao mesmo corpus textual, com a mesma representação de atributos, os mesmos hiperparâmetros de treinamento e a mesma semente aleatória. Qualquer diferença observada entre os modelos resultantes é, por construção, atribuível exclusivamente à fonte dos rótulos de supervisão. A metodologia estrutura-se em três módulos sequenciais: o primeiro estima a concordância inicial entre os grupos anotadores por meio do coeficiente κ de Cohen; o segundo realiza o treinamento pareado de classificadores e estima a concordância entre suas predições pela mesma métrica; o terceiro quantifica a amplificação como a diferença entre essas duas estimativas, cuja significância estatística é avaliada por reamostragem bootstrap.

A MIVA é avaliada por meio de duas instanciações complementares que respondem a perguntas distintas e mutuamente informativas. A primeira é um estudo empírico conduzido sobre o conjunto de dados MQD-1209 — composto por 1.209 instâncias em português brasileiro extraídas do blog *Meu Querido Diário* e anotadas por grupos equilibrados de quatro anotadores masculinos e quatro anotadoras femininas em regime de anotação independente. Essa instanciação verifica, em condições reais de anotação, se a divergência interpretativa associada ao gênero do anotador se manifesta e se amplifica ao longo do pipeline de aprendizado supervisionado. A segunda é um estudo sintético controlado, conduzido sobre doze cenários com taxas de concordância nominal parametrizadas no intervalo de 50% a 99%, no qual a única variável experimental manipulada é o grau de divergência entre as fontes de rotulagem. Essa instanciação caracteriza o comportamento estrutural do fenômeno sob controle paramétrico, permitindo avaliar como a magnitude da amplificação varia em função da concordância inicial e das propriedades indutivas de diferentes arquiteturas de classificação.

Os resultados obtidos nas duas instanciações fornecem evidência convergente de que a amplificação de divergências interpretativas é um fenômeno estrutural do aprendizado supervisionado, e não um artefato específico do conjunto de dados empírico. No estudo empírico, todos os quatro classificadores avaliados — Máquina de Vetores de Suporte, Naive Bayes, Random Forest e Regressão Logística — apresentaram redução sistemática e estatisticamente significativa da concordância intermodelos em relação à concordância inicial entre os grupos humanos, com Δκ médio de aproximadamente 0,29 pontos e intervalos de confiança de 95% que não cruzaram o valor zero em nenhum caso. No estudo sintético, o mesmo padrão se manifestou de forma robusta ao longo de toda a escala de concordância nominal investigada, com a magnitude da amplificação revelando dependência tanto do nível basal de divergência entre as fontes quanto das propriedades indutivas de cada algoritmo — o Random Forest exibindo consistentemente os maiores valores de amplificação, enquanto os modelos lineares e probabilísticos apresentaram comportamento mais estável e previsível.

Do ponto de vista das contribuições, este trabalho opera em quatro dimensões. No plano metodológico, formaliza um protocolo modular capaz de separar analiticamente três níveis distintos de divergência — a divergência humana inicial, a divergência induzida pelo processo de modelagem e a diferença entre ambas — tornando a amplificação um fenômeno mensurável e comparável entre contextos. No plano empírico, oferece evidência pioneira sobre divergências anotativas por gênero em análise de sentimentos para o português brasileiro, caracterizando os padrões distributivos de cada grupo e documentando quantitativamente o fenômeno de amplificação em classificadores clássicos de aprendizado de máquina. No plano teórico, os resultados reforçam a concepção do viés como fenômeno emergente do processo de construção e uso de dados — e não como atributo individual dos anotadores —, e demonstram que mesmo divergências moderadas entre fontes de anotação podem produzir efeitos estruturalmente relevantes nos modelos resultantes. No plano prático, os achados têm implicações diretas para o design de protocolos de anotação e para a seleção de algoritmos em pipelines que operam sobre dados com múltiplas fontes anotativas, sugerindo que a escolha do classificador não é indiferente ao risco de amplificação quando a divergência interpretativa entre grupos é esperada ou inevitável.

O estudo foi conduzido em conformidade com os princípios éticos aplicáveis à pesquisa envolvendo seres humanos. A participação dos anotadores foi voluntária, mediante consentimento informado, com garantia de anonimato e confidencialidade das informações coletadas. O gênero dos participantes foi autodeclarado e utilizado exclusivamente como critério de estratificação analítica, sem associação a qualquer outro dado pessoal identificável. O foco do estudo recai sobre as divergências oriundas do processo de anotação e sobre como essas divergências se manifestam no comportamento de modelos supervisionados — não sobre diferenças individuais ou grupais de capacidade cognitiva. O projeto foi aprovado pelo Comitê de Ética em Pesquisa sob o protocolo CAAE 82267824.8.0000.5289.

### I.1 — Organização da Dissertação

O restante desta dissertação está estruturado da seguinte forma. O Capítulo II estabelece os fundamentos teóricos que sustentam a investigação, articulando os conceitos de classificação textual supervisionada, anotação como prática interpretativa, mensuração de divergência anotativa, viés em sistemas de PLN e amplificação de divergências pelo aprendizado de máquina. O Capítulo III mapeia os trabalhos relacionados, organizando a literatura em torno das três linhas de pesquisa que convergem para o problema investigado: a anotação como fonte estrutural de viés, o gênero como eixo de divergência interpretativa, e os estudos sobre amplificação e mitigação de viés em contextos supervisionados. O Capítulo IV descreve em detalhe a arquitetura da MIVA — seus módulos, métricas, hipótese estatística e procedimentos operacionais —, bem como as duas instanciações conduzidas e a estratégia de integração interpretativa entre elas. O Capítulo V apresenta os resultados das duas instanciações, seguidos de uma análise integrativa que avalia a consistência estrutural do fenômeno observado. O Capítulo VI conclui o trabalho discutindo as implicações dos achados, as limitações do estudo e as perspectivas para investigações futuras.

---

## Proposta de Nomes para a Metodologia e Título da Dissertação

Boa percepção. Deixa eu primeiro articular o diagnóstico preciso, e depois as propostas.

---

## Diagnóstico

**O problema da MIVA:**
"Metodologia de *Identificação de Viés Amplificado*" sugere que a metodologia detecta viés que já está amplificado — como se o objeto fosse um estado final. O que a MIVA realmente faz é medir se e quanto o processo de aprendizado *produz* amplificação. O agente do fenômeno é o pipeline, não os dados. Além disso, "viés" é um termo mais carregado e menos preciso do que o que a metodologia de fato mede — que é *divergência interpretativa* entre fontes de anotação.

**O problema do título:**
"Amplificação de *Viés de Gênero*" posiciona o gênero como o fenômeno central, quando ele é o *eixo de estratificação* por onde se observa um fenômeno mais geral. O resultado mais significativo da dissertação não é que o gênero cria viés — isso já era sabido — mas que o aprendizado supervisionado *intensifica* divergências que existiam entre anotadores. "Da Anotação ao Modelo" é elegante, mas genérico demais para diferenciar o trabalho.

---

## Alternativas para a metodologia

Organizadas por ênfase conceitual:

---

**Ênfase na amplificação como fenômeno mensurável:**

> **MADI** — *Metodologia de Análise de Divergência Interpretativa*

Substitui "viés amplificado" (resultado presumido) por "divergência interpretativa" (objeto real de análise). Mais neutro epistemologicamente, mais preciso tecnicamente, e abre a metodologia para aplicação além do eixo gênero.

---

**Ênfase no rastreamento ao longo do pipeline:**

> **TADI** — *Traçado de Amplificação de Divergências Interpretativas*

"Traçado" captura a ideia de seguir o caminho da divergência desde a anotação até o modelo — evocando tanto o instrumento analítico quanto a trajetória do fenômeno. Conceptualmente próximo da ideia de *tracing* em inferência causal.

---

**Ênfase diagnóstica e de verificação:**

> **PADI** — *Protocolo de Análise de Divergência Interpretativa*

"Protocolo" em vez de "metodologia" é mais modesto e mais preciso — a MIVA é, de fato, um protocolo experimental replicável. "Análise" substitui "identificação", que é passivo demais para o que a metodologia produz.

---

**Ênfase na ressonância do sinal anotativo:**

> **ARIS** — *Análise de Ressonância Interpretativa em Sistemas Supervisionados*

"Ressonância" é a metáfora mais rica: captura o mecanismo pelo qual a divergência original é amplificada pelo modelo como uma frequência que encontra um sistema com ganho. Conceitualmente instigante e academicamente defensável — ressonância é um termo preciso em física de sistemas, e a analogia é direta.

---

## Alternativas para o título da dissertação

Organizadas do mais direto ao mais evocativo:

---

**Opção 1 — Ênfase na jornada conceitual (próximo ao atual, mais preciso):**

> **Da Discordância à Amplificação: Divergências Interpretativas de Gênero no Aprendizado Supervisionado para Análise de Sentimentos em Português Brasileiro**

Substitui "Da Anotação ao Modelo" (técnico, genérico) por "Da Discordância à Amplificação" (conceitual, específico ao fenômeno). Posiciona o trabalho imediatamente no campo da divergência interpretativa, não do viés de gênero em sentido amplo.

---

**Opção 2 — Ênfase na ruptura epistemológica:**

> **Além do Consenso: Amplificação de Divergências Anotativas de Gênero em Sistemas Supervisionados de Análise de Sentimentos**

"Além do Consenso" é duplamente eficaz: referencia a ruptura com o paradigma de maximização de concordância interanotadores (a virada perspectivista do Cap. II) e sinaliza que o trabalho vai além do que a literatura estabeleceu. Academicamente instigante.

---

**Opção 3 — Ênfase no mecanismo (mais técnica, mais direta):**

> **Supervisão Dividida: Amplificação de Divergências Interpretativas de Gênero em Classificadores de Análise de Sentimentos em Português Brasileiro**

"Supervisão Dividida" nomeia com precisão o design experimental — dois classificadores treinados sobre supervisões divergentes — e é imediatamente compreensível para leitores da área de aprendizado de máquina. Seco e preciso.

---

**Opção 4 — Ênfase na propagação (metáfora acústica):**

> **Ecos de Gênero: Como o Aprendizado Supervisionado Amplifica Divergências Anotativas em Análise de Sentimentos**

"Ecos de Gênero" é a opção mais literária e mais memorável. A metáfora é conceitualmente honesta — um eco não reproduz o som original, amplifica certas frequências e atenua outras, assim como o pipeline amplifica padrões sistemáticos e atenua ruído aleatório. Funciona especialmente bem se o nome da metodologia também usar a família semântica da ressonância (ARIS).

---

**Opção 5 — Ênfase no achado surpreendente:**

> **Quando os Modelos Discordam Mais Que os Anotadores: Amplificação de Divergências Interpretativas de Gênero em Aprendizado Supervisionado para Análise de Sentimentos**

Estrutura de "quando" convida o leitor a uma descoberta. O subtítulo técnico ancora o trabalho. Funciona muito bem como título de artigo derivado, possivelmente mais do que como título de dissertação.

---

## Recomendação

Para a **metodologia**, recomendo **ARIS** se o objetivo é instigar e diferenciar, ou **MADI** se o objetivo é manter a clareza descritiva com maior precisão que a MIVA atual. ARIS tem a vantagem de criar uma família semântica coerente com a ideia de que o pipeline "ressoa" com as divergências dos anotadores — e ressoa é exatamente o que Δκ > 0 mede.

Para o **título**, recomendo **"Além do Consenso"** como primeira opção — é o que melhor captura tanto a contribuição epistemológica (a virada perspectivista) quanto a contribuição empírica (a amplificação), sem sobrecarregar o título com detalhes técnicos que pertencem ao subtítulo. Como segunda opção, **"Da Discordância à Amplificação"** é mais seguro e igualmente preciso.

A combinação que me parece mais coesa:

> **Além do Consenso: Amplificação de Divergências Interpretativas de Gênero em Aprendizado Supervisionado para Análise de Sentimentos em Português Brasileiro**
> *Metodologia: ARIS — Análise de Ressonância Interpretativa em Sistemas Supervisionados*

---

## Análise das Propostas de Nome vs. Voto Majoritário

Sim — e a identificação é precisa. O voto majoritário cria um problema conceitual específico com algumas propostas. Deixa eu mapear isso com clareza.

---

## O que o voto majoritário implica para a nomenclatura

A MIVA não opera sobre divergências individuais dos anotadores. Ela opera sobre **dois vetores de consenso de grupo** — y_masc e y_fem — produzidos por voto de pluralidade. Isso significa que:

1. A discordância intragrupo já foi **descartada** antes de qualquer análise
2. O que κ_inicial mede é a divergência entre **posições coletivas consolidadas**, não entre interpretações individuais
3. O que o modelo aprende é o **padrão majoritário de cada grupo**, não a variabilidade interpretativa dentro dele

---

## Propostas que entram em conflito

**"Além do Consenso"** — **conflito direto e grave**

É a mais problemática. O título posiciona a dissertação como superando o paradigma do consenso — exatamente o que a literatura perspectivista propõe ao defender soft labels e anotações individuais. Mas a MIVA faz o oposto: *constrói* consenso dentro de cada grupo por voto majoritário antes de qualquer comparação. Um revisor familiarizado com Uma et al. [2021] ou Plank [2022] leria o título esperando uma metodologia que prescinde do voto majoritário — e encontraria exatamente o contrário. O título promete o que a metodologia não entrega.

---

**"Divergência Interpretativa" em todos os acrônimos (MADI, TADI, PADI, ARIS)** — **conflito moderado**

"Interpretativa" remete à variação de interpretação individual — o domínio onde a divergência é produzida por julgamentos subjetivos de cada anotador. Mas o objeto real da MIVA é a divergência entre **fontes de supervisão consolidadas**. Usar "interpretativa" sugere que a metodologia rastreia ou preserva a variação interpretativa individual, quando ela a agrega e descarta.

O termo mais preciso para o que a MIVA mede é **divergência anotativa** — a diferença entre os rótulos que dois grupos distintos produziram, já consolidados — não divergência interpretativa no sentido individual.

---

**"Ecos de Gênero"** — **conflito leve**

A metáfora do eco implica que o sinal original é propagado pelo sistema. Mas o voto majoritário já filtra o sinal antes da entrada no pipeline — o que é amplificado não é a divergência bruta dos anotadores, mas a divergência residual entre os consensos de grupo. O eco seria de uma versão já editada do sinal, o que enfraquece a metáfora.

---

**"Da Discordância à Amplificação"** — **conflito leve**

"Da Discordância" sugere que o ponto de partida é a discordância individual — mas o ponto de partida real é a divergência entre duas posições majoritárias já consolidadas. A discordância intragrupo não entra na análise. Defensável se "discordância" for entendido como divergência intergrupal, mas ambíguo.

---

## Propostas que permanecem válidas

**"Supervisão Dividida"** — sem conflito. Nomeia com precisão o que a MIVA realmente usa: dois vetores de supervisão consolidados, provenientes de grupos distintos. Não promete nada sobre preservação de divergência individual.

**"Quando os Modelos Discordam Mais Que os Anotadores"** — conflito mínimo. A comparação é, a rigor, entre divergência intermodelos e divergência entre consensos de grupo — não entre anotadores individuais. Ajustável com um subtítulo preciso.

---

## Reformulações consistentes com o voto majoritário

**Para a metodologia:**

> **MADA** — *Metodologia de Análise de Divergência Anotativa*

"Anotativa" em vez de "interpretativa" — refere-se aos rótulos produzidos pelos grupos, já consolidados, não às interpretações individuais que os geraram. Preciso e neutro.

> **MACS** — *Metodologia de Amplificação entre Consensos Supervisionados*

Nomeia explicitamente que a metodologia opera sobre *consensos* — transparente sobre o papel do voto majoritário e sobre o que é amplificado.

> **PADS** — *Protocolo de Análise de Divergência entre Supervisões*

"Entre Supervisões" é o frame mais preciso: a divergência medida é entre dois vetores de supervisão (y_masc e y_fem), não entre anotadores individuais.

---

**Para o título:**

> **Supervisão Dividida: Amplificação de Divergências Anotativas de Gênero em Classificadores Supervisionados de Análise de Sentimentos**

Permanece a opção mais consistente com o design da metodologia.

> **Da Rotulagem ao Modelo: Amplificação de Divergências entre Grupos Anotadores de Gênero em Análise de Sentimentos em Português Brasileiro**

"Da Rotulagem" em vez de "Da Anotação" ou "Da Discordância" — o rótulo consolidado é o objeto, não o processo interpretativo bruto.

> **Entre Grupos, Entre Modelos: Amplificação de Divergências Anotativas de Gênero em Aprendizado Supervisionado**

Captura a estrutura pareada da MIVA — dois grupos de anotadores, dois classificadores, uma métrica de divergência em cada nível — sem prometer rastreamento de interpretações individuais.

---

## Síntese

A principal lição é que a MIVA não é uma metodologia perspectivista — ela usa consenso. Qualquer nome que sinalize ruptura com o voto majoritário ou preservação de variação interpretativa individual vai contra o design. O campo semântico mais seguro e preciso é **divergência anotativa entre fontes de supervisão** — que é exatamente o que κ_inicial mede e o que Δκ quantifica como amplificação.

---

