# MIVA -- Metodologia de Identificacao de Vies Amplificado

## 1. Descricao do Estudo

A MIVA e uma metodologia proposta para detectar e quantificar a **amplificacao de vies** em modelos de classificacao de texto treinados com anotacoes provenientes de diferentes grupos demograficos. O estudo investiga se classificadores supervisionados, ao aprenderem a partir de rotulos atribuidos por anotadores humanos segregados por genero, produzem predicoes que divergem entre si mais do que as proprias anotacoes originais divergiam.

Os resultados, obtidos tanto em dados empiricos quanto em dados sinteticos com concordancia controlada, confirmaram que todos os classificadores avaliados amplificam sistematicamente as divergencias iniciais entre os grupos de anotadores, com magnitude e severidade que variam conforme o tipo de modelo utilizado.

---

## 2. Dados de Entrada

### 2.1. Dataset Primario (MQD-1465)

O corpus original contem 1.465 frases extraidas da plataforma "Meu Querido Diario" (www.meuqueridodiario.com.br), que coleta e processa sem qualquer moderação, entradas em forma de diário. As frases foram submetidas a uma tarefa de classificacao de sentimento em tres categorias: negativa, neutra e positiva.

### 2.2. Anotacoes Humanas

As anotacoes foram coletadas por meio da plataforma PCIbex Farm, com participantes divididos em dois grupos por genero autodeclarado (masculino e feminino). O dataset foi segmentado em 10 blocos de ate 150 frases, distribuidos aleatoriamente com semente fixa para reprodutibilidade. Cada frase recebeu exatamente quatro classificacoes por grupo de genero, e o rotulo final foi definido por voto de pluralidade, onde a classe com mais votos prevalece, descartando apenas os casos de empate entre as duas classes mais votadas.

### 2.3. Dataset Processado (MQD-1209)

Apos remocao de duplicatas, filtragem por voto de pluralidade e garantia de paridade entre generos, o dataset final utilizado no experimento empirico contem 1.209 frases com classificacoes majoritarias validas para ambos os grupos.

### 2.4. Datasets Sinteticos (SynSA)

Para validacao em ambiente controlado, foram gerados 12 datasets sinteticos com concordancia ajustada por parametro (50%, 55%, 60%, 65%, 70%, 75%, 80%, 85%, 90%, 95%, 97% e 99%). Cada dataset contem 999 instancias perfeitamente balanceadas entre as tres classes, com textos semanticamente neutros compostos por tokens genericos, de modo a isolar o efeito dos rotulos sobre o comportamento dos modelos.

---

## 3. Etapas do Estudo

### Fase 1 -- Processamento dos Logs

Processamento dos registros brutos exportados da plataforma de anotacao. Inclui concatenacao dos blocos, identificacao de genero dos anotadores, aplicacao do criterio de pluralidade e construcao do dataset MQD-1209 com as classificacoes majoritarias por grupo.

### Fase 2 -- Experimento Empirico

Treinamento pareado de quatro classificadores (SVM, Naive Bayes Multinomial, Random Forest e Regressao Logistica) sobre as anotacoes majoritarias de cada grupo. A representacao textual emprega TF-IDF com unigramas a trigramas. A validacao cruzada estratificada com cinco particoes garante que os modelos masculino e feminino sejam avaliados nas mesmas divisoes de dados. Si calcula o coeficiente de concordancia entre as predicoes dos modelos pareados e compara-se com a concordancia original entre os anotadores.

### Fase 3 -- Experimento Sintetico

Replicacao da mesma metodologia da Fase 2 sobre os 12 datasets sinteticos, permitindo observar o comportamento dos classificadores sob niveis de concordancia conhecidos a priori e perfeitamente controlados.

### Resultados Unificados

Comparacao sistematica dos resultados empiricos e sinteticos, consolidando evidencias sobre a presenca, magnitude e severidade da amplificacao.

---

## 4. Metricas e Criterios de Avaliacao

| Metrica                                    | Finalidade                                                                                                          |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Kappa de Cohen                             | Concordancia entre anotadores (baseline) e entre predicoes dos modelos (pos-treinamento)     |
| Delta Kappa                                | Diferenca entre o kappa dos anotadores e o kappa dos modelos; metrica central da MIVA que quantifica a amplificacao |
| V de Cramer                                | Forca da associacao entre as predicoes dos dois grupos                                                              |
| Qui-quadrado                               | Teste de independencia estatistica entre as predicoes                                                               |
| Intervalo de confianca por bootstrap (95%) | Significancia estatistica do Delta Kappa, obtida por reamostragem com 1.000 iteracoes                               |

Adicionalmente, acuracia, precisao, cobertura e medida-F foram calculadas para cada classificador individual como verificacao de adequacao. Essas metricas nao integram o argumento central do estudo, mas asseguram que os modelos atingiram desempenho suficiente na tarefa de classificacao, condicao necessaria para que o Delta Kappa reflita amplificacao de vies e nao mero erro de predicao.

### Classificacao de Severidade

A severidade da amplificacao e determinada pela queda nas faixas de interpretacao de Landis e Koch (1977):

| Queda de faixas  | Severidade |
| ---------------- | ---------- |
| 0 faixas         | Ausente    |
| 1 faixa          | Leve       |
| 2 faixas         | Moderada   |
| 3 ou mais faixas | Severa     |

As faixas de referencia sao: Poor (< 0), Slight (0,00 a 0,20), Fair (0,21 a 0,40), Moderate (0,41 a 0,60), Substantial (0,61 a 0,80) e Almost Perfect (0,81 a 1,00).

---

## 5. Classificadores Empregados

Quatro classificadores foram utilizados para os treinamentos pareados:

| Classificador                       | Configuracao                            |
| ----------------------------------- | --------------------------------------- |
| Maquina de Vetores de Suporte (SVM) | Kernel linear, semente fixa             |
| Naive Bayes Multinomial (NB)        | Parametros padrao                       |
| Random Forest (RF)                  | Semente fixa                            |
| Regressao Logistica (LR)            | Maximo de 1.000 iteracoes, semente fixa |

A representacao textual foi feita com TF-IDF (unigramas a trigramas, limite de 10.000 atributos, ponderacao sublinear, remocao de stopwords em portugues). A validacao cruzada estratificada com cinco particoes e divisoes identicas para os modelos masculino e feminino garantem comparabilidade direta.

---

## 6. Resultados Esperados e Obtidos

### 6.1. Experimento Empirico (MQD-1209)

O coeficiente de concordancia entre os anotadores humanos (baseline) foi de 0,7652, classificado como Substantial. Todos os quatro modelos apresentaram concordancia inferior entre suas predicoes, com Delta Kappa positivo e estatisticamente significativo (intervalos de confianca a 95% excluem o zero):

| Classificador | Kappa dos modelos | Delta Kappa | Severidade     |
| ------------- | ----------------- | ----------- | -------------- |
| SVM           | 0,4647            | +0,3005     | Leve (1 faixa) |
| NB            | 0,4862            | +0,2791     | Leve (1 faixa) |
| RF            | 0,4378            | +0,3275     | Leve (1 faixa) |
| LR            | 0,4986            | +0,2666     | Leve (1 faixa) |

A concordancia caiu da faixa Substantial (anotadores) para a faixa Moderate (modelos) em todos os casos.

### 6.2. Experimento Sintetico

Os 12 datasets sinteticos, abrangendo todos os quatro classificadores (48 combinacoes), apresentaram amplificacao em 100% dos casos. Em datasets de alta concordancia (acima de 90%), o Random Forest apresentou amplificacao severa, com Delta Kappa superior a 0,70 e perda de tres a quatro faixas, mesmo quando a concordancia inicial era proxima da unanimidade.

### 6.3. Ordenacao dos Classificadores por Amplificacao

Do menos ao mais amplificador, observou-se a seguinte ordenacao, consistente entre as fases empirica e sintetica:

**Regressao Logistica < Naive Bayes < SVM < Random Forest**

### 6.4. Resultado Contra-Intuitivo

Alta concordancia entre anotadores nao impede amplificacao severa em modelos de maior complexidade. O tipo de classificador mostrou-se mais determinante para a magnitude da amplificacao do que a qualidade inicial dos dados de treinamento.

---

## 7. Contribuicoes

1. Metodologia pioneira a quantificar a amplificacao (e nao apenas a presenca) de vies em classificadores de texto, com criterio objetivo de severidade baseado nas faixas de Landis e Koch (1977).
2. Validacao cruzada entre dados empiricos e sinteticos, demonstrando a generalizabilidade dos achados.
3. Evidencia de que a arquitetura do classificador consiste em um fator determinante da amplificacao, com implicacoes diretas para a selecao de modelos em cenarios sensiveis a vies.

---

## 8. Trabalho Futuro

Uma analise qualitativa complementar esta prevista para investigar individualmente as frases com classificacao mais divergente entre os modelos pareados, identificando padroes recorrentes de amplificacao (bilateral, unilateral, preservacao, resolucao e persistencia). Essa etapa visa aprofundar a compreensao dos mecanismos linguisticos subjacentes a amplificacao detectada pela MIVA.

---

## 9. Estrutura do Repositorio

```
fase1_processamento_logs_pcibex.ipynb   Processamento dos logs e construcao do dataset
fase2_experimento_empirico.ipynb        Experimento com dados empíricos (MQD-1209)
fase3_experimento_sintetico.ipynb       Experimento com dados sinteticos (SynSA)
resultados_MIVA.ipynb                   Analise comparativa unificada

data/
  MQD-1465.csv                          Dataset original
  logs_brutos/                          Registros exportados do PCIbex
  logs_processados/                     Datasets intermediarios e finais
  sinteticos/                           Datasets SynSA (12 niveis de concordancia)
  resultados_empiricos/                 Saidas da Fase 2
  resultados_sinteticos/                Saidas da Fase 3
  resultados_gerais/                    Tabelas consolidadas e graficos comparativos
  analise_qualitativa/                  Saidas da analise qualitativa
```
