# MIKE — Manual de Identidade + UI/UX + Design System (Markdown)

**Versão:** v1.0
**Data:** 2026-02-16
**Status:** Baseado no manual anterior (HTML) — complemento Markdown

---

## Sumário

* [1) Visão geral e norte](#1-visão-geral-e-norte)
* [2) Arquitetura do Design System](#2-arquitetura-do-design-system)
* [3) Identidade da marca](#3-identidade-da-marca)
* [4) Paleta de cores](#4-paleta-de-cores)
* [5) Tipografia](#5-tipografia)
* [6) Grid, layout e espaçamento](#6-grid-layout-e-espaçamento)
* [7) Iconografia e estilo gráfico](#7-iconografia-e-estilo-gráfico)
* [8) Componentes UI (catálogo operacional)](#8-componentes-ui-catálogo-operacional)
* [9) Padrões de UI/UX e fluxos principais (MIKE)](#9-padrões-de-uiux-e-fluxos-principais-mike)
* [10) Microcopy e feedback (comportamento)](#10-microcopy-e-feedback-comportamento)
* [11) Acessibilidade e Inclusão (checklist)](#11-acessibilidade-e-inclusão-checklist)
* [12) Data viz / relatórios (padrões de gráficos)](#12-data-viz--relatórios-padrões-de-gráficos)
* [13) Heurísticas + Economia Comportamental aplicadas (lista explícita)](#13-heurísticas--economia-comportamental-aplicadas-lista-explícita)
* [14) Checklist de implementação (Dev + Design QA)](#14-checklist-de-implementação-dev--design-qa)
* [15) Apêndice](#15-apêndice)

---

## 1) Visão geral e norte

### Essência da marca (1 frase)

**Registro rigoroso para progresso inevitável.**

### Promessa central do MIKE (1 parágrafo)

O MIKE reduz fricção no registro e aumenta rigor nos dados: você registra exercícios, variações e séries com precisão (reps/carga/tempo, com RPE/RIR opcionais) e recebe clareza prática sobre progressão, volume, PRs, consistência e aderência. O app existe para transformar treino em decisão objetiva — **sem distrações, sem “firula”, com feedback confiável**.

### Personalidade (3–5 adjetivos + implicações visuais)

1. **Disciplinado**

   * **Implica:** layouts limpos, poucas opções por padrão, CTA único por tela.
2. **Preciso**

   * **Implica:** números em mono/tabulares, validações claras, estados consistentes.
3. **Implacável (sem agressividade)**

   * **Implica:** linguagem direta e motivadora por evidência (“+1kg vs última sessão”), sem culpa.
4. **Moderno**

   * **Implica:** dark mode forte, superfícies em camadas, microinterações discretas.
5. **Motivador por evidência**

   * **Implica:** progresso saliente (PR, streak, tendência), sem gamificação infantil.

### Princípios do design (5–7) com exemplos práticos

1. **Clareza acima de estética**

   * **Por quê:** reduz carga cognitiva; melhora velocidade de decisão.
   * **Como aplicar:** títulos curtos, rótulos explícitos, números sempre alinhados.
2. **Fricção mínima, rigor máximo**

   * **Por quê:** comportamento alvo = registrar sempre; rigor = confiar no histórico.
   * **Como aplicar:** autopreencher último set; validação “reps OU tempo”.
3. **Progresso como recompensa (raridade crível)**

   * **Por quê:** reforço mais forte quando não é constante/banal.
   * **Como aplicar:** PR aparece só quando real; destaque moderado (badge + toast).
4. **Consistência de padrões (UI previsível)**

   * **Por quê:** reduz erros, aumenta sensação de controle.
   * **Como aplicar:** mesmos estados e tokens em toda tela; ícones consistentes.
5. **Escolhas mínimas por padrão (anti-overchoice)**

   * **Por quê:** excesso de opções aumenta abandono.
   * **Como aplicar:** 3 variações recentes; “ver todas” em secundário.
6. **Acessibilidade como requisito (não opcional)**

   * **Por quê:** melhora legibilidade e retenção; reduz erros de toque.
   * **Como aplicar:** contrastes, focus ring visível, touch targets 44px+.
7. **Escalável para nutrição e modalidades**

   * **Por quê:** evita “trocar de pele” no futuro; reduz retrabalho.
   * **Como aplicar:** tokens por função, sem “cores de módulo” conflitantes.

---

## 2) Arquitetura do Design System

### Filosofia do sistema (tokens → componentes → padrões → templates)

* **Tokens:** valores atômicos (cor, tipografia, espaço, radius, sombra, estados).
* **Componentes:** botões, inputs, cards, tabela, badges etc. construídos com tokens.
* **Padrões:** regras de uso (ex.: “1 CTA principal por tela”, “defaults inteligentes”).
* **Templates:** telas compostas (Treino, Exercício, Relatório) usando padrões e componentes.

**Por quê:** reduz inconsistência, acelera desenvolvimento, facilita escalabilidade e QA.
**Como aplicar:** toda nova UI começa validando tokens → componente → padrão → template.

### Convenções de nomenclatura

**Cores (funcionais):**

* `bg`, `surface`, `surface-2`, `border`, `text`, `text-muted`
* `accent`, `accent-2`
* `success`, `warning`, `danger`, `info`

**Tipografia:**

* `font-ui` (Inter), `font-head` (Oswald), `font-mono` (JetBrains Mono)

**Espaçamento (8px grid):**

* `s-1=4`, `s-2=8`, `s-3=12`, `s-4=16`, `s-5=24`, `s-6=32`, `s-7=40`, `s-8=48`

**Raio / sombra:**

* `radius-card`, `radius-input`, `radius-pill`
* `shadow-xs`, `shadow-sm`

### Como versionar e atualizar este manual (processo simples)

* **Versão semântica:** `vMAJOR.MINOR`

  * **MAJOR:** mudança de direção (tokens/identidade)
  * **MINOR:** adição/ajuste de componentes/padrões sem quebrar
* **Processo (rápido):**

  1. Abrir PR com a mudança (design/dev)
  2. Atualizar seção relevante + checklist QA
  3. Validar em 2 temas (light/dark) + 2 tamanhos (mobile/desktop)
  4. Publicar changelog no topo (abaixo da data)

---

## 3) Identidade da marca

### Nome e escrita correta

* Nome do produto: **MIKE** (sempre em caixa alta em marca/título).
* Em frases corridas: **MIKE** (preferencial) — evitar “mike”.
* Em código/rotas: pode usar `mike` (técnico), mas UI visível ao usuário = **MIKE**.

**Do / Don’t**

* ✅ “Abrir MIKE”, “MIKE — Progresso”
* ❌ “mike”, “Mike app” (inconsistente)

### Tom de voz: guidelines + exemplos de microcopy

**Guidelines**

* Direto, objetivo, sem ironia.
* Motivação por evidência (“vs última sessão”, “PR detectado”).
* Sem culpa: nunca “você falhou”; preferir “não há dados suficientes ainda”.

**CTAs (verbo + resultado)**

* “Registrar série”
* “Salvar treino”
* “Adicionar exercício”
* “Duplicar treino”
* “Ver progresso”

**Erros (curtos e acionáveis)**

* “Confira: reps OU tempo (não ambos).”
* “Carga inválida. Use apenas números.”
* “Ordem duplicada. Ajuste a posição.”

**Empty states (orientam próximo passo)**

* “Ainda não há treinos. Registre o primeiro.”
* “Sem tendência ainda. Faça mais 2 sessões neste exercício.”
* “Sem PRs — ótimo. O primeiro vem rápido.”

### Uso do logo (regras textuais)

* **Área de respiro:** mínimo = altura do “I” ao redor.
* **Tamanho mínimo:** wordmark 120px (web) / 24px (header mobile); ícone 24px (UI), 64px+ (store).
* **Usos proibidos:** distorcer, inclinar, gradientes pesados, baixo contraste, usar vermelho/laranja como “accent principal” do logo.

### “Sensação Heavy Duty” aplicada (disciplina e foco sem agressividade)

**Como manter**

* **Uma ação principal por momento** (registrar/salvar/duplicar).
* **Hierarquia forte de informação** (dados essenciais visíveis; avançado opcional).
* **Feedback firme, respeitoso** (“Série registrada. +1 passo.”).
* **Acento energético controlado** (Signal Lime) apenas para progresso/CTA.

**Evitar agressividade**

* Evitar linguagem punitiva (“perdeu”, “fracassou”).
* Evitar estética “gamer neon” ou “bodybuilding caricatural”.

---

## 4) Paleta de cores

### Lista completa (HEX + função)

**Primárias (core)**

* **MIKE Core / Graphite:** `#0B0F14` — base dark, foco, seriedade
* **MIKE Surface / Slate:** `#121A24` — cards no dark, camadas
* **MIKE Accent / Signal Lime:** `#A3E635` — CTA, PR, progresso (uso controlado)

**Secundárias**

* **Data Blue:** `#3B82F6` — info, links, métricas neutras, gráficos
* **Steel Gray:** `#2A3441` — bordas/divisórias
* **Mist (texto light):** `#E6EDF5` — texto em dark
* **Ice (bg light):** `#F5F7FA` — fundo em light

**Neutros (referência operacional)**

* **Text Dark:** `#0E1726` — texto em light
* **Text Muted (light):** `#5B6778` — secundário em light
* **Text Light:** `#E6EDF5` — texto em dark
* **Text Light Muted:** `#A7B0BD` — secundário em dark

**Semânticas**

* **Success:** `#22C55E`
* **Warning:** `#F59E0B`
* **Danger:** `#EF4444`
* **Info:** `#3B82F6`

### Regras para light e dark mode (o que muda, o que não muda)

**Não muda**

* `accent` (Signal Lime) e semânticas mantêm identidade.
* Hierarquia (CTA, PR, erro) segue mesma lógica.

**Muda**

* `bg/surface/border/text` invertem para manter contraste e conforto visual.
* Sombras ficam mais suaves no light (evitar “peso” excessivo).

**Por quê:** consistência de reconhecimento + acessibilidade em ambos os temas.
**Como aplicar:** sempre use tokens funcionais, nunca cor “solta” no componente.

### Cores semânticas (quando usar)

* **Success:** confirmação real (salvo, registrado, concluído).
* **Warning:** atenção sem erro (ex.: “volume alto”, “fadiga”).
* **Danger:** erro real (falha de salvar, validação inválida, delete).
* **Info:** conteúdo neutro informativo (dica, link, ajuda).

### Regras de contraste (WCAG AA como referência)

**Práticas**

* Validar contraste de **texto** com o fundo (AA para texto normal).
* Evitar usar `accent` como cor de texto em fundo claro (cansa e pode falhar).
* Em dados críticos (ex.: PR), além de cor, use **ícone/label**.

**Como validar**

* Check rápido com ferramenta de contraste (qualquer checker WCAG).
* Regra manual: se o texto “some” ao baixar brilho da tela, provavelmente falha.

### Paleta para gráficos (séries, volume, PRs, alertas)

* **Série/Volume (padrão):** Data Blue (`#3B82F6`) + variações em opacidade
* **Grid/linhas de apoio:** baseado no token `chart-grid` (bem discreto)
* **PR (evento):** Signal Lime (`#A3E635`) — apenas no ponto/coluna do PR
* **Alertas:** Warning/Danger apenas quando necessário (sem dramatizar)

### Do / Don’t (exemplos claros)

**Do**

* ✅ CTA principal em Signal Lime com texto escuro (legível)
* ✅ PR em badge Lime + ícone troféu (não só cor)
* ✅ Data Blue para links e gráficos

**Don’t**

* ❌ Vermelho como “positivo”
* ❌ Dois acentos vibrantes juntos (polui)
* ❌ Lime como texto longo em fundo branco

---

## 5) Tipografia

### Fontes escolhidas (e motivo)

* **Principal (UI): Inter** — legibilidade, neutralidade moderna, leitura rápida
* **Secundária (títulos/impacto): Oswald** — disciplina, peso visual sem caricatura
* **Mono (dados): JetBrains Mono** — números comparáveis, alinhamento tabular

**Por quê:** melhora fluência cognitiva, reduz erro de leitura de números.
**Como aplicar:** métricas e valores sempre em mono; títulos curtos em Oswald.

### Escala tipográfica (tamanhos + pesos)

> Ajustar responsivamente (mobile-first). Valores base.

* **H1:** 32–36 / 700 (Oswald)
* **H2:** 24–28 / 600 (Oswald)
* **H3:** 20–22 / 600 (Inter)
* **H4:** 18–20 / 600 (Inter)
* **H5:** 16–18 / 700 (Inter)
* **H6 / Label:** 12–14 / 700 (Inter) + tracking leve
* **Body:** 16 / 400 (Inter)
* **Small:** 14 / 400 (Inter)
* **Caption:** 12 / 500 (Inter)

### Regras para números e dados

* Use **JetBrains Mono** com **tabular nums** para: carga, reps, volume, PR, streak.
* Alinhar números à direita em tabelas (comparação rápida).
* Separadores claros (ex.: `92.5 kg`, `6 reps`) e unidades sempre visíveis.

**Do / Don’t**

* ✅ `92.5 kg` (mono + unidade)
* ❌ `92,5` sem unidade (ambíguo)
* ❌ números em fonte proporcional em tabelas densas

### Espaçamento, altura de linha, CAPS

* **Line-height:**

  * títulos: 1.1–1.2
  * body: 1.45–1.6
* **CAPS:** apenas para labels curtos (tabs, badges), com tracking +2% a +4%.
* Evitar blocos longos em caps (cansa).

### Exemplos de hierarquia (descritos)

**Tela de treino**

* Topo: título “Treino A — Peito/Tríceps” (Oswald H2)
* Sub: data/hora (caption, muted)
* Cards de exercício: nome (Inter H4), comparativo “vs última sessão” (small, mono)
* Sets: valores (mono), labels (caps small)

**Tela de relatório**

* Métricas principais: números grandes (mono), rótulo (caps)
* Gráfico: título curto (Inter H5) + legenda minimal
* Tabela: cabeçalho em caps small + valores em mono

---

## 6) Grid, layout e espaçamento

### Grid base (8px) e por quê

* Base: **8px** (com subdivisão 4px).
  **Por quê:** padroniza ritmo visual, acelera composição e QA.
  **Como aplicar:** paddings/margens em múltiplos de 8 (4 apenas para microajustes).

### Breakpoints e comportamento mobile-first

* Mobile: 360–480 (prioridade)
* Tablet: 768
* Desktop: 1024–1200

**Regras**

* Mobile: 1 coluna; evitar tabelas grandes (usar cards/linhas)
* Desktop: 2 colunas em relatórios; treino mantém foco (1 coluna + painel lateral opcional)

### Margens e paddings recomendados

* Padding de tela: 16 (mobile), 24 (tablet), 32 (desktop)
* Espaço entre cards: 12–16
* Espaço entre seções: 24–32

### Densidade de informação (mostrar muito sem poluir)

* Use **camadas** (surface/surface-2) + divisórias leves.
* Priorize **3–5 itens** por bloco (acima disso, colapsar).
* Mostre “avançado” sob demanda (expansível).

**Por quê:** reduz abandono e erros em contexto de treino (atenção limitada).
**Como aplicar:** padrões de “mostrar mais”, filtros, tabs.

### Padrões de cards (sessão, exercício, set)

* **Sessão:** resumo + CTA (Salvar/Finalizar)
* **Exercício:** nome + status (PR/OK) + comparativo vs última
* **Set:** linha compacta com carga/reps/tempo + ações rápidas (duplicar/editar)

---

## 7) Iconografia e estilo gráfico

### Estilo de ícone

* Preferência: **outline** consistente (equivalente a 2px).
* Cantos levemente arredondados, sem detalhes excessivos.
* Evitar filled como padrão (usar apenas para estados selecionados se necessário).

### Regras de uso

* Ícone sozinho apenas quando universal (ex.: trash, edit).
* Com texto em CTAs importantes (“Salvar treino”, “Adicionar série”).
* Não usar ícone como decoração — sempre suporte de leitura.

### Ilustrações (se usar): princípios e limites

* Minimalistas, geométricas, baseadas em shapes/grids/medição.
* Sem mascotes, sem humor infantil.

### Fotografia (se usar): direção e limites

* Preto-e-branco, alto contraste, foco em detalhes (mãos, barras, anilhas).
* Evitar “bro science”, poses exageradas e excesso de estética bodybuilding.

---

## 8) Componentes UI (catálogo operacional)

> Para todos os componentes:
> **Regra base:** tokens funcionais + estados acessíveis + microcopy objetiva.

### 8.1 Buttons (primary/secondary/ghost/danger)

**Objetivo:** ações claras com hierarquia.

**Anatomia:** label (verbo), ícone opcional, container, estado.

**Variantes**

* **Primary:** Signal Lime (CTA principal)
* **Secondary:** outline (ações secundárias)
* **Ghost:** ação terciária (config/avançado)
* **Danger:** destrutivo (excluir)

**Estados**

* default / hover / active / focus (ring visível) / disabled / loading

**Acessibilidade**

* Área mínima 44px altura
* `aria-label` quando só ícone
* Focus ring sempre visível

**Regras de uso**

* 1 Primary por tela (principal).
* Danger nunca como Primary padrão.

**Anti-padrões**

* Várias primárias na mesma seção.
* Botão “Salvar” com label genérica sem contexto (“OK”).

---

### 8.2 Inputs (text/number), Select, Textarea

**Objetivo:** registro rápido e confiável.

**Anatomia:** label, campo, unidade/sufixo, helper/erro.

**Variantes**

* Text: nome/observação
* Number: carga/reps/tempo
* Select: variação/tipo
* Textarea: observações

**Estados**

* default / focus / filled / invalid / disabled

**Acessibilidade**

* Label sempre presente (não depender de placeholder)
* Erro associado ao campo (`aria-describedby`)
* Teclado numérico para números (mobile)

**Regras**

* Unidades sempre visíveis (kg, reps, s/min).
* Evitar campo “livre” sem validação para números.

**Anti-padrões**

* Placeholder como label.
* Erro genérico (“inválido”) sem ação.

---

### 8.3 Form validation (erro, helper text)

**Objetivo:** prevenir erro e manter confiança no histórico.

**Padrão**

* **Helper** (antes do erro) orienta formato.
* **Erro** curto, objetivo, acionável.

**Regra crítica do MIKE**

* **reps XOR tempo** (um ou outro, não ambos).

**Acessibilidade**

* Não depender apenas de cor: ícone + texto.

---

### 8.4 Cards (sessão/exercício/set)

**Objetivo:** organizar densidade de dados em camadas.

**Anatomia**

* Header (título + status)
* Body (dados)
* Actions (botões/atalhos)

**Variantes**

* Sessão: sumário + CTA
* Exercício: nome + comparativo + badge PR
* Set: linha compacta com ações rápidas

**Estados**

* default / highlighted (PR) / selected / disabled

**Acessibilidade**

* Hierarquia com headings e leitura linear.

**Anti-padrões**

* Card “gigante” com tudo (vira ruído).

---

### 8.5 Badges/Chips (PR, falha, deload, etc.)

**Objetivo:** sinalização rápida sem poluição visual.

**Regras**

* Use **PR** com Lime (evento).
* **Falha** pode usar Warning (atenção, não culpa).
* **Deload** com Data Blue (neutro).

**Anti-padrões**

* Badge em excesso (vira ruído).

---

### 8.6 Tabs/Navigation

**Objetivo:** organizar áreas: Treino / Histórico / Relatórios.

**Regras**

* Máximo 3–5 tabs visíveis; “mais” em overflow.
* Tab ativa clara, sem depender só de cor.

**Acessibilidade**

* Navegação por teclado (setas/Tab).

---

### 8.7 Table (histórico)

**Objetivo:** leitura comparativa.

**Anatomia:** head em caps, rows, alinhamento numérico.

**Regras**

* Números em mono, alinhados à direita
* Zebra leve
* Em mobile: converter para cards/linhas

**Anti-padrões**

* Tabela complexa em mobile sem adaptação.

---

### 8.8 Toast/Alert

**Objetivo:** feedback imediato sem interromper fluxo.

**Toast**

* Sucesso curto (“Série registrada. +1 passo.”)
* 2–3s, não bloquear UI

**Alert**

* Usar para avisos persistentes (ex.: “sem dados suficientes”)

**Anti-padrões**

* Toast para erros críticos (use validação no campo).

---

### 8.9 Modal/Confirm (ex.: deletar set)

**Objetivo:** prevenir ações destrutivas acidentais.

**Regras**

* Apenas para destrutivo (delete sessão/set).
* Copy claro: “Excluir esta série? Isso não pode ser desfeito.”
* Botão danger + botão cancelar (default = cancelar)

---

### 8.10 Empty state

**Objetivo:** orientar próximo passo.

**Estrutura**

* Mensagem curta + motivo + CTA único.

**Anti-padrões**

* Vazio sem ação.

---

### 8.11 Loading states (skeleton vs spinner)

**Regra**

* **Skeleton** para listas e relatórios (percepção de velocidade).
* **Spinner** apenas para ação curta (salvar).

**Por quê:** reduz ansiedade e abandono.
**Como aplicar:** skeleton em cards de exercícios e tabelas.

---

## 9) Padrões de UI/UX e fluxos principais (MIKE)

### Regra de ouro

**“Registro tem que ser mais rápido que pensar.”**

### Fluxo 1 — Criar sessão → adicionar exercícios → registrar sets → finalizar

1. Criar sessão (tipo/data opcional)
2. Adicionar exercício (buscar + variação recente)
3. Registrar sets (quick-add + autopreencher)
4. Revisar rápido (erros/ordem)
5. Finalizar/Salvar

**Defaults e auto-preenchimento (onde usar)**

* Ao abrir exercício: sugerir último set (carga/reps)
* Ao adicionar set: autopreencher valores recentes
* Ao escolher variação: 3 recentes + “todas”

**Por quê:** reduz fricção e aumenta consistência.
**Como aplicar:** “último treino” como ponto de partida, não como obrigação.

### Fluxo 2 — Duplicar treino anterior / template

1. Home: “Duplicar treino anterior” (CTA secundário forte)
2. Ajustar 1–2 exercícios no máximo
3. Registrar sets com valores pré-carregados

**Por quê:** commitment device + redução de custo de entrada.
**Como aplicar:** duplicação preserva estrutura e sugere progressão mínima.

### Fluxo 3 — Editar e corrigir erro (peso/reps/ordem) rapidamente

* Ações rápidas em set: **editar**, **duplicar**, **excluir**
* Reordenação automática após delete (consistência)

**Por quê:** erros acontecem no treino (pressa); correção precisa ser trivial.
**Como aplicar:** botões compactos por set e validação no campo.

### Fluxo 4 — Visualizar histórico de um exercício (progressão)

* Card do exercício → “Histórico”
* Mostrar: top set, volume, tendência (linha/barras), PRs
* Comparativo “vs última sessão” sempre visível

### Fluxo 5 — Relatório semanal/mensal

* Visão: PRs, consistência, volume total
* Insights: “melhor que semana passada” com contexto, sem exagero
* Drill-down: exercício específico

---

## 10) Microcopy e feedback (comportamento)

### Biblioteca de mensagens

**Sucesso**

* “Série registrada. +1 passo.”
* “Treino salvo. Consistência mantida.”
* “PR registrado. Progresso real.”

**Erro**

* “Confira: reps OU tempo (não ambos).”
* “Campo obrigatório: carga.”
* “Não foi possível salvar. Tente novamente.”

**Aviso**

* “Sem dados suficientes ainda. Faça mais 2 sessões.”
* “Volume alto esta semana. Considere deload.”

**Vazio**

* “Nenhum treino ainda. Comece registrando o primeiro.”
* “Sem histórico deste exercício. Registre hoje.”

### Padrões para botões (verbo + resultado)

* “Salvar treino” (não “Salvar”)
* “Adicionar série” (não “Adicionar”)
* “Ver progresso” (não “Relatório”)

### Reforço positivo sem infantilizar

* Use evidência: “+1 rep vs última sessão”, “PR detectado”.
* Evitar emojis excessivos, gírias ou “hype”.

### Evitar culpa/pressão (ética e retenção)

* Nunca: “você falhou”, “você perdeu”.
* Preferir: “ainda não”, “sem dados suficientes”, “próximo passo sugerido”.

---

## 11) Acessibilidade e Inclusão (checklist)

### Contraste, tamanho mínimo, touch targets

* Texto body 16px mínimo (mobile)
* Touch target 44px+
* Verificar contraste em light/dark (WCAG AA)

### Focus ring e teclado

* Focus ring sempre visível em botões, inputs, tabs
* Ordem de tabulação lógica
* Componentes interativos com `aria-label` quando necessário

### Cores sem depender só de cor

* PR = cor + ícone + label (“PR”)
* Erro = borda + mensagem + ícone (opcional)

### Linguagem clara

* Frases curtas
* Termos consistentes (“Série”, “Exercício”, “Sessão”)

### Checklist final de acessibilidade

* [ ] Contraste AA para texto essencial
* [ ] Focus ring aparece em todos os interativos
* [ ] Labels presentes (não só placeholder)
* [ ] Erros associados ao campo
* [ ] Mobile: toque confortável, sem itens colados
* [ ] Não depender apenas de cor para status

---

## 12) Data viz / relatórios (padrões de gráficos)

### Regras para gráficos

**Progresso (linha)**

* Linha principal em Data Blue
* Grid discreto
* Marcador Lime apenas no PR

**Volume (barras)**

* Barras em Data Blue (opacidades)
* PR/maior ponto em Lime (1 barra/ponto)

**Distribuição (simples)**

* Evitar gráficos complexos (pizza/3D).
* Preferir barras horizontais simples.

### Destacar PRs (saliência)

* 1 elemento Lime por gráfico (evento)
* Badge “PR” no card do gráfico
* Texto “PR em 2026-02-16” (contexto)

### Evitar enganar (ética)

* Escalas consistentes; não “cortar eixo” sem aviso.
* Comparações sempre com contexto (“vs última sessão”, “últimas 6 semanas”).
* Evitar “%” sem base clara.

### Paleta e hierarquia

* 1 cor principal (Data Blue) + neutros
* Lime só para evento
* Warning/Danger apenas quando necessário (fadiga, erro)

---

## 13) Heurísticas + Economia Comportamental aplicadas (lista explícita)

> Formato: Comportamento alvo → Problema → Intervenção → Por quê → Como implementar

1. **Registrar sempre**

* Problema: fricção (digitar muito)
* Intervenção: quick-add + autopreencher último set
* Por quê: redução de custo/atrito
* Implementar: botão “Adicionar série (autopreencher)”

2. **Manter consistência semanal**

* Problema: esquecimento/abandono
* Intervenção: métrica “semanas ativas” + streak discreto
* Por quê: viés do progresso + compromisso
* Implementar: card no dashboard/relatório

3. **Perceber evolução**

* Problema: evolução lenta “invisível”
* Intervenção: “vs última sessão” em cada exercício
* Por quê: referência próxima aumenta saliência
* Implementar: subtitle mono no card do exercício

4. **Evitar overchoice**

* Problema: muitas variações/opções
* Intervenção: mostrar 3 recentes; “ver todas” secundário
* Por quê: paradox of choice
* Implementar: select com “recentes”

5. **Aumentar confiança nos dados**

* Problema: entradas inconsistentes
* Intervenção: validações rígidas e claras (reps XOR tempo)
* Por quê: prevenção de erro (Nielsen)
* Implementar: erro no campo + mensagem acionável

6. **Acelerar início do treino**

* Problema: “não sei por onde começar”
* Intervenção: “Duplicar treino anterior”
* Por quê: choice architecture + default
* Implementar: CTA secundário forte no home

7. **Recompensa sem infantilizar**

* Problema: gamificação exagerada descredibiliza
* Intervenção: PR como evento raro (badge + toast curto)
* Por quê: reforço variável crível
* Implementar: Lime apenas no PR real

8. **Reduzir medo de errar**

* Problema: usuário evita registrar por medo de “ficar errado”
* Intervenção: editar/duplicar set com 1 toque
* Por quê: controle percebido
* Implementar: ações por set

9. **Evitar perda por ação destrutiva**

* Problema: deletar sem querer
* Intervenção: modal confirm destrutivo
* Por quê: prevenção de erro
* Implementar: confirm para deletar set/sessão

10. **Evitar fadiga e abandono**

* Problema: excesso de volume sem perceber
* Intervenção: alert “volume alto” (warning) + sugestão deload
* Por quê: feedback preventivo
* Implementar: badge/alert no relatório semanal

11. **Aprendizado rápido do app**

* Problema: onboarding longo
* Intervenção: empty states com CTA e frase curta
* Por quê: instrução contextual
* Implementar: vazio → “Registre o primeiro treino”

12. **Decisão objetiva no próximo treino**

* Problema: dúvida sobre progressão
* Intervenção: sugestão “+1 rep ou +1.25kg”
* Por quê: meta mínima (gradiente)
* Implementar: card “próximo passo sugerido”

13. **Manter foco durante treino**

* Problema: distração por UI barulhenta
* Intervenção: 1 coluna foco + painel opcional
* Por quê: limita estímulos
* Implementar: layout treino simples

14. **Aumentar aderência ao registro**

* Problema: registrar parece “trabalho”
* Intervenção: templates e duplicação + defaults
* Por quê: hábito e rotina
* Implementar: templates por dia/treino

15. **Reduzir atrito de leitura de dados**

* Problema: números difíceis de comparar
* Intervenção: mono + alinhamento + unidades
* Por quê: fluência cognitiva
* Implementar: tabelas e cards com padrões fixos

---

## 14) Checklist de implementação (Dev + Design QA)

### Checklist por tela

**Tela Sessão (Treino)**

* [ ] 1 CTA principal (“Salvar treino”)
* [ ] Quick-add set e duplicar set disponíveis
* [ ] Comparativo vs última sessão visível por exercício
* [ ] Erros aparecem no campo correto
* [ ] Funciona em dark e light

**Tela Exercício**

* [ ] Histórico acessível em 1 toque
* [ ] PR destacado com badge + label
* [ ] Variações recentes (3) antes de “todas”

**Tela Relatório**

* [ ] Métricas principais: PRs, consistência, volume
* [ ] Gráficos com 1 cor principal + Lime só para PR
* [ ] Tabela legível (mono, alinhamento, zebra)
* [ ] Avisos (warning) sem dramatizar

### Checklist por componente

* [ ] Estados: default/hover/active/focus/disabled/loading
* [ ] Focus ring visível
* [ ] Touch targets 44px+
* [ ] Labels presentes
* [ ] Erro com texto acionável
* [ ] Não depender só de cor para status

### Checklist de consistência

* [ ] Usa tokens (não cores soltas)
* [ ] Espaçamento em múltiplos de 8px
* [ ] Tipos corretos (Inter/Oswald/Mono)
* [ ] Ícones consistentes (outline)

### Definição de pronto (DoD) visual/UX

* [ ] Cumpre regra de ouro (registrar mais rápido que pensar)
* [ ] Acessibilidade básica validada (contraste + foco + labels)
* [ ] Sem overchoice (poucas opções por padrão)
* [ ] Feedback imediato sem poluir
* [ ] Dark + light aprovados (mobile-first)

---

## 15) Apêndice

### Glossário

* **RPE:** percepção de esforço (1–10)
* **RIR:** repetições em reserva (0 = falha)
* **PR:** personal record (melhor marca)
* **Volume:** carga × reps × sets (ou variação conforme regra do app)
* **Deload:** semana/estratégia de redução de carga/volume
* **Top set:** melhor set de trabalho (geralmente maior carga)
* **Streak:** sequência de dias/semanas com registro

### Regras de expansão futura (nutrição e outras modalidades) sem quebrar o sistema

* Reaproveitar tokens e componentes (cards, tabela, tabs).
* Evitar “paleta por módulo” — usar semânticas e Data Blue como neutro informativo.
* Novos módulos devem:

  * manter 1 CTA principal por tela
  * manter padrões de dados em mono
  * manter contraste e hierarquia idênticos

### Roadmap de maturidade do design system (v1 → v2)

**v1 (agora)**

* Tokens + componentes base + padrões essenciais (treino/histórico/relatório)

**v1.1**

* Estados de loading (skeletons) padronizados
* Padrões de empty states por módulo

**v1.2**

* Componentes avançados: filtros, segmentação por período, comparações

**v2**

* Biblioteca completa de templates (nutrição, cardio, sono)
* Auditoria WCAG mais rígida e testes com usuários
* Documentação de decisões (changelog + rationale)
