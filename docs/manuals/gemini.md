# MIKE Design System & Product Manual

**Versão:** 1.0

**Data:** 16 de Fevereiro de 2026

**Status:** Baseado no manual anterior (HTML) — Complemento Operacional Markdown

---

## Sumário

1. [Visão Geral e Norte](https://www.google.com/search?q=%231-vis%C3%A3o-geral-e-norte)
2. [Arquitetura do Design System](https://www.google.com/search?q=%232-arquitetura-do-design-system)
3. [Identidade da Marca](https://www.google.com/search?q=%233-identidade-da-marca)
4. [Paleta de Cores](https://www.google.com/search?q=%234-paleta-de-cores)
5. [Tipografia](https://www.google.com/search?q=%235-tipografia)
6. [Grid, Layout e Espaçamento](https://www.google.com/search?q=%236-grid-layout-e-espa%C3%A7amento)
7. [Iconografia e Estilo Gráfico](https://www.google.com/search?q=%237-iconografia-e-estilo-gr%C3%A1fico)
8. [Componentes UI](https://www.google.com/search?q=%238-componentes-ui)
9. [Padrões de UI/UX e Fluxos Principais](https://www.google.com/search?q=%239-padr%C3%B5es-de-uiux-e-fluxos-principais)
10. [Microcopy e Feedback](https://www.google.com/search?q=%2310-microcopy-e-feedback)
11. [Acessibilidade e Inclusão](https://www.google.com/search?q=%2311-acessibilidade-e-inclus%C3%A3o)
12. [Data Viz e Relatórios](https://www.google.com/search?q=%2312-data-viz-e-relat%C3%B3rios)
13. [Heurísticas e Economia Comportamental](https://www.google.com/search?q=%2313-heur%C3%ADsticas-e-economia-comportamental)
14. [Checklist de Implementação (QA)](https://www.google.com/search?q=%2314-checklist-de-implementa%C3%A7%C3%A3o-qa)
15. [Apêndice](https://www.google.com/search?q=%2315-ap%C3%AAndice)

---

## 1. Visão Geral e Norte

### Essência da Marca

> "Progresso bruto através da precisão absoluta."

### Promessa Central

O MIKE elimina a subjetividade do treino. Ele não é um diário social; é um laboratório de performance. Cada entrada de dado deve servir ao propósito de superar a última sessão, aplicando os princípios de Mike Mentzer: intensidade máxima, volume controlado e recuperação monitorada.

### Personalidade

* **Estóico:** Visual limpo, focado no essencial. Nada de decorações.
* **Analítico:** Decisões baseadas em números e tendências, não em "feeling".
* **Robusto:** Sensação de durabilidade e força (uso de pesos pesados e cores industriais).
* **Direto:** Sem "gamificação" infantil; o progresso é a única recompensa necessária.

### Princípios de Design

1. **Redução de Fricção no Registro:** O ato de logar um peso deve ser mais rápido que o descanso entre séries.
2. **Saliência de Dados Críticos:** O que você fez na semana passada é a informação mais importante hoje.
3. **Feedback de Progressão:** Cada PR (Personal Record) deve ser visualmente celebrado de forma técnica.
4. **Prioridade Mobile-In-Gym:** Botões grandes (touch targets) para mãos suadas ou trêmulas após o esforço.

---

## 2. Arquitetura do Design System

O sistema segue a lógica de **Design Tokens** para garantir que uma mudança no "Lima-Ácido" se propague por todo o app (nutrição, corrida, etc).

* **Tokens:** Valores atômicos (Cores, Fontes, Spacing).
* **Componentes:** Elementos funcionais (Botão, Input, Card).
* **Padrões:** Combinação de componentes para fluxos (Lista de Exercícios).
* **Templates:** Telas completas (Dashboard de Progresso).

**Nomenclatura:** BEM (Block Element Modifier) para CSS e CamelCase para Tokens (ex: `mike.color.accent`).

---

## 3. Identidade da Marca

* **Nome:** Sempre escrito em **ALL CAPS** (**MIKE**). Transmite autoridade e remete à força do nome "Mike Mentzer".
* **Tom de Voz:**
* **CTA:** Use verbos imperativos e diretos: "LOG SET", "START WORKOUT", "SAVE PR".
* **Erros:** Técnico e não-culpabilizante: "Carga inválida. Insira apenas números."
* **Empty States:** Desafiador: "Nenhum dado registrado. A evolução começa no primeiro set."



---

## 4. Paleta de Cores

| Nome do Token | HEX | Função | Justificativa |
| --- | --- | --- | --- |
| `mike-bg` | `#0B0C0E` | Fundo Principal | Reduz emissão de luz em ambientes de academia; foco no conteúdo. |
| `mike-surface` | `#181A1F` | Cards e Superfícies | Cria profundidade e separa grupos de exercícios. |
| `mike-accent` | `#D1FF26` | Ações e Destaques | O "Lima-Ácido" gera urgência e energia sem o estresse do vermelho. |
| `mike-text` | `#FFFFFF` | Leitura Principal | Máximo contraste sobre o fundo escuro. |
| `mike-muted` | `#8E929B` | Textos secundários | Reduz o ruído visual em informações não críticas. |

### Regras de Modo

* **Dark Mode (Default):** O MIKE nasceu para ser escuro.
* **Light Mode:** Inverter `bg` para `#F4F5F7` e `text` para `#0B0C0E`. O `mike-accent` deve ser ajustado para `#A8CC1D` para manter contraste WCAG AA sobre branco.

**Do:** Usar `mike-accent` apenas em elementos de interação ou sucesso.
**Don't:** Usar o verde lima para mensagens de erro. Para erros, use `#FF4545`.

---

## 5. Tipografia

* **Display (Títulos/Números):** `Bebas Neue`.
* *Por quê:* Condensada e impactante. Ótima para números de carga que precisam de escala sem ocupar largura excessiva.


* **UI/Body:** `Inter`.
* *Por quê:* Altíssima legibilidade em telas pequenas e diversos pesos.


* **Data/Mono:** `JetBrains Mono`.
* *Por quê:* Evita que números "pulem" em contadores de tempo/timer devido ao espaçamento fixo.



### Escala (Mobile)

* **H1 (Títulos de tela):** 32px / Bold / All Caps
* **H2 (Nomes de Exercício):** 20px / Semi-bold
* **Body:** 16px / Regular
* **Small/Caption:** 12px / Medium

---

## 6. Grid, Layout e Espaçamento

* **Sistema de 8px:** Todos os paddings e margens devem ser múltiplos de 8 (8, 16, 24, 32, 40, 48).
* **Margens Laterais:** Padrão de 16px para telas mobile.
* **Densidade:** Em telas de log, use espaçamento de 8px entre linhas de "sets" para permitir visualização de mais dados sem scroll.

---

## 7. Iconografia e Estilo Gráfico

* **Estilo:** Ícones de linha (Outline), 2px de espessura, cantos levemente arredondados (2px).
* **Ícone vs Texto:** Nunca use ícones solitários para ações críticas (ex: Salvar). Use `Ícone + Texto`.
* **Fotografia:** Estilo "cinematográfico industrial". Preto e branco com alto contraste. Foco em detalhes (textura da anilha, suor, magnésio nas mãos). Evitar modelos sorrindo ou "estilo stock photo".

---

## 8. Componentes UI

### Buttons

* **Primary:** Background `mike-accent`, texto preto, All Caps, Bold.
* **Secondary:** Borda `mike-accent`, sem preenchimento, texto `mike-accent`.
* **Ghost:** Sem borda ou fundo, apenas texto `mike-muted`.

### Cards de Exercício

* **Anatomia:** Cabeçalho (Nome + Meta-dados) + Corpo (Tabela de Sets) + Rodapé (Botão Adicionar Set).
* **Estado Ativo:** Quando o usuário está em um set, o card ganha uma borda de 1px `mike-accent`.

### Badges (Chips)

* **PR:** `#D1FF26` (Lima). Indica recorde pessoal.
* **Falha:** `#FF4545` (Vermelho). Indica que a série foi interrompida por falha mecânica.
* **Deload:** `#8E929B` (Cinza). Treino com foco em recuperação.

---

## 9. Padrões de UI/UX e Fluxos Principais

### Fluxo de Registro de Set

1. O usuário entra na tela de treino.
2. O campo "Carga" já vem pré-preenchido com o valor do treino anterior (**Defaulting**).
3. O foco do cursor vai automaticamente para "Reps".
4. Ao clicar em "Log Set", um timer de descanso inicia automaticamente.

**Regra de Ouro:** "O app deve trabalhar para o usuário, não o contrário." Reduza cada clique possível. Se o usuário sempre faz 3 séries, o 4º set deve ser uma ação secundária.

---

## 10. Microcopy e Feedback

* **Feedback Imediato:** Ao completar uma série, o checkmark deve ter uma micro-animação de "bounce".
* **Comemoração Técnica:** "Volume semanal atingido: +500kg. Progressão consistente."
* **Prevenção de Erro:** Se o usuário tentar logar 1000kg (erro de digitação comum), perguntar: "Confirmar carga de 1000kg?".

---

## 11. Acessibilidade e Inclusão

* **Touch Targets:** Mínimo de 48x48px para todos os botões clicáveis.
* **Não use apenas cor:** Para indicar sucesso/erro, use um ícone (check/erro) junto com a cor.
* **Leitores de Tela:** Adicione `aria-label` descritivos: "Registrar série 1 com 80 quilos".

---

## 12. Data Viz / Relatórios

* **Gráfico de Linha (Progressão):** Use `mike-accent` para a linha de carga. Use uma linha pontilhada cinza para a média móvel.
* **Gráfico de Barras (Volume):** Barras em cinza escuro, com a barra atual em `mike-accent` se for maior que a anterior.
* **Destaque de PR:** Pequena estrela ou ponto brilhante no vértice do gráfico onde o recorde ocorreu.

---

## 13. Heurísticas e Economia Comportamental

1. **Efeito de Dotação:** Ao sugerir a carga anterior, o usuário sente que "já possui" aquele nível de força e se esforça para não diminuir.
2. **Viés do Progresso:** Mostrar "Treino 85% concluído" motiva a finalizar a última série.
3. **Redução de Escolha (Lei de Hick):** Não mostre todos os exercícios do mundo. Mostre "Meus Exercícios" primeiro.
4. **Carga Cognitiva:** Esconda detalhes como "Volume Total da Sessão" até que o treino seja finalizado; foque na série atual.
5. **Comprometimento:** Notificação às 09:00 (baseada na agenda do usuário): "Hora da Intensidade Máxima. Seu último agachamento foi 120kg. Hoje buscamos 122kg."

---

## 14. Checklist de Implementação (QA)

* [ ] As fontes `Bebas Neue` e `Inter` estão carregando corretamente?
* [ ] O contraste do texto `muted` em relação ao `bg` passa no teste WCAG AA?
* [ ] O botão de "Log Set" é facilmente clicável com o polegar (zona de alcance)?
* [ ] O modo escuro ativa automaticamente baseado no sistema operacional?
* [ ] Gráficos são responsivos e não quebram em telas pequenas (iPhone SE)?
* [ ] O teclado numérico abre automaticamente em campos de carga/reps?

---

## 15. Apêndice

* **Glossário Técnico:**
* **RPE:** Rate of Perceived Exertion (1-10).
* **RIR:** Reps in Reserve (Quantas reps sobraram antes da falha).
* **Volume:** Carga x Reps x Séries.


* **Expansão Futura:** No módulo de nutrição, manter o cinza industrial, mas usar o token `mike-accent-nutrition` (Azul-Ciano) para diferenciar contextos sem quebrar a marca.