# MIKE — Manual de Identidade Visual, UI/UX e Design System

**Versão:** 1.0  
**Data:** 16 de fevereiro de 2026  
**Status:** Documento operacional — Baseado no manual HTML v1.0  
**Autoria:** Equipe de Produto MIKE  
**Objetivo:** Referência diária para decisões de design, desenvolvimento e QA

---

## Sumário

1. [Visão Geral e Norte](#1-visão-geral-e-norte)
2. [Arquitetura do Design System](#2-arquitetura-do-design-system)
3. [Identidade da Marca](#3-identidade-da-marca)
4. [Paleta de Cores](#4-paleta-de-cores)
5. [Tipografia](#5-tipografia)
6. [Grid, Layout e Espaçamento](#6-grid-layout-e-espaçamento)
7. [Iconografia e Estilo Gráfico](#7-iconografia-e-estilo-gráfico)
8. [Componentes UI](#8-componentes-ui)
9. [Padrões de UI/UX e Fluxos Principais](#9-padrões-de-uiux-e-fluxos-principais)
10. [Microcopy e Feedback](#10-microcopy-e-feedback)
11. [Acessibilidade e Inclusão](#11-acessibilidade-e-inclusão)
12. [Data Visualization / Relatórios](#12-data-visualization--relatórios)
13. [Heurísticas + Economia Comportamental Aplicadas](#13-heurísticas--economia-comportamental-aplicadas)
14. [Checklist de Implementação](#14-checklist-de-implementação)
15. [Apêndice](#15-apêndice)

---

## 1. Visão Geral e Norte

### Essência da Marca

**"Progresso registrado. Resultados verificados."**

### Promessa Central do MIKE

MIKE transforma treinos em dados acionáveis. Cada sessão é registrada com precisão, cada progressão é verificada objetivamente, e cada decisão de treino é baseada em evidências — não em achismos. Inspirado na metodologia Heavy Duty de Mike Mentzer, eliminamos ruído e entregamos clareza: você sabe exatamente o que melhorou, onde estagnou e o que fazer na próxima sessão. Simplicidade no registro, profundidade na análise. Resultado: controle total sobre seu progresso.

### Personalidade da Marca

| Atributo | Descrição | Implicação Visual |
|----------|-----------|-------------------|
| **PRECISO** | Cada número importa. Não arredondamos, não estimamos. PRs são celebrados com dados. | Números em destaque (bold, tabular), badges claros, gráficos com marcadores exatos |
| **DIRETO** | Zero floreios. Sem gamification infantil ou motivação artificial. A recompensa é o progresso real. | UI limpa, alta hierarquia, botões com verbos claros, sem animações excessivas |
| **CONFIÁVEL** | Consistência visual e funcional. O app funciona, os dados estão seguros, o histórico é imutável. | Componentes consistentes, tokens rígidos, paleta estável, sem "exceções criativas" |
| **MOTIVADOR (sem exagero)** | Celebramos conquistas com destaque visual claro, mas mantemos o tom sério. | PRs destacados em laranja, feedback imediato, mas sem confetes ou emojis |
| **INTELIGENTE** | Antecipa necessidades (sugere carga anterior, destaca padrões), mas nunca assume. | Defaults inteligentes, sugestões contextuais, auto-preenchimento opcional |

### Princípios de Design

#### 1. **Hierarquia Implacável**
**Definição:** Informação crítica domina visualmente. Dados secundários recuam.  
**Como aplicar:**
- Carga e reps em 20–28px bold
- Labels em 12–14px regular secondary
- PRs recebem cor accent + badge
- Usar contraste de peso (700 vs 400) antes de aumentar tamanho

#### 2. **Fricção Zero no Core Flow**
**Definição:** Registrar série = 3 toques ou menos. Defaults eliminam digitação repetitiva.  
**Como aplicar:**
- Botão "+1 set" duplica último automaticamente
- Input de carga pré-preenchido com último valor
- Teclado numérico aparece imediatamente
- Templates de treino acessíveis em 1 toque

#### 3. **Feedback Imediato e Proporcional**
**Definição:** Cada ação gera resposta instantânea. Magnitude do feedback = importância.  
**Como aplicar:**
- Check de série: animação 200ms + cor verde
- Novo PR: animação 600ms + badge laranja permanente
- Erro: shake 300ms + borda vermelha
- Haptic feedback em ações importantes (iOS/Android)

#### 4. **Consistência Obsessiva**
**Definição:** Mesmos padrões em todas as telas. Tokens rígidos. Zero "exceções criativas".  
**Como aplicar:**
- Espaçamento sempre múltiplo de 8px
- Botões primários sempre mesma cor/altura
- Cards sempre 16px padding
- Ícones sempre 24×24px stroke 2px

#### 5. **Dark Mode First**
**Definição:** Projetado para ambientes de treino (academia escura). Light mode é adaptação.  
**Como aplicar:**
- Paleta testada primeiro em dark (#0A0E17 background)
- Contraste elevado garantido (mín. 7:1 para primary text)
- Sombras sutis em dark (elevação por borda, não blur pesado)
- Accent laranja funciona bem em ambos os modos

#### 6. **Dados Antes de Decoração**
**Definição:** Qualquer elemento visual que não comunica dados ou facilita ação é removido.  
**Como aplicar:**
- Sem ilustrações decorativas
- Sem gradientes complexos
- Sem animações "de charme"
- Gráficos mostram dados reais, não placeholders bonitos

#### 7. **Mobile-First, Performance-First**
**Definição:** Projetado para uso em ambiente de treino (mobile, mãos sujas/molhadas, tempo limitado).  
**Como aplicar:**
- Touch targets mínimo 44×44px
- Botões grandes, espaçados
- Loads instantâneos (skeleton screens)
- Funciona offline (dados salvos localmente primeiro)

---

## 2. Arquitetura do Design System

### Filosofia do Sistema

O design system do MIKE segue a estrutura:
```
TOKENS (valores atômicos)
    ↓
COMPONENTES (UI reutilizável)
    ↓
PADRÕES (combinações de componentes)
    ↓
TEMPLATES (telas completas)
```

**Tokens** = CSS variables (cores, fontes, espaçamento, raios, sombras)  
**Componentes** = Botões, inputs, cards, badges, tabs  
**Padrões** = Formulário de exercício, lista de sets, header de sessão  
**Templates** = Tela de treino ativo, tela de relatório, tela de histórico

### Convenções de Nomenclatura

#### Cores
Formato: `--{categoria}-{função}-{variante}`

Exemplos:
- `--mike-core` (primária)
- `--mike-accent` (destaque)
- `--surface-light` / `--surface-dark`
- `--text-primary-light` / `--text-primary-dark`
- `--success` / `--warning` / `--error` / `--info`

#### Tipografia
Formato: `--text-{tamanho}` ou `--font-{função}`

Exemplos:
- `--text-xs` (12px)
- `--text-base` (16px)
- `--text-4xl` (32px)
- `--font-primary` (Inter)
- `--font-secondary` (Manrope)

#### Espaçamento
Formato: `--space-{multiplicador}`

Exemplos:
- `--space-1` (8px)
- `--space-2` (16px)
- `--space-6` (48px)

### Versionamento e Atualização

**Processo de atualização do manual:**

1. **Proposta de mudança** — Designer/Dev abre issue descrevendo problema e solução proposta
2. **Revisão** — Equipe de produto valida impacto (quantas telas afetadas, breaking change?)
3. **Atualização** — Manual atualizado com nova versão (1.0 → 1.1 para minor, 1.0 → 2.0 para breaking)
4. **Comunicação** — Changelog publicado, equipe notificada
5. **Implementação** — Tokens/componentes atualizados no código

**Regra de ouro:** Qualquer mudança que quebra consistência visual entre telas = breaking change = versão major.

**Changelog mínimo:**
- Data da mudança
- O que mudou (token, componente, padrão)
- Por que mudou (problema resolvido)
- Como migrar (se breaking)

---

## 3. Identidade da Marca

### Nome e Uso Correto

**Nome oficial:** MIKE (all caps)

**Regras de escrita:**

✅ **Usar:**
- "MIKE" em títulos, logo, marketing
- "MIKE" em início de frase
- "o app MIKE" em texto corrido

❌ **Evitar:**
- "mike" (minúsculo) — exceto em URLs/handles técnicos
- "Mike" (capitalizado como nome próprio)
- "M.I.K.E." (pontos)
- "MIKE App" (redundante)

**Contextos:**
- Marketing: "Conheça o MIKE"
- UI interna: "MIKE" no logo, "Registrar treino" nos botões (sem repetir nome)
- Documentação técnica: "MIKE Design System v1.0"

### Tom de Voz

#### Princípios Gerais

1. **Objetividade antes de charme** — Dados > adjetivos
2. **Respeito à inteligência do usuário** — Sem explicações condescendentes
3. **Reforço positivo sem infantilizar** — Celebre, mas seja factual
4. **Transparência em erros** — Explique o que deu errado, não desculpe genericamente

#### Guidelines de Microcopy

**Botões (CTAs):**
- Formato: `[Verbo] + [Objeto]` ou `[Verbo] + [Resultado]`
- ✅ "Registrar treino", "Adicionar exercício", "Ver progresso"
- ❌ "Vamos lá!", "Clique aqui", "OK"

**Mensagens de sucesso:**
- Formato: `[Ação] + [Resultado objetivo]`
- ✅ "Treino registrado. +2kg no supino — novo PR."
- ✅ "Exercício adicionado."
- ❌ "Parabéns! Você é incrível! 💪🔥"

**Mensagens de erro:**
- Formato: `[Problema] + [Como resolver]`
- ✅ "Série incompleta. Adicione reps ou carga."
- ✅ "Conexão perdida. Dados salvos localmente — sincronizaremos quando voltar."
- ❌ "Ops! Algo deu errado :("
- ❌ "Erro 500. Tente novamente mais tarde."

**Empty states:**
- Formato: `[Estado] + [Ação sugerida]`
- ✅ "Nenhum treino registrado ainda. Comece agora para rastrear seu progresso."
- ✅ "Sem PRs este mês. Continue treinando — todo progresso conta."
- ❌ "Cadê os gainz? Bora malhar!"

**Nudges e sugestões:**
- Formato: `[Dado objetivo] + [Sugestão opcional]`
- ✅ "Última vez: 3×8 com 60kg. Tente 62.5kg hoje."
- ✅ "Volume total -12% vs. semana passada. Considere adicionar 1 set."
- ❌ "Você consegue mais! Bora bater recorde!"

**Feedback de progresso:**
- ✅ "+2.5kg vs. último treino"
- ✅ "Melhor série: 8 reps (anterior: 6)"
- ❌ "Evoluindo! 🚀"

### Uso do Logo

#### Regras Gerais

**Formato principal:** Wordmark "MIKE" em Manrope ExtraBold, all caps, tracking -2%

**Variações:**
1. **Full logo** — Símbolo + Wordmark (splash, marketing)
2. **Icon** — Apenas símbolo (ícone de app, favicon)
3. **Compact** — Símbolo + "MK" (notificações, widgets)

**Área de respiro:**
- Mínimo de 1× altura do símbolo em todas as direções
- Em layouts apertados, mínimo de 0.5× mas nunca encostar em outros elementos

**Tamanhos mínimos:**
- Digital: 24px altura
- Print: 12mm altura
- Ícone de app: seguir guidelines da plataforma (iOS 1024×1024, Android adaptive)

**Usos proibidos:**
- ❌ Distorcer proporções (esticar/comprimir)
- ❌ Aplicar efeitos (gradientes, sombras, outline, bevel)
- ❌ Usar sobre imagens sem contraste adequado (mín. 4.5:1)
- ❌ Mudar cores fora da paleta oficial
- ❌ Rotacionar, inclinar ou refletir
- ❌ Animar o logo (exceto fade in/out simples)

**Cores permitidas:**
- Primário: `#1E3A8A` (MIKE Core) sobre fundos claros
- Branco `#FFFFFF` sobre fundos escuros ou MIKE Core
- Preto `#0F172A` sobre fundos muito claros (quando Core não funcionar)
- Accent `#F97316` apenas em contextos especiais (lançamento, campanhas)

### "Sensação Heavy Duty" Aplicada

**O que é:** Manter disciplina, foco e seriedade sem parecer agressivo ou "meathead".

**Como aplicar:**

1. **Tipografia forte, mas legível** — Manrope em títulos, Inter em corpo. Pesos bold para dados, não para decoração.

2. **Paleta sólida, não brutal** — Azul profundo (não preto puro). Laranja vibrante (não vermelho agressivo).

3. **Grid rígido, respiros generosos** — Espaçamento consistente evita "poluição visual" sem parecer austero.

4. **Microcopy direto, não rude** — "Série incompleta" (factual) vs. "Você esqueceu de preencher" (acusatório).

5. **Celebração objetiva** — "Novo PR: +5kg" (dado) vs. "ESMAGOU! 💪🔥" (exagero).

6. **Sem atalhos visuais de bodybuilding clichê** — Evitar: fontes tipo "impact condensed italic", fotos de pessoas posando, texturas de metal exageradas, frases motivacionais genéricas.

**Teste rápido:** Se um executivo de tech usaria o app sem constrangimento = acertamos o tom.

---

## 4. Paleta de Cores

### Cores Primárias

| Nome | HEX | Uso | Psicologia |
|------|-----|-----|------------|
| **MIKE Core** | `#1E3A8A` | Botões primários, navegação, identidade | Azul profundo transmite confiança, estabilidade, disciplina. Tom escuro evita associação infantil. |
| **MIKE Accent** | `#F97316` | PRs, conquistas, CTAs de alta importância | Laranja equilibra energia (vermelho) + otimismo (amarelo). Cria saliência visual sem agressividade. |
| **MIKE Deep** | `#0F172A` | Background dark mode, superfícies elevadas | Azul-cinza escuro reduz fadiga ocular vs. preto puro. Mantém coerência com paleta. |

### Superfícies

| Nome | HEX | Uso | Light/Dark |
|------|-----|-----|------------|
| **Surface Light** | `#F8FAFC` | Background light mode, cards | Light |
| **Surface Dark** | `#1E293B` | Cards e containers em dark mode | Dark |
| **Surface Elevated** | `#FFFFFF` (light) / `#1E293B` (dark) | Modals, popovers | Ambos |
| **Border Light** | `#E2E8F0` | Divisores, bordas em light | Light |
| **Border Dark** | `#334155` | Divisores, bordas em dark | Dark |

### Texto

| Nome | HEX | Uso | Contraste |
|------|-----|-----|-----------|
| **Text Primary Light** | `#0F172A` | Texto principal em light mode | 14.1:1 em Surface Light ✅ |
| **Text Secondary Light** | `#475569` | Labels, metadados em light | 7.2:1 em Surface Light ✅ |
| **Text Tertiary Light** | `#94A3B8` | Timestamps, hints em light | 4.6:1 em Surface Light ✅ |
| **Text Primary Dark** | `#F8FAFC` | Texto principal em dark mode | 14.8:1 em MIKE Deep ✅ |
| **Text Secondary Dark** | `#CBD5E1` | Labels, metadados em dark | 8.1:1 em MIKE Deep ✅ |
| **Text Tertiary Dark** | `#64748B` | Timestamps, hints em dark | 4.7:1 em MIKE Deep ✅ |

### Cores Semânticas

| Nome | HEX | Uso | Quando Usar |
|------|-----|-----|-------------|
| **Success** | `#10B981` | Feedback positivo, validação | Série completa, treino salvo (sem PR), validação de form |
| **Warning** | `#F59E0B` | Alertas, confirmações | "Carga muito maior que último treino — confirmar?" |
| **Error** | `#EF4444` | Erros, ações destrutivas | Validação de form, "Excluir treino" |
| **Info** | `#3B82F6` | Dicas, tutoriais | Tooltips, onboarding, help text |

### Regras de Light/Dark Mode

**O que muda:**
- Background: `#F8FAFC` → `#0F172A`
- Surface: `#FFFFFF` → `#1E293B`
- Border: `#E2E8F0` → `#334155`
- Text Primary: `#0F172A` → `#F8FAFC`
- Text Secondary: `#475569` → `#CBD5E1`
- Text Tertiary: `#94A3B8` → `#64748B`
- Sombras: opacidade reduzida em dark (0.05 → 0.3)

**O que NÃO muda:**
- MIKE Core `#1E3A8A` (funciona em ambos)
- MIKE Accent `#F97316` (funciona em ambos)
- Success/Warning/Error/Info (ajustados para contraste, mas HEX permanece)

**Regra de implementação:**
```css
:root {
  --surface: #F8FAFC;
  --text-primary: #0F172A;
}

[data-theme="dark"] {
  --surface: #0F172A;
  --text-primary: #F8FAFC;
}
```

### Regras de Contraste (WCAG)

**Padrão mínimo:** WCAG AA (4.5:1 para texto normal, 3:1 para texto grande ≥18px)  
**Alvo recomendado:** WCAG AAA (7:1 para texto normal)

**Combinações validadas:**

| Fundo | Texto | Contraste | Status |
|-------|-------|-----------|--------|
| MIKE Core | Branco | 8.2:1 | AAA ✅ |
| MIKE Accent | Branco | 3.1:1 | AA ❌ (apenas em badges bold ou ícones) |
| MIKE Deep | Text Primary Dark | 14.8:1 | AAA ✅ |
| Surface Light | Text Primary Light | 14.1:1 | AAA ✅ |
| Surface Dark | Text Primary Dark | 11.2:1 | AAA ✅ |

**Ferramentas de validação:**
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Stark (plugin Figma/Sketch)
- Chrome DevTools: Lighthouse Accessibility Audit

**Prática obrigatória:**
1. Sempre testar combinação de cor ANTES de implementar
2. Se contraste falhar, ajustar tom (mais claro/escuro) até passar
3. NUNCA usar texto pequeno (<18px) em MIKE Accent sobre branco

### Paleta para Gráficos

**Uso em visualizações de dados:**

| Contexto | Cor Principal | Cor Secundária | Cor de Destaque |
|----------|---------------|----------------|-----------------|
| Linha de progresso (carga ao longo do tempo) | MIKE Core `#1E3A8A` | - | MIKE Accent `#F97316` (PRs) |
| Barras de volume (semanal/mensal) | MIKE Core `#1E3A8A` | Info `#3B82F6` (séries secundárias) | MIKE Accent (semana com PR) |
| Múltiplas séries (comparação) | MIKE Core, Info `#3B82F6`, `#8B5CF6` (roxo), MIKE Accent | - | - |
| Heatmap de consistência | Success `#10B981` (treinou), `#E2E8F0` (não treinou) | - | MIKE Accent (PR) |

**Regras:**
- Máximo 4 cores diferentes em um único gráfico (evitar confusão)
- PRs sempre em MIKE Accent com marcador maior (8px vs. 6px)
- Grid de fundo em 10% opacity de Border
- Tooltip em Surface Elevated com sombra-md

### Do / Don't de Cor

#### ✅ DO

- **Usar MIKE Accent apenas para destaques reais** — PRs, novos recordes, ações importantes
- **Manter 80%+ da interface em neutros** — Surface, Border, Text. Cores saturadas são acentos.
- **Usar Success para micro-sucessos** — "Série completa", "Treino salvo"
- **Testar contraste com ferramentas** — Nunca confiar apenas na intuição visual
- **Usar cores semânticas consistentemente** — Verde = sucesso, Amarelo = aviso, Vermelho = erro

#### ❌ DON'T

- **Usar vermelho (Error) como destaque positivo** — Conflito semântico universal
- **Usar MIKE Accent como cor de texto <18px** — Contraste insuficiente
- **Misturar 3+ cores saturadas na mesma tela** — Poluição visual
- **Usar gradientes complexos** — Mantém flat ou gradiente sutil de 1 cor (ex.: Core → Core 20% lighter)
- **Inventar novas cores fora da paleta** — Toda cor deve estar documentada aqui

---

## 5. Tipografia

### Fontes Escolhidas

#### Fonte Principal: **Inter**

**Por quê:**
- Desenhada especificamente para UIs digitais (hinting otimizado, x-height generoso)
- Números tabulares nativos (crucial para tabelas de métricas)
- 9 pesos disponíveis (400–900)
- Open source, disponível no Google Fonts
- Legibilidade superior em telas de alta e baixa resolução

**Pesos usados:**
- 400 (Regular): Body text, labels
- 500 (Medium): Botões, small bold
- 600 (SemiBold): Subtítulos, ênfases
- 700 (Bold): Números de métricas, headers secundários
- 800 (ExtraBold): H1, números de PRs

**Onde usar:**
- Todo corpo de texto
- Inputs, forms
- Botões
- Tabelas
- Números e métricas

#### Fonte Secundária: **Manrope**

**Por quê:**
- Grotesca moderna com personalidade (mais carismática que Inter)
- Condensada naturalmente (tracking apertado funciona bem)
- ExtraBold weight poderoso para impacto
- Diferenciação clara de hierarquia vs. Inter

**Pesos usados:**
- 700 (Bold): H2, H3
- 800 (ExtraBold): H1, logo, navegação principal

**Onde usar:**
- H1, H2
- Logo
- Navegação principal (tabs, bottom nav)
- Títulos de seções importantes

#### Fonte Mono (Opcional): **JetBrains Mono**

**Quando usar:**
- Tabelas de dados técnicos extremamente detalhadas (ex.: export CSV)
- Códigos de referência (se houver integração com APIs externas)
- **NÃO** usar para métricas principais (Inter tabular é superior)

### Escala Tipográfica

| Elemento | Fonte | Tamanho | Peso | Line Height | Uso |
|----------|-------|---------|------|-------------|-----|
| **H1** | Manrope | 32px | 800 | 40px (1.25) | Título de página principal |
| **H2** | Manrope | 24px | 700 | 32px (1.33) | Seção principal |
| **H3** | Inter | 20px | 600 | 28px (1.4) | Header de card |
| **H4** | Inter | 18px | 600 | 24px (1.33) | Subsection |
| **Body** | Inter | 16px | 400 | 24px (1.5) | Texto padrão |
| **Body Bold** | Inter | 16px | 600 | 24px (1.5) | Ênfase inline |
| **Small** | Inter | 14px | 400 | 20px (1.43) | Labels, secondary info |
| **Caption** | Inter | 12px | 500 | 16px (1.33) | Metadados, timestamps |
| **Number Large** | Inter | 28px | 700 | 32px (1.14) | Métricas principais (carga, volume, PRs) |
| **Number Medium** | Inter | 20px | 700 | 24px (1.2) | Métricas secundárias (reps, sets) |
| **Number Small** | Inter | 18px | 600 | 24px (1.33) | Números em tabelas |

**CSS Variables:**
```css
--text-xs: 12px;
--text-sm: 14px;
--text-base: 16px;
--text-lg: 18px;
--text-xl: 20px;
--text-2xl: 24px;
--text-3xl: 28px;
--text-4xl: 32px;
```

### Regras para Números e Dados

**Princípio:** Números são informação crítica — devem ser instantaneamente legíveis.

#### Legibilidade

1. **Tabular nums obrigatório** — Números alinhados verticalmente em tabelas
```css
.metric-value {
  font-feature-settings: 'tnum';
  font-variant-numeric: tabular-nums;
}
```

2. **Peso bold para destaque** — Carga, reps, volume em 700 (bold) mínimo

3. **Unidade menor que valor** — "80**kg**" (80 em 28px bold, kg em 18px regular)

4. **Espaçamento entre valor e unidade** — 4px gap ou espaço não-quebrável

#### Hierarquia de Métricas

**Tela de treino ativo:**
- Carga atual: 28px bold (prioridade máxima)
- Reps: 20px bold
- Set number: 14px medium secondary
- Última carga: 14px regular tertiary

**Tela de relatório:**
- Métrica principal (ex.: Volume total): 28px bold
- Sub-métricas (ex.: PRs batidos): 20px bold
- Dados de tabela: 16px regular tabular

### Regras de Espaçamento e Line Height

**Line height:**
- Headers (H1–H4): 1.2–1.4 (condensado para impacto)
- Body text: 1.5 (conforto de leitura)
- Small/Caption: 1.33–1.43 (evitar muito espaço em textos curtos)
- Números grandes: 1.1–1.2 (aperto visual reforça peso)

**Letter spacing (tracking):**
- Headers grandes (H1, H2): `-0.02em` (condensado, impacto)
- ALL CAPS: `+0.05em` (respiro entre letras)
- Body: `0` (padrão)
- Números tabulares: `0` (alinhamento vertical perfeito)

**Uso de ALL CAPS:**

✅ **Quando usar:**
- Navegação principal (TREINOS, PROGRESSO, PERFIL)
- Labels de badges (NOVO PR, COMPLETO)
- Botões secundários pequenos (DETALHES, EDITAR)

❌ **Quando NÃO usar:**
- Parágrafos (reduz legibilidade em 50%)
- Títulos longos (>3 palavras)
- Dados numéricos (confunde leitura)

**Regra:** ALL CAPS sempre com tracking +0.05em e tamanho 12–14px max.

### Exemplos de Hierarquia

#### Exemplo 1: Tela de Treino Ativo
```
TREINO A — PEITO/TRÍCEPS          ← H2 (Manrope 24px bold)
45 min em andamento · 8/12 séries  ← Caption (Inter 12px medium secondary)

Supino reto — Barra                ← H4 (Inter 18px semibold)
Última vez: 3×8 com 75kg           ← Small (Inter 14px regular tertiary)

Set 1: 80kg × 8 reps ✓             ← Body bold (Inter 16px bold) + Caption secondary
       ↑ Number medium (20px bold)
```

#### Exemplo 2: Tela de Relatório
```
PROGRESSO SEMANAL                  ← H1 (Manrope 32px extrabold)

Volume Total                       ← Small (Inter 14px medium secondary)
12,480kg                           ← Number Large (Inter 28px bold core)
+8% vs. semana passada             ← Caption (Inter 12px medium success)

PRs Batidos                        ← Small (Inter 14px medium secondary)
3                                  ← Number Large (Inter 28px bold accent)
```

---

## 6. Grid, Layout e Espaçamento

### Grid Base: 8px

**Por quê:**
- Divisível por 2 (4px, 8px, 16px, 24px...)
- Compatível com densidade de pixels de telas modernas (1x, 2x, 3x)
- Facilita alinhamento visual e consistência
- Reduz decisões arbitrárias ("quanto espaço colocar?" → múltiplo de 8)

**Escala de espaçamento:**
```
--space-1: 8px    (micro-espaçamento, gap entre ícone e texto)
--space-2: 16px   (padding de cards, gap entre inputs)
--space-3: 24px   (padding de telas, gap entre seções)
--space-4: 32px   (separação de blocos grandes)
--space-5: 40px   (margem superior de seções)
--space-6: 48px   (espaçamento hero/destaque)
```

**Regra de ouro:** Todo padding, margin, gap deve ser múltiplo de 8px. Se precisar de 12px, use 16px. Se precisar de 20px, use 24px.

### Breakpoints Mobile-First

**Estratégia:** Projetar para mobile primeiro, expandir para tablets e desktops.

| Breakpoint | Largura | Dispositivo | Colunas |
|------------|---------|-------------|---------|
| **xs** | <576px | Mobile portrait | 1 coluna (full-width) |
| **sm** | ≥576px | Mobile landscape | 1–2 colunas |
| **md** | ≥768px | Tablet portrait | 2 colunas |
| **lg** | ≥992px | Tablet landscape, desktop | 3 colunas |
| **xl** | ≥1200px | Desktop grande | 3–4 colunas |

**Comportamento por tela:**

**Tela de treino ativo (mobile):**
- 1 coluna
- Cards full-width com padding 16px
- Bottom nav fixo

**Tela de treino ativo (desktop):**
- 2 colunas: exercícios à esquerda (60%), histórico/insights à direita (40%)
- Padding lateral 32px

**Tela de relatório (mobile):**
- 1 coluna
- Gráficos full-width
- Tabelas scrolláveis horizontalmente

**Tela de relatório (desktop):**
- 3 colunas para cards de métricas
- Gráficos em 2/3 da largura
- Tabelas full-width com colunas expandidas

### Margens e Paddings Recomendados

#### Telas Principais

**Mobile:**
- Padding lateral: 16px
- Padding superior: 16px (abaixo do header)
- Padding inferior: 80px (acima do bottom nav)
- Gap entre cards: 16px

**Desktop:**
- Padding lateral: 32px (ou max-width 1200px centralizado)
- Padding superior: 24px
- Padding inferior: 32px
- Gap entre cards: 24px

#### Cards

**Padding interno:**
- Mobile: 16px
- Desktop: 16px (não aumentar — densidade é boa)

**Gap entre elementos dentro de card:**
- Header → conteúdo: 12px
- Entre linhas de dados: 8px
- Entre seções dentro do card: 16px (divisor visual)

#### Forms

**Gap entre inputs:**
- Vertical: 16px
- Horizontal (quando lado a lado): 16px

**Padding de input:**
- Vertical: 12px
- Horizontal: 16px

### Densidade de Informação

**Problema:** Mostrar muitos dados (sets, reps, carga, tempo, RPE, notas) sem poluir.

**Solução:**

1. **Hierarquia clara** — Dado principal (carga) em destaque, secundários recuam
2. **Agrupamento visual** — Bordas sutis, background alternado (zebra striping em tabelas)
3. **Progressive disclosure** — Dados avançados (RPE, RIR, notas) em "Mais detalhes" colapsável
4. **Truncate + Tooltip** — Notas longas truncadas em 1 linha, expandem ao toque/hover
5. **Ícones substituem texto** — "✓" em vez de "Completo", troféu em vez de "Novo PR"

**Exemplo: Card de exercício (densidade ideal)**
```
┌─────────────────────────────────────┐
│ Supino reto — Barra           [...]│ ← H4 + kebab menu
│ Última: 3×8 com 75kg               │ ← Small tertiary (contexto)
├─────────────────────────────────────┤
│ Set 1  80kg × 8 ✓                  │ ← Bold + check (info primária)
│ Set 2  80kg × 7 ✓                  │
│ Set 3  80kg × 6 ✓                  │
│ [+ Adicionar set]                  │ ← Ghost button
└─────────────────────────────────────┘
```

**Informação secundária (RPE, tempo de descanso) escondida até expandir.**

### Padrões de Cards

#### Card de Sessão (histórico)

**Anatomia:**
- Header: Nome do treino (H3) + badge de PR (se houver)
- Meta: Duração, total de séries, data relativa (Caption secondary)
- Divisor: 1px border
- Lista de exercícios: Nome + carga principal (Small + Bold)
- Ação: Tap inteiro do card para abrir detalhes

**Padding:** 16px  
**Border-radius:** 12px  
**Hover (desktop):** Border muda para MIKE Core, sombra-sm

#### Card de Exercício (durante treino)

**Anatomia:**
- Header: Nome do exercício (H4) + variação (Small) + menu (ícone)
- Hint: "Última vez: X" (Small tertiary)
- Lista de sets: Número, carga, reps, check (layout em grid)
- Ação: "+Adicionar set" (ghost button)

**Padding:** 16px  
**Gap entre sets:** 8px  
**Estados:** Check verde quando set completo, cinza quando vazio

#### Card de Métrica (relatório)

**Anatomia:**
- Label: Nome da métrica (Small secondary)
- Valor: Número grande (28px bold) + unidade (18px)
- Delta: Comparação vs. período anterior (Caption + ícone ↑↓)

**Padding:** 16px  
**Background:** Surface Elevated  
**Layout:** Grid de 2–3 cards por linha (desktop), 1 por linha (mobile)

---

## 7. Iconografia e Estilo Gráfico

### Estilo de Ícone

**Biblioteca:** Bootstrap Icons (https://icons.getbootstrap.com/)

**Por quê:**
- 1.800+ ícones consistentes
- CDN disponível (load rápido)
- Outline e filled disponíveis
- Open source, sem licença

**Especificações:**

| Propriedade | Valor | Motivo |
|-------------|-------|--------|
| **Grid** | 24×24px | Padrão Material Design, touch target adequado |
| **Stroke** | 2px (outline) | Balanceado — não muito fino, não muito grosso |
| **Cantos** | Arredondados 2px | Sutil, moderno, coerente com border-radius de componentes |
| **Estilo principal** | Outline | Mais leve, funciona bem em densidade alta |
| **Estilo de destaque** | Filled 90% opacity | Para ações importantes (adicionar, PRs) |

**Ícones core do MIKE:**

| Contexto | Ícone Bootstrap | Nome | Uso |
|----------|-----------------|------|-----|
| Treino | `bi-clipboard-check` | clipboard-check | Lista de treinos, iniciar sessão |
| Exercício | `bi-list-task` | list-task | Adicionar exercício |
| PR | `bi-trophy-fill` | trophy-fill | Badge de PR (filled, laranja) |
| Progresso | `bi-graph-up-arrow` | graph-up-arrow | Tela de relatórios |
| Calendário | `bi-calendar3` | calendar3 | Histórico por data |
| Configurações | `bi-gear` | gear | Settings |
| Adicionar | `bi-plus-circle` | plus-circle | Adicionar set, exercício |
| Editar | `bi-pencil` | pencil | Editar dados |
| Deletar | `bi-trash` | trash | Excluir (uso com confirmação) |
| Check | `bi-check-circle-fill` | check-circle-fill | Set completo |
| Info | `bi-info-circle` | info-circle | Tooltips, ajuda |

### Regras de Uso

#### Ícone Sozinho vs. Ícone + Texto

**Ícone sozinho (sem label):**
- ✅ Quando a ação é universal e óbvia (ex.: "×" para fechar, "⚙" para settings)
- ✅ Em espaços muito apertados (mobile nav, action buttons)
- ⚠️ SEMPRE com `aria-label` ou `title` para acessibilidade

**Ícone + Texto:**
- ✅ Ações menos óbvias (ex.: "Duplicar treino")
- ✅ Botões primários importantes (ex.: "+ Adicionar exercício")
- ✅ Navegação principal (tabs com ícone + label)

**Regra de ouro:** Na dúvida, use ícone + texto. Usuários não devem adivinhar.

#### Cor de Ícone

**Padrão:**
- Ícones seguem cor do texto ao redor
- Ícones de navegação: tertiary quando inativo, core quando ativo
- Ícones em botões: branco (se botão core/accent), core (se botão outline)

**Exceções (ícones semânticos):**
- Check de set completo: success green
- Troféu de PR: accent laranja
- Ícone de erro em validação: error red
- Ícone de info em tooltip: info blue

### Ilustrações

**Filosofia:** Minimalista funcional — apenas quando necessário.

**Quando usar:**
- Empty states (ex.: clipboard vazio para "Nenhum treino")
- Onboarding (explicar conceitos: "O que é RPE?")
- Erros de conexão (ex.: wifi off)

**Quando NÃO usar:**
- Decoração genérica
- Headers de seção (substituir por dados ou ícones)
- Placeholders de loading (usar skeleton screens)

**Características quando usadas:**
- Estilo: Line art, 2px stroke, cantos arredondados 2px
- Paleta: 1 cor (MIKE Core ou Accent) + neutros (Border)
- Tamanho: 120×120px max
- Posição: Centralizada acima do texto do empty state
- Sem personagens humanos (evita infantilização)

**Exemplo:** Empty state de histórico
```
    [Ícone clipboard-check outline em cinza 30%]
           ↓
    Nenhum treino registrado ainda
    ↓
    [Botão: Começar primeiro treino]
```

### Fotografia

**Uso:** **NÃO** usar fotografia dentro do app (dados > fotos).

**Exceção:** Marketing e onboarding externo (landing page, app store).

**Se usada em marketing:**
- Estilo: P&B alto contraste + overlay laranja 10%
- Foco: Detalhes de equipamento (anilhas, barras, knurling) — não pessoas
- Crop: Close-ups, ângulos técnicos (não poses heroicas)
- Tratamento: Desaturação 100%, contraste +20%, clarity +15%

**Regra:** Dentro do app, substituir fotos por gráficos de progresso. Dados motivam mais que imagens genéricas.

---

## 8. Componentes UI

### 8.1 Buttons

#### Objetivo
Ações primárias, secundárias e terciárias. Hierarquia clara de importância.

#### Anatomia
- Label (texto do botão)
- Ícone (opcional, à esquerda ou direita do texto)
- Container (background + borda + padding)

#### Variantes

**Primary Button**
- **Uso:** Ação principal da tela (ex.: "Registrar treino", "Finalizar sessão")
- **Estilo:** Background MIKE Core, texto branco, sem borda
- **Altura:** 48px (mobile), 44px (desktop)
- **Padding:** 16px horizontal
- **Border-radius:** 12px
- **Fonte:** Inter 16px weight 600

**Secondary Button (Outline)**
- **Uso:** Ação secundária (ex.: "Cancelar", "Ver histórico")
- **Estilo:** Background transparente, borda 2px Border, texto Text Primary
- **Altura:** 48px (mobile), 44px (desktop)
- **Padding:** 16px horizontal
- **Border-radius:** 12px

**Ghost Button**
- **Uso:** Ação terciária, links de ação (ex.: "Adicionar set", "Editar")
- **Estilo:** Background transparente, sem borda, texto MIKE Core
- **Padding:** 8px horizontal, 8px vertical
- **Fonte:** Inter 14px weight 600

**Accent Button**
- **Uso:** CTAs de altíssima importância, raros (ex.: "Bater PR", "Upgrade Pro")
- **Estilo:** Background MIKE Accent, texto branco, sombra 0 4px 12px rgba(249,115,22,0.3)
- **Altura:** 48px
- **Padding:** 16px horizontal
- **Border-radius:** 12px

**Danger Button**
- **Uso:** Ações destrutivas (ex.: "Excluir treino", "Resetar dados")
- **Estilo:** Background Error, texto branco
- **Altura:** 44px
- **Padding:** 16px horizontal
- **Border-radius:** 12px

#### Estados

| Estado | Visual | Comportamento |
|--------|--------|---------------|
| **Default** | Cores padrão da variante | - |
| **Hover** | Primary: background 10% lighter. Secondary: background Surface. Ghost: background Core 5%. | Cursor pointer |
| **Active** | `transform: scale(0.98)` | Feedback tátil ao tocar |
| **Focus** | Outline 2px MIKE Accent offset 2px | Navegação por teclado |
| **Disabled** | Opacity 40%, cursor not-allowed | Sem interação, sem hover |
| **Loading** | Spinner 20px branco (ou Core se outline) + opacity 70% | Sem interação |

#### Acessibilidade

- ✅ Área de toque mínima: 44×44px (iOS HIG)
- ✅ Label claro e descritivo (evitar "OK", "Enviar" genérico)
- ✅ `aria-label` se ícone sozinho
- ✅ Focus ring SEMPRE visível (nunca `outline: none` sem alternativa)
- ✅ Estado disabled comunicado via `aria-disabled="true"`

#### Regras de Uso

✅ **DO:**
- Usar no máximo 1 Primary por tela (exceção: wizards com "Próximo" + "Finalizar")
- Label com verbo + objeto ("Registrar treino", não "Registrar")
- Ícone à esquerda para ações de criação ("+"), à direita para navegação ("→")

❌ **DON'T:**
- Usar 3+ Primary Buttons na mesma tela
- Labels genéricos ("OK", "Clique aqui")
- Botões muito largos (max-width: 320px em desktop)

---

### 8.2 Inputs

#### Text Input / Number Input

**Objetivo:** Capturar dados textuais ou numéricos (exercício, carga, reps).

**Anatomia:**
- Label (acima do input)
- Input field (container + texto)
- Helper text (abaixo, opcional)
- Error message (abaixo, se erro)

**Estilo:**
- Altura: 48px
- Padding: 12px vertical, 16px horizontal
- Border: 1px solid Border
- Border-radius: 12px
- Fonte: Inter 16px regular (evita zoom no iOS)
- Background: Surface Elevated

**Variantes:**
- **Text:** `<input type="text">`
- **Number:** `<input type="number">` com steppers opcionais
- **Number com steppers:** Botões -/+ laterais (44×44px touch target)

**Estados:**

| Estado | Visual | Comportamento |
|--------|--------|---------------|
| **Default** | Border Border color, placeholder tertiary | - |
| **Focus** | Border MIKE Core 2px, box-shadow 0 0 0 2px rgba(30,58,138,0.1) | Teclado apropriado (numérico para number) |
| **Error** | Border Error 2px, mensagem de erro abaixo em vermelho 14px | - |
| **Disabled** | Opacity 50%, cursor not-allowed | Sem edição |
| **Filled** | Texto em Text Primary bold (se dado importante como carga) | - |

**Acessibilidade:**
- ✅ `<label>` sempre associado com `for="inputId"`
- ✅ `aria-describedby` para helper text e erro
- ✅ `aria-invalid="true"` se erro
- ✅ Error message com ícone + texto (não só cor)

**Regras de Uso:**

✅ **DO:**
- Label descritivo (ex.: "Carga (kg)", não só "Carga")
- Placeholder com exemplo (ex.: "Ex: 80")
- Teclado numérico para inputs de número (mobile)
- Auto-focus no primeiro input de um form (mobile: com cuidado, pode abrir teclado indesejado)

❌ **DON'T:**
- Placeholder como label (some ao digitar)
- Inputs muito largos (max-width: 320px para texto, 120px para número)
- Validação enquanto usuário digita (validar ao blur ou submit)

---

#### Select

**Objetivo:** Escolher uma opção de lista (ex.: exercício, variação).

**Estilo:** Igual a Input, com ícone chevron-down à direita.

**Dropdown:**
- Background: Surface Elevated
- Border: 1px Border
- Border-radius: 12px
- Sombra: shadow-md
- Itens: Padding 12px 16px, hover background Surface (5% core)

**Acessibilidade:**
- ✅ Navegação por teclado (↑↓ para navegar, Enter para selecionar)
- ✅ Opção selecionada com checkmark visual
- ✅ `aria-expanded` no botão

---

#### Textarea

**Objetivo:** Notas, observações longas (ex.: "Sentiu dor no ombro").

**Estilo:**
- Min-height: 96px (3 linhas)
- Max-height: 240px (scrollable depois)
- Resize: vertical apenas
- Demais specs iguais a Input

**Regras:**
- Usar apenas quando necessário (evitar poluir formulários)
- Placeholder claro (ex.: "Adicione observações sobre este treino (opcional)")

---

### 8.3 Form Validation

**Objetivo:** Comunicar erros e orientar correção.

#### Quando Validar
- **Ao blur (sair do campo):** Validação imediata de formato (ex.: email inválido)
- **Ao submit:** Validação final de campos obrigatórios
- **Nunca while typing:** Irritante e desmotivador

#### Mensagem de Erro

**Formato:** `[O que está errado] + [Como corrigir]`

Exemplos:
- ✅ "Carga obrigatória. Adicione um valor."
- ✅ "Reps deve ser maior que 0."
- ❌ "Erro."
- ❌ "Campo inválido."

**Estilo:**
- Texto: Error color, 14px regular
- Ícone: `bi-exclamation-circle` à esquerda
- Posição: Abaixo do input, margin-top 4px

#### Helper Text (Sucesso)

**Formato:** Texto em Success color com ícone check

Exemplo:
- ✅ "Carga +5kg vs. último treino"

---

### 8.4 Cards

#### Card de Sessão (Histórico)

**Objetivo:** Exibir treino passado na lista de histórico.

**Anatomia:**
- Header: Nome treino (H3) + Badge PR (se houver)
- Meta: Duração, séries, data (Caption secondary)
- Divisor: 1px Border
- Preview: Primeiros 3 exercícios com carga principal (Small)
- Ação: Tap/click abre detalhes

**Estilo:**
- Padding: 16px
- Border: 1px Border
- Border-radius: 12px
- Background: Surface Elevated

**Estados:**
- Hover (desktop): Border → MIKE Core, sombra-sm
- Active: `transform: scale(0.99)`

---

#### Card de Exercício (Durante Treino)

**Objetivo:** Gerenciar sets de um exercício durante sessão ativa.

**Anatomia:**
- Header: Nome exercício (H4) + variação (Small) + menu (kebab)
- Hint: "Última vez: 3×8 com 75kg" (Small tertiary)
- Sets: Lista de sets (número, carga, reps, check)
- Ação: "+ Adicionar set" (ghost button)

**Estilo:**
- Padding: 16px
- Border: 1px Border
- Border-radius: 12px
- Gap entre sets: 8px

**Estados dos Sets:**
- Vazio: Border color, check cinza
- Completo: Border Success 1px, check verde filled

---

#### Card de Métrica (Relatório)

**Objetivo:** Exibir métrica principal (volume, PRs, consistência).

**Anatomia:**
- Label: Nome da métrica (Small secondary, ALL CAPS)
- Valor: Número grande (28px bold) + unidade
- Delta: Comparação (Caption + ícone ↑↓ + cor semântica)

**Estilo:**
- Padding: 16px
- Background: Surface Elevated
- Border: 1px Border
- Border-radius: 12px

**Layout:** Grid 2–3 colunas (desktop), 1 coluna (mobile)

---

### 8.5 Badges / Chips

#### Badge PR

**Objetivo:** Destacar novo recorde pessoal.

**Estilo:**
- Background: MIKE Accent
- Texto: Branco, 12px bold, ALL CAPS
- Padding: 4px 12px
- Border-radius: 4px
- Ícone: `bi-trophy-fill` branco
- Sombra: `0 2px 8px rgba(249,115,22,0.3)`

**Animação:** Pop (scale 0 → 1.1 → 1) ao aparecer pela primeira vez (600ms)

---

#### Badge de Status

**Variantes:**
- **Completo:** Background Success, texto branco
- **Deload:** Background Border, texto Text Secondary
- **Falha:** Background Error, texto branco
- **Ajustar:** Background Warning, texto branco

**Estilo:** Igual a Badge PR, sem ícone.

---

### 8.6 Tabs / Navigation

#### Bottom Navigation (Mobile)

**Objetivo:** Navegação principal (5 itens max).

**Anatomia:**
- Ícone 24px
- Label 12px
- Indicador de ativo: Barra superior 3px MIKE Accent

**Estilo:**
- Height: 56px + safe-area-inset-bottom
- Background: Surface Elevated
- Border-top: 1px Border
- Active: Ícone + label MIKE Core
- Inactive: Ícone + label Text Tertiary

**Acessibilidade:**
- ✅ `aria-label` em cada tab
- ✅ `aria-current="page"` no ativo
- ✅ Touch target 44×44px mínimo

---

#### Tabs Horizontais

**Objetivo:** Navegação entre seções de uma tela (ex.: Treinos / Nutrição / Sono).

**Estilo:**
- Underline style
- Active: Border-bottom 3px MIKE Core, texto Core bold
- Inactive: Texto Text Secondary regular
- Hover (desktop): Texto Core
- Scroll horizontal em mobile (se >3 tabs)

---

### 8.7 Table (Histórico)

**Objetivo:** Exibir dados tabulares (histórico de exercício, volume semanal).

**Anatomia:**
- Header: Background Surface, texto Small bold ALL CAPS secondary
- Rows: Padding 12px, border-bottom 1px Border
- Cells: Alinhamento left para texto, right para números

**Estilo:**
- Zebra striping: Rows pares com background Surface (3% core)
- Sticky header: Position sticky top 0 ao scroll
- Hover row (desktop): Background 5% core

**Colunas Típicas:**
- Data (left align)
- Exercício (left align)
- Sets (center align)
- Carga (right align, tabular-nums)
- Reps (right align, tabular-nums)
- Volume Total (right align, tabular-nums bold)

**Responsividade Mobile:**
- Scroll horizontal se >4 colunas
- Priorizar colunas principais (Data, Carga) visíveis sem scroll

---

### 8.8 Toast / Alert

#### Toast (Feedback Temporário)

**Objetivo:** Confirmar ação (ex.: "Treino salvo", "Set adicionado").

**Estilo:**
- Background: Surface Elevated (escurecido 10% em light, clareado 10% em dark)
- Border: 1px Success (sucesso), Error (erro), Info (info)
- Border-radius: 12px
- Padding: 12px 16px
- Ícone: Check (sucesso), X (erro), Info (info) à esquerda
- Texto: 14px regular
- Sombra: shadow-lg

**Posição:** Bottom center (mobile), top right (desktop)

**Duração:** 3s (auto-dismiss) com botão "Desfazer" se ação reversível

**Acessibilidade:**
- ✅ `role="alert"` para leitores de tela
- ✅ Não bloqueia interação (não é modal)

---

#### Alert (Atenção Persistente)

**Objetivo:** Avisos importantes que não somem automaticamente (ex.: "Sem conexão — dados salvos localmente").

**Estilo:**
- Background: Warning 10% opacity
- Border-left: 4px Warning
- Padding: 16px
- Ícone: `bi-exclamation-triangle` à esquerda
- Texto: 14px regular
- Botão: "Entendi" ou "Detalhes" (ghost)

**Posição:** Topo da tela (abaixo do header) ou inline (acima do conteúdo afetado)

---

### 8.9 Modal / Confirm

**Objetivo:** Confirmação de ações destrutivas (ex.: "Excluir treino?") ou formulários complexos.

**Anatomia:**
- Overlay: Background MIKE Deep 60% opacity
- Container: Surface Elevated, border-radius 16px, sombra-lg
- Header: H3 + botão fechar (×)
- Content: Texto explicativo
- Footer: Botões (secondary "Cancelar" + danger "Excluir")

**Dimensões:**
- Mobile: Full-width com margin 16px (topo e laterais), bottom-sheet style
- Desktop: Max-width 480px, centralizado

**Acessibilidade:**
- ✅ `role="dialog"` e `aria-modal="true"`
- ✅ Focus trap (Tab navega apenas dentro do modal)
- ✅ Escape fecha o modal
- ✅ Focus inicial no botão primário (ou campo de input)

**Regras de Uso:**

✅ **DO:**
- Usar apenas para ações que precisam de confirmação ou dados complexos
- Título claro ("Excluir treino?", não "Atenção")
- Explicar consequência ("Todos os dados serão perdidos")

❌ **DON'T:**
- Usar para simples avisos (use Toast)
- Encadear modals (modal abre outro modal)
- Modal sem botão de fechar

---

### 8.10 Empty State

**Objetivo:** Comunicar ausência de dados e orientar primeira ação.

**Anatomia:**
- Ícone: 120×120px outline em Border color 30%
- Título: H4 em Text Secondary
- Descrição: Small em Text Tertiary (opcional)
- CTA: Primary button

**Exemplo:**
```
    [Ícone clipboard-check]
    
    Nenhum treino registrado ainda
    
    Comece agora para rastrear seu progresso
    
    [Botão: Registrar primeiro treino]
```

**Tom:** Neutro e orientador, nunca culposo ("Você ainda não treinou" ❌)

---

### 8.11 Loading States

#### Skeleton Screen

**Objetivo:** Placeholder animado enquanto dados carregam.

**Estilo:**
- Background: Border color
- Animation: Pulse (opacity 100% → 60% → 100%, 1.5s infinite)
- Shape: Replica layout do conteúdo (retângulos para texto, círculos para avatares)

**Quando usar:**
- Listas (histórico de treinos)
- Cards de métricas
- Tabelas

---

#### Spinner

**Objetivo:** Loading genérico (ex.: salvando treino, sincronizando).

**Estilo:**
- Tamanho: 20px (inline), 48px (full-screen)
- Cor: MIKE Core (ou branco se dentro de botão)
- Animation: Rotate 1s linear infinite

**Quando usar:**
- Dentro de botões (estado loading)
- Full-screen para ações críticas (sincronizando, processando)

**Regra:** Preferir skeleton screens (mostram estrutura) sobre spinners genéricos.

---

## 9. Padrões de UI/UX e Fluxos Principais

### Regra de Ouro
**"Registrar uma série deve ser mais rápido que pensar nela."**

**Implicação:** Defaults inteligentes, auto-preenchimento, duplicação automática, teclado numérico imediato.

---

### Fluxo 1: Criar Sessão → Registrar Sets → Finalizar

#### Etapa 1: Iniciar Sessão

**Tela:** Home  
**Ação:** Botão "Registrar treino" (primary, central, 48px height)  
**Decisão:** Exibir opções:
1. "Treino rápido" (template predefinido — 1 toque)
2. "Treino A / B / C" (templates salvos)
3. "Treino customizado" (montar do zero)

**Fricção:** 0 — usuário escolhe em 1 toque.

**Default inteligente:** Se usuário treinou ontem "Treino A", sugerir "Treino B" no topo (baseado em padrão A/B/C).

---

#### Etapa 2: Adicionar Exercícios

**Tela:** Sessão ativa (vazia)  
**Ação:** "Adicionar exercício" (accent button, destaque visual)  
**Input:** Busca com autocomplete (últimos 10 exercícios no topo)  
**Decisão:** Exercício selecionado → abre card de exercício vazio

**Fricção:** Reduzida — busca rápida, histórico acessível.

---

#### Etapa 3: Registrar Sets

**Tela:** Card de exercício  
**Ação:** Inputs de carga e reps pré-preenchidos com último valor  
**Flow:**
1. Usuário ajusta carga/reps se necessário (steppers ±)
2. Toca "✓" (check button grande, 56×56px, verde)
3. Set salvo, próximo set duplicado automaticamente (botão "+1 set" invisível — automação)
4. Repete até finalizar exercício

**Fricção:** Mínima — 1–2 toques por set (ajuste opcional + check).

**Feedback:** Check verde animado (200ms) + haptic suave.

**Comportamento inteligente:**
- Se carga aumentou >10% vs. último treino → alerta: "Carga muito maior — confirmar?" (evitar erro de digitação)
- Se fez mais reps que último treino → destaque sutil "+2 reps vs. última vez"

---

#### Etapa 4: Finalizar Sessão

**Tela:** Sessão ativa (com exercícios completos)  
**Ação:** "Finalizar treino" (primary button, fixo no bottom)  
**Decisão:** Modal de resumo:
- Tempo total
- Séries completas
- Volume total
- **PRs batidos** (highlight laranja com animação)
- Botão: "Salvar e encerrar"

**Fricção:** 0 — um toque, sem campos extras obrigatórios.

**Opcional:** Campo "Notas" (textarea colapsável, não obrigatório).

---

### Fluxo 2: Duplicar Treino Anterior

**Problema:** Usuário faz mesmo treino toda semana (Treino A).  
**Solução:** Botão "Repetir treino anterior" na home.

**Flow:**
1. Lista últimos 5 treinos
2. Seleciona "Treino A — Peito/Tríceps"
3. Sessão criada com todos os exercícios e último valor de carga/reps pré-preenchido
4. Usuário só ajusta se necessário e marca checks

**Fricção:** Reduzida drasticamente — de 20+ toques para 3–5 toques.

**Justificativa comportamental:** **Default effect** — pessoas aceitam sugestões pré-configuradas. **Redução de carga cognitiva** — elimina decisões repetitivas.

---

### Fluxo 3: Editar e Corrigir Erro

**Problema:** Usuário digitou 800kg em vez de 80kg.  
**Solução:** Edit inline + Undo.

**Flow:**
1. Toque no valor errado (800kg)
2. Input aparece inline (sem abrir modal)
3. Corrige para 80kg
4. Salva automaticamente ao blur
5. Toast: "Set atualizado" com botão "Desfazer" (5s)

**Fricção:** Mínima — correção imediata, sem navegação extra.

**Justificativa:** **Zero switching cost** — custo de corrigir erro = 0 → reduz abandono.

---

### Fluxo 4: Visualizar Histórico de Exercício

**Problema:** Usuário quer saber se está progredindo no supino.  
**Solução:** Tela de histórico de exercício com gráfico e tabela.

**Flow:**
1. Tela de exercício → tap em "Histórico"
2. Gráfico de linha: carga ao longo do tempo (últimos 3 meses)
3. PRs destacados em laranja (marcador maior)
4. Tabela abaixo: Data, Sets×Reps, Carga, Volume
5. Filtros: "Último mês", "3 meses", "Tudo"

**Fricção:** 0 — dados já processados, gráfico gerado automaticamente.

**Insight automático:** "Você progrediu +12.5kg em 8 semanas — parabéns!" (texto acima do gráfico).

---

### Fluxo 5: Relatório Semanal/Mensal

**Problema:** Usuário quer avaliar desempenho global.  
**Solução:** Tela de progresso com cards de métricas + gráficos.

**Flow:**
1. Bottom nav → "Progresso"
2. Cards principais:
   - Treinos completos: 4/4 (100%)
   - Volume total: 12,480kg (+8% vs. semana passada)
   - PRs batidos: 3
3. Gráfico de barras: Volume por dia da semana
4. Tabela: PRs detalhados (exercício, nova carga, delta)

**Fricção:** 0 — tudo gerado automaticamente.

**Justificativa:** **Temptation bundling** — juntar ação fácil (ver progresso) com recompensa (dados positivos) cria hábito de consulta.

---

## 10. Microcopy e Feedback

### Biblioteca de Mensagens

#### Mensagens de Sucesso

| Contexto | Mensagem |
|----------|----------|
| Treino salvo | "Treino registrado. Volume total: 3,200kg." |
| Treino salvo com PR | "Treino registrado. +5kg no supino — novo PR." |
| Set adicionado | "Set completo." |
| Exercício adicionado | "Exercício adicionado." |
| Meta atingida | "Meta semanal completa: 4/4 treinos." |

---

#### Mensagens de Erro

| Contexto | Mensagem |
|----------|----------|
| Série incompleta | "Série incompleta. Adicione reps ou carga." |
| Campo obrigatório vazio | "Carga obrigatória. Adicione um valor." |
| Conexão perdida | "Sem conexão. Dados salvos localmente — sincronizaremos quando voltar." |
| Erro ao salvar | "Não foi possível salvar. Tente novamente." |
| Valor inválido | "Reps deve ser maior que 0." |

---

#### Mensagens de Aviso

| Contexto | Mensagem |
|----------|----------|
| Carga muito alta | "Carga +50% vs. último treino. Confirmar?" |
| Deletar treino | "Excluir treino? Todos os dados serão perdidos." |
| Resetar dados | "Resetar todos os dados? Esta ação é irreversível." |

---

#### Empty States

| Contexto | Mensagem |
|----------|----------|
| Nenhum treino | "Nenhum treino registrado ainda. Comece agora para rastrear seu progresso." |
| Nenhum PR | "Sem PRs este mês. Continue treinando — todo progresso conta." |
| Nenhum exercício | "Adicione seu primeiro exercício para começar." |
| Histórico vazio | "Nenhum dado para este exercício ainda." |

---

### Padrões de Texto para Botões

**Formato:** `[Verbo] + [Objeto/Resultado]`

| Contexto | Texto do Botão |
|----------|----------------|
| Iniciar sessão | "Registrar treino" |
| Adicionar exercício | "Adicionar exercício" |
| Salvar set | "✓" (check, sem texto) |
| Finalizar treino | "Finalizar treino" |
| Ver histórico | "Ver histórico" |
| Deletar treino | "Excluir treino" |
| Cancelar ação | "Cancelar" |
| Duplicar treino | "Repetir treino anterior" |

**Evitar:**
- "OK", "Enviar", "Clique aqui", "Vamos lá"

---

### Reforço Positivo sem Infantilizar

#### ✅ Princípios

1. **Factual antes de emocional** — "Novo PR: +5kg" > "Você é incrível!"
2. **Dados como recompensa** — "+8% volume vs. semana passada" é mais motivador que "Parabéns!"
3. **Celebrar objetivamente** — Badge laranja + animação sutil > confetes e emojis

#### Exemplos

**Situação:** Usuário bateu PR  
❌ "ARRASOU! Você é um MONSTRO! 💪🔥"  
✅ "Novo PR: Supino 82.5kg (+2.5kg vs. anterior)"

**Situação:** Usuário completou meta semanal  
❌ "PARABÉNS, CAMPEÃO! Meta batida! 🎉"  
✅ "Meta semanal completa: 4/4 treinos. Consistência de 100%."

**Situação:** Usuário melhorou volume  
❌ "Evoluindo demais! Continue assim!"  
✅ "Volume total +12% vs. semana passada."

---

### Evitar Culpa e Pressão

#### ❌ Mensagens ruins (culpa/pressão)

- "Você não treinou esta semana. Cadê a disciplina?"
- "Meta não atingida. Tente melhorar."
- "Você está abaixo da média."
- "Últimos 3 treinos foram fracos."

#### ✅ Mensagens boas (neutras/positivas)

- "Você treinou 2 de 7 dias esta semana."
- "Próximo treino: Terça-feira às 18h (seu horário habitual)."
- "Volume total: 8,200kg. Média histórica: 10,500kg."
- "PRs este mês: 0. Último PR: Supino 80kg em 2 Fev."

**Princípio:** Dados neutros permitem auto-avaliação sem julgamento externo.

---

## 11. Acessibilidade e Inclusão

### Contraste

**Padrão mínimo:** WCAG AA (4.5:1 para texto normal, 3:1 para texto grande ≥18px)  
**Alvo:** WCAG AAA (7:1 para texto normal)

#### Validação Obrigatória

Toda combinação de cor de texto + fundo deve ser testada antes de produção:
- Ferramenta: WebAIM Contrast Checker, Stark, ou Chrome DevTools Lighthouse

#### Regras

✅ **DO:**
- Text Primary em Surface sempre ≥7:1
- Text Secondary em Surface sempre ≥4.5:1
- Botões com texto branco em backgrounds saturados sempre ≥4.5:1

❌ **DON'T:**
- Texto cinza claro em fundo branco sem validar
- MIKE Accent como background de texto <18px (contraste 3.1:1 insuficiente)

---

### Tamanho Mínimo

**Texto:**
- Mínimo absoluto: 14px para texto corrido
- Recomendado: 16px (body text padrão)
- Botões: mínimo 16px

**Touch targets (mobile):**
- Mínimo: 44×44px (iOS HIG, WCAG 2.1 Success Criterion 2.5.5)
- Recomendado: 48×48px
- Espaçamento entre targets: mínimo 8px

---

### Focus Ring e Navegação por Teclado

#### Regras Críticas

1. **NUNCA remover outline sem alternativa**
```css
/* ❌ PROIBIDO */
button:focus {
  outline: none;
}

/* ✅ PERMITIDO */
button:focus {
  outline: none;
  box-shadow: 0 0 0 2px var(--mike-accent);
}
```

2. **Focus ring sempre visível**
- Cor: MIKE Accent
- Espessura: 2px
- Offset: 2px (não colado na borda do elemento)

3. **Navegação por teclado funcional**
- Tab: avança entre elementos interativos
- Shift+Tab: retrocede
- Enter/Space: ativa botões e links
- Escape: fecha modals e dropdowns
- Arrow keys: navega em selects e tabs

---

### Cores sem Depender Apenas de Cor

**Problema:** Usuários com daltonismo (8% homens, 0.5% mulheres) não distinguem vermelho/verde.

**Solução:** Sempre combinar cor + ícone ou texto.

#### Exemplos

**Set completo:**
- ❌ Apenas borda verde
- ✅ Borda verde + ícone check verde

**Erro de validação:**
- ❌ Apenas input com borda vermelha
- ✅ Borda vermelha + ícone de erro + mensagem de texto

**PR batido:**
- ❌ Apenas texto laranja "Novo PR"
- ✅ Badge laranja + ícone troféu + texto "NOVO PR"

---

### Linguagem Clara

**Princípios:**
1. **Simplicidade** — Frases curtas, vocabulário comum
2. **Objetividade** — Evitar jargões técnicos desnecessários
3. **Consistência** — Mesmos termos para mesmas ações (nunca "Registrar" em uma tela e "Salvar" em outra)

#### Glossário de Termos (usar consistentemente)

| Termo | Uso |
|-------|-----|
| **Treino** | Sessão completa (não "Workout", "Ficha") |
| **Exercício** | Movimento específico (não "Movimento") |
| **Série/Set** | Sequência de reps (usar "Set" no código, "Série" no UI) |
| **Carga** | Peso usado (não "Peso", "Quilagem") |
| **Reps** | Repetições (abreviação aceita) |
| **PR** | Personal Record / Recorde Pessoal (explicar no onboarding) |
| **Volume** | Carga × Reps × Sets (explicar na primeira vez) |

---

### Checklist Final de Acessibilidade

#### Por Componente

- [ ] Contraste validado (WCAG AA mínimo)
- [ ] Touch target ≥44×44px
- [ ] Focus ring visível (2px MIKE Accent)
- [ ] Navegação por teclado funcional
- [ ] Labels semânticos (`<label>`, `aria-label`)
- [ ] Estados comunicados (`aria-disabled`, `aria-invalid`, `aria-expanded`)
- [ ] Erros com ícone + texto (não só cor)

#### Por Tela

- [ ] Heading hierarchy correta (H1 → H2 → H3, sem pular níveis)
- [ ] Landmarks semânticos (`<header>`, `<nav>`, `<main>`, `<footer>`)
- [ ] Imagens com `alt` descritivo (ou `alt=""` se decorativo)
- [ ] Forms com labels associados
- [ ] Modals com focus trap
- [ ] Feedback de loading (skeleton ou spinner + `aria-live="polite"`)

---

## 12. Data Visualization / Relatórios

### Regras para Gráficos de Progresso (Linha)

**Objetivo:** Mostrar evolução de carga ao longo do tempo.

**Especificações:**

| Elemento | Estilo |
|----------|--------|
| **Linha** | 3px, MIKE Core, sem gradiente |
| **Fill** | Gradient vertical Core → transparente (30% → 0%) |
| **Grid** | Linhas horizontais 1px, Border 10% opacity |
| **Eixo X** | Caption tertiary, labels de data |
| **Eixo Y** | Caption tertiary, labels de carga (kg) |
| **Marcadores** | Círculos 6px preenchidos, borda branca 2px |
| **PR** | Marcador laranja 8px + label acima "PR" |

**Interação:**
- Hover (desktop): Tooltip com data, carga, reps
- Tap (mobile): Tooltip fixo até tap fora

---

### Regras para Gráficos de Volume (Barras)

**Objetivo:** Comparar volume entre dias/semanas.

**Especificações:**

| Elemento | Estilo |
|----------|--------|
| **Barras** | MIKE Core, border-radius-top 4px |
| **Espaçamento** | 8px entre barras |
| **Altura** | Proporcional ao valor max (não começar de valor arbitrário) |
| **Labels** | Valor no topo de cada barra (Small bold) |
| **Eixo X** | Caption tertiary, labels de dia da semana |
| **Destaque** | Barra com maior volume em MIKE Accent |

**Interação:**
- Hover: Opacity 80% + tooltip com breakdown (quantos exercícios, séries)

---

### Regras para Distribuição (Simples)

**Objetivo:** Mostrar proporção (ex.: % de treinos por grupo muscular).

**Tipo:** Barras horizontais (evitar pizza — difícil de comparar).

**Especificações:**
- Barras horizontais 100% width
- Segmentos coloridos (max 4 cores)
- Labels inline com %
- Legenda abaixo

---

### Como Destacar PRs (Saliência)

**Princípio:** PRs são eventos especiais — devem ser impossíveis de ignorar.

**Técnicas:**

1. **Cor diferente** — MIKE Accent (laranja) em todos os gráficos
2. **Tamanho maior** — Marcador 8px vs. 6px padrão
3. **Label flutuante** — "PR" acima do ponto
4. **Linha vertical tracejada** — Sutil, do PR até o eixo X
5. **Animação ao hover** — Scale 1.2 + tooltip detalhado

**Exemplo visual (gráfico de linha):**
```
 Carga (kg)
    |
 85 |           ● PR (8px laranja)
    |          /│\
 80 |       ●─┘ │ └─●
    |      /    │    \
 75 |   ●─┘     │     └─●
    |           │
    └───────────┼─────────► Tempo
              label "PR"
```

---

### Como Evitar Enganar (Ética)

#### Escalas

❌ **DON'T:**
- Eixo Y que não começa em 0 (exagera diferenças)
- Escalas logarítmicas sem aviso claro
- Escalas diferentes em gráficos lado a lado

✅ **DO:**
- Eixo Y sempre começando em 0 (exceto se variação é muito pequena — avisar)
- Escalas consistentes em comparações
- Labels claros em ambos os eixos

#### Comparações

❌ **DON'T:**
- Comparar períodos diferentes sem normalizar (ex.: "semana passada" com 3 treinos vs. "esta semana" com 6)
- Omitir contexto (ex.: mostrar +10kg sem dizer que foi deload anterior)

✅ **DO:**
- Normalizar comparações (ex.: volume/treino, não volume total)
- Sempre incluir contexto (ex.: "Volume +8% vs. semana passada (ambas 4 treinos)")

#### Contexto

❌ **DON'T:**
- Gráficos sem unidades
- Deltas sem referência ("Você melhorou!" — melhorou quanto?)

✅ **DO:**
- Sempre incluir unidades (kg, reps, treinos, %)
- Deltas com valor absoluto E percentual ("Volume +800kg (+8%)")

---

### Paleta e Hierarquia Visual dos Gráficos

#### Hierarquia de Cores

1. **MIKE Core** — Dados principais (carga, volume)
2. **MIKE Accent** — Destaques (PRs, recordes)
3. **Info Blue** — Séries secundárias (ex.: volume acessório)
4. **Success Green** — Metas atingidas
5. **Border** — Grid, eixos, divisores

#### Regra de Máximo

- Max 4 cores diferentes em um único gráfico
- Se precisar de mais, usar tons diferentes da mesma cor (Core 100%, Core 70%, Core 40%)

#### Acessibilidade em Gráficos

- Não depender apenas de cor (usar padrões de preenchimento também: sólido, tracejado, pontilhado)
- Incluir tabela de dados abaixo do gráfico (para leitores de tela e usuários que preferem números)

---

## 13. Heurísticas + Economia Comportamental Aplicadas

### 1. Saliência de Progresso (PRs e Streaks)

**Comportamento alvo:** Reconhecer pequenos ganhos como progresso real

**Problema:** Usuário não percebe progressos pequenos (+2.5kg, +1 rep) → desmotivação

**Intervenção de design:**
- PRs recebem badge laranja permanente + animação "pop" (scale 0 → 1.1 → 1, 600ms)
- Streak de dias consecutivos visível no topo do app (ícone 🔥 + número)
- Comparação automática: "Hoje: +2.5kg vs. semana passada" exibida inline

**Por que funciona:**
- **Efeito de saliência** — Humanos subavaliam pequenos ganhos incrementais. Destacar visualmente aumenta percepção de progresso.
- **Peak-end rule** — Experiências positivas no final (PR ao concluir treino) criam memória afetiva forte.

**Onde aparece:**
- Card de exercício (durante treino ativo)
- Tela de resumo pós-treino
- Gráficos com marcadores laranja em PRs

---

### 2. Defaults Inteligentes (Redução de Fricção)

**Comportamento alvo:** Minimizar esforço cognitivo no registro

**Problema:** Usuário abandona registro porque digitação repetitiva é chata e demorada

**Intervenção de design:**
- Botão "+1 set" duplica automaticamente carga/reps do último set
- Input de carga pré-preenchido com valor do último treino idêntico
- Templates de treino salvos ("Treino A", "Treino B") acessíveis em 1 toque

**Por que funciona:**
- **Default effect** — Pessoas aceitam sugestões pré-configuradas (opt-out > opt-in). Reduzir toques de 12 para 3 elimina fricção cognitiva.
- **Paradoxo da escolha** — Menos decisões = menos fadiga = maior conclusão.

**Onde aparece:**
- Tela de registro de sets (auto-preenchimento de carga/reps)
- Home screen (botão "Repetir treino anterior")
- Início de novo treino (templates visíveis)

---

### 3. Feedback Imediato (Dopamina Comportamental)

**Comportamento alvo:** Criar loop de reforço positivo

**Problema:** Sem feedback instantâneo, ação parece "perdida" → usuário sente que app não registrou

**Intervenção de design:**
- Check verde + micro-animação (200ms) ao completar set
- Vibração háptica suave (iOS/Android)
- Toast "Treino salvo" com ícone check aparece <500ms após ação

**Por que funciona:**
- **Condicionamento operante** — Reforço imediato (<500ms) aumenta repetição do comportamento.
- **Dopamina** — Feedback visual + tátil dispara dopamina, associando registro a recompensa.

**Onde aparece:**
- Ao salvar set (check animado)
- Ao finalizar treino (toast + resumo)
- Ao bater PR (animação + badge)

---

### 4. Efeito Gradiente de Metas (Goal Gradient Effect)

**Comportamento alvo:** Aumentar taxa de conclusão de treinos e metas semanais

**Problema:** Metas distantes são desmotivadoras ("faltam 3 treinos esta semana" = desânimo)

**Intervenção de design:**
- Barra de progresso semanal visível: "3/4 treinos — 75%"
- Micro-metas por treino: "Faltam 2 exercícios"
- Checklist visual ao final do treino

**Por que funciona:**
- **Goal gradient effect** — Quanto mais perto da meta, maior o esforço. Mostrar "falta pouco" aumenta taxa de conclusão em 30% (estudos de reward cards).

**Onde aparece:**
- Topo da tela de treino ativo (progresso do treino atual)
- Home screen (progresso semanal)
- Resumo pós-treino

---

### 5. Viés do Progresso (Progress Bias)

**Comportamento alvo:** Motivar novos usuários a completar primeira semana

**Problema:** Começar do zero desmotiva ("vou levar 1 ano para chegar lá")

**Intervenção de design:**
- Novos usuários iniciam com "10% completo" (artifício: contamos criação de perfil + primeiro exercício como avanço)
- Gráficos sempre mostram tendência positiva em destaque (linha verde ascendente)
- Framing positivo: "Você já treinou 5 vezes este mês" (não "Você faltou 3 vezes")

**Por que funciona:**
- **Endowed progress effect** — Dar algum "progresso" inicial aumenta conclusão em 50+% (estudo de cartões de café: começar com 2 selos grátis).

**Onde aparece:**
- Onboarding (primeiros passos pré-completos)
- Tela inicial de progresso
- Resumos mensais

---

### 6. Commitment Device (Pré-compromisso)

**Comportamento alvo:** Aumentar aderência e retorno ao app

**Problema:** Usuário não volta ao app → abandono

**Intervenção de design:**
- Pergunta no setup: "Qual seu objetivo esta semana?" → Meta visível no topo do app ("Meta: 4 treinos/semana — 2/4 completos")
- Notificação: "Você disse que treinaria hoje às 18h" (lembrete sem julgamento)

**Por que funciona:**
- **Commitment consistency** — Declarar intenção publicamente (mesmo que só para si) cria pressão psicológica leve para follow-through.

**Onde aparece:**
- Setup inicial (definir meta semanal)
- Home screen (meta visível)
- Notificações (se usuário permitir)

---

### 7. Evitar Overchoice (Paradoxo da Escolha)

**Comportamento alvo:** Acelerar seleção de exercícios e configurações

**Problema:** Muitas opções → paralisia decisória → abandono

**Intervenção de design:**
- Máximo 5 variações de exercício visíveis por padrão (restante em "Ver mais +12")
- Template "Treino rápido" pré-montado para iniciantes (3 exercícios básicos)
- Configuração avançada (RPE, RIR, tempo de descanso) escondida em "Mais opções" colapsável

**Por que funciona:**
- **Overchoice** — Muitas opções reduzem satisfação e aumentam abandono. Simplicidade default + opção de expandir = best of both worlds.

**Onde aparece:**
- Busca de exercícios (primeiros 5 resultados + "Ver mais")
- Configurações de treino (básico visível, avançado colapsado)

---

### 8. Loss Aversion (Aversão à Perda)

**Comportamento alvo:** Prevenir quebra de streak

**Problema:** Usuário perde streak de 7 dias e desiste completamente

**Intervenção de design:**
- Notificação: "Não perca seu streak de 7 dias!" (framing negativo, mais eficaz que "Continue seu streak")
- Ao perder, mostrar: "Você treinou 89% do tempo em 2024" (foco no acumulado, não na falha)
- Botão "Registrar treino rápido" (5 min, 1 exercício) para "salvar" o dia

**Por que funciona:**
- **Loss aversion** — Perdas doem 2× mais que ganhos equivalentes. Framing de perda (não perca) aumenta ação imediata.

**Onde aparece:**
- Notificações (quando streak em risco)
- Home screen (alerta sutil se streak vai quebrar hoje)

---

### 9. Social Proof (Prova Social)

**Comportamento alvo:** Validar esforço do usuário

**Problema:** Usuário não sabe se está indo bem (sem referência externa)

**Intervenção de design:**
- Benchmarks anônimos: "80% dos usuários que treinam 4×/semana veem PRs no 1º mês"
- Comparação interna: "Você está 15% acima da sua média de 3 meses" (sem competição externa)

**Por que funciona:**
- **Social proof** — Humanos usam normas sociais como atalho decisório. Comparação interna evita desmotivação competitiva.

**Onde aparece:**
- Relatórios semanais/mensais
- Insights automáticos

---

### 10. Fresh Start Effect (Recomeço)

**Comportamento alvo:** Re-engajar usuários que falharam

**Problema:** Usuário falhou na meta e sente culpa → abandono

**Intervenção de design:**
- "Nova semana, novo recorde" (toda segunda-feira)
- "Janeiro — mês de novos PRs" (marcos temporais)
- Botão "Resetar meta" sem penalidade visual (não mostra "você falhou")

**Por que funciona:**
- **Fresh start effect** — Marcos temporais (início de semana/mês/ano) criam sensação de "slate limpo", reduzindo culpa e aumentando motivação.

**Onde aparece:**
- Transição de semana (segunda-feira)
- Transição de mês (dia 1)
- Após quebra de streak

---

### 11. Micro-recompensas (Gamification Sutil)

**Comportamento alvo:** Manter dopamina elevada durante treino longo

**Problema:** Sessão de 60 min sem recompensa intermediária → tédio

**Intervenção de design:**
- Check verde animado a cada set (feedback constante)
- Confete sutil (partículas discretas, 10 partículas max) ao bater PR
- Badge "Streak de 10 treinos" (visual, não pontos numéricos)

**Por que funciona:**
- **Variable reward** — Recompensas frequentes mantêm dopamina elevada. **Evitamos** leaderboards e pontos (recompensas extrínsecas matam motivação intrínseca).

**Onde aparece:**
- Inline durante treino (check verde)
- Resumo final (badges de conquistas)

---

### 12. Ancoragem (Anchor Effect)

**Comportamento alvo:** Guiar progressão realista

**Problema:** Usuário não sabe que carga usar (iniciante) ou aumenta demais (risco de lesão)

**Intervenção de design:**
- "Última vez: 60kg" exibido ANTES do input de carga (âncora visual)
- Sugestão: "Tente 62.5kg hoje" (micro-progressão como âncora de cima)

**Por que funciona:**
- **Anchor effect** — Primeira informação vista vira referência mental. Sugerir +2.5kg ancora usuário em progressão segura e realista.

**Onde aparece:**
- Input de carga (hint com último valor)
- Card de exercício (sugestão de carga)

---

### 13. Custo de Mudança Zero (Zero Switching Cost)

**Comportamento alvo:** Encorajar correção de erros

**Problema:** Usuário erra digitação (800kg em vez de 80kg) e desiste de corrigir (friction)

**Intervenção de design:**
- Edit inline sem abrir modal (tap no valor → input aparece ali mesmo)
- Undo imediato: Toast com "Desfazer" por 5s após qualquer edição
- Validação não-bloqueante: "Carga muito alta — tem certeza?" com opção "Sim, confirmar"

**Por que funciona:**
- **Zero switching cost** — Custo de corrigir = 0 → usuário não abandona. Undo reduz ansiedade de erro permanente.

**Onde aparece:**
- Qualquer input editável (carga, reps, notas)
- Ações reversíveis (deletar set, remover exercício)

---

### 14. Temptation Bundling (Agrupar Tentação)

**Comportamento alvo:** Aumentar consulta de relatórios (tarefa "chata")

**Problema:** Usuário não consulta relatórios porque parece "trabalho extra"

**Intervenção de design:**
- Insights semanais automatizados no **feed principal** (não em aba separada): "Você bateu 3 PRs esta semana 🏆"
- Gráfico de progresso aparece AO LADO do botão "Iniciar treino" (não escondido)

**Por que funciona:**
- **Temptation bundling** — Juntar ação fácil (ver feed/treino) com recompensa (ver progresso) cria hábito de consulta sem esforço extra.

**Onde aparece:**
- Home feed (cards de insights entre treinos)
- Transição de telas (gráfico de progresso após finalizar treino)

---

### 15. Framing Positivo (Positive Framing)

**Comportamento alvo:** Manter auto-eficácia alta

**Problema:** Mensagens negativas desmotivam e aumentam churn

**Intervenção de design:**
- ❌ Evitar: "Você faltou 2 treinos esta semana"
- ✅ Usar: "Você treinou 5 de 7 dias — 71% de consistência"
- ❌ Evitar: "Não bateu PR hoje"
- ✅ Usar: "Volume total +8% vs. semana passada"

**Por que funciona:**
- **Framing effect** — Mesma informação, apresentação diferente = reação emocional diferente. Framing positivo mantém auto-eficácia alta.

**Onde aparece:**
- Todos os textos de resumo e feedback
- Notificações
- Relatórios

---

## 14. Checklist de Implementação

### Checklist por Tela

#### Tela: Home / Dashboard

**Design:**
- [ ] Botão "Registrar treino" (primary, 48px height, centralizado)
- [ ] Streak visível (ícone fogo + número)
- [ ] Meta semanal visível (barra de progresso + "3/4 treinos")
- [ ] Cards de insights (últimos PRs, volume semanal)
- [ ] Bottom nav (5 itens max, ícone + label)

**Comportamento:**
- [ ] Botão "Registrar treino" abre opções (templates + custom)
- [ ] Streak atualiza diariamente
- [ ] Meta atualiza em tempo real ao completar treino
- [ ] Tap em card de insight abre detalhes

**Acessibilidade:**
- [ ] Contraste validado (todos os textos ≥4.5:1)
- [ ] Touch targets ≥44×44px
- [ ] Focus ring visível em todos os botões
- [ ] Landmarks semânticos (`<header>`, `<nav>`, `<main>`)

---

#### Tela: Sessão Ativa (Treino em Andamento)

**Design:**
- [ ] Header com nome do treino (H2) + tempo decorrido
- [ ] Barra de progresso (sets completos / total)
- [ ] Cards de exercício (nome, hint, lista de sets)
- [ ] Botão "Finalizar treino" fixo no bottom

**Comportamento:**
- [ ] Sets duplicam automaticamente ao adicionar ("+1 set")
- [ ] Check verde animado ao completar set (200ms)
- [ ] Validação ao finalizar: todos os exercícios têm ≥1 set
- [ ] Modal de resumo ao finalizar (tempo, volume, PRs)

**Acessibilidade:**
- [ ] Inputs de carga/reps com labels associados
- [ ] Teclado numérico aparece automaticamente em inputs number
- [ ] Estados de set (vazio/completo) comunicados visualmente E semanticamente

---

#### Tela: Histórico de Exercício

**Design:**
- [ ] Gráfico de linha (carga ao longo do tempo)
- [ ] PRs destacados em laranja (marcador 8px)
- [ ] Tabela abaixo (Data, Sets, Carga, Volume)
- [ ] Filtros (Último mês / 3 meses / Tudo)

**Comportamento:**
- [ ] Gráfico carrega em <1s (dados pré-processados)
- [ ] Tooltip ao hover/tap em marcadores
- [ ] Tabela ordenável por coluna (tap em header)
- [ ] Filtros atualizam gráfico + tabela instantaneamente

**Acessibilidade:**
- [ ] Tabela de dados abaixo do gráfico (fallback para leitores de tela)
- [ ] Cores do gráfico não dependem apenas de cor (PRs têm label textual)
- [ ] Tooltip com dados completos (não só visual)

---

#### Tela: Relatório Semanal/Mensal

**Design:**
- [ ] Cards de métricas (treinos, volume, PRs) em grid 2–3 colunas
- [ ] Gráfico de barras (volume por dia)
- [ ] Lista de PRs detalhados (exercício, nova carga, delta)
- [ ] Filtros de período (Semana / Mês / Ano)

**Comportamento:**
- [ ] Cards atualizam ao mudar filtro de período
- [ ] Gráfico de barras com hover tooltip (breakdown de volume)
- [ ] PRs clicáveis (abrem histórico do exercício)

**Acessibilidade:**
- [ ] Deltas com ícone + texto (↑ +8%, não só ↑)
- [ ] Gráficos com tabela de dados abaixo
- [ ] Cores semânticas (verde = positivo, vermelho = negativo) + ícones

---

### Checklist por Componente

#### Componente: Button

**Estados:**
- [ ] Default: cores corretas por variante (primary/secondary/ghost/danger)
- [ ] Hover: background muda (validar em desktop)
- [ ] Active: `transform: scale(0.98)`
- [ ] Focus: ring 2px MIKE Accent offset 2px
- [ ] Disabled: opacity 40%, cursor not-allowed
- [ ] Loading: spinner + opacity 70%

**Acessibilidade:**
- [ ] Touch target ≥44×44px (mobile)
- [ ] Label descritivo (não "OK", "Enviar")
- [ ] `aria-label` se ícone sozinho
- [ ] `aria-disabled="true"` se disabled

---

#### Componente: Input (Text/Number)

**Estados:**
- [ ] Default: border Border color
- [ ] Focus: border MIKE Core 2px + box-shadow
- [ ] Error: border Error 2px + mensagem abaixo
- [ ] Disabled: opacity 50%, cursor not-allowed
- [ ] Filled: texto bold se dado importante (carga)

**Acessibilidade:**
- [ ] `<label>` associado via `for="inputId"`
- [ ] `aria-describedby` para helper text
- [ ] `aria-invalid="true"` se erro
- [ ] Teclado numérico em inputs number (mobile)

---

#### Componente: Card

**Estados:**
- [ ] Default: border Border color
- [ ] Hover: border MIKE Core + sombra-sm (desktop)
- [ ] Active: `transform: scale(0.99)`

**Layout:**
- [ ] Padding 16px consistente
- [ ] Border-radius 12px
- [ ] Gap entre elementos internos múltiplo de 8px

---

### Checklist de Consistência

#### Tokens

**Cores:**
- [ ] Todas as cores usadas estão no `:root` (CSS variables)
- [ ] Dark mode implementado via `[data-theme="dark"]`
- [ ] Contraste validado em ambos os modos (WCAG AA mínimo)

**Tipografia:**
- [ ] Fontes Inter e Manrope carregadas via Google Fonts
- [ ] Pesos corretos (Inter 400/500/600/700/800, Manrope 700/800)
- [ ] Escala tipográfica seguida (H1–H6, body, small, caption)

**Espaçamento:**
- [ ] Todos os paddings/margins são múltiplos de 8px
- [ ] Grid 8px visível (dev mode) para validar alinhamento

**Raios:**
- [ ] Botões e inputs: 12px
- [ ] Cards: 12px
- [ ] Badges: 4px
- [ ] Modals: 16px

**Sombras:**
- [ ] shadow-sm, shadow-md, shadow-lg consistentes
- [ ] Sombras sutis em dark mode (opacity ajustada)

---

#### Componentes

**Botões:**
- [ ] Altura 48px (mobile), 44px (desktop)
- [ ] Padding 16px horizontal
- [ ] Font-size 16px, weight 600
- [ ] Variantes (primary/secondary/ghost/danger) consistentes

**Inputs:**
- [ ] Altura 48px
- [ ] Padding 12px vertical, 16px horizontal
- [ ] Font-size 16px (evita zoom no iOS)
- [ ] Border-radius 12px

**Cards:**
- [ ] Padding 16px
- [ ] Border 1px Border
- [ ] Border-radius 12px
- [ ] Hover border MIKE Core (desktop)

---

### Definição de Pronto (DoD) Visual/UX

#### Por Feature

- [ ] Design aprovado (Figma/Sketch)
- [ ] Implementação fiel ao design (pixel-perfect em breakpoints principais)
- [ ] Responsivo (mobile/tablet/desktop testados)
- [ ] Dark mode funcional (toggle testado)
- [ ] Acessibilidade validada (Lighthouse score ≥90)
- [ ] Contraste validado (todas as combinações ≥4.5:1)
- [ ] Navegação por teclado funcional
- [ ] Microcopy revisado (tom de voz consistente)
- [ ] Loading states implementados (skeleton ou spinner)
- [ ] Error states implementados (validação + mensagens)
- [ ] Empty states implementados (ícone + texto + CTA)
- [ ] Animações sutis (200–600ms, easing suave)
- [ ] Performance OK (load <2s, interações <100ms)

---

## 15. Apêndice

### Glossário de Termos (Fitness)

| Termo | Definição | Uso no MIKE |
|-------|-----------|-------------|
| **PR** | Personal Record — Recorde pessoal em carga para um exercício | Badge laranja "NOVO PR" ao bater recorde |
| **Reps** | Repetições — Número de vezes que movimento é executado | Input "Reps" em card de set |
| **Set / Série** | Sequência de reps sem pausa | "Set 1", "Set 2", etc. |
| **Carga** | Peso usado no exercício (kg ou lbs) | Input "Carga (kg)" em card de set |
| **Volume** | Total de peso movido (Carga × Reps × Sets) | Métrica em relatórios "Volume Total: 12,480kg" |
| **RPE** | Rate of Perceived Exertion — Escala 1–10 de dificuldade percebida | Campo opcional avançado |
| **RIR** | Reps in Reserve — Quantas reps sobraram no tanque | Campo opcional avançado |
| **Deload** | Redução intencional de carga para recuperação | Badge "Deload" em sets com -10%+ carga |
| **Falha** | Não conseguir completar rep (falha muscular) | Badge "Falha" se reps < planejado |
| **Superset** | 2 exercícios executados consecutivamente sem pausa | Feature futura (v2.0) |

---

### Regras de Expansão Futura (Nutrição e Outras Modalidades)

**Objetivo:** Adicionar módulos de Nutrição, Sono, Medidas Corporais sem quebrar identidade visual.

#### Estratégia de Cores por Módulo

| Módulo | Cor Principal | Cor Accent | Uso |
|--------|---------------|------------|-----|
| **Treino** | MIKE Core `#1E3A8A` | MIKE Accent `#F97316` | Atual |
| **Nutrição** | Success `#10B981` | `#34D399` (verde claro) | Tabs, ícones, gráficos de macros |
| **Sono** | `#8B5CF6` (roxo) | `#A78BFA` (roxo claro) | Tabs, ícones, gráficos de qualidade |
| **Medidas** | Info `#3B82F6` | `#60A5FA` (azul claro) | Tabs, ícones, gráficos de evolução |
| **Cardio** | `#F59E0B` (amarelo) | `#FBBF24` (amarelo claro) | Tabs, ícones, gráficos de pace/distância |

**Princípio:** Cada módulo tem cor primária distinta, mas mantém:
- Tipografia (Inter + Manrope)
- Grid (8px)
- Componentes (botões, inputs, cards)
- Tom de voz (direto, objetivo, factual)

#### Componentes Reutilizáveis

**Cards:**
- Template de card existente (padding 16px, border-radius 12px) serve para qualquer módulo
- Apenas ajustar cor de borda/ícone conforme módulo

**Gráficos:**
- Mesmas regras de linha/barra/distribuição
- Apenas ajustar paleta (verde para macros, roxo para sono, etc.)

**Navegação:**
- Bottom nav expande para 5 itens (Treino, Nutrição, Home, Sono, Perfil)
- Ícones distintos, cores de ativo seguem módulo

---

### Roadmap de Maturidade do Design System

#### v1.0 (Atual — MVP Treino)

**Escopo:**
- Tokens core (cores, tipografia, espaçamento)
- Componentes básicos (botões, inputs, cards, badges, tabs, table)
- Padrões de treino (registro de sets, histórico, relatórios)
- Acessibilidade WCAG AA
- Dark mode

**Gaps conhecidos:**
- Falta biblioteca de ícones customizados (usando Bootstrap Icons)
- Falta animações complexas (apenas micro-animações básicas)
- Falta testes A/B de microcopy

---

#### v1.1 (Q2 2026 — Refinamento)

**Adições:**
- Ícones customizados (set de 40 ícones core do MIKE em SVG)
- Animações de transição entre telas (page transitions)
- Biblioteca de microcopy expandida (200+ mensagens padronizadas)
- Testes A/B de tom de voz (factual vs. motivador)
- Componente de gráfico interativo (zoom, pan)

**Melhorias:**
- Acessibilidade WCAG AAA em componentes críticos
- Performance (skeleton screens em todas as telas)
- Testes com usuários (5 sessões de usability testing)

---

#### v2.0 (Q4 2026 — Expansão Multi-Modal)

**Adições:**
- Módulo de Nutrição (registro de refeições, macros, relatórios)
- Módulo de Sono (registro de horas, qualidade, insights)
- Módulo de Medidas Corporais (peso, BF%, circunferências)
- Componentes novos (date picker, time picker, photo upload)
- Paleta expandida (verde, roxo, amarelo para novos módulos)

**Melhorias:**
- Design system documentado em Storybook
- Componentes em biblioteca React (reutilizáveis entre módulos)
- Testes automatizados de acessibilidade (axe-core)

---

#### v3.0 (2027 — Inteligência e Social)

**Adições:**
- Insights automatizados por IA (análise de padrões, sugestões de treino)
- Features sociais opcionais (compartilhar PRs, desafios com amigos)
- Integração com wearables (Apple Watch, Garmin)
- Modo offline completo (PWA)

**Melhorias:**
- Design system como produto standalone (open source?)
- Suporte a temas customizados (além de light/dark)
- Internacionalização (i18n) completa

---

### Regras de Contribuição ao Design System

**Para designers:**
1. Propor mudança via issue (descrever problema + solução)
2. Validar que mudança não quebra componentes existentes
3. Atualizar manual (Markdown + HTML) antes de marcar como concluído
4. Comunicar mudança em changelog

**Para devs:**
1. Usar tokens (CSS variables) sempre que possível (nunca hardcode cores/fontes)
2. Reutilizar componentes existentes antes de criar novos
3. Validar acessibilidade antes de merge (Lighthouse + testes manuais)
4. Documentar edge cases e limitações

**Para produto:**
1. Priorizar consistência > inovação (exceto se inovação resolve problema real)
2. Testar mudanças com usuários antes de escalar
3. Medir impacto (NPS, retenção, tempo de registro)

---

**FIM DO MANUAL**

---

**Versão:** 1.0  
**Última atualização:** 16 de fevereiro de 2026  
**Próxima revisão:** Q2 2026 (v1.1)  

**Contato:** design@mikeapp.com (fictício)  
**Repositório:** github.com/mikeapp/design-system (fictício)  

---