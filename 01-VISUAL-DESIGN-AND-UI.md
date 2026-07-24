# CONSOLIDADO 01: VISUAL DESIGN, UI E DIREÇÃO ESTÉTICA

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/visual-direction.md -->
## Archivo / Seção: knowledge/normalized/visual-direction.md

# Normalizado: Direção Estética e Identidade Visual (Visual Direction)

> **Fontes Principais:** Taste Skill (`Leonxlnx/taste-skill`), Anthropic Skills (`anthropics/skills`), Impeccable (`pbakaus/impeccable`)

## 1. Princípios de Direção Estética
A estética de uma interface deve ser uma escolha consciente baseada no tipo de produto, no público-alvo e na mensagem da marca. A IA deve evitar impor automaticamente o mesmo estilo genérico (modo escuro de baixo contraste com gradientes roxos).

---

## 2. Catálogo de Estilos Visuais

### Minimalismo Editorial
- **Características:** Foco em leitura, grandes títulos com fontes serifadas ou sans-serif clássicas, bastante espaço em branco, paleta monocromática com uma cor de destaque forte.
- **Uso Recomendado:** Blogs de conteúdo, portfólios, sites de notícias, marcas de moda.

### Luxo Refinado
- **Características:** Cores sóbrias (marrom profundo, creme, dourado opaco, preto), linhas finas, espaçamento generoso, animações lentas e elegantes.
- **Uso Recomendado:** Arquitetura, alta gastronomia, finanças pessoais *premium*, imobiliárias de alto padrão.

### Brutalismo Funcional / Industrial
- **Características:** Bordas pretas marcadas, fundos de alto contraste, tipografia monoespaçada, elementos visíveis e utilitários.
- **Uso Recomendado:** Ferramentas para desenvolvedores, dashboards operacionais, plataformas de trading.

### Corporativo Contemporâneo
- **Características:** Azul marinho, cinza neutro e branco; layout limpo, cartões estruturados sem excessos, hierarquia clara.
- **Uso Recomendado:** SaaS B2B, bancos corporativos, plataformas de RH.

---

## 3. Combate a Clichês de IA
- Substitua cartões desnecessários por alinhamento e hierarquia tipográfica.
- Evite fundos com gradientes genéricos sem relação com a marca.
- Garanta que cada elemento na tela cumpra uma função clara.


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/typography.md -->
## Archivo / Seção: knowledge/normalized/typography.md

# Normalizado: Tipografia e Hierarquia Vertical (Typography)

> **Fontes Principais:** Impeccable (`pbakaus/impeccable`), UI UX Pro Max (`nextlevelbuilder/ui-ux-pro-max-skill`)

## 1. Princípios de Tipografia Front-end
A tipografia representa mais de 80% do design de interface na web. Uma boa hierarquia garante escaneabilidade e reduz o cansaço visual.

---

## 2. Escalas Tipográficas Recomendadas

```css
/* Escala de Tipo Modular recomendada (Rácio 1.25 - Major Third) */
--text-xs: 0.75rem;   /* 12px - Legendas secundárias */
--text-sm: 0.875rem;  /* 14px - Textos auxiliares e dados */
--text-base: 1rem;    /* 16px - Corpo de texto padrão */
--text-lg: 1.125rem;  /* 18px - Subtítulos pequenos */
--text-xl: 1.25rem;   /* 20px - Títulos de cartões */
--text-2xl: 1.5rem;   /* 24px - Títulos de seção */
--text-3xl: 1.875rem; /* 30px - Títulos de página */
--text-4xl: 2.25rem;  /* 36px - Destaques / Decks */
```

---

## 3. Emparelhamento de Fontes (*Font Pairing*)
- **Moderna / Tecnológica:** Inter + JetBrains Mono
- **Editorial / Elegante:** Playfair Display + Inter
- **Corporativa / Robusta:** Roboto / Open Sans + Fira Code
- **Industrial / Utilitária:** Space Grotesk + Space Mono

---

## 4. Regras de Ouro
1. **Comprimento de Linha (*Measure*):** Limite parágrafos entre 45 e 75 caracteres por linha para leitura ideal.
2. **Altura de Linha (*Line Height*):** 
   - Títulos grandes (`h1`, `h2`): `1.1` a `1.2`.
   - Corpo de texto: `1.5` a `1.6`.
3. **Contraste Mínimo:** Atender WCAG AA (mínimo `4.5:1` para texto normal e `3:1` para texto grande).


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/color-and-theming.md -->
## Archivo / Seção: knowledge/normalized/color-and-theming.md

# Normalizado: Cores, Temas e Paletas Semânticas (Color & Theming)

> **Fontes Principais:** UI UX Pro Max (`nextlevelbuilder/ui-ux-pro-max-skill`), Anthropic Skills (`anthropics/skills`)

## 1. Arquitetura Semântica de Cores
Evite definir cores no CSS usando nomes brutos como `blue-500` diretamente nos componentes. Utilize **tokens semânticos**:

```css
:root {
  /* Cores Básicas da Marca */
  --brand-primary: #0f172a;
  --brand-accent: #2563eb;

  /* Cores Semânticas de Superfície */
  --bg-page: #f8fafc;
  --bg-surface: #ffffff;
  --bg-muted: #f1f5f9;

  /* Cores de Texto */
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #94a3b8;

  /* Cores de Estado */
  --status-success: #16a34a;
  --status-warning: #d97706;
  --status-error: #dc2626;
  --status-info: #0284c7;
}

/* Suporte Automático a Dark Mode */
@media (prefers-color-scheme: dark) {
  :root {
    --bg-page: #090d16;
    --bg-surface: #1e293b;
    --bg-muted: #334155;
    --text-primary: #f8fafc;
    --text-secondary: #cbd5e1;
    --text-muted: #64748b;
  }
}
```

---

## 2. Proporção da Regra 60-30-10
- **60% Cor Dominante:** Fundos de página e superfícies neutras.
- **30% Cor Secundária:** Cartões, menus, estrutura de suporte e divisores.
- **10% Cor de Destaque (*Accent*):** Botões de ação primária (CTA), indicadores ativos e elementos focais.

---

## 3. Diretrizes de Contraste e Acessibilidade
- Verifique se a combinação de texto e fundo possui taxa de contraste conforme WCAG 2.1 AA (`4.5:1` para texto padrão).
- Nunca transmita informação **apenas através da cor**; adicione ícone, texto ou padrão visual auxiliar.


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/layout-and-spacing.md -->
## Archivo / Seção: knowledge/normalized/layout-and-spacing.md

# Normalizado: Layout, Grades e Espaçamento (Layout & Spacing)

> **Fontes Principais:** UI UX Pro Max (`nextlevelbuilder/ui-ux-pro-max-skill`), Microsoft Skills (`microsoft/skills`)

## 1. Sistema de Grade de 8px (8pt Grid System)
Todos os espaçamentos, margens, paddings e dimensões devem ser múltiplos de **8px** (ou 4px para micro-ajustes):

```css
--space-1: 0.25rem; /* 4px */
--space-2: 0.5rem;  /* 8px */
--space-3: 0.75rem; /* 12px */
--space-4: 1rem;    /* 16px */
--space-6: 1.5rem;  /* 24px */
--space-8: 2rem;    /* 32px */
--space-12: 3rem;   /* 48px */
--space-16: 4rem;   /* 64px */
```

---

## 2. Padrões de Layout

### CSS Grid para Aplicações e Dashboards
Utilize CSS Grid para estruturas de colunas com comportamento previsível:
```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-6);
}
```

### Flexbox para Alinhamento de Componentes
Utilize Flexbox para itens unidimensionais (barras de navegação, cabeçalhos, listas de ações):
```css
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
}
```

---

## 3. Densidade Visual por Tipo de Aplicação
- **Alta Densidade (Sistemas de Operação, Trading, Analytics):** Padding `8px` a `12px`, fontes `12px` a `14px`, linhas compactas.
- **Média Densidade (SaaS B2B, Gerenciadores de Tarefas):** Padding `16px`, fontes `14px` a `16px`.
- **Baixa Densidade / Editorial (Landing Pages, Consumo):** Padding `24px` a `48px`, tipografia grande, amplo espaço negativo.


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/responsive-design.md -->
## Archivo / Seção: knowledge/normalized/responsive-design.md

# Normalizado: Design Responsivo e Dispositivos (Responsive Design)

> **Fontes Principais:** Vercel Agent Skills (`vercel-labs/agent-skills`), Ibelick UI Skills (`ibelick/ui-skills`)

## 1. Abordagem Mobile-First
Desenvolva a estrutura CSS pensando primeiramente na tela mobile menor e expanda progressivamente usando media queries min-width.

```css
/* Estilo Base: Mobile (< 640px) */
.container {
  padding: 1rem;
  width: 100%;
}

/* Tablet (>= 640px) */
@media (min-width: 640px) {
  .container {
    padding: 1.5rem;
  }
}

/* Desktop (>= 1024px) */
@media (min-width: 1024px) {
  .container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 2rem;
  }
}
```

---

## 2. Breakpoints Canônicos
- **sm:** `640px` (Smartphones em modo paisagem / tablets pequenos)
- **md:** `768px` (Tablets / telas pequenas)
- **lg:** `1024px` (Laptops e desktops padrão)
- **xl:** `1280px` (Monitores de alta resolução)
- **2xl:** `1536px` (Telas ultra-wide)

---

## 3. Diretrizes Práticas de Adaptabilidade
- Evite larguras fixas em pixels (`width: 500px` ❌); prefira `max-width: 100%` ou porcentagens/rem.
- Em telas touch (mobiles/tablets), garanta que áreas clicáveis tenham no mínimo **44x44px**.
- Substitua tabelas complexas por cartões sanfonados ou scroll horizontal controlado em dispositivos móveis.


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/interaction-and-motion.md -->
## Archivo / Seção: knowledge/normalized/interaction-and-motion.md

# Normalizado: Animação e Microinterações (Interaction & Motion)

> **Fontes Principais:** Impeccable (`pbakaus/impeccable`), Ibelick UI Skills (`ibelick/ui-skills`)

## 1. Princípios de Animação Performática
Animações na web devem ser rápidas, intencionais e aceleradas por GPU.

### Propriedades Seguras (Aceleração por GPU)
- ✅ `transform` (`translate3d`, `scale`, `rotate`)
- ✅ `opacity`

### Propriedades Perigosas (Causam Layout Thrashing / Reflow)
- ❌ `width`, `height`, `margin`, `padding`
- ❌ `top`, `left`, `right`, `bottom`

---

## 2. Durabilidade e Curvas de Transição (*Easings*)
- **Microinterações rápidas (Hover em botões, seleção):** `150ms` a `200ms` (`ease-out`).
- **Transições de modal e gavetas:** `250ms` a `300ms` (`cubic-bezier(0.16, 1, 0.3, 1)`).
- **Animações decorativas ou entrada de página:** `300ms` a `400ms`.

---

## 3. Respeito às Preferências do Usuário (Reduced Motion)
Sempre inclua suporte para usuários que desativaram animações no sistema operacional:

```css
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/content-and-copy.md -->
## Archivo / Seção: knowledge/normalized/content-and-copy.md

# Normalizado: UX Writing e Conteúdo (Content & Copy)

> **Fontes Principais:** Impeccable (`pbakaus/impeccable`), Microsoft Skills (`microsoft/skills`)

## 1. Eliminação de Textos Genéricos e Placeholders
- ❌ Evite: *"Lorem ipsum dolor sit amet"*, *"Texto de exemplo vai aqui"*, *"Botão 1"*.
- ✅ Utilize: Textos realistas contextualizados com o produto (ex: *"Relatório Financeiro Q3"*, *"Confirmar Transferência de R$ 500,00"*).

---

## 2. Princípios de UX Writing
1. **Clareza e Concisão:** Vá direto ao ponto, sem ambiguidades.
2. **Orientado à Ação (CTA Clear):** Em botões, declare exatamente o resultado da ação (*"Criar Conta Grátis"* em vez de *"Enviar"*).
3. **Erros Construtivos:** Explique o que aconteceu e como resolver (*"A senha deve conter no mínimo 8 caracteres"* em vez de *"Entrada inválida"*).


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/forms-and-validation.md -->
## Archivo / Seção: knowledge/normalized/forms-and-validation.md

# Normalizado: Formulários e Validação (Forms & Validation)

> **Fontes Principais:** Microsoft Skills (`microsoft/skills`), Ibelick UI Skills (`ibelick/ui-skills`)

## 1. Estrutura Padrão de Campo de Formulário
Cada campo interativo deve conter rótulo claro, indicação de obrigatoriedade, campo de entrada e área dedicada para erro inline:

```html
<div class="form-group">
  <label for="email-input" class="form-label">
    E-mail profissional <span class="required" aria-hidden="true">*</span>
  </label>
  <input 
    type="email" 
    id="email-input" 
    name="email" 
    class="form-input" 
    placeholder="nome@empresa.com"
    required
    aria-invalid="false"
    aria-describedby="email-error"
  />
  <span id="email-error" class="form-error-message" role="alert"></span>
</div>
```

---

## 2. Validação Inline vs Ao Submeter
- **Ao Digitar (Debounced):** Valide regras simples de formato (e-mail, formato de telefone) após o usuário pausar a digitação.
- **Ao Perder Foco (*On Blur*):** Ideal para verificar campos obrigatórios preenchidos.
- **Ao Submeter (*On Submit*):** Dispare validação completa e posicione o foco automático no primeiro campo com erro.


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/states-and-feedback.md -->
## Archivo / Seção: knowledge/normalized/states-and-feedback.md

# Normalizado: Estados de UI e Feedback (States & Feedback)

> **Fontes Principais:** Microsoft Skills (`microsoft/skills`), Ibelick UI Skills (`ibelick/ui-skills`)

## 1. Os 5 Estados Obrigatórios de uma UI
Toda tela ou componente assíncrono deve contemplar explicitamente os 5 estados:

1. **Estado Inicial / Vazio (*Empty State*):** Exibido antes de haver dados. Deve explicar o motivo e oferecer um CTA claro (*"Nenhum relatório encontrado. Criar primeiro relatório"*).
2. **Estado de Carregamento (*Loading State*):** Prefira *Skeletons* (estruturas fantasma) em vez de spinners centralizados para manter a percepção de velocidade.
3. **Estado de Sucesso (*Success State*):** Feedback visual claro de que a ação foi concluída.
4. **Estado de Erro (*Error State*):** Mensagem amigável com opção de tentar novamente (*Retry button*).
5. **Estado Parcial / Paginado (*Partial State*):** Exibição de dados parciais durante o carregamento de mais itens.


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/dashboards-and-data-visualization.md -->
## Archivo / Seção: knowledge/normalized/dashboards-and-data-visualization.md

# Normalizado: Dashboards e Visualização de Dados (Dashboards & Data Viz)

> **Fontes Principais:** UI UX Pro Max (`nextlevelbuilder/ui-ux-pro-max-skill`), Impeccable (`pbakaus/impeccable`)

## 1. Princípios de Hierarquia de Informação em Dashboards
- **Topo (Nível 1 - KPIs Principais):** Números consolidados, métricas de saúde do negócio com indicação de variação (ex: `+12.4% vs mês anterior`).
- **Meio (Nível 2 - Tendências e Gráficos):** Gráficos de linha ou barras mostrando a evolução ao longo do tempo.
- **Base (Nível 3 - Detalhamento e Tabelas):** Tabela operacional com filtros, paginação e busca.

---

## 2. Escolha Correta de Tipos de Gráficos
- **Evolução Temporal:** Gráfico de Linha ou Área (`Recharts`, `Chart.js`).
- **Comparação de Categorias:** Gráfico de Barras Horizontais ou Verticais.
- **Composição / Proporção (Com poucas categorias < 5):** Gráfico de Rosca (*Donut Chart*). Evite gráficos de pizza com muitas fatias.
- **Distribuição de Status:** Badges e barras de progresso agrupadas.

---

## 3. Combate ao "Efeito Árvore de Natal"
- Evite usar uma cor diferente para cada barra ou cartão.
- Mantenha os gráficos com cores neutras (cinza/azul) e reserve cores vivas apenas para alertas (verde/vermelho/amarelo).


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/slides-and-presentations.md -->
## Archivo / Seção: knowledge/normalized/slides-and-presentations.md

# Normalizado: Apresentações e Slides em HTML/CSS (Slides & Presentations)

> **Fontes Principais:** Anthropic Skills (`anthropics/skills`), Taste Skill (`Leonxlnx/taste-skill`)

## 1. Princípios de Slides em Web
Apresentações baseadas em HTML/CSS/JS permitem animações fluídas, interatividade real e responsividade nativa sem depender de softwares proprietários.

---

## 2. Estrutura Padrão de Slide Deck (Aspect Ratio 16:9)

```html
<div class="slide-deck">
  <section class="slide current">
    <span class="slide-number">01 / 10</span>
    <h1 class="slide-title">Visão Estratégica Q3</h1>
    <p class="slide-subtitle">Transformação Digital e Arquitetura Front-end</p>
  </section>
</div>

<style>
.slide-deck {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  position: relative;
  background: var(--bg-page);
}
.slide {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4rem;
  box-sizing: border-box;
}
</style>
```

---

## 3. Navegação e Atalhos por Teclado
- Seta para Direita / Espaço: Próximo slide.
- Seta para Esquerda: Slide anterior.
- Tecla `F`: Ativar modo Tela Cheia (*Fullscreen API*).


---

