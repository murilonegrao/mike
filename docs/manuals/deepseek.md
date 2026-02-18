# Manual de Identidade + UI/UX + Design System · MIKE

**Versão:** v1.0  
**Data:** 2025-04-13  
**Status:** Baseado no manual anterior (HTML) — complemento Markdown  
**Autoria:** Design System Lead / UI/UX Sênior

---

## Sumário
1. [Visão geral e norte](#1-visão-geral-e-norte)  
2. [Arquitetura do Design System](#2-arquitetura-do-design-system)  
3. [Identidade da marca](#3-identidade-da-marca)  
4. [Paleta de cores](#4-paleta-de-cores)  
5. [Tipografia](#5-tipografia)  
6. [Grid, layout e espaçamento](#6-grid-layout-e-espaçamento)  
7. [Iconografia e estilo gráfico](#7-iconografia-e-estilo-gráfico)  
8. [Componentes UI (catálogo operacional)](#8-componentes-ui-catálogo-operacional)  
9. [Padrões de UI/UX e fluxos principais](#9-padrões-de-uiux-e-fluxos-principais)  
10. [Microcopy e feedback (comportamento)](#10-microcopy-e-feedback-comportamento)  
11. [Acessibilidade e Inclusão (checklist)](#11-acessibilidade-e-inclusão-checklist)  
12. [Data viz / relatórios (padrões de gráficos)](#12-data-viz--relatórios-padrões-de-gráficos)  
13. [Heurísticas + Economia Comportamental aplicadas](#13-heurísticas--economia-comportamental-aplicadas)  
14. [Checklist de implementação (Dev + Design QA)](#14-checklist-de-implementação-dev--design-qa)  
15. [Apêndice](#15-apêndice)

---

## 1. Visão geral e norte

### Essência da marca
**Precisão que gera força.**

### Promessa central do MIKE
MIKE é o diário de bordo definitivo para quem busca resultados mensuráveis nos treinos de força. Baseado na filosofia Heavy Duty (Mike Mentzer), o app oferece registro rigoroso, análises claras e um fluxo sem fricção, transformando disciplina em dados e dados em progresso real.

### Personalidade
- **Preciso** – cada elemento tem um propósito, sem ruído visual.  
- **Direto** – linguagem clara, microcopy objetiva.  
- **Confiável** – dados consistentes, feedback imediato.  
- **Motivador (pelo desempenho)** – reforço positivo baseado em conquistas (PRs, evolução).  
- **Sem exageros** – evita estética “maromba” ou infantil; aposta na elegância dos números.

### Princípios do design (com exemplos práticos)
1. **Clareza absoluta**  
   - *Exemplo:* Tabela de séries com colunas bem definidas, números alinhados à direita.  
2. **Foco no dado**  
   - *Exemplo:* Gráficos destacam a evolução, sem enfeites.  
3. **Consistência rigorosa**  
   - *Exemplo:* Mesmo componente de badge usado para PR, falha, deload; varia apenas a cor.  
4. **Feedback imediato**  
   - *Exemplo:* Toast verde ao salvar treino; badge “PR!” animado suavemente.  
5. **Escalabilidade funcional**  
   - *Exemplo:* Cards de exercício preparados para receber campos de nutrição futuramente.  
6. **Redução de fricção**  
   - *Exemplo:* Auto-preenchimento da última carga usada.  
7. **Acessibilidade nativa**  
   - *Exemplo:* Contraste WCAG AA, foco visível em todos os elementos interativos.

---

## 2. Arquitetura do Design System

### Filosofia do sistema
**Tokens → Componentes → Padrões → Templates**  
- **Tokens:** valores atômicos (cores, tipografia, espaçamento, sombras).  
- **Componentes:** elementos reutilizáveis (botões, inputs, cards).  
- **Padrões:** combinações de componentes para fluxos (registro de sets, relatórios).  
- **Templates:** layouts de tela prontos (ex.: tela de treino, histórico).

### Convenções de nomenclatura
- **Cores:** `--mike-{função}` (ex.: `--mike-accent`, `--mike-success`).  
- **Tipografia:** `--font-{primary|secondary|mono}`.  
- **Espaçamento:** `--space-{1|2|3|4|5}` (múltiplos de 8px).  
- **Sombras:** `--shadow-{sm|md}`.  
- **Bordas:** `--radius-{sm|md|lg}`.

### Versionamento e atualização
- O manual (Markdown) é a fonte da verdade. Qualquer alteração deve ser proposta via PR e revisada pelo time.  
- Versões seguem [SemVer](https://semver.org/): major para mudanças visuais que quebram compatibilidade, minor para novos componentes, patch para ajustes de documentação.  
- Manter changelog no início do documento.

---

## 3. Identidade da marca

### Nome e escrita correta
- Sempre **MIKE** (em caixa alta). Evitar “mike” ou “Mike” em contextos internos; no app, o nome aparece apenas no logo e em títulos.  
- Tagline: “precisão que gera força” (opcional, usada em splash screen e marketing).

### Tom de voz (guidelines + exemplos)
- **Direto, técnico, sem rodeios.** Use verbos fortes: “Registrar”, “Finalizar”, “Comparar”.  
- **Reforce progresso:** mensagens como “+5kg desde a última sessão”.  
- **Evite culpa:** em vez de “Você perdeu 3 dias”, use “Seu último treino foi há 3 dias. Bora retomar?”.  

| Contexto       | Microcopy exemplo                          |
|----------------|--------------------------------------------|
| CTA principal  | “Registrar treino”                         |
| Sucesso        | “Treino registrado. Força ++”               |
| Erro           | “Campo obrigatório: carga”                  |
| Empty state    | “Nenhum treino ainda. Inicie agora.”        |
| Novo PR        | “Novo recorde! Carga atual: 100kg”          |
| Aviso          | “Carga muito acima do último treino. Confirma?” |

### Uso do logo
- **Logotipo (wordmark):** fonte Space Grotesk Bold, tracking -0.03em.  
- **Versão compacta:** monograma “M” com barra de progresso estilizada (ícone do app).  
- **Área de respiro:** altura igual à altura do “M” em cada lado.  
- **Tamanho mínimo:** 24px de altura para o wordmark; 20px para o ícone.  
- **Usos proibidos:**  
  - ❌ Alterar cores (usar apenas branco/preto ou accent sobre fundo escuro).  
  - ❌ Aplicar sombras fortes ou efeitos 3D.  
  - ❌ Redimensionar desproporcionalmente.

### “Sensação Heavy Duty” aplicada ao design
- **Disciplina visual:** grids rígidos, poucas cores, tipografia sóbria.  
- **Foco no essencial:** cada elemento tem função; eliminar decoração gratuita.  
- **Força nos dados:** números grandes, badges de conquista discretos, gráficos sem distorções.

---

## 4. Paleta de cores

### Cores definidas
| Nome           | HEX     | Função principal                          |
|----------------|---------|-------------------------------------------|
| MIKE Black     | #0A0C0B | Fundos principais, cards (modo escuro)    |
| MIKE Core      | #2C302E | Superfícies, inputs, bordas                |
| MIKE Accent    | #39FF9F | Botões primários, destaques, PRs           |
| Sucesso        | #2ECC71 | Confirmações, badges de conclusão          |
| Atenção        | #F39C12 | Alertas moderados, deload                  |
| Erro           | #E74C3C | Ações destrutivas, campos inválidos        |
| Info           | #3498DB | Dicas, informações complementares          |
| Texto primário | #FFFFFF | Títulos, texto principal (modo escuro)     |
| Texto secundário | #B0B3B2 | Labels, legendas                         |
| Texto sobre accent | #1E1E1E | Texto em botões accent (contraste)       |

### Light mode
- Fundo claro: #F0F2F1 (quase branco)  
- Cards: #FFFFFF  
- Texto primário: #1E1E1E  
- MIKE Core (bordas): #C0C6C3  
- Demais cores semânticas mantêm os mesmos matizes.

### Regras de contraste (WCAG AA)
- Texto normal sobre fundo: ≥4.5:1  
- Texto grande (≥18pt ou 14pt bold): ≥3:1  
- **Verifique sempre** com ferramentas como Contrast Checker.  
- Exemplo válido: branco (#FFFFFF) sobre MIKE Black (#0A0C0B) → 15:1.  
- Exemplo inválido: amarelo (#F39C12) sobre branco → ~2:1 (não use para texto, apenas para badges com fundo escuro).

### Cores para gráficos
- Linha de progresso: MIKE Accent (#39FF9F)  
- Barras de volume: tom mais suave do accent (80% opacidade)  
- Destaque de PR: badge accent com ícone de estrela  
- Séries múltiplas (futuro): usar paleta sequencial de verdes, sem vermelho para evitar associação negativa.

### Do / Don’t
- ✅ Usar accent em botões primários e badges de recorde.  
- ✅ Usar vermelho apenas para exclusão ou erro crítico.  
- ❌ Não usar accent em áreas extensas de texto (fadiga visual).  
- ❌ Não usar verde e vermelho juntos sem rótulo adicional (daltônicos).

---

## 5. Tipografia

### Fontes escolhidas
- **Principal (UI):** Inter (Google Fonts) – legibilidade excelente em mobile, neutralidade técnica.  
- **Secundária (títulos, números grandes):** Space Grotesk – caráter geométrico, passa precisão e modernidade.  
- **Mono (dados, tabelas):** JetBrains Mono – alinhamento perfeito de números, ideal para cargas e repetições.

### Escala tipográfica
| Elemento       | Tamanho | Peso      | Fonte         | Observação                    |
|----------------|---------|-----------|---------------|-------------------------------|
| H1             | 2.5rem  | 700       | Space Grotesk | Tela de boas-vindas, títulos  |
| H2             | 2rem    | 700       | Space Grotesk | Seções principais             |
| H3             | 1.5rem  | 700       | Space Grotesk | Cards de treino               |
| Body           | 1rem    | 400       | Inter         | Texto geral                    |
| Body large     | 1.125rem| 400       | Inter         | Ênfase                         |
| Small          | 0.875rem| 400       | Inter         | Labels, legendas               |
| Caption        | 0.75rem | 500       | Inter         | All caps, tracking 0.5px       |
| Dados em tabela| 1rem    | 400       | JetBrains Mono| Alinhamento à direita          |

### Regras para números e dados
- Usar JetBrains Mono sempre que houver cargas, repetições, datas.  
- Alinhar números à direita em tabelas para facilitar comparação.  
- Destacar PRs com peso 700 e cor accent.

### Espaçamento, altura de linha, CAPS
- Altura de linha padrão: 1.5 (1.2 para títulos).  
- Tracking normal; títulos podem usar -0.02em.  
- CAPS reservado para captions, badges e botões ghost.

### Exemplos de hierarquia visual
- **Tela de treino ativo:**  
  - H2: nome do treino (ex.: “Treino A”)  
  - Body large: nome do exercício  
  - Caption: labels “kg” e “reps”  
  - Mono: valores dos inputs  
- **Tela de relatório:**  
  - H2: “Evolução supino”  
  - Body: estatísticas (volume total, PR)  
  - Gráfico com eixos em small mono

---

## 6. Grid, layout e espaçamento

### Grid base 8px
- Todos os espaçamentos, paddings e margens são múltiplos de 8px: 8, 16, 24, 32, 40…  
- Isso garante consistência e alinhamento perfeito entre elementos.

### Breakpoints mobile-first
| Breakpoint | Largura | Comportamento                          |
|------------|---------|-----------------------------------------|
| Pequeno    | <576px  | Layout em coluna única                  |
| Médio      | 576–992 | Duas colunas para cards                 |
| Grande     | >992px  | Grid mais flexível, sidebars opcionais  |

### Margens e paddings recomendados
- Corpo do app: padding horizontal de 16px (mobile) a 24px (desktop).  
- Cards: padding interno 16px (24px em telas grandes).  
- Entre cards: gap de 16px.

### Densidade de informação
- Em telas de registro, exibir até 3 exercícios por scroll; permitir expansão.  
- Usar separadores finos (1px, cor core) para agrupar sets.  
- Evitar sobreposição de informações; collapse de detalhes avançados (RPE/RIR) em um toque.

### Padrões de cards
- **Card de sessão:** título, data, badge de status (finalizado/planejado).  
- **Card de exercício:** nome do exercício, lista de sets (cada set em linha), botão de adicionar set.  
- **Card de set:** linha com campos de carga, reps, checkbox de concluído.

---

## 7. Iconografia e estilo gráfico

### Estilo de ícone
- **Outline com traço de 2px**, cantos arredondados em 2px.  
- Tamanho padrão: 24x24px.  
- Utilizar ícones do Bootstrap Icons por padronização; em caso de necessidade, criar ícones personalizados seguindo o mesmo estilo.

### Regras de uso
- Ícone sozinho apenas em ações reconhecíveis (menu, adicionar, deletar).  
- Ícone + texto em botões principais para redundância semântica.  
- Cor do ícone herda a cor do texto do elemento pai, a menos que seja para destaque (accent).

### Ilustrações
- **Quando usar:** telas de empty state, onboarding, conquistas.  
- **Estilo:** geométrico, monocromático (branco ou accent), sem detalhes humanos exagerados.  
- **Tema:** elementos de academia (anilhas, barras, gráficos abstratos).

### Fotografia (se usada)
- **Direção:** alto contraste, P&B, foco em detalhes (mãos na barra, anilhas, textura de couro).  
- **Evitar:** fotos de fisiculturistas posando (bro science).  
- **Limites:** usar apenas em áreas de perfil ou inspiração, nunca no fluxo principal.

---

## 8. Componentes UI (catálogo operacional)

### Botões

| Variante     | Exemplo de uso                       | Estados (hover, focus, disabled)                       |
|--------------|--------------------------------------|--------------------------------------------------------|
| Primary      | Registrar, Salvar, Finalizar         | Hover: brightness 95%, focus: outline accent 2px       |
| Secondary    | Cancelar, Adicionar exercício        | Hover: background core, focus: outline accent          |
| Ghost        | Editar, Ver mais                     | Hover: texto accent, sem fundo                          |
| Danger       | Excluir set, Remover treino          | Hover: mais escuro, focus outline error                 |
| Disabled     | Qualquer ação indisponível           | Opacidade 0.5, sem hover                                |

**Acessibilidade:**  
- Todos os botões devem ter `min-width: 44px` e `min-height: 44px` (target touch).  
- Focus ring visível (outline 2px accent + offset 2px).  
- Em telas pequenas, botões ocupam largura total.

### Inputs (text, number, select, textarea)

- Fundo: `--bg-input` (core com 20% de opacidade no light mode).  
- Padding: 16px.  
- Borda: none, apenas focus ring accent.  
- Placeholder: `--text-placeholder`.  
- Validação:  
  - Sucesso: borda verde sutil (2px solid success).  
  - Erro: borda vermelha + mensagem abaixo com ícone.  
- Select: seta personalizada (ícone de chevron).  
- Textarea: altura mínima 80px.

### Form validation (helper text)
- Mensagem abaixo do campo, tamanho small, cor warning/error.  
- Exemplo: “Carga deve ser maior que 0”.

### Cards

**Card de sessão:**  
- Cabeçalho: nome da sessão, data, badge (ex.: “finalizado”).  
- Corpo: lista de exercícios (apenas nomes).  
- Ações: botão “continuar” ou “ver detalhes”.

**Card de exercício (dentro da sessão):**  
- Título: nome do exercício, ícone de variação.  
- Lista de sets (cada set em linha com inputs).  
- Botão “+ adicionar set”.

**Card de set (modo leitura):**  
- Ex: “1x10 100kg” + badge “PR” se aplicável.

### Badges/Chips
- Uso: tags de status, PR, deload, falha, volume alto.  
- Tamanho: padding 4px 8px, small, all caps.  
- Cores:  
  - PR: accent  
  - Falha: warning  
  - Deload: info  
  - Volume alto: success (ou accent mais escuro)  
- Ícone opcional ao lado (ex.: estrela para PR).

### Tabs/Navigation
- Tabs horizontais com underline accent na ativa.  
- Cor inativa: texto secundário.  
- Uso: alternar entre “Treino”, “Histórico”, “Relatórios”.  
- Em telas pequenas, tabs podem rolar horizontalmente.

### Table (histórico)
- Colunas: Data, Exercício, Carga, Reps, Volume, PR.  
- Zebrado suave (linhas alternadas com fundo levemente diferente).  
- Ordenação por data decrescente.

### Toast/Alert
- Aparece no topo ou inferior, dura 3s.  
- Fundo: `--bg-elevated` com borda colorida (success, error, warning).  
- Ícone representativo.  
- Mensagem concisa.  
- Pode incluir ação “desfazer” (ex.: “Set excluído. Desfazer?”).

### Modal/Confirm (ex.: deletar set)
- Overlay escuro com 70% opacidade.  
- Card centralizado com título, mensagem, botões secundário (cancelar) e danger (confirmar).  
- Foco no botão perigoso (danger).  
- Fechar ao clicar fora ou ESC.

### Empty state
- Ilustração simples + mensagem: “Nenhum treino registrado ainda. Comece agora!”  
- Botão primário “Criar primeiro treino”.

### Loading states
- Skeleton loader para listas (cards com gradiente animado).  
- Spinner (ícone circular) para ações curtas.  
- Evitar spinners em tela cheia; usar shimmer nos cards.

---

## 9. Padrões de UI/UX e fluxos principais

### Fluxo 1: Criar sessão → adicionar exercícios → registrar sets → finalizar

1. **Início:** tela “Hoje” com botão “Iniciar treino” (se não houver treino planejado) ou retomar treino em andamento.  
2. **Adicionar exercícios:** campo de busca + lista de exercícios (favoritos primeiro).  
3. **Registrar sets:** cada exercício tem sets pré-preenchidos com base no último treino (carga e reps). Usuário pode ajustar e marcar como concluído.  
4. **Finalizar:** botão fixo inferior “Finalizar treino” → resumo + confirmação.  

**Redução de fricção:**  
- Auto-preenchimento da última carga (âncora).  
- Quick-add set: botão que duplica o set anterior (viés do status quo).  
- Atalho de teclado para next field (mobile: botão “próximo” no teclado numérico).

### Fluxo 2: Duplicar treino anterior / template
- Na tela de histórico, ícone de cópia ao lado do treino → cria nova sessão com mesmos exercícios e cargas iniciais (baseado no último treino daquele exercício).  
- Justificativa: reduzir atrito, aproveitar rotina já estabelecida.

### Fluxo 3: Editar e corrigir erro
- Em qualquer set não finalizado, tocar sobre o campo e alterar.  
- Se já finalizado, opção “editar” no menu do exercício que reabre os sets para correção.  
- Feedback: toast “Set atualizado”.

### Fluxo 4: Visualizar histórico de um exercício
- Na tela de detalhe do exercício, gráfico de progresso (carga máxima ao longo do tempo) + tabela de sessões anteriores.  
- Botão “Ver todos os registros” para expandir.

### Fluxo 5: Relatório semanal/mensal
- Acessível via aba “Relatórios”.  
- Cards: volume total, PRs batidos, consistência (dias de treino).  
- Gráfico de barras por semana.  
- Opção de comparar com período anterior.

**Regra de ouro:** “O registro tem que ser mais rápido que pensar”.  
- Defaults inteligentes, campos pré-preenchidos, atalhos.

---

## 10. Microcopy e feedback (comportamento)

### Biblioteca de mensagens

| Tipo        | Mensagem                                     | Tom / Observação                    |
|-------------|----------------------------------------------|-------------------------------------|
| Sucesso     | “Treino registrado. Força ++”                 | Reforço positivo, sem exagero       |
| Sucesso (PR)| “Novo recorde! +2kg no supino”               | Destaque do progresso               |
| Erro        | “Carga inválida. Digite um número positivo.”  | Específico, instrutivo              |
| Aviso       | “Carga 20% acima do último registro. Confirma?” | Previne erros, pede confirmação   |
| Empty state | “Nenhum treino ainda. Bora começar?”          | Convidativo, sem culpa              |
| Confirmação | “Excluir este set? Essa ação não pode ser desfeita.” | Claro, com botão de perigo       |
| Streak      | “Você treinou 5 dias seguidos. Continue!”     | Reforço positivo                    |

### Padrões de texto para botões
- Sempre verbo + substantivo (ex.: “Adicionar exercício”, não só “Adicionar”).  
- Evitar “OK” ou “Cancelar” sem contexto.

### Reforço positivo sem infantilizar
- Usar linguagem de academia: “Boa série!”, “PR registrado”, “Força ++”.  
- Nunca usar emojis excessivos; apenas um ícone de check ou estrela.

### Evitar culpa/pressão
- Se o usuário ficou dias sem treinar, mensagem neutra: “Seu último treino foi há 5 dias. Que tal retomar?”.  
- Não usar “você está perdendo progresso”.

---

## 11. Acessibilidade e Inclusão (checklist)

- **Contraste:** todas as combinações de texto/fundo devem atender WCAG AA (ver seção 4).  
- **Tamanhos mínimos:** alvos de toque ≥44x44px.  
- **Focus ring:** sempre visível, com outline 2px accent + offset 2px.  
- **Navegação por teclado:** todos os elementos interativos alcançáveis via Tab, ordem lógica.  
- **Cores não são a única forma de comunicação:** badges com ícones, labels, padrões.  
- **Linguagem clara:** frases curtas, evitar jargões sem explicação.  
- **Suporte a leitores de tela:** usar `aria-label`, `role` adequados.  
- **Redimensionamento de fonte:** layout não quebra com zoom de até 200%.  
- **Modo claro/escuro:** ambos testados com contraste.

---

## 12. Data viz / relatórios (padrões de gráficos)

### Regras gerais
- Gráficos devem ser simples, sem 3D.  
- Eixos com labels em small mono.  
- Cores: accent para linha principal; tons mais claros para séries secundárias.

### Gráfico de progresso (linha)
- Exibe carga máxima de um exercício por data.  
- Pontos nos dados; destacar PRs com círculo accent maior.  
- Tooltip ao tocar: “12/04 – 100kg”.

### Gráfico de volume (barras)
- Volume total semanal (reps × carga).  
- Barras em accent com 80% opacidade; barra da semana atual mais forte.  
- Linha de meta (opcional) tracejada.

### Distribuição (pizza? evitar)
- Prefira barras empilhadas para tipos de exercício.

### Ética nos dados
- Escalas sempre começam em zero para não exagerar diferenças.  
- Comparações com período anterior com mesmo eixo.  
- Não omitir contexto: “volume 20% maior que semana passada” é melhor que apenas o número.

### Destaque de PRs
- Ícone de estrela ao lado do ponto no gráfico.  
- Badge “PR” na tabela de histórico.  
- Notificação ao bater PR.

---

## 13. Heurísticas + Economia Comportamental aplicadas

Lista de 15 decisões de produto com base comportamental:

1. **Saliência de progresso (PRs)**  
   - *Problema:* Usuário não percebe evolução.  
   - *Intervenção:* Badge accent + animação suave ao registrar novo PR.  
   - *Por que funciona:* Viés de destaque; reforça autoeficácia.

2. **Auto-preenchimento da última carga**  
   - *Problema:* Registrar toda vez a mesma carga gera atrito.  
   - *Intervenção:* Input já preenchido com valor anterior.  
   - *Por que funciona:* Ancoragem e redução de esforço.

3. **Quick-add set**  
   - *Problema:* Adicionar vários sets manualmente é cansativo.  
   - *Intervenção:* Botão que duplica o set anterior.  
   - *Por que funciona:* Viés do status quo; facilita repetição.

4. **Checklist de treino**  
   - *Problema:* Usuário perde a noção do que já fez.  
   - *Intervenção:* Cada set tem checkbox; barra de progresso no topo.  
   - *Por que funciona:* Gradiente de metas; sensação de conclusão.

5. **Streak visual (calendário)**  
   - *Problema:* Falta de consistência.  
   - *Intervenção:* Pequeno calendário com dias treinados marcados.  
   - *Por que funciona:* Aversão à perda; usuário não quer quebrar a sequência.

6. **Feedback imediato ao salvar**  
   - *Problema:* Incerteza se ação foi concluída.  
   - *Intervenção:* Toast colorido com mensagem.  
   - *Por que funciona:* Reforço imediato; reduz ansiedade.

7. **Templates pré-definidos (Heavy Duty split)**  
   - *Problema:* Iniciantes não sabem por onde começar.  
   - *Intervenção:* Oferecer 2-3 splits prontos.  
   - *Por que funciona:* Reduz overchoice; facilita adoção.

8. **Gráfico de progresso sempre visível no perfil do exercício**  
   - *Problema:* Usuário não acompanha evolução de longo prazo.  
   - *Intervenção:* Mini gráfico na listagem de exercícios.  
   - *Por que funciona:* Viés de confirmação; mostra que o esforço vale a pena.

9. **Metas de curto prazo (ex.: “adicionar 2,5kg esta semana”)**  
   - *Problema:* Falta de objetivos tangíveis.  
   - *Intervenção:* Sugestão de meta baseada no histórico.  
   - *Por que funciona:* Efeito gradiente de metas; pequenos passos.

10. **Confirmação antes de carga muito alta**  
    - *Problema:* Usuário pode se machucar ao tentar carga excessiva.  
    - *Intervenção:* Modal de alerta se carga > 10% do último registro.  
    - *Por que funciona:* Prevenção de viés otimista; commitment device.

11. **Opção de “duplicar treino”**  
    - *Problema:* Criar treino igual toda semana é repetitivo.  
    - *Intervenção:* Botão de cópia no histórico.  
    - *Por que funciona:* Redução de fricção; aproveita rotina.

12. **Badges de consistência (ex.: “3 treinos na semana”)**  
    - *Problema:* Falta de reconhecimento por aderência.  
    - *Intervenção:* Badge discreto no perfil.  
    - *Por que funciona:* Recompensa intrínseca; status social.

13. **Modo escuro como padrão**  
    - *Problema:* Uso noturno cansa a vista.  
    - *Intervenção:* Dark mode ativado por padrão, com toggle.  
    - *Por que funciona:* Conforto visual, foco.

14. **Inputs numéricos com teclado otimizado (mobile)**  
    - *Problema:* Digitar números no teclado padrão é lento.  
    - *Intervenção:* type="number" abre teclado numérico.  
    - *Por que funciona:* Reduz tempo de entrada.

15. **Comparação com “melhor semana”**  
    - *Problema:* Usuário não tem referência de bom desempenho.  
    - *Intervenção:* No relatório, destacar “sua melhor semana: volume X”.  
    - *Por que funciona:* Viés de comparação social consigo mesmo.

---

## 14. Checklist de implementação (Dev + Design QA)

### Por tela

**Tela de treino ativo**  
- [ ] Botão “Iniciar” leva à tela de seleção de exercícios.  
- [ ] Lista de exercícios com scroll.  
- [ ] Cada set tem inputs de carga/reps com auto-preenchimento.  
- [ ] Checkbox marca set como concluído.  
- [ ] Barra de progresso atualiza.  
- [ ] Botão finalizar só ativo após todos sets concluídos? (flexível: permite finalizar incompleto com aviso).  
- [ ] Ao finalizar, mostra resumo e toast de sucesso.

**Tela de relatório**  
- [ ] Cards de volume, PRs, consistência.  
- [ ] Gráfico de barras com dados mock (ou reais).  
- [ ] Tabela de histórico com rolagem.  
- [ ] Filtros por período (semana/mês).

### Por componente
- [ ] Botões: todos os estados testados.  
- [ ] Inputs: focus, placeholder, validação.  
- [ ] Badges: cores corretas, texto em CAPS.  
- [ ] Tabs: underline accent na ativa.  
- [ ] Toast: aparece e some, com ícone.

### Consistência
- [ ] Variáveis CSS usadas em vez de valores fixos.  
- [ ] Espaçamentos seguem grid 8px.  
- [ ] Tipografia conforme escala.  
- [ ] Dark/light mode testados.

### Definição de pronto (DoD) visual/UX
- Design aprovado pelo time.  
- Testes de contraste OK.  
- Navegação por teclado funcional.  
- Microcopy revisado.  
- Componente documentado neste manual.

---

## 15. Apêndice

### Glossário
- **RPE** (Rating of Perceived Exertion): escala de 1 a 10 de esforço.  
- **RIR** (Reps in Reserve): quantas repetições ainda conseguiria fazer.  
- **PR** (Personal Record): recorde pessoal.  
- **Volume:** carga × repetições (ou soma total).  
- **Deload:** semana de treino com carga reduzida.  
- **Set:** série.

### Regras de expansão futura (nutrição, outras modalidades)
- Novos módulos (nutrição, cardio) devem manter a mesma linguagem visual e de componentes.  
- Cores: usar a paleta existente; se necessário, adicionar novos tons na secundária, mas sempre revisando contraste.  
- Ícones: seguir o mesmo estilo outline.  
- Tipografia: manter as fontes.  
- Cards de refeição podem seguir anatomia similar aos de treino (título, lista de alimentos, botões).  
- Gráficos de nutrição usar paleta derivada do accent.

### Roadmap de maturidade do design system

| Versão | Foco                                   |
|--------|----------------------------------------|
| v1.0   | Fundação, componentes essenciais       |
| v1.1   | Novos componentes (modal, toast, empty)|
| v1.2   | Padrões de nutrição e cardio           |
| v2.0   | Design system unificado multiplataforma (web + iOS + Android) |

---

**Fim do manual**  
*Para dúvidas ou sugestões, contate o time de design.*