# Manual de Identidade, UI/UX e Design System do App MIKE

**Versão:** v1.0
**Data:** 16 de fevereiro de 2026
**Status:** Baseado no manual anterior (HTML) — complemento Markdown

## Sumário

1.  [Visão Geral e Norte](#1-visão-geral-e-norte)
2.  [Arquitetura do Design System](#2-arquitetura-do-design-system)
3.  [Identidade da Marca](#3-identidade-da-marca)
4.  [Paleta de Cores](#4-paleta-de-cores)
5.  [Tipografia](#5-tipografia)
6.  [Grid, Layout e Espaçamento](#6-grid-layout-e-espaçamento)
7.  [Iconografia e Estilo Gráfico](#7-iconografia-e-estilo-gráfico)
8.  [Componentes UI (Catálogo Operacional)](#8-componentes-ui-catálogo-operacional)
9.  [Padrões de UI/UX e Fluxos Principais (MIKE)](#9-padrões-de-uiux-e-fluxos-principais-mike)
10. [Microcopy e Feedback (Comportamento)](#10-microcopy-e-feedback-comportamento)
11. [Acessibilidade e Inclusão (Checklist)](#11-acessibilidade-e-inclusão-checklist)
12. [Data Viz / Relatórios (Padrões de Gráficos)](#12-data-viz--relatórios-padrões-de-gráficos)
13. [Heurísticas + Economia Comportamental Aplicadas](#13-heurísticas--economia-comportamental-aplicadas)
14. [Checklist de Implementação (Dev + Design QA)](#14-checklist-de-implementação-dev--design-qa)
15. [Apêndice](#15-apêndice)

---

## 1. Visão Geral e Norte

### Essência da Marca

MIKE é a **disciplina implacável que transforma esforço em progresso mensurável**.

### Promessa Central do MIKE

O app MIKE oferece aos praticantes de musculação uma plataforma robusta e objetiva para registrar, analisar e otimizar seus treinos. Inspirado na filosofia Heavy Duty de Mike Mentzer, ele elimina distrações e foca na progressão rigorosa, fornecendo clareza sobre o que fazer e recompensando a consistência com dados visuais e insights acionáveis. Isso permite que o usuário sinta controle total sobre seu desenvolvimento, maximizando resultados com eficiência e precisão.

### Personalidade

*   **Objetivo:** MIKE é direto ao ponto, sem floreios. Sua comunicação e interface são claras, focadas na tarefa e na entrega de informações essenciais para o treino. Isso reflete a mentalidade de quem busca resultados concretos. **Implicações Visuais:** Interfaces limpas, hierarquia visual clara, ausência de elementos decorativos desnecessários.
*   **Preciso:** Cada dado, cada registro, cada análise no MIKE é tratado com exatidão. A precisão não é apenas uma característica, mas um valor que garante a confiabilidade das informações e a eficácia do acompanhamento do progresso. **Implicações Visuais:** Alinhamentos perfeitos, tipografia com boa legibilidade para números, gráficos exatos e sem ruído.
*   **Motivador:** Embora sério, MIKE inspira o usuário a ir além. Através de feedback claro e visualização de progresso, ele impulsiona a disciplina e a busca contínua por melhoria, sem recorrer a artifícios infantis ou superficiais. **Implicações Visuais:** Uso estratégico da cor de acento para feedback positivo, gráficos de progresso claros, badges de conquista.
*   **Disciplinado:** O app reflete a disciplina necessária para o treinamento Heavy Duty. Ele encoraja a consistência e a aderência a um plano, transformando o registro de treino em um hábito recompensador. **Implicações Visuais:** Consistência visual em todos os componentes, padrões de interação previsíveis, foco na funcionalidade.

### Princípios de Design

1.  **Foco no Essencial:** Eliminar qualquer elemento visual ou funcional que não contribua diretamente para o registro ou análise do treino. A interface deve ser limpa, sem distrações, permitindo que o usuário se concentre na tarefa.
    *   **Por quê:** Reduz a carga cognitiva, melhora a usabilidade e alinha-se à filosofia Heavy Duty de "sem firula".
    *   **Como aplicar:** Layouts minimalistas, hierarquia visual clara, uso parcimonioso de cores e ícones. Priorizar informações críticas e esconder complexidade progressivamente.
2.  **Clareza e Legibilidade:** As informações mais importantes (cargas, repetições, séries, progresso) devem ser imediatamente compreensíveis e fáceis de ler, mesmo em condições de pouca luz ou em movimento.
    *   **Por quê:** Garante acessibilidade, reduz erros e aumenta a eficiência do usuário no registro de dados.
    *   **Como aplicar:** Tipografia robusta e de alto contraste, tamanhos de fonte adequados, espaçamento generoso. Testar legibilidade em diferentes dispositivos e condições de iluminação.
3.  **Feedback Instantâneo e Acionável:** Cada interação do usuário deve gerar uma resposta clara e imediata, informando sobre o sucesso da ação ou a necessidade de correção. O feedback deve guiar o usuário para a próxima etapa ou para a melhoria.
    *   **Por quê:** Reforça o comportamento desejado (recompensa), reduz a incerteza e melhora a sensação de controle do usuário.
    *   **Como aplicar:** Microinterações, mensagens de confirmação/erro concisas (toasts), indicadores de progresso visualmente distintos. Usar cores semânticas para feedback de status.
4.  **Consistência Previsível:** Elementos de interface, padrões de interação e linguagem visual devem ser consistentes em todo o aplicativo, construindo familiaridade e reduzindo a carga cognitiva. O usuário deve saber o que esperar.
    *   **Por quê:** Constrói confiança, acelera o aprendizado do usuário e otimiza o desenvolvimento e manutenção do produto.
    *   **Como aplicar:** Reuso de componentes, padrões de navegação unificados, estilo de ícones e ilustrações coesos. Utilizar tokens de design para garantir uniformidade.
5.  **Progressão Visual e Motivadora:** O design deve destacar o progresso do usuário de forma clara e inspiradora, utilizando elementos visuais que reforcem a ideia de avanço, superação e conquista.
    *   **Por quê:** Explora o viés do progresso e o efeito gradiente de metas, incentivando a continuidade e a disciplina.
    *   **Como aplicar:** Gráficos de progresso intuitivos, badges de conquista, comparações visuais com desempenhos anteriores, uso estratégico da cor de destaque para indicar sucesso (PRs, streaks).

## 2. Arquitetura do Design System

### Filosofia do Sistema

O Design System do MIKE adota uma abordagem atômica, onde os elementos são construídos a partir de unidades menores e mais reutilizáveis. Essa filosofia garante consistência, escalabilidade e eficiência no desenvolvimento e manutenção do produto.

*   **Tokens:** As menores unidades visuais (cores, tipografia, espaçamento, raio de borda). São a base de todas as decisões de design e permitem mudanças globais rápidas e consistentes.
*   **Componentes:** Blocos de UI reutilizáveis (botões, inputs, cards) construídos a partir dos tokens. Possuem estados e regras de uso bem definidos.
*   **Padrões:** Combinações de componentes e tokens para resolver problemas de UI/UX comuns (ex: formulários de login, navegação). Guiam a interação e a experiência do usuário.
*   **Templates:** Estruturas de layout pré-definidas para telas inteiras, utilizando padrões e componentes. Aceleram a criação de novas telas e garantem a coesão visual.

### Convenções de Nomenclatura

Para garantir clareza e consistência, as convenções de nomenclatura seguem um padrão lógico e descritivo:

*   **Cores:** `color-<função>-<intensidade>` (ex: `color-mike-accent`, `color-text-primary`, `color-success-light`).
*   **Tipografia:** `font-family-<tipo>`, `font-weight-<peso>`, `font-size-<tamanho>`, `line-height-<tamanho>` (ex: `font-family-primary`, `font-size-h1`).
*   **Espaçamento:** `spacing-<tamanho>` (ex: `spacing-md`, `spacing-xl`).
*   **Raio de Borda:** `border-radius-<tamanho>` (ex: `border-radius-md`).

### Como Versionar e Atualizar este Manual

Este manual é um documento vivo. Sua versão (`v1.0`) indica o estado atual das diretrizes. Atualizações e novas versões serão gerenciadas através de um sistema de controle de versão (ex: Git) e comunicadas à equipe. Pequenas alterações podem ser incorporadas em revisões menores (ex: v1.1), enquanto mudanças significativas na arquitetura ou na identidade visual justificarão uma nova versão principal (ex: v2.0).

---

## 3. Identidade da Marca

### Nome e Escrita Correta

O nome do aplicativo é **MIKE**. Deve ser sempre escrito em **letras maiúsculas** para transmitir força e impacto, alinhado à filosofia Heavy Duty.

*   **DO:** MIKE
*   **DON'T:** Mike, mike, M.I.K.E.

### Tom de Voz: Guidelines e Exemplos de Microcopy

O tom de voz do MIKE é **direto, encorajador e informativo**, sempre com foco no progresso e na objetividade. Evita jargões desnecessários e mantém uma postura de guia confiável. A comunicação deve ser concisa e funcional, sem infantilizar ou usar linguagem excessivamente informal.

*   **Guidelines:**
    *   **Clareza:** Use linguagem simples e direta. Evite ambiguidades.
    *   **Objetividade:** Vá direto ao ponto. O usuário está focado no treino.
    *   **Encorajamento:** Motive o usuário a continuar, a progredir, a ser consistente.
    *   **Respeito:** Mantenha uma postura profissional e respeitosa, mesmo em mensagens de erro.

*   **Exemplos de Microcopy:**
    *   **Botões (CTA):** "Registrar Treino", "Iniciar Série", "Finalizar Exercício", "Ver Progresso", "Adicionar Carga", "Salvar Alterações", "Excluir Treino".
    *   **Mensagens de Sucesso:**
        *   "Treino registrado com sucesso! Mais um passo rumo ao seu objetivo."
        *   "Novo Recorde Pessoal! Excelente trabalho."
        *   "Consistência é a chave. Mantenha o ritmo!"
    *   **Mensagens de Erro:**
        *   "Ops! Não foi possível registrar o treino. Verifique sua conexão."
        *   "Carga inválida. Por favor, insira um valor numérico."
        *   "Algo deu errado. Tente novamente mais tarde."
    *   **Empty States:**
        *   "Nenhum treino registrado ainda. Que tal começar hoje?"
        *   "Seu histórico de progresso aparecerá aqui. Registre seu primeiro treino!"
        *   "Sem dados para este período. Ajuste o filtro ou registre mais treinos."

### Uso do Logo (Regras, Respiros, Usos Proibidos)

O logo do MIKE, seja o wordmark ou o símbolo compacto, deve ser tratado com rigor para manter sua integridade e reconhecimento.

*   **Regras de Uso:**
    *   **Wordmark:** Usado em contextos onde o nome completo do app é necessário e há espaço suficiente (ex: telas de onboarding, cabeçalhos de seções principais).
    *   **Símbolo Compacto:** Ideal para ícones de aplicativo, favicons, e pequenos espaços onde o reconhecimento visual é primordial.
    *   **Cores:** O logo deve ser aplicado nas cores `MIKE Primary` (Light Mode) ou `MIKE Primary Dark` (Dark Mode) sobre fundos de alto contraste. Versões monocromáticas (branco ou preto) são permitidas para fundos coloridos ou imagens.

*   **Área de Respiro:** Uma área de respiro mínima deve ser mantida ao redor do logo para garantir sua clareza e destaque. Essa área deve ser equivalente a `X` (onde `X` é a altura da letra "M" do logotipo) em todos os lados. Isso evita que outros elementos visuais invadam o espaço do logo.

*   **Tamanhos Mínimos:** Definir tamanhos mínimos para o logotipo e o símbolo para assegurar legibilidade em diferentes contextos digitais e impressos. Para o símbolo, o tamanho mínimo recomendado é de 24x24px para ícones de interface e 48x48px para ícones de aplicativo.

*   **Usos Proibidos:**
    *   NÃO distorcer, esticar ou comprimir o logo.
    *   NÃO alterar as cores do logo fora das especificações da paleta.
    *   NÃO adicionar efeitos (sombras, gradientes) ou elementos gráficos ao logo.
    *   NÃO rotacionar o logo.
    *   NÃO usar o logo sobre fundos de baixo contraste que comprometam a legibilidade.
    *   NÃO usar o símbolo compacto como wordmark e vice-versa.

### "Sensação Heavy Duty" Aplicada: Como Manter Disciplina e Foco no Design sem Agressividade

A "Sensação Heavy Duty" no design do MIKE é alcançada através de uma combinação de elementos visuais e interativos que transmitem **força, objetividade e seriedade**, sem cair na agressividade ou no caricatural. É sobre a **disciplina implacável** de Mike Mentzer, não sobre a imagem estereotipada de fisiculturistas.

*   **Como Aplicar:**
    *   **Minimalismo Funcional:** Remover elementos decorativos. Cada pixel deve ter um propósito.
    *   **Tipografia Robusta:** Fontes fortes e legíveis que transmitam autoridade e clareza.
    *   **Alto Contraste:** Garante que as informações mais importantes se destaquem, especialmente dados e métricas.
    *   **Espaçamento Generoso:** Cria uma sensação de ordem e permite que os elementos "respirem", evitando a sobrecarga visual.
    *   **Cores Estratégicas:** Usar o acento de forma pontual para guiar o olhar e destacar o progresso, mantendo a base neutra e séria.
    *   **Feedback Direto:** Mensagens claras e concisas, sem rodeios, que informam o usuário sobre o status de suas ações.
    *   **Evitar Clichês:** Abster-se de imagens ou ícones que remetam a estereótipos de "bodybuilding" ou "gamer exagerado". Focar na performance e nos dados.

---

## 4. Paleta de Cores

A paleta de cores do app MIKE é projetada para reforçar a filosofia Heavy Duty: **foco, seriedade, progresso e motivação**, sem distrações. As escolhas são fundamentadas na psicologia das cores e na economia comportamental para otimizar a experiência do usuário, reduzir a fricção e incentivar a consistência. A paleta é robusta para funcionar tanto em modo claro quanto escuro, com atenção especial à acessibilidade.

### Lista Completa das Cores

#### Paleta Primária

| Nome Funcional | HEX (Light Mode) | HEX (Dark Mode) | Uso Principal |
|---|---|---|---|
| **MIKE Primary** | `#1A1A1A` | `#F0F0F0` | Fundo principal (Dark Mode), texto primário (Light Mode) |
| **MIKE Surface** | `#FFFFFF` | `#121212` | Fundo principal (Light Mode), superfícies de cards, painéis |
| **MIKE Accent** | `#007BFF` | `#66B2FF` | Botões de ação primária, indicadores de progresso, gráficos de destaque |

#### Paleta Secundária

| Nome Funcional | HEX (Light Mode) | HEX (Dark Mode) | Uso Principal |
|---|---|---|---|
| **MIKE Secondary** | `#4A4A4A` | `#B0B0B0` | Texto secundário, ícones não interativos, bordas de elementos |
| **MIKE Border** | `#E0E0E0` | `#333333` | Linhas divisórias, bordas de inputs e cards |
| **MIKE Graph** | `#6C757D` | `#888888` | Linhas de gráficos secundárias, elementos de dados menos proeminentes |

#### Neutros (Cinzas/Tons para Fundo e Texto)

| Nome Funcional | HEX (Light Mode) | HEX (Dark Mode) | Uso Principal |
|---|---|---|---|
| **Text Primary** | `#1A1A1A` | `#F0F0F0` | Títulos, textos de corpo principal |
| **Text Secondary** | `#4A4A4A` | `#B0B0B0` | Descrições, legendas, textos de menor importância |
| **Background Light** | `#F8F8F8` | `#0A0A0A` | Fundo de telas, áreas de conteúdo |

#### Cores Semânticas

| Nome Funcional | HEX (Light Mode) | HEX (Dark Mode) | Uso Principal |
|---|---|---|---|
| **Success** | `#28A745` | `#4CAF50` | Mensagens de sucesso, ícones de conclusão, indicadores de progresso positivo |
| **Warning** | `#FFC107` | `#FFD700` | Alertas, avisos, informações que requerem atenção |
| **Error** | `#DC3545` | `#EF5350` | Mensagens de erro, validação de formulário falha, ações destrutivas |
| **Info** | `#17A2B8` | `#2196F3` | Informações adicionais, dicas, estados neutros de notificação |

### Regras para Light e Dark Mode

O sistema de cores do MIKE é projetado para ser totalmente adaptável entre os modos claro e escuro. As variáveis CSS (`--color-<nome>-light` e `--color-<nome>-dark`) garantem que a transição seja suave e consistente.

*   **O que muda:** As cores de fundo, texto e elementos de superfície são invertidas ou ajustadas para manter a legibilidade e o conforto visual. Por exemplo, o `MIKE Primary` é escuro no modo claro e claro no modo escuro.
*   **O que não muda:** As cores semânticas (`Success`, `Warning`, `Error`, `Info`) mantêm sua conotação, mas seus tons são ajustados para garantir contraste e vivacidade em ambos os modos. O `MIKE Accent` também mantém sua função de destaque, com um tom ligeiramente mais claro no dark mode para maior visibilidade.

### Cores Semânticas e Quando Usar

As cores semânticas são cruciais para fornecer feedback rápido e intuitivo ao usuário, aproveitando associações universais.

*   **Success (`#28A745` / `#4CAF50`):** Use para indicar ações bem-sucedidas, conclusão de tarefas, progresso positivo (ex: PRs, streaks), e feedback de validação positiva. **Por quê:** O verde é universalmente associado a sucesso e segurança, reforçando o viés do progresso.
*   **Warning (`#FFC107` / `#FFD700`):** Use para alertas, avisos, informações que requerem atenção, ou para indicar um estado intermediário/neutro que não é necessariamente um erro, mas precisa de verificação (ex: deload, volume alto). **Por quê:** Amarelo/laranja sinaliza cautela e atenção, sem ser alarmante.
*   **Error (`#DC3545` / `#EF5350`):** Use para mensagens de erro, validação de formulário falha, ações destrutivas ou feedback negativo. **Por quê:** O vermelho é universalmente associado a perigo e erro, exigindo atenção imediata.
*   **Info (`#17A2B8` / `#2196F3`):** Use para informações adicionais, dicas, ou estados neutros de notificação que fornecem contexto sem conotação positiva ou negativa forte. **Por quê:** Azul/ciano transmite informação, clareza e neutralidade.

### Regras de Contraste (WCAG AA como Referência)

A acessibilidade é uma prioridade. Todas as combinações de cores de texto e fundo devem atender, no mínimo, aos requisitos WCAG AA.

*   **Regra Geral:** Contraste mínimo de **4.5:1** para texto normal e **3:1** para texto grande (18pt ou 14pt bold).
*   **Práticas para Validar:**
    *   Utilize ferramentas online como [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) ou plugins de navegador (ex: Axe DevTools) para verificar as combinações de cores.
    *   Teste em diferentes condições de iluminação e em dispositivos variados.
    *   Considere usuários com diferentes tipos de daltonismo.

#### Tabela de Combinações de Contraste (Exemplos)

| Fundo | Texto Claro (Ex: `#F0F0F0`) | Texto Escuro (Ex: `#1A1A1A`) |
|---|---|---|
| **MIKE Primary** (`#1A1A1A`) | ✅ Bom Contraste | ❌ Baixo Contraste |
| **MIKE Surface** (`#FFFFFF`) | ❌ Baixo Contraste | ✅ Bom Contraste |
| **MIKE Accent** (`#007BFF`) | ✅ Bom Contraste | ❌ Baixo Contraste |
| **Success** (`#28A745`) | ✅ Bom Contraste | ❌ Baixo Contraste |
| **Error** (`#DC3545`) | ✅ Bom Contraste | ❌ Baixo Contraste |
| **Background Light** (`#F8F8F8`) | ❌ Baixo Contraste | ✅ Bom Contraste |
| **MIKE Primary (Dark Mode)** (`#F0F0F0`) | ❌ Baixo Contraste | ✅ Bom Contraste |
| **MIKE Surface (Dark Mode)** (`#121212`) | ✅ Bom Contraste | ❌ Baixo Contraste |
| **MIKE Accent (Dark Mode)** (`#66B2FF`) | ✅ Bom Contraste | ❌ Baixo Contraste |

### Paleta para Gráficos (Séries, Volume, PRs, Alertas)

Para visualização de dados, a paleta deve ser usada de forma estratégica para garantir clareza e destaque das informações mais importantes.

*   **Séries/Volumes:** Utilizar o `MIKE Accent` para a série principal ou o volume total. Para diferenciar múltiplas séries ou categorias, usar tons mais claros/escuros do `MIKE Accent` ou cores da paleta secundária (`MIKE Graph`, `MIKE Secondary`) de forma hierárquica.
*   **PRs (Recordes Pessoais):** Sempre destacar PRs com a cor `Success` para reforçar a conquista e o progresso.
*   **Alertas/Metas:** Usar `Warning` para indicar que uma meta está próxima ou que há um desvio, e `Error` para indicar falhas ou problemas críticos nos dados.

### Do / Don’t de Cor

*   **DO:**
    *   Use `MIKE Accent` para indicar ações primárias, elementos interativos e feedback positivo de progresso. **Por quê:** Cria saliência e motivação.
    *   Use `Success` para mensagens de êxito e conclusão de tarefas. **Por quê:** Reforça o viés do progresso.
    *   Mantenha um contraste mínimo de 4.5:1 para texto pequeno e 3:1 para texto grande em relação ao fundo. **Por quê:** Garante acessibilidade (WCAG AA).
    *   Utilize a paleta de neutros para estabelecer hierarquia visual e garantir legibilidade. **Por quê:** Reduz a carga cognitiva.
    *   Garanta que o `MIKE Accent` seja vibrante o suficiente para motivar, mas não tão saturado que cause fadiga visual. **Por quê:** Equilíbrio entre impacto e conforto.

*   **DON’T:**
    *   NÃO use `Error` (vermelho) para indicar sucesso ou progresso positivo. **Por quê:** Cria confusão e ansiedade no usuário.
    *   NÃO use cores de acento ou semânticas para grandes blocos de texto ou fundos extensos, a menos que seja para um propósito muito específico e com contraste garantido. **Por quê:** Dilui o impacto e polui a interface.
    *   NÃO introduza cores fora desta paleta sem justificativa e validação de acessibilidade. **Por quê:** Compromete a consistência e a acessibilidade.
    *   NÃO use cores muito claras em fundos claros ou cores muito escuras em fundos escuros para texto. **Por quê:** Compromete severamente a legibilidade e a acessibilidade.
    *   NÃO use o `MIKE Accent` de forma excessiva. **Por quê:** Dilui seu impacto e torna a interface visualmente poluída. Ele deve ser um ponto de destaque, não a regra.

---

## 5. Tipografia

A escolha tipográfica para o app MIKE é fundamental para comunicar os valores de **performance, disciplina e precisão**, ao mesmo tempo em que garante **legibilidade máxima** em ambientes digitais, especialmente em dispositivos móveis. As fontes foram selecionadas com foco em clareza, modernidade e a capacidade de transmitir dados de forma eficiente. Preferencialmente, serão utilizadas fontes do Google Fonts para facilitar a implementação.

### Fontes Escolhidas e Motivo

*   **Fonte Principal (UI): Montserrat**
    *   **Motivo:** Montserrat é uma fonte geométrica sans-serif com uma estética moderna e limpa. Sua estrutura robusta e formas bem definidas transmitem **solidez e confiabilidade**, alinhando-se perfeitamente à Rota Visual "Industrial / Minimalista / Força". Possui uma ampla gama de pesos, o que permite uma hierarquia tipográfica rica e flexível. Sua legibilidade é excelente em diferentes tamanhos, crucial para a interface de um aplicativo.
*   **Fonte Secundária (Destaques, Números, Títulos): Oswald**
    *   **Motivo:** Oswald é uma fonte sans-serif condensada, otimizada para uso em telas digitais. Sua natureza condensada e forte confere **impacto e eficiência** ao ocupar menos espaço horizontal, ideal para títulos e números que precisam se destacar. Ela complementa a Montserrat ao adicionar um toque de **força e dinamismo**, sem comprometer a seriedade. É particularmente eficaz para exibir métricas e dados numéricos, onde a clareza e a leitura rápida são essenciais.
*   **Fonte Mono (Opcional para Dados Tabulares): Roboto Mono**
    *   **Motivo:** Roboto Mono é uma fonte monoespaçada que garante alinhamento preciso de caracteres, ideal para exibir dados tabulares, códigos ou qualquer informação que exija uniformidade de largura. Transmite **precisão e organização**, facilitando a leitura e comparação de dados como séries, repetições e cargas em tabelas de histórico de treino.

### Escala Tipográfica

A escala tipográfica é baseada em um sistema modular para garantir consistência e hierarquia visual em todo o aplicativo. Os tamanhos e pesos são definidos para otimizar a legibilidade em dispositivos móveis.

| Elemento | Fonte | Peso | Tamanho (px) | Line-height | Uso |
|---|---|---|---|---|---|
| **H1** | Oswald | Bold (700) | 32px | 1.2 | Títulos de página principais |
| **H2** | Oswald | SemiBold (600) | 24px | 1.3 | Títulos de seção |
| **H3** | Montserrat | Bold (700) | 20px | 1.4 | Subtítulos, destaques |
| **H4** | Montserrat | SemiBold (600) | 18px | 1.5 | Títulos de cards |
| **H5** | Montserrat | Medium (500) | 16px | 1.5 | Labels, elementos de UI |
| **H6** | Montserrat | Regular (400) | 14px | 1.6 | Texto de corpo secundário |
| **Body** | Montserrat | Regular (400) | 16px | 1.6 | Texto de corpo principal, parágrafos |
| **Small** | Montserrat | Regular (400) | 12px | 1.6 | Legendas, textos de apoio |
| **Caption** | Montserrat | Light (300) | 10px | 1.6 | Textos muito pequenos, notas de rodapé |
| **Numbers (Large)** | Oswald | Bold (700) | 48px | 1 | Cargas, PRs em destaque |

### Regras para Números e Dados (Legibilidade de Carga, Reps, Volume)

A legibilidade de números é crítica para o app MIKE. A fonte Oswald, com seu estilo condensado e forte, é ideal para este propósito.

*   **Prioridade:** Números que representam cargas, repetições, séries, volume e PRs devem ser instantaneamente legíveis e distinguíveis.
*   **Uso:** Utilizar Oswald com peso Bold para números em destaque (ex: 48px para PRs, 32px para cargas atuais). Para tabelas e listas de dados, Roboto Mono pode ser usada para garantir alinhamento preciso.
*   **Espaçamento:** Garantir espaçamento adequado entre números e unidades (ex: "100 kg" e não "100kg").

### Regras de Espaçamento, Altura de Linha, Uso de CAPS

*   **Espaçamento:** Utilizar o sistema de espaçamento baseado em 8px (ver seção 6) para margens, paddings e espaçamento entre elementos. Isso garante harmonia vertical e horizontal.
*   **Altura de Linha (Line-height):** As alturas de linha são especificadas na escala tipográfica para otimizar a legibilidade. Manter `line-height` ligeiramente maior que o tamanho da fonte para textos de corpo, e mais compacto para títulos.
*   **Uso de CAPS:** Utilizar ALL CAPS com moderação, principalmente para títulos curtos ou labels de botões onde se deseja um impacto maior e uma sensação de comando. Evitar em blocos de texto longos para não prejudicar a legibilidade. **Por quê:** ALL CAPS em textos longos dificulta a leitura e a identificação de palavras.

### Exemplos de Hierarquia: “Tela de Treino” e “Tela de Relatório” (Descrito)

*   **Tela de Treino:**
    *   **Título da Página (H1):** "Treino de Costas" (Oswald Bold, 32px)
    *   **Nome do Exercício (H3):** "Barra Fixa" (Montserrat Bold, 20px)
    *   **Detalhes da Série (Body):** "3 séries x 10 reps" (Montserrat Regular, 16px)
    *   **Carga/Repetições Atuais (Numbers Large):** "100 kg" / "10 reps" (Oswald Bold, 48px)
    *   **Botões de Ação (H5):** "Registrar Série" (Montserrat Medium, 16px, ALL CAPS)

*   **Tela de Relatório:**
    *   **Título da Página (H1):** "Seu Progresso" (Oswald Bold, 32px)
    *   **Métrica Principal (Numbers Large):** "120 kg" (PR de Supino) (Oswald Bold, 48px)
    *   **Subtítulo da Métrica (H4):** "Supino Reto" (Montserrat SemiBold, 18px)
    *   **Eixo de Gráfico (Small):** "Semana 1" (Montserrat Regular, 12px)
    *   **Legendas de Gráfico (Caption):** "Volume Total" (Montserrat Light, 10px)

---

## 6. Grid, Layout e Espaçamento

O sistema de grid, layout e espaçamento do MIKE é projetado para criar interfaces organizadas, eficientes e visualmente equilibradas, garantindo uma experiência consistente em diferentes tamanhos de tela.

### Grid Base (8px) e Por Quê

O MIKE utiliza um **grid base de 8px** para todas as medidas de espaçamento e dimensionamento de elementos. Isso significa que margens, paddings, alturas e larguras de componentes devem ser múltiplos de 8px.

*   **Por quê:**
    *   **Consistência:** Garante que todos os elementos se alinhem harmoniosamente, criando um ritmo visual coeso.
    *   **Escalabilidade:** Facilita a adaptação do design para diferentes resoluções e densidades de pixel, mantendo a proporção.
    *   **Eficiência:** Simplifica o processo de design e desenvolvimento, pois as decisões de espaçamento são pré-definidas.
    *   **Acessibilidade:** Ajuda a manter touch targets de tamanho adequado e espaçamento suficiente entre elementos interativos.

### Breakpoints e Comportamento Mobile-First

O design do MIKE é **mobile-first**, o que significa que a experiência é projetada e desenvolvida primeiramente para telas pequenas, e depois adaptada para telas maiores (tablets, desktops).

*   **Breakpoints (Bootstrap 5):**
    *   `xs`: < 576px (Extra small devices - portrait phones)
    *   `sm`: ≥ 576px (Small devices - landscape phones)
    *   `md`: ≥ 768px (Medium devices - tablets)
    *   `lg`: ≥ 992px (Large devices - desktops)
    *   `xl`: ≥ 1200px (Extra large devices - large desktops)
    *   `xxl`: ≥ 1400px (Extra extra large devices - wider desktops)
*   **Comportamento Mobile-First:**
    *   Priorizar o conteúdo essencial em telas pequenas.
    *   Utilizar layouts de coluna única ou empilhados para facilitar a leitura e a interação.
    *   Elementos de navegação adaptados (ex: bottom navigation, menu hambúrguer).
    *   Aumentar o espaçamento e a complexidade do layout progressivamente para telas maiores.

### Margens e Paddings Recomendados para Telas Principais

*   **Margens Externas (Container):** `var(--spacing-lg)` (32px) nas laterais para telas maiores, reduzindo para `var(--spacing-md)` (24px) ou `var(--spacing-sm)` (16px) em mobile.
*   **Paddings Internos (Seções/Cards):** `var(--spacing-md)` (24px) ou `var(--spacing-lg)` (32px) para seções principais. `var(--spacing-sm)` (16px) para paddings internos de cards e componentes menores.
*   **Espaçamento entre Elementos:** Utilizar `var(--spacing-xs)` (8px), `var(--spacing-sm)` (16px) ou `var(--spacing-md)` (24px) para espaçamento vertical e horizontal entre elementos, dependendo da hierarquia e agrupamento.

### Regras de Densidade de Informação (Como Mostrar Muitos Dados sem Poluir)

O MIKE lida com muitos dados de treino. É crucial apresentá-los de forma clara e sem sobrecarga.

*   **Agrupamento Lógico:** Agrupar informações relacionadas em cards ou seções distintas.
*   **Hierarquia Visual:** Usar tipografia, cores e espaçamento para guiar o olho do usuário para as informações mais importantes.
*   **Progressive Disclosure:** Esconder detalhes menos relevantes atrás de toggles, modais ou navegação secundária, revelando-os apenas quando o usuário precisar.
*   **Visualização de Dados:** Utilizar gráficos e tabelas de forma eficiente, destacando tendências e PRs, sem sobrecarregar com números brutos.
*   **Minimalismo:** Remover bordas, sombras ou fundos desnecessários que adicionem ruído visual.

### Padrões de Cards (Sessão, Exercício, Set)

Cards são contêineres versáteis para agrupar informações. No MIKE, eles são usados para representar sessões de treino, exercícios individuais e sets.

*   **Card de Sessão de Treino:**
    *   **Objetivo:** Resumir um treino completo.
    *   **Conteúdo:** Data, duração, número de exercícios, volume total, status (concluído/em progresso).
    *   **Estilo:** Fundo `MIKE Surface`, `border-radius-lg`, `shadow-md`.
*   **Card de Exercício:**
    *   **Objetivo:** Detalhar um exercício dentro de uma sessão.
    *   **Conteúdo:** Nome do exercício, número de séries/repetições, carga média, PRs alcançados.
    *   **Estilo:** Fundo `MIKE Surface`, `border-radius-md`, `shadow-sm`.
*   **Card de Set:**
    *   **Objetivo:** Registrar ou exibir os detalhes de um set individual.
    *   **Conteúdo:** Número da série, repetições, carga, RPE/RIR (opcional), status (concluído/falha).
    *   **Estilo:** Fundo `MIKE Surface` ou `Background Light`, `border-radius-sm`, sem sombra para sets individuais dentro de um card de exercício.

---

## 7. Iconografia e Estilo Gráfico

O estilo gráfico do app MIKE complementa a direção visual "Industrial / Minimalista / Força", focando na **funcionalidade, clareza e impacto visual**, sem elementos desnecessários. A abordagem é sóbria, moderna e alinhada à seriedade do propósito do aplicativo.

### Estilo de Ícone

Os ícones devem ser **lineares (outline)**, com uma **espessura de linha consistente** (ex: 2px) e **cantos levemente arredondados** (ex: 2px de raio) para suavizar a estética industrial sem perder a robustez. Devem ser **geométricos e simplificados**, representando conceitos de forma direta e universalmente compreensível.

*   **Consistência:** Utilizar uma biblioteca de ícones unificada (ex: Bootstrap Icons) para garantir coesão.
*   **Grid:** Recomenda-se um grid de 24x24px ou 32x32px para o design dos ícones.
*   **Por quê:** Ícones outline são mais leves visualmente e contribuem para a estética minimalista. A consistência na espessura e nos cantos arredondados cria uma linguagem visual coesa e profissional. A simplicidade garante que os ícones sejam facilmente reconhecíveis e não sobrecarreguem a interface, reduzindo a fricção cognitiva.

### Regras de Uso (Quando Usar Ícone Sozinho vs com Texto)

*   **Ícone Sozinho:** Usar apenas quando o significado é universalmente compreendido (ex: ícone de "play", "configurações", "lixeira"). Ideal para barras de navegação, botões de ação secundária e elementos de lista.
*   **Ícone com Texto:** Usar quando o significado pode ser ambíguo ou para reforçar a mensagem. Essencial para botões de ação primária, itens de menu complexos e para guiar o usuário em novas funcionalidades. **Por quê:** A combinação de ícone e texto melhora a clareza e a acessibilidade, especialmente para usuários menos familiarizados ou com deficiências cognitivas.

### Ilustrações (Se Usar): Princípios e Limites

As ilustrações, se utilizadas, devem ser **minimalistas e funcionais**, servindo para clarificar conceitos ou guiar o usuário, e não como elementos puramente decorativos. Devem seguir a paleta de cores definida, utilizando principalmente os neutros e o `MIKE Accent` para destaques.

*   **Princípios:**
    *   **Funcionalidade:** Cada ilustração deve ter um propósito claro (ex: explicar um conceito, preencher um empty state de forma útil).
    *   **Minimalismo:** Linhas limpas, formas geométricas simples, sem detalhes excessivos.
    *   **Coerência:** Estilo e paleta de cores alinhados com o restante do design system.
*   **Limites:**
    *   NÃO usar ilustrações complexas ou com muitos detalhes que possam distrair.
    *   NÃO usar ilustrações com estilo "cartoon" ou infantilizado.
    *   NÃO usar ilustrações que não adicionem valor funcional ou explicativo.

### Fotografia (Se Usar): Direção e Limites (Sem “Bro Science”)

Se a fotografia for incorporada, ela deve ser utilizada com moderação e seguir um estilo que reforce a seriedade e a autenticidade do treino, evitando clichês ou imagens "bro science".

*   **Direção:**
    *   **Preto e Branco com Acabamento Fosco:** Fotografias em preto e branco com alto contraste, mas com um acabamento que evite o brilho excessivo, transmitindo uma sensação de realismo e foco.
    *   **Foco em Detalhes de Treino:** Imagens que capturam a essência do esforço e da técnica: mãos segurando barras, a textura de anilhas, o suor na pele, a concentração no rosto. Priorizar a ação e o processo.
    *   **Composição Limpa:** Fotografias com composições simples, que destacam o elemento principal sem fundos poluídos.
*   **Limites:**
    *   NÃO usar fotos de modelos posando ou com foco excessivo em corpos esculturais. **Por quê:** Evita a superficialidade e o estereótipo de "bro science", focando na performance real.
    *   NÃO usar fotos com cores vibrantes ou filtros excessivos que destoem da paleta de cores do app.
    *   NÃO usar fotos que não transmitam autenticidade ou que pareçam genéricas. 

---

## 8. Componentes UI (Catálogo Operacional)

Os componentes UI são os blocos de construção reutilizáveis do aplicativo MIKE, desenvolvidos com base nos tokens de design. Cada componente é projetado para ser funcional, acessível e consistente, garantindo uma experiência de usuário coesa e eficiente.

### Buttons (Botões)

Botões são elementos interativos que permitem ao usuário realizar ações. Devem ser claros, responsivos e visualmente distintos para cada tipo de ação.

*   **Objetivo:** Iniciar uma ação ou evento.
*   **Anatomia:** Texto (obrigatório), Ícone (opcional).
*   **Variantes:**
    *   **Primary:** Para a ação mais importante em uma tela. Usa `MIKE Accent`.
    *   **Secondary:** Para ações secundárias, menos proeminentes. Usa `MIKE Secondary` ou `MIKE Primary` com fundo `MIKE Surface`.
    *   **Ghost:** Botão transparente, para ações de baixa hierarquia ou em contextos onde o fundo já é visualmente rico.
    *   **Danger:** Para ações destrutivas ou irreversíveis. Usa `Error`.
*   **Estados:**
    *   **Default:** Estado normal do botão.
    *   **Hover:** Feedback visual quando o cursor está sobre o botão (opacidade reduzida).
    *   **Active:** Feedback visual quando o botão é clicado.
    *   **Focus:** Anel de foco visível (`--state-focus-ring`) para navegação por teclado.
    *   **Disabled:** Botão inativo, com opacidade reduzida (`--state-disabled-opacity`) e cursor `not-allowed`.
    *   **Loading:** Indicador visual (spinner) dentro do botão para ações assíncronas.
*   **Acessibilidade:**
    *   Garantir que o contraste de cor do texto do botão com o fundo atenda ao WCAG AA.
    *   Fornecer um `aria-label` descritivo se o botão contiver apenas um ícone.
    *   Garantir que o estado `focus` seja claramente visível.
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Use um botão primário por tela para guiar o usuário para a ação mais importante. Use texto claro e conciso. Posicione botões de ação destrutiva de forma que não sejam clicados acidentalmente.
    *   **DON'T:** Use múltiplos botões primários na mesma tela. Use texto ambíguo. Esconda o estado `disabled` ou `focus`.

### Inputs (Text/Number), Select, Textarea

Campos de entrada de dados para o usuário. Devem ser claros, com feedback de estado e acessíveis.

*   **Objetivo:** Coletar informações do usuário.
*   **Anatomia:** Label, Campo de entrada, Placeholder, Helper text (opcional), Ícone (opcional).
*   **Variantes:** `text`, `number`, `email`, `password`, `select`, `textarea`.
*   **Estados:**
    *   **Default:** Estado normal do campo.
    *   **Focus:** Borda destacada (`MIKE Accent`) e anel de foco visível.
    *   **Disabled:** Campo inativo, com fundo e texto esmaecidos.
    *   **Error:** Borda e/ou texto do helper text em `Error`.
    *   **Success:** Borda e/ou texto do helper text em `Success`.
*   **Acessibilidade:**
    *   Labels associadas aos campos (`for` e `id`).
    *   Mensagens de erro claras e associadas ao campo (`aria-describedby`).
    *   Navegação por teclado e foco lógico.
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Use labels claras e descritivas. Forneça helper text para guiar o usuário. Use tipos de input apropriados (ex: `type="number"` para números). Use `autofocus` com moderação.
    *   **DON'T:** Use placeholders como substitutos de labels. Esconda mensagens de erro. Use inputs de texto para números sem validação.

### Form Validation (Validação de Formulário)

Feedback visual e textual para informar o usuário sobre o status da entrada de dados.

*   **Objetivo:** Guiar o usuário na correção de erros e na entrada de dados válidos.
*   **Anatomia:** Mensagem de erro/sucesso, destaque visual no campo.
*   **Variantes:** `error`, `success`, `warning`.
*   **Estados:**
    *   **Error:** Campo com borda `Error`, mensagem de erro em `Error`.
    *   **Success:** Campo com borda `Success`, mensagem de sucesso em `Success`.
*   **Acessibilidade:**
    *   Mensagens de erro devem ser programaticamente associadas ao campo (ex: `aria-describedby`).
    *   Feedback visual e textual para todos os tipos de deficiência.
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Valide em tempo real (on blur) para feedback imediato. Seja específico sobre o erro. Posicione a mensagem de erro próxima ao campo relevante.
    *   **DON'T:** Valide apenas no submit. Use mensagens genéricas de erro. Esconda o feedback de validação.

### Cards (Sessão/Exercício/Set)

Contêineres para agrupar informações relacionadas, como detalhes de uma sessão de treino, um exercício específico ou um conjunto de séries.

*   **Objetivo:** Organizar e apresentar informações de forma modular e hierárquica.
*   **Anatomia:** Título, Conteúdo, Ações (opcional), Imagem (opcional).
*   **Variantes:**
    *   **Sessão de Treino:** Resumo de um treino completo.
    *   **Exercício:** Detalhes de um exercício dentro de uma sessão.
    *   **Set:** Detalhes de um set individual.
*   **Estados:** Default, Hover (para cards clicáveis).
*   **Acessibilidade:**
    *   Garantir ordem de leitura lógica para leitores de tela.
    *   Áreas clicáveis devem ter tamanho mínimo de 44x44px.
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Use cards para agrupar conteúdo logicamente. Mantenha a hierarquia visual clara dentro do card. Use sombras (`shadow-sm`, `shadow-md`) para indicar profundidade.
    *   **DON'T:** Coloque conteúdo não relacionado no mesmo card. Use cards para elementos que não precisam de agrupamento visual.

### Badges/Chips (PR, Falha, Deload, etc.)

Pequenos indicadores visuais para destacar status ou informações importantes de forma concisa.

*   **Objetivo:** Chamar a atenção para um status ou atributo específico.
*   **Anatomia:** Texto, Ícone (opcional).
*   **Variantes:**
    *   **Semânticas:** `Success` (PR), `Error` (Falha), `Warning` (Deload), `Info` (Volume Alto).
    *   **Informativas:** Para categorização ou tags (ex: "Costas", "Pernas").
*   **Estados:** Default.
*   **Acessibilidade:**
    *   Contraste de cor adequado.
    *   Texto descritivo para leitores de tela.
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Use badges para informações curtas e de alto impacto. Use cores semânticas para status. Posicione próximo ao elemento que descrevem.
    *   **DON'T:** Use badges para frases longas. Use cores semânticas de forma inconsistente.

### Tabs/Navigation (Abas/Navegação)

Elementos de navegação para alternar entre diferentes seções ou visualizações dentro de uma mesma tela ou contexto.

*   **Objetivo:** Organizar conteúdo relacionado em seções distintas e permitir a navegação entre elas.
*   **Anatomia:** Lista de itens clicáveis (abas), conteúdo associado a cada aba.
*   **Variantes:** Horizontal, Vertical (raro no MIKE).
*   **Estados:**
    *   **Default:** Aba inativa.
    *   **Hover:** Feedback visual ao passar o mouse.
    *   **Active:** Aba selecionada, visualmente destacada (ex: borda inferior com `MIKE Accent`, texto `font-weight-semibold`).
    *   **Disabled:** Aba inativa, não clicável.
*   **Acessibilidade:**
    *   Navegação por teclado (setas para mover entre abas, Enter para selecionar).
    *   `aria-selected` e `aria-controls` para indicar o estado e a relação entre abas e painéis.
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Use tabs para conteúdo que pertence à mesma hierarquia. Mantenha o número de abas gerenciável. Indique claramente a aba ativa.
    *   **DON'T:** Use tabs para navegação entre páginas diferentes. Esconda conteúdo importante em abas não óbvias.

### Table (Tabela - Histórico)

Exibição estruturada de dados, essencial para o histórico de treinos e relatórios.

*   **Objetivo:** Apresentar dados tabulares de forma clara e comparável.
*   **Anatomia:** Cabeçalho, Linhas, Células, Rodapé (opcional).
*   **Variantes:** Simples, com ordenação, com paginação.
*   **Estados:** Default, Hover (para linhas interativas).
*   **Acessibilidade:**
    *   Cabeçalhos de coluna (`<th>`) com `scope` para leitores de tela.
    *   Navegação por teclado.
    *   Responsividade para telas pequenas (rolagem horizontal).
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Use `Roboto Mono` para dados numéricos. Use linhas alternadas para melhorar a legibilidade. Mantenha as colunas essenciais visíveis. Permita ordenação e filtragem.
    *   **DON'T:** Crie tabelas muito largas que exijam rolagem excessiva. Use tabelas para layout.

### Toast/Alert (Notificações)

Mensagens temporárias que aparecem para fornecer feedback rápido ao usuário, sem interromper o fluxo principal.

*   **Objetivo:** Informar o usuário sobre o resultado de uma ação ou um evento importante.
*   **Anatomia:** Ícone (opcional), Título (opcional), Mensagem, Botão de fechar (opcional).
*   **Variantes:** `Success`, `Error`, `Warning`, `Info` (usando cores semânticas).
*   **Estados:** Visível, Escondido.
*   **Acessibilidade:**
    *   Devem ser anunciados por leitores de tela (`aria-live`).
    *   Tempo de exibição adequado para que o usuário possa ler.
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Use para feedback não crítico. Mantenha as mensagens curtas e diretas. Permita que o usuário feche a notificação.
    *   **DON'T:** Use para informações críticas que exigem interação imediata. Exiba muitas notificações ao mesmo tempo.

### Modal/Confirm (Caixas de Diálogo)

Sobreposições que exigem uma interação do usuário antes que ele possa continuar com o aplicativo.

*   **Objetivo:** Obter confirmação do usuário para uma ação importante ou exibir informações que exigem atenção.
*   **Anatomia:** Título, Mensagem, Botões de ação (ex: Confirmar, Cancelar).
*   **Variantes:** Confirmação, Alerta, Informação.
*   **Estados:** Aberto, Fechado.
*   **Acessibilidade:**
    *   Foco deve ser movido para o modal ao abrir e restaurado ao fechar.
    *   Navegação por teclado dentro do modal.
    *   `aria-modal="true"` e `role="dialog"`.
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Use para ações irreversíveis (ex: deletar treino). Mantenha o conteúdo conciso. Forneça opções claras de ação.
    *   **DON'T:** Use modais para exibir informações que poderiam estar na página. Use modais em excesso.

### Empty State (Estados Vazios)

Telas ou seções que não contêm dados, fornecendo orientação ao usuário sobre como preenchê-las.

*   **Objetivo:** Informar o usuário sobre a ausência de conteúdo e incentivá-lo a tomar uma ação.
*   **Anatomia:** Título, Mensagem explicativa, Ilustração (opcional), CTA (Call to Action).
*   **Variantes:** Diferentes mensagens e CTAs dependendo do contexto.
*   **Estados:** Default.
*   **Acessibilidade:**
    *   Texto claro e conciso.
    *   CTA acessível.
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Seja útil e encorajador. Sugira a próxima ação. Use ilustrações minimalistas para adicionar personalidade.
    *   **DON'T:** Deixe a tela vazia sem orientação. Use linguagem culpabilizadora.

### Loading States (Estados de Carregamento)

Feedback visual para o usuário durante o carregamento de conteúdo ou processamento de ações.

*   **Objetivo:** Informar o usuário que o sistema está processando e evitar a sensação de que o aplicativo travou.
*   **Anatomia:** Spinner, Skeleton Loader, Mensagem (opcional).
*   **Variantes:**
    *   **Spinner:** Para carregamentos rápidos ou ações pontuais.
    *   **Skeleton Loader:** Para carregamentos de conteúdo mais complexos, simulando a estrutura da interface.
*   **Estados:** Carregando, Concluído.
*   **Acessibilidade:**
    *   `aria-live="polite"` para spinners.
    *   Texto alternativo para spinners.
*   **Regras de Uso e Anti-Padrões:**
    *   **DO:** Use o tipo de loading state apropriado para o contexto. Mantenha o usuário informado. Use animações suaves.
    *   **DON'T:** Deixe o usuário sem feedback durante o carregamento. Use spinners excessivamente grandes ou chamativos.

---
## 9. Padrões de UI/UX e Fluxos Principais (MIKE)

Os padrões de UI/UX no MIKE são projetados para otimizar a experiência do usuário, tornando o registro de treinos e o acompanhamento do progresso o mais eficiente e intuitivo possível. A regra de ouro é: **“o registro tem que ser mais rápido que pensar”**.

### Fluxos Principais

#### 9.1. Criar Sessão → Adicionar Exercícios → Registrar Sets → Finalizar Sessão

Este é o fluxo central do aplicativo, projetado para ser linear e com mínima fricção.

1.  **Criar Sessão:**
    *   **Ação:** Usuário clica em "Iniciar Novo Treino" ou seleciona um template.
    *   **Decisão:** Escolher entre treino livre ou carregar um template/treino anterior.
    *   **Padrão:** Tela inicial com CTA proeminente para iniciar treino. Opções de template visíveis ou acessíveis rapidamente.
    *   **Justificativa Comportamental:** **Redução de Fricção** (facilitar o início) e **Viés do Status Quo** (oferecer templates para guiar a escolha).

2.  **Adicionar Exercícios:**
    *   **Ação:** Usuário adiciona exercícios à sessão.
    *   **Decisão:** Pesquisar exercício existente ou criar novo.
    *   **Padrão:** Campo de busca com sugestões automáticas. Lista de exercícios favoritos/recentes. Botão "Adicionar Exercício".
    *   **Justificativa Comportamental:** **Redução de Fricção** (busca rápida, sugestões) e **Viés da Familiaridade** (priorizar exercícios recentes/favoritos).

3.  **Registrar Sets:**
    *   **Ação:** Usuário registra séries, repetições e carga para cada exercício.
    *   **Decisão:** Aceitar sugestão de carga/reps ou ajustar.
    *   **Padrão:** Interface clara para input de números. Botão "Quick-Add Set" para duplicar a última série. Sugestão automática da última carga/reps.
    *   **Justificativa Comportamental:** **Redução de Fricção** (quick-add, auto-preenchimento), **Viés da Ancoragem** (sugestão da última carga como ponto de partida) e **Feedback Imediato** (confirmação visual do registro).

4.  **Finalizar Sessão:**
    *   **Ação:** Usuário conclui o treino.
    *   **Decisão:** Salvar, descartar ou pausar treino.
    *   **Padrão:** Botão "Finalizar Treino" proeminente. Confirmação opcional para ações destrutivas (descartar).
    *   **Justificativa Comportamental:** **Clareza de Ação** (botão claro) e **Prevenção de Erros** (confirmação para descarte).

#### 9.2. Duplicar Treino Anterior / Template (Redução de Fricção)

*   **Objetivo:** Agilizar o início de um novo treino, especialmente para rotinas repetitivas.
*   **Fluxo:** Na tela de "Iniciar Novo Treino", o usuário tem a opção de "Duplicar Último Treino" ou "Carregar Template".
*   **Padrão:** Botões de ação clara para essas opções. O treino duplicado/template é pré-preenchido com exercícios e cargas.
*   **Justificativa Comportamental:** **Redução de Fricção** (minimiza o esforço de configuração), **Viés do Status Quo** (usuários tendem a seguir o caminho de menor resistência) e **Efeito Compromisso** (facilita a aderência a um plano pré-definido).

#### 9.3. Editar e Corrigir Erro (Peso/Reps/Ordem) Rapidamente

*   **Objetivo:** Permitir que o usuário corrija dados de forma ágil, sem interromper o fluxo do treino.
*   **Fluxo:** Durante o registro, o usuário pode tocar em uma série ou exercício para editar. Opções de reordenar ou excluir exercícios/séries.
*   **Padrão:** Edição inline ou modal leve. Ícones de edição/exclusão claros. Drag-and-drop para reordenar.
*   **Justificativa Comportamental:** **Controle e Liberdade do Usuário** (capacidade de corrigir erros), **Feedback Imediato** (correção visual instantânea) e **Redução de Fricção** (edição rápida).

#### 9.4. Visualizar Histórico de um Exercício (Progressão)

*   **Objetivo:** Permitir que o usuário acompanhe a evolução de um exercício específico ao longo do tempo.
*   **Fluxo:** Na tela de detalhes de um exercício, o usuário acessa o histórico. Pode filtrar por período.
*   **Padrão:** Gráfico de linha mostrando carga/reps ao longo do tempo. Tabela detalhada com todos os registros. Destaque de PRs.
*   **Justificativa Comportamental:** **Viés do Progresso** (visualização clara da evolução), **Efeito Gradiente de Metas** (motivação ao ver a curva ascendente) e **Saliência** (destaque de PRs).

#### 9.5. Relatório Semanal/Mensal (Volume, PR, Consistência)

*   **Objetivo:** Fornecer uma visão consolidada do desempenho do usuário em um período.
*   **Fluxo:** Acessível via dashboard ou seção de relatórios.
*   **Padrão:** Cards de resumo com métricas chave (volume total, PRs alcançados, aderência ao plano). Gráficos de barras para volume, gráficos de linha para progressão de carga. Badges de conquista.
*   **Justificativa Comportamental:** **Recompensa por Consistência** (celebração de PRs e aderência), **Feedback de Valor** (insights acionáveis) e **Viés do Progresso** (visualização macro do avanço).

### Onde Usar Defaults e Auto-Preenchimento (Com Justificativa Comportamental)

*   **Auto-preenchimento da Última Carga/Reps:** Ao adicionar um exercício, preencher automaticamente os campos de carga e repetições com os valores da última vez que o usuário realizou aquele exercício. **Justificativa:** **Redução de Fricção** (economiza tempo e esforço), **Viés da Ancoragem** (fornece um ponto de partida familiar).
*   **Sugestão de Treino Anterior/Template:** Na tela de início de treino, oferecer a opção de carregar o último treino ou um template salvo. **Justificativa:** **Redução de Fricção** (minimiza a tomada de decisão), **Viés do Status Quo** (facilita a repetição de um comportamento).
*   **Defaults para RPE/RIR:** Se o usuário não preencher RPE/RIR, o sistema pode usar um valor padrão (ex: 8 para RPE) ou simplesmente deixar em branco, mas com uma dica sutil para preenchimento. **Justificativa:** **Evitar Overchoice** (não forçar o preenchimento de campos opcionais), **Nudging** (incentivar o uso de funcionalidades avançadas sem obrigar).
*   **Ordem Padrão de Exercícios:** Ao criar um novo treino, a ordem dos exercícios pode seguir um padrão lógico (ex: grandes grupos musculares primeiro). **Justificativa:** **Redução da Carga Cognitiva** (fornece uma estrutura, evitando que o usuário tenha que pensar na ordem ideal).

---

## 10. Microcopy e Feedback (Comportamento)

O microcopy no MIKE é uma ferramenta poderosa para guiar o usuário, motivar e construir uma relação de confiança, sempre alinhado ao tom de voz objetivo e encorajador da marca.

### Biblioteca de Mensagens (Sucesso, Erro, Aviso, Vazio)

*   **Sucesso:**
    *   "Treino registrado! Sua disciplina está valendo a pena."
    *   "Novo Recorde Pessoal! Você superou suas expectativas."
    *   "Série concluída. Próximo desafio!"
    *   "Progresso salvo com sucesso."
*   **Erro:**
    *   "Falha ao registrar. Verifique sua conexão e tente novamente."
    *   "Dados inválidos. Por favor, revise os campos marcados."
    *   "Não foi possível carregar o histórico. Tente novamente."
*   **Aviso:**
    *   "Você está prestes a excluir este treino. Esta ação não pode ser desfeita."
    *   "Atenção: Seu volume de treino está abaixo da média esta semana."
    *   "Lembrete: Seu próximo treino está agendado para amanhã."
*   **Vazio (Empty States):**
    *   "Sua jornada começa agora. Registre seu primeiro treino e veja seu progresso."
    *   "Nenhum PR registrado ainda. Cada treino é uma nova oportunidade."
    *   "Sem dados para exibir. Comece a registrar para desbloquear insights."

### Padrões de Texto para Botões (Verbo + Resultado)

Os textos dos botões devem ser claros, concisos e indicar a ação e o resultado esperado.

*   **Padrão:** Verbo de ação + Objeto (ex: "Registrar Treino", "Salvar Alterações", "Ver Relatório").
*   **Exemplos:**
    *   "Iniciar Treino"
    *   "Adicionar Exercício"
    *   "Registrar Série"
    *   "Finalizar Sessão"
    *   "Editar Perfil"
    *   "Excluir Conta"

### Reforço Positivo sem Infantilizar (“PR registrado”, “+1kg vs última sessão”)

O feedback positivo é crucial para a motivação, mas deve ser entregue de forma madura e alinhada à seriedade do app.

*   **Como Aplicar:**
    *   **Foco em Dados:** "+5kg no supino em relação à semana passada" em vez de "Uhuu! Você é demais!".
    *   **Conquistas Reais:** Celebrar PRs, streaks e aderência ao plano com mensagens diretas e badges.
    *   **Linguagem de Progresso:** Usar termos como "superação", "avanço", "consistência", "disciplina".
    *   **Exemplos:**
        *   "PR Registrado! 120kg no Supino Reto."
        *   "Você está em uma sequência de 7 treinos consecutivos!"
        *   "+2 repetições na remada curvada comparado ao último treino."
        *   "Sua aderência ao plano esta semana foi de 100%."

### Evitar Culpa/Pressão (Ética e Retenção)

Embora o app incentive a disciplina, ele deve evitar mensagens que gerem culpa ou pressão excessiva, o que pode levar ao abandono.

*   **Como Aplicar:**
    *   **Linguagem Neutra em Falhas:** Em vez de "Você falhou em seu treino", usar "Não foi possível completar o treino" ou "Treino não registrado".
    *   **Incentivo ao Recomeço:** Em empty states ou após inatividade, focar no "fresh start" e na oportunidade de recomeçar, em vez de apontar a ausência.
    *   **Flexibilidade:** Reconhecer que pausas acontecem e oferecer caminhos para retomar (ex: "Sentimos sua falta! Que tal um treino leve para recomeçar?").
    *   **Foco no Processo:** Enfatizar que a consistência é mais importante que a perfeição em um único dia.

---

## 11. Acessibilidade e Inclusão (Checklist)

A acessibilidade é um pilar fundamental do design do MIKE, garantindo que o aplicativo seja utilizável por todos, independentemente de suas habilidades ou limitações. Seguir as diretrizes WCAG (Web Content Accessibility Guidelines) é essencial.

### Contraste, Tamanho Mínimo, Touch Targets

*   **Contraste:** Todas as combinações de cores de texto e fundo devem atender, no mínimo, ao WCAG AA (4.5:1 para texto normal, 3:1 para texto grande). Utilize ferramentas de verificação de contraste.
*   **Tamanho Mínimo de Texto:** O tamanho mínimo de fonte para texto de corpo deve ser 16px (ou equivalente em rem/em) para garantir legibilidade. Textos menores (12-14px) podem ser usados para legendas e notas, desde que o contraste seja alto.
*   **Touch Targets:** Áreas clicáveis (botões, links, ícones interativos) devem ter um tamanho mínimo de 44x44px para facilitar a interação em dispositivos touch, evitando cliques acidentais.

### Focus Ring e Navegação por Teclado

*   **Focus Ring Visível:** Todos os elementos interativos (botões, links, campos de formulário) devem ter um indicador de foco claro e visível (`--state-focus-ring`) quando navegados via teclado. Isso é crucial para usuários que não utilizam mouse.
*   **Navegação por Teclado:** A ordem de tabulação (`tabindex`) deve ser lógica e intuitiva, permitindo que o usuário navegue por todos os elementos interativos da tela usando apenas o teclado.

### Cores Sem Depender Apenas de Cor (Use Ícones/Texto)

*   **Princípio:** A cor não deve ser o único meio de transmitir informação. Isso é vital para usuários daltônicos ou com baixa visão.
*   **Como Aplicar:**
    *   **Feedback de Status:** Além da cor, use ícones (ex: `✓` para sucesso, `X` para erro) ou texto descritivo (ex: "Erro: Campo obrigatório") para indicar status.
    *   **Gráficos:** Use padrões de preenchimento, rótulos de texto ou diferentes tipos de linha para diferenciar séries em gráficos, além das cores.

### Linguagem Clara

*   **Princípio:** A linguagem utilizada no app deve ser simples, direta e fácil de entender, evitando jargões técnicos ou complexos.
*   **Como Aplicar:** Escreva microcopy conciso. Use frases curtas. Evite duplas negativas. Forneça glossários para termos específicos (ex: RPE, RIR).

### Checklist Final de Acessibilidade

*   [ ] Todas as combinações de texto/fundo atendem WCAG AA.
*   [ ] Elementos interativos têm touch targets de 44x44px.
*   [ ] Focus rings são visíveis e claros.
*   [ ] A navegação por teclado é lógica e completa.
*   [ ] Informações críticas não dependem apenas da cor.
*   [ ] Imagens e ícones têm texto alternativo (`alt text`) descritivo.
*   [ ] Formulários possuem labels associadas e mensagens de erro claras.
*   [ ] O idioma principal do documento/página está definido (`lang="pt-BR"`).
*   [ ] O conteúdo é compreensível para um público amplo.

---

## 12. Data Viz / Relatórios (Padrões de Gráficos)

A visualização de dados no MIKE é fundamental para que o usuário compreenda seu progresso, identifique tendências e tome decisões informadas sobre seu treinamento. Os gráficos devem ser claros, objetivos e éticos.

### Regras para Gráficos de Progresso (Linha), Volume (Barras), Distribuição (Simples)

*   **Gráficos de Linha (Progresso de Carga/Reps):**
    *   **Objetivo:** Mostrar a evolução de uma métrica ao longo do tempo.
    *   **Padrão:** Linhas sólidas e claras, com marcadores nos pontos de dados. Eixos claramente rotulados. `MIKE Accent` para a linha principal. Destaque de PRs com `Success`.
    *   **Por quê:** Facilita a identificação de tendências e o viés do progresso.
*   **Gráficos de Barras (Volume Semanal/Mensal):**
    *   **Objetivo:** Comparar quantidades em diferentes categorias ou períodos.
    *   **Padrão:** Barras com cantos levemente arredondados. `MIKE Accent` para o preenchimento. Grid sutil no fundo. Eixos claramente rotulados.
    *   **Por quê:** Permite uma comparação rápida e visual do volume de treino.
*   **Gráficos de Distribuição (Simples, ex: % de treinos por grupo muscular):**
    *   **Objetivo:** Mostrar a proporção de diferentes categorias.
    *   **Padrão:** Gráficos de pizza ou barra simples. Cores distintas, mas harmoniosas (usando a paleta secundária ou variações do `MIKE Accent`). Rótulos claros.
    *   **Por quê:** Oferece uma visão rápida da alocação de esforço.

### Como Destacar PRs (Saliência)

Recordes Pessoais (PRs) são marcos importantes e devem ser destacados para reforçar o feedback positivo.

*   **No Gráfico:** Marcar o ponto do PR com um ícone (`bi-award` ou `bi-star`) e/ou uma cor de destaque (`Success`). Uma tooltip ao passar o mouse pode fornecer detalhes.
*   **No Relatório:** Cards de resumo dedicados a PRs recentes. Badges `Success` ao lado dos valores de PR em tabelas ou listas.
*   **Justificativa Comportamental:** **Saliência** (chamar a atenção para a conquista) e **Recompensa por Consistência** (celebrar o esforço e o progresso).

### Como Evitar Enganar (Ética): Escalas, Comparações, Contexto

A ética na visualização de dados é crucial para manter a confiança do usuário.

*   **Escalas:** Sempre começar o eixo Y em zero para gráficos de barra. Para gráficos de linha, usar escalas que representem a variação real dos dados, sem exagerar ou minimizar tendências.
*   **Comparações:** Ao comparar períodos, usar a mesma escala para ambos. Evitar comparações que possam ser enganosas (ex: comparar um dia de treino com uma semana).
*   **Contexto:** Fornecer contexto para os dados (ex: "Volume de treino vs. média histórica", "PR em relação ao seu peso corporal"). Explicar o que os dados significam.
*   **Por quê:** Transparência e honestidade constroem confiança. Evitar manipulação de dados, mesmo que não intencional, é fundamental para a credibilidade do app.

### Paleta e Hierarquia Visual dos Gráficos

*   **Paleta:** Utilizar o `MIKE Accent` para a métrica principal. Para séries secundárias, usar `MIKE Graph` ou variações de tonalidade do `MIKE Accent`. Cores semânticas para alertas ou destaques (PRs).
*   **Hierarquia Visual:** A informação mais importante deve ser a mais proeminente. Títulos de gráficos claros, rótulos de eixos legíveis. Linhas de grid sutis para não competir com os dados.

---

## 13. Heurísticas + Economia Comportamental Aplicadas

O design do app MIKE é intencionalmente construído sobre princípios da psicologia comportamental e economia comportamental para **maximizar o engajamento do usuário, reduzir a fricção e promover a consistência** no registro de treinos e na busca por progresso. Cada decisão de design visa influenciar positivamente o comportamento do usuário, transformando o registro de treino em um hábito recompensador e motivador.

### Decisões de Produto Baseadas em Comportamento

Abaixo, são apresentadas 15 decisões de design que aplicam diretamente conceitos de psicologia e economia comportamental:

1.  **Comportamento Alvo:** Aumentar a frequência e a consistência do registro de treinos.
    *   **Problema:** Usuário abandona o registro por perceber o processo como demorado ou complexo.
    *   **Intervenção de Design:** Botão "Quick-Add Set" e "Duplicar Último Treino".
    *   **Por que funciona (Viés/Heurística):** **Redução de Fricção** (diminui o esforço necessário) e **Viés do Status Quo** (facilita a repetição do comportamento anterior).
    *   **Como implementar no MIKE:** Botões proeminentes na tela de registro de treino e na tela inicial para iniciar um novo treino.

2.  **Comportamento Alvo:** Motivar o usuário a continuar treinando e buscando novos desafios.
    *   **Problema:** Falta de percepção clara do progresso, levando à desmotivação.
    *   **Intervenção de Design:** Destaque visual de "Streaks" (sequências de treinos), "PRs" (Recordes Pessoais) e comparações como "Melhor que semana passada".
    *   **Por que funciona (Viés/Heurística):** **Efeito Gradiente de Metas** (motivação aumenta à medida que se aproxima do objetivo) e **Viés do Progresso** (valorização do avanço).
    *   **Como implementar no MIKE:** Dashboard principal, cards de resumo de treino, tela de detalhes do exercício, e notificações.

3.  **Comportamento Alvo:** Aumentar a aderência a um plano de treino.
    *   **Problema:** Dificuldade em manter o "commitment" com o plano.
    *   **Intervenção de Design:** Metas simples e visíveis no dashboard (ex: "Completar 3 treinos esta semana").
    *   **Por que funciona (Viés/Heurística):** **Efeito Compromisso (Commitment Device)** (metas visíveis aumentam a probabilidade de serem cumpridas).
    *   **Como implementar no MIKE:** Dashboard principal, seção de metas e progresso.

4.  **Comportamento Alvo:** Reduzir a sobrecarga cognitiva e a paralisia de escolha.
    *   **Problema:** Usuário se sente sobrecarregado com muitas opções ou informações complexas.
    *   **Intervenção de Design:** **Evitar Overchoice** e **Progressive Disclosure** (esconder opções avançadas por padrão).
    *   **Por que funciona (Viés/Heurística):** **Redução da Carga Cognitiva** (menos opções facilitam a decisão).
    *   **Como implementar no MIKE:** Tela de registro de treino, formulários de edição de exercício.

5.  **Comportamento Alvo:** Fornecer feedback imediato e claro sobre as ações do usuário.
    *   **Problema:** Incerteza ou sensação de que a ação não foi registrada.
    *   **Intervenção de Design:** Microanimações (check animado), toasts (mensagens pop-up) e checklists visuais.
    *   **Por que funciona (Viés/Heurística):** **Princípio do Feedback** (confirmação instantânea reforça o comportamento).
    *   **Como implementar no MIKE:** Após registrar uma série, finalizar um exercício, salvar um treino.

6.  **Comportamento Alvo:** Agilizar a entrada de dados para exercícios repetitivos.
    *   **Problema:** Dificuldade em lembrar as cargas e repetições do treino anterior.
    *   **Intervenção de Design:** Auto-preenchimento da Carga Anterior.
    *   **Por que funciona (Viés/Heurística):** **Redução de Fricção** (economiza esforço mental) e **Viés da Ancoragem** (fornece um ponto de partida).
    *   **Como implementar no MIKE:** Campo de input de carga e repetições na tela de registro de treino.

7.  **Comportamento Alvo:** Guiar o usuário na progressão do treino.
    *   **Problema:** Usuário não sabe qual exercício fazer em seguida ou como progredir.
    *   **Intervenção de Design:** Sugestão do Próximo Exercício e Progressão Guiada (pequena elevação de carga/reps).
    *   **Por que funciona (Viés/Heurística):** **Redução da Carga Cognitiva** (o app guia a decisão) e **Nudging** (incentivo suave ao progresso).
    *   **Como implementar no MIKE:** Tela de registro de treino, após a conclusão de um exercício.

8.  **Comportamento Alvo:** Incentivar a consistência diária/semanal.
    *   **Problema:** Dificuldade em visualizar o impacto da consistência ao longo do tempo.
    *   **Intervenção de Design:** Visualização de "Streaks" e Calendário de Treinos.
    *   **Por que funciona (Viés/Heurística):** **Viés do Progresso** (visualização de sequência ininterrupta) e **Efeito Compromisso** (motivação para não "quebrar a corrente").
    *   **Como implementar no MIKE:** Dashboard principal, seção de histórico de treinos.

9.  **Comportamento Alvo:** Incentivar o registro de dados opcionais (RPE/RIR, observações).
    *   **Problema:** Usuário não percebe o valor de registrar dados opcionais.
    *   **Intervenção de Design:** Recompensa por Detalhes (badges ou insights gerados a partir desses dados).
    *   **Por que funciona (Viés/Heurística):** **Recompensa Variável** (insights úteis como recompensa) e **Feedback de Valor** (mostrar o benefício da informação).
    *   **Como implementar no MIKE:** Tela de análise de treino, cards de insights no dashboard.

10. **Comportamento Alvo:** Facilitar o recomeço após uma pausa ou o início de um novo hábito.
    *   **Problema:** Dificuldade em iniciar um novo hábito ou em retornar ao treino após uma pausa.
    *   **Intervenção de Design:** Defaults Inteligentes e "Fresh Start Effect" (sugerir treino "básico" ou "de reinício").
    *   **Por que funciona (Viés/Heurística):** **Redução de Fricção** (remove barreiras de início) e **Efeito "Fresh Start"** (aproveita a motivação para novos começos).
    *   **Como implementar no MIKE:** Tela inicial, após um período de inatividade detectado.

11. **Comportamento Alvo:** Aumentar a percepção de controle e autonomia do usuário.
    *   **Problema:** Usuário se sente preso a um sistema rígido.
    *   **Intervenção de Design:** Opções de personalização (ex: criar exercícios, templates de treino) e edição flexível de dados.
    *   **Por que funciona (Viés/Heurística):** **Ilusão de Controle** (sentimento de ter influência sobre o resultado) e **Autonomia** (satisfação de fazer escolhas).
    *   **Como implementar no MIKE:** Seções de "Meus Exercícios", "Meus Treinos", funcionalidade de edição de sets/exercícios.

12. **Comportamento Alvo:** Reduzir a procrastinação na hora de registrar o treino.
    *   **Problema:** Usuário adia o registro, esquecendo detalhes.
    *   **Intervenção de Design:** Lembretes inteligentes e feedback de "treino pendente".
    *   **Por que funciona (Viés/Heurística):** **Nudging** (lembretes suaves) e **Aversão à Perda** (evitar perder o registro de um treino).
    *   **Como implementar no MIKE:** Notificações push (com permissão), banner na tela inicial se houver um treino não finalizado.

13. **Comportamento Alvo:** Incentivar a exploração de funcionalidades avançadas.
    *   **Problema:** Usuário não descobre ou não usa recursos mais complexos.
    *   **Intervenção de Design:** Dicas contextuais e onboarding progressivo para funcionalidades avançadas.
    *   **Por que funciona (Viés/Heurística):** **Progressive Disclosure** (apresentar informações no momento certo) e **Curiosidade** (dicas instigam a exploração).
    *   **Como implementar no MIKE:** Tooltips em ícones de funcionalidades avançadas, mini-tutoriais ao acessar uma nova seção.

14. **Comportamento Alvo:** Reforçar a importância da recuperação e do descanso.
    *   **Problema:** Usuário foca apenas no treino, negligenciando a recuperação.
    *   **Intervenção de Design:** Mensagens de "descanso ativo" ou "dia de recuperação" e insights sobre a importância do sono.
    *   **Por que funciona (Viés/Heurística):** **Nudging** (incentivo a comportamentos saudáveis) e **Feedback de Valor** (mostrar o benefício da recuperação).
    *   **Como implementar no MIKE:** Sugestões no dashboard em dias de descanso, cards de insights sobre recuperação.

15. **Comportamento Alvo:** Criar um senso de comunidade e pertencimento (futuro).
    *   **Problema:** Usuário se sente isolado em sua jornada de treino.
    *   **Intervenção de Design:** Compartilhamento de PRs (opcional), desafios com amigos (futuro).
    *   **Por que funciona (Viés/Heurística):** **Prova Social** (ver outros progredindo) e **Reciprocidade** (interação com a comunidade).
    *   **Como implementar no MIKE:** Opção de compartilhar conquistas, integração com redes sociais de fitness (futuro).

---
## 10. Microcopy e Feedback (Comportamento)

O microcopy no MIKE é uma ferramenta poderosa para guiar o usuário, motivar e construir uma relação de confiança, sempre alinhado ao tom de voz objetivo e encorajador da marca.

### Biblioteca de Mensagens (Sucesso, Erro, Aviso, Vazio)

*   **Sucesso:**
    *   "Treino registrado! Sua disciplina está valendo a pena."
    *   "Novo Recorde Pessoal! Você superou suas expectativas."
    *   "Série concluída. Próximo desafio!"
    *   "Progresso salvo com sucesso."
*   **Erro:**
    *   "Falha ao registrar. Verifique sua conexão e tente novamente."
    *   "Dados inválidos. Por favor, revise os campos marcados."
    *   "Não foi possível carregar o histórico. Tente novamente."
*   **Aviso:**
    *   "Você está prestes a excluir este treino. Esta ação não pode ser desfeita."
    *   "Atenção: Seu volume de treino está abaixo da média esta semana."
    *   "Lembrete: Seu próximo treino está agendado para amanhã."
*   **Vazio (Empty States):**
    *   "Sua jornada começa agora. Registre seu primeiro treino e veja seu progresso."
    *   "Nenhum PR registrado ainda. Cada treino é uma nova oportunidade."
    *   "Sem dados para exibir. Comece a registrar para desbloquear insights."

### Padrões de Texto para Botões (Verbo + Resultado)

Os textos dos botões devem ser claros, concisos e indicar a ação e o resultado esperado.

*   **Padrão:** Verbo de ação + Objeto (ex: "Registrar Treino", "Salvar Alterações", "Ver Relatório").
*   **Exemplos:**
    *   "Iniciar Treino"
    *   "Adicionar Exercício"
    *   "Registrar Série"
    *   "Finalizar Sessão"
    *   "Editar Perfil"
    *   "Excluir Conta"

### Reforço Positivo sem Infantilizar (“PR registrado”, “+1kg vs última sessão”)

O feedback positivo é crucial para a motivação, mas deve ser entregue de forma madura e alinhada à seriedade do app.

*   **Como Aplicar:**
    *   **Foco em Dados:** "+5kg no supino em relação à semana passada" em vez de "Uhuu! Você é demais!".
    *   **Conquistas Reais:** Celebrar PRs, streaks e aderência ao plano com mensagens diretas e badges.
    *   **Linguagem de Progresso:** Usar termos como "superação", "avanço", "consistência", "disciplina".
    *   **Exemplos:**
        *   "PR Registrado! 120kg no Supino Reto."
        *   "Você está em uma sequência de 7 treinos consecutivos!"
        *   "+2 repetições na remada curvada comparado ao último treino."
        *   "Sua aderência ao plano esta semana foi de 100%."

### Evitar Culpa/Pressão (Ética e Retenção)

Embora o app incentive a disciplina, ele deve evitar mensagens que gerem culpa ou pressão excessiva, o que pode levar ao abandono.

*   **Como Aplicar:**
    *   **Linguagem Neutra em Falhas:** Em vez de "Você falhou em seu treino", usar "Não foi possível completar o treino" ou "Treino não registrado".
    *   **Incentivo ao Recomeço:** Em empty states ou após inatividade, focar no "fresh start" e na oportunidade de recomeçar, em vez de apontar a ausência.
    *   **Flexibilidade:** Reconhecer que pausas acontecem e oferecer caminhos para retomar (ex: "Sentimos sua falta! Que tal um treino leve para recomeçar?").
    *   **Foco no Processo:** Enfatizar que a consistência é mais importante que a perfeição em um único dia.

---

## 11. Acessibilidade e Inclusão (Checklist)

A acessibilidade é um pilar fundamental do design do MIKE, garantindo que o aplicativo seja utilizável por todos, independentemente de suas habilidades ou limitações. Seguir as diretrizes WCAG (Web Content Accessibility Guidelines) é essencial.

### Contraste, Tamanho Mínimo, Touch Targets

*   **Contraste:** Todas as combinações de cores de texto e fundo devem atender, no mínimo, ao WCAG AA (4.5:1 para texto normal, 3:1 para texto grande). Utilize ferramentas de verificação de contraste.
*   **Tamanho Mínimo de Texto:** O tamanho mínimo de fonte para texto de corpo deve ser 16px (ou equivalente em rem/em) para garantir legibilidade. Textos menores (12-14px) podem ser usados para legendas e notas, desde que o contraste seja alto.
*   **Touch Targets:** Áreas clicáveis (botões, links, ícones interativos) devem ter um tamanho mínimo de 44x44px para facilitar a interação em dispositivos touch, evitando cliques acidentais.

### Focus Ring e Navegação por Teclado

*   **Focus Ring Visível:** Todos os elementos interativos (botões, links, campos de formulário) devem ter um indicador de foco claro e visível (`--state-focus-ring`) quando navegados via teclado. Isso é crucial para usuários que não utilizam mouse.
*   **Navegação por Teclado:** A ordem de tabulação (`tabindex`) deve ser lógica e intuitiva, permitindo que o usuário navegue por todos os elementos interativos da tela usando apenas o teclado.

### Cores Sem Depender Apenas de Cor (Use Ícones/Texto)

*   **Princípio:** A cor não deve ser o único meio de transmitir informação. Isso é vital para usuários daltônicos ou com baixa visão.
*   **Como Aplicar:**
    *   **Feedback de Status:** Além da cor, use ícones (ex: `✓` para sucesso, `X` para erro) ou texto descritivo (ex: "Erro: Campo obrigatório") para indicar status.
    *   **Gráficos:** Use padrões de preenchimento, rótulos de texto ou diferentes tipos de linha para diferenciar séries em gráficos, além das cores.

### Linguagem Clara

*   **Princípio:** A linguagem utilizada no app deve ser simples, direta e fácil de entender, evitando jargões técnicos ou complexos.
*   **Como Aplicar:** Escreva microcopy conciso. Use frases curtas. Evite duplas negativas. Forneça glossários para termos específicos (ex: RPE, RIR).

### Checklist Final de Acessibilidade

*   [ ] Todas as combinações de texto/fundo atendem WCAG AA.
*   [ ] Elementos interativos têm touch targets de 44x44px.
*   [ ] Focus rings são visíveis e claros.
*   [ ] A navegação por teclado é lógica e completa.
*   [ ] Informações críticas não dependem apenas da cor.
*   [ ] Imagens e ícones têm texto alternativo (`alt text`) descritivo.
*   [ ] Formulários possuem labels associadas e mensagens de erro claras.
*   [ ] O idioma principal do documento/página está definido (`lang="pt-BR"`).
*   [ ] O conteúdo é compreensível para um público amplo.

---

## 12. Data Viz / Relatórios (Padrões de Gráficos)

A visualização de dados no MIKE é fundamental para que o usuário compreenda seu progresso, identifique tendências e tome decisões informadas sobre seu treinamento. Os gráficos devem ser claros, objetivos e éticos.

### Regras para Gráficos de Progresso (Linha), Volume (Barras), Distribuição (Simples)

*   **Gráficos de Linha (Progresso de Carga/Reps):**
    *   **Objetivo:** Mostrar a evolução de uma métrica ao longo do tempo.
    *   **Padrão:** Linhas sólidas e claras, com marcadores nos pontos de dados. Eixos claramente rotulados. `MIKE Accent` para a linha principal. Destaque de PRs com `Success`.
    *   **Por quê:** Facilita a identificação de tendências e o viés do progresso.
*   **Gráficos de Barras (Volume Semanal/Mensal):**
    *   **Objetivo:** Comparar quantidades em diferentes categorias ou períodos.
    *   **Padrão:** Barras com cantos levemente arredondados. `MIKE Accent` para o preenchimento. Grid sutil no fundo. Eixos claramente rotulados.
    *   **Por quê:** Permite uma comparação rápida e visual do volume de treino.
*   **Gráficos de Distribuição (Simples, ex: % de treinos por grupo muscular):**
    *   **Objetivo:** Mostrar a proporção de diferentes categorias.
    *   **Padrão:** Gráficos de pizza ou barra simples. Cores distintas, mas harmoniosas (usando a paleta secundária ou variações do `MIKE Accent`). Rótulos claros.
    *   **Por quê:** Oferece uma visão rápida da alocação de esforço.

### Como Destacar PRs (Saliência)

Recordes Pessoais (PRs) são marcos importantes e devem ser destacados para reforçar o feedback positivo.

*   **No Gráfico:** Marcar o ponto do PR com um ícone (`bi-award` ou `bi-star`) e/ou uma cor de destaque (`Success`). Uma tooltip ao passar o mouse pode fornecer detalhes.
*   **No Relatório:** Cards de resumo dedicados a PRs recentes. Badges `Success` ao lado dos valores de PR em tabelas ou listas.
*   **Justificativa Comportamental:** **Saliência** (chamar a atenção para a conquista) e **Recompensa por Consistência** (celebrar o esforço e o progresso).

### Como Evitar Enganar (Ética): Escalas, Comparações, Contexto

A ética na visualização de dados é crucial para manter a confiança do usuário.

*   **Escalas:** Sempre começar o eixo Y em zero para gráficos de barra. Para gráficos de linha, usar escalas que representem a variação real dos dados, sem exagerar ou minimizar tendências.
*   **Comparações:** Ao comparar períodos, usar a mesma escala para ambos. Evitar comparações que possam ser enganosas (ex: comparar um dia de treino com uma semana).
*   **Contexto:** Fornecer contexto para os dados (ex: "Volume de treino vs. média histórica", "PR em relação ao seu peso corporal"). Explicar o que os dados significam.
*   **Por quê:** Transparência e honestidade constroem confiança. Evitar manipulação de dados, mesmo que não intencional, é fundamental para a credibilidade do app.

### Paleta e Hierarquia Visual dos Gráficos

*   **Paleta:** Utilizar o `MIKE Accent` para a métrica principal. Para séries secundárias, usar `MIKE Graph` ou variações de tonalidade do `MIKE Accent`. Cores semânticas para alertas ou destaques (PRs).
*   **Hierarquia Visual:** A informação mais importante deve ser a mais proeminente. Títulos de gráficos claros, rótulos de eixos legíveis. Linhas de grid sutis para não competir com os dados.

---

## 13. Heurísticas + Economia Comportamental Aplicadas

O design do app MIKE é intencionalmente construído sobre princípios da psicologia comportamental e economia comportamental para **maximizar o engajamento do usuário, reduzir a fricção e promover a consistência** no registro de treinos e na busca por progresso. Cada decisão de design visa influenciar positivamente o comportamento do usuário, transformando o registro de treino em um hábito recompensador e motivador.

### Decisões de Produto Baseadas em Comportamento

Abaixo, são apresentadas 15 decisões de design que aplicam diretamente conceitos de psicologia e economia comportamental:

1.  **Comportamento Alvo:** Aumentar a frequência e a consistência do registro de treinos.
    *   **Problema:** Usuário abandona o registro por perceber o processo como demorado ou complexo.
    *   **Intervenção de Design:** Botão "Quick-Add Set" e "Duplicar Último Treino".
    *   **Por que funciona (Viés/Heurística):** **Redução de Fricção** (diminui o esforço necessário) e **Viés do Status Quo** (facilita a repetição do comportamento anterior).
    *   **Como implementar no MIKE:** Botões proeminentes na tela de registro de treino e na tela inicial para iniciar um novo treino.

2.  **Comportamento Alvo:** Motivar o usuário a continuar treinando e buscando novos desafios.
    *   **Problema:** Falta de percepção clara do progresso, levando à desmotivação.
    *   **Intervenção de Design:** Destaque visual de "Streaks" (sequências de treinos), "PRs" (Recordes Pessoais) e comparações como "Melhor que semana passada".
    *   **Por que funciona (Viés/Heurística):** **Efeito Gradiente de Metas** (motivação aumenta à medida que se aproxima do objetivo) e **Viés do Progresso** (valorização do avanço).
    *   **Como implementar no MIKE:** Dashboard principal, cards de resumo de treino, tela de detalhes do exercício, e notificações.

3.  **Comportamento Alvo:** Aumentar a aderência a um plano de treino.
    *   **Problema:** Dificuldade em manter o "commitment" com o plano.
    *   **Intervenção de Design:** Metas simples e visíveis no dashboard (ex: "Completar 3 treinos esta semana").
    *   **Por que funciona (Viés/Heurística):** **Efeito Compromisso (Commitment Device)** (metas visíveis aumentam a probabilidade de serem cumpridas).
    *   **Como implementar no MIKE:** Dashboard principal, seção de metas e progresso.

4.  **Comportamento Alvo:** Reduzir a sobrecarga cognitiva e a paralisia de escolha.
    *   **Problema:** Usuário se sente sobrecarregado com muitas opções ou informações complexas.
    *   **Intervenção de Design:** **Evitar Overchoice** e **Progressive Disclosure** (esconder opções avançadas por padrão).
    *   **Por que funciona (Viés/Heurística):** **Redução da Carga Cognitiva** (menos opções facilitam a decisão).
    *   **Como implementar no MIKE:** Tela de registro de treino, formulários de edição de exercício.

5.  **Comportamento Alvo:** Fornecer feedback imediato e claro sobre as ações do usuário.
    *   **Problema:** Incerteza ou sensação de que a ação não foi registrada.
    *   **Intervenção de Design:** Microanimações (check animado), toasts (mensagens pop-up) e checklists visuais.
    *   **Por que funciona (Viés/Heurística):** **Princípio do Feedback** (confirmação instantânea reforça o comportamento).
    *   **Como implementar no MIKE:** Após registrar uma série, finalizar um exercício, salvar um treino.

6.  **Comportamento Alvo:** Agilizar a entrada de dados para exercícios repetitivos.
    *   **Problema:** Dificuldade em lembrar as cargas e repetições do treino anterior.
    *   **Intervenção de Design:** Auto-preenchimento da Carga Anterior.
    *   **Por que funciona (Viés/Heurística):** **Redução de Fricção** (economiza esforço mental) e **Viés da Ancoragem** (fornece um ponto de partida).
    *   **Como implementar no MIKE:** Campo de input de carga e repetições na tela de registro de treino.

7.  **Comportamento Alvo:** Guiar o usuário na progressão do treino.
    *   **Problema:** Usuário não sabe qual exercício fazer em seguida ou como progredir.
    *   **Intervenção de Design:** Sugestão do Próximo Exercício e Progressão Guiada (pequena elevação de carga/reps).
    *   **Por que funciona (Viés/Heurística):** **Redução da Carga Cognitiva** (o app guia a decisão) e **Nudging** (incentivo suave ao progresso).
    *   **Como implementar no MIKE:** Tela de registro de treino, após a conclusão de um exercício.

8.  **Comportamento Alvo:** Incentivar a consistência diária/semanal.
    *   **Problema:** Dificuldade em visualizar o impacto da consistência ao longo do tempo.
    *   **Intervenção de Design:** Visualização de "Streaks" e Calendário de Treinos.
    *   **Por que funciona (Viés/Heurística):** **Viés do Progresso** (visualização de sequência ininterrupta) e **Efeito Compromisso** (motivação para não "quebrar a corrente").
    *   **Como implementar no MIKE:** Dashboard principal, seção de histórico de treinos.

9.  **Comportamento Alvo:** Incentivar o registro de dados opcionais (RPE/RIR, observações).
    *   **Problema:** Usuário não percebe o valor de registrar dados opcionais.
    *   **Intervenção de Design:** Recompensa por Detalhes (badges ou insights gerados a partir desses dados).
    *   **Por que funciona (Viés/Heurística):** **Recompensa Variável** (insights úteis como recompensa) e **Feedback de Valor** (mostrar o benefício da informação).
    *   **Como implementar no MIKE:** Tela de análise de treino, cards de insights no dashboard.

10. **Comportamento Alvo:** Facilitar o recomeço após uma pausa ou o início de um novo hábito.
    *   **Problema:** Dificuldade em iniciar um novo hábito ou em retornar ao treino após uma pausa.
    *   **Intervenção de Design:** Defaults Inteligentes e "Fresh Start Effect" (sugerir treino "básico" ou "de reinício").
    *   **Por que funciona (Viés/Heurística):** **Redução de Fricção** (remove barreiras de início) e **Efeito "Fresh Start"** (aproveita a motivação para novos começos).
    *   **Como implementar no MIKE:** Tela inicial, após um período de inatividade detectado.

11. **Comportamento Alvo:** Aumentar a percepção de controle e autonomia do usuário.
    *   **Problema:** Usuário se sente preso a um sistema rígido.
    *   **Intervenção de Design:** Opções de personalização (ex: criar exercícios, templates de treino) e edição flexível de dados.
    *   **Por que funciona (Viés/Heurística):** **Ilusão de Controle** (sentimento de ter influência sobre o resultado) e **Autonomia** (satisfação de fazer escolhas).
    *   **Como implementar no MIKE:** Seções de "Meus Exercícios", "Meus Treinos", funcionalidade de edição de sets/exercícios.

12. **Comportamento Alvo:** Reduzir a procrastinação na hora de registrar o treino.
    *   **Problema:** Usuário adia o registro, esquecendo detalhes.
    *   **Intervenção de Design:** Lembretes inteligentes e feedback de "treino pendente".
    *   **Por que funciona (Viés/Heurística):** **Nudging** (lembretes suaves) e **Aversão à Perda** (evitar perder o registro de um treino).
    *   **Como implementar no MIKE:** Notificações push (com permissão), banner na tela inicial se houver um treino não finalizado.

13. **Comportamento Alvo:** Incentivar a exploração de funcionalidades avançadas.
    *   **Problema:** Usuário não descobre ou não usa recursos mais complexos.
    *   **Intervenção de Design:** Dicas contextuais e onboarding progressivo para funcionalidades avançadas.
    *   **Por que funciona (Viés/Heurística):** **Progressive Disclosure** (apresentar informações no momento certo) e **Curiosidade** (dicas instigam a exploração).
    *   **Como implementar no MIKE:** Tooltips em ícones de funcionalidades avançadas, mini-tutoriais ao acessar uma nova seção.

14. **Comportamento Alvo:** Reforçar a importância da recuperação e do descanso.
    *   **Problema:** Usuário foca apenas no treino, negligenciando a recuperação.
    *   **Intervenção de Design:** Mensagens de "descanso ativo" ou "dia de recuperação" e insights sobre a importância do sono.
    *   **Por que funciona (Viés/Heurística):** **Nudging** (incentivo a comportamentos saudáveis) e **Feedback de Valor** (mostrar o benefício da recuperação).
    *   **Como implementar no MIKE:** Sugestões no dashboard em dias de descanso, cards de insights sobre recuperação.

15. **Comportamento Alvo:** Criar um senso de comunidade e pertencimento (futuro).
    *   **Problema:** Usuário se sente isolado em sua jornada de treino.
    *   **Intervenção de Design:** Compartilhamento de PRs (opcional), desafios com amigos (futuro).
    *   **Por que funciona (Viés/Heurística):** **Prova Social** (ver outros progredindo) e **Reciprocidade** (interação com a comunidade).
    *   **Como implementar no MIKE:** Opção de compartilhar conquistas, integração com redes sociais de fitness (futuro).

---

## 14. Checklist de Implementação (Dev + Design QA)

Este checklist serve como um guia para desenvolvedores e designers garantirem a qualidade e a conformidade com o Design System durante a implementação e o controle de qualidade.

### Checklist por Tela (Sessão, Exercício, Relatório)

*   [ ] **Sessão de Treino:**
    *   [ ] Todos os elementos de UI estão usando tokens de cor e tipografia corretos.
    *   [ ] Espaçamento entre elementos segue o grid de 8px.
    *   [ ] Botões de ação primária e secundária estão corretos.
    *   [ ] Inputs de carga/reps estão funcionando com auto-preenchimento.
    *   [ ] Feedback visual para registro de série (microanimação, toast).
    *   [ ] Modo claro/escuro funciona corretamente.
    *   [ ] Responsividade testada em mobile.
*   [ ] **Detalhes do Exercício:**
    *   [ ] Histórico do exercício carregado corretamente.
    *   [ ] Gráfico de progresso está usando a paleta e estilo definidos.
    *   [ ] PRs estão destacados visualmente.
    *   [ ] Opções de edição/exclusão estão acessíveis.
*   [ ] **Relatório de Progresso:**
    *   [ ] Cards de resumo exibem métricas corretas.
    *   [ ] Gráficos de volume e progressão estão formatados conforme o DS.
    *   [ ] Escalas dos gráficos são éticas (eixo Y começando em zero para barras).
    *   [ ] Badges de PRs e consistência estão visíveis.

### Checklist por Componente (Estados, Acessibilidade)

*   [ ] **Botões:**
    *   [ ] Todos os estados (default, hover, active, focus, disabled, loading) estão implementados.
    *   [ ] Contraste de texto/fundo OK.
    *   [ ] Touch target mínimo de 44x44px.
    *   [ ] `aria-label` presente para botões apenas com ícone.
*   [ ] **Inputs:**
    *   [ ] Labels associadas corretamente.
    *   [ ] Estados (default, focus, error, success, disabled) implementados.
    *   [ ] Mensagens de erro claras e associadas (`aria-describedby`).
    *   [ ] Tipos de input (`type="number"`, `type="email"`) corretos.
*   [ ] **Cards:**
    *   [ ] Sombras e raios de borda conforme tokens.
    *   [ ] Conteúdo agrupado logicamente.
    *   [ ] Ordem de leitura lógica.
*   [ ] **Badges/Chips:**
    *   [ ] Cores semânticas usadas corretamente.
    *   [ ] Contraste de texto/fundo OK.
    *   [ ] Texto descritivo.
*   [ ] **Tabelas:**
    *   [ ] Cabeçalhos (`<th>`) com `scope`.
    *   [ ] Responsividade (rolagem horizontal).
    *   [ ] Linhas alternadas.

### Checklist de Consistência (Tokens, Tipografia, Espaçamento)

*   [ ] Todas as cores estão sendo referenciadas via variáveis CSS.
*   [ ] Todas as fontes e tamanhos estão usando os tokens tipográficos.
*   [ ] Espaçamento (margens, paddings) está em múltiplos de 8px.
*   [ ] Raio de borda dos elementos está usando os tokens.
*   [ ] Sombras estão usando os tokens definidos.
*   [ ] Estilo de ícones é consistente em todo o app.

### “Definição de Pronto” (DoD) Visual/UX

Um componente ou tela só é considerado "pronto" quando:

*   [ ] Funcionalidade implementada e testada.
*   [ ] Design visualmente idêntico ao protótipo/especificação (pixel-perfect).
*   [ ] Todos os estados (default, hover, focus, active, disabled, error, success) estão implementados e funcionando.
*   [ ] Acessibilidade (WCAG AA) verificada e aprovada.
*   [ ] Responsividade testada em todos os breakpoints relevantes.
*   [ ] Performance otimizada (carregamento rápido, animações suaves).
*   [ ] Microcopy revisado e aprovado.
*   [ ] Coerência com os princípios de psicologia comportamental aplicada.

---

## 15. Apêndice

### Glossário

*   **RPE (Rate of Perceived Exertion):** Escala de 1 a 10 para medir a intensidade subjetiva de um set ou exercício. 10 significa esforço máximo, 1 significa muito fácil.
*   **RIR (Reps In Reserve):** Número de repetições que o usuário ainda conseguiria fazer antes de atingir a falha muscular em um set. Ex: RIR 2 significa que ainda conseguiria fazer mais 2 repetições.
*   **PR (Personal Record):** Recorde Pessoal. A maior carga, repetições ou volume alcançado em um exercício específico.
*   **Volume:** Quantidade total de trabalho realizado em um treino ou período. Geralmente calculado como (Séries x Repetições x Carga).
*   **Deload:** Período de redução intencional da intensidade ou volume de treino para permitir a recuperação e evitar o overtraining.
*   **Streak:** Sequência ininterrupta de dias ou treinos consecutivos.
*   **Nudging:** Incentivos sutis para guiar o comportamento do usuário em uma direção desejada, sem restringir a liberdade de escolha.
*   **Progressive Disclosure:** Técnica de UI que esconde informações ou funcionalidades menos importantes até que o usuário precise delas, reduzindo a sobrecarga cognitiva inicial.

### Regras de Expansão Futura (Nutrição e Outras Modalidades) sem Quebrar o Sistema

O Design System do MIKE é construído para ser escalável e acomodar futuras expansões sem comprometer a identidade visual ou a experiência do usuário.

*   **Cores:** A paleta de cores é robusta. Novas cores podem ser introduzidas para diferenciar módulos (ex: um verde para nutrição), mas devem ser complementares e seguir as regras de contraste e uso semântico.
*   **Tipografia:** As fontes Montserrat e Oswald são versáteis o suficiente para acomodar novos tipos de conteúdo. Se necessário, uma nova fonte pode ser introduzida para um propósito muito específico (ex: dados nutricionais), mas com justificativa e alinhamento com a estética geral.
*   **Componentes:** Novos componentes podem ser criados, mas devem reutilizar tokens existentes e seguir os padrões de acessibilidade e responsividade. A criação de novos componentes deve ser justificada pela necessidade de resolver um problema de UI/UX específico que não pode ser resolvido com componentes existentes.
*   **Estilo Gráfico:** O estilo minimalista e funcional de ícones e ilustrações deve ser mantido. Novas ilustrações para nutrição (ex: alimentos, balanças) devem seguir a mesma linguagem visual.
*   **Psicologia Comportamental:** Os princípios de redução de fricção, feedback e motivação são universais e devem ser aplicados a novos módulos (ex: registro de refeições, acompanhamento de sono).

### Roadmap de Maturidade do Design System (v1 → v2)

*   **v1.0 (Atual):** Foco na fundação (tokens, componentes básicos, princípios de marca e UX) para o core do app (registro de treinos).
*   **v1.x:** Expansão do catálogo de componentes, refinamento de padrões de interação, adição de guidelines para animações e microinterações mais complexas.
*   **v2.0:** Incorporação de novos módulos (nutrição, sono, outras atividades) com a introdução de novos padrões e, se necessário, uma extensão controlada da paleta de cores ou tipografia para diferenciar os módulos, mantendo a coesão geral. Integração de ferramentas de design (Figma, Sketch) com o Design System (ex: bibliotecas de componentes).
