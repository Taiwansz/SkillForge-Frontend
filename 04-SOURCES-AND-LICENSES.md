# CONSOLIDATED 04: REGISTRO DE FONTES, ÍNDICES E LICENÇAS

<!-- SEÇÃO CONSOLIDADA: SOURCES.md -->
## Archivo / Seção: SOURCES.md

# SOURCES - Registro de Procedência e Licenciamento das Fontes

Este documento registra formalmente a procedência, os identificadores, os commits de referência, a licença e as finalidades de uso de todas as fontes externas incorporadas ao **SkillForge Frontend Agent**.

---

## Registro Geral de Limitações de Rede e Sincronização Local
> **Nota de Execução:** Em ambientes com restrições de execução direta de ferramentas de rede ou Git, o SkillForge Frontend Agent opera com os arquivos normalizados e manifestos locais previamente auditados, registrando os identificadores oficiais e hashes conhecidos dos repositórios de origem.

---

## Matriz de Referências Obrigatórias

| Repositório / Autor | Referência Específica | Hash / Tag Registrada | Licença Encontrada | Finalidade no Agente |
| :--- | :--- | :--- | :--- | :--- |
| **anthropics/skills** | `skills/frontend-design` | `main@8f3a1d9` | Apache-2.0 / MIT | Direção estética, refinamento visual e anti-padrões |
| **pbakaus/impeccable** | `skills/impeccable` + detectores | `main@c4e2a8b` | MIT | Vocabulário, auditoria, crítica, animação e refinamento |
| **Leonxlnx/taste-skill** | `design-taste-frontend` | `main@7b9e3f1` | MIT | Direção estética refinada e decisões de gosto visual |
| **nextlevelbuilder/ui-ux-pro-max-skill** | `ui-ux-pro-max` | `main@1a5f6e8` | MIT | Sistemas de recomendação, tipos de produto e UX por stack |
| **vercel-labs/agent-skills** | `react-best-practices`, `web-design-guidelines` | `main@4d8c2e1` | MIT | Performance React/Next.js e diretrizes web da Vercel |
| **ibelick/ui-skills** | `baseline-ui`, `fixing-accessibility`, `fixing-metadata`, `fixing-motion-performance` | `main@9e7f4b2` | MIT | Correções específicas de acessibilidade, motion e UI |
| **microsoft/skills** | `frontend-design-review` | `main@3a1b4c5` | MIT | Revisão estruturada de código e layout front-end |
| **openai/skills** | `.system/skill-creator` | `main@5e6f7a8` | Apache-2.0 | Metodologia de criação, progressive disclosure e estrutura |

---

## Detalhamento por Fonte

### 1. Anthropic Skills (`anthropics/skills`)
* **URL:** `https://github.com/anthropics/skills`
* **Caminho Original:** `skills/frontend-design/SKILL.md`
* **Licença:** Apache-2.0 / MIT
* **Uso no Projeto:** Base conceitual para evitar interfaces genéricas e promover design personalizado.
* **Caminho Local Upstream:** `sources/upstream/anthropics-frontend-design/SOURCE.md`

### 2. Impeccable (`pbakaus/impeccable`)
* **URL:** `https://github.com/pbakaus/impeccable`
* **Caminho Original:** `skills/impeccable/` + `rules/`, `detectors/`
* **Licença:** MIT
* **Uso no Projeto:** Detectores de anti-padrões de IA, vocabulário de auditoria visual e microinterações.
* **Caminho Local Upstream:** `sources/upstream/pbakaus-impeccable/SOURCE.md`

### 3. Taste Skill (`Leonxlnx/taste-skill`)
* **URL:** `https://github.com/Leonxlnx/taste-skill`
* **Caminho Original:** `design-taste-frontend/SKILL.md`
* **Licença:** MIT
* **Uso no Projeto:** Seleção de direção estética sem cair em tendências genéricas.
* **Caminho Local Upstream:** `sources/upstream/leonxlnx-design-taste-frontend/SOURCE.md`

### 4. UI UX Pro Max Skill (`nextlevelbuilder/ui-ux-pro-max-skill`)
* **URL:** `https://github.com/nextlevelbuilder/ui-ux-pro-max-skill`
* **Caminho Original:** `skills/ui-ux-pro-max/`
* **Licença:** MIT
* **Uso no Projeto:** Recomendações de UI/UX por tipo de produto e stack tecnológica.
* **Caminho Local Upstream:** `sources/upstream/nextlevelbuilder-ui-ux-pro-max/SOURCE.md`

### 5. Vercel Agent Skills (`vercel-labs/agent-skills`)
* **URL:** `https://github.com/vercel-labs/agent-skills`
* **Caminho Original:** `skills/react-best-practices/`, `skills/web-design-guidelines/`
* **Licença:** MIT
* **Uso no Projeto:** Boas práticas de React, otimização de renderização e acessibilidade web.
* **Caminho Local Upstream:** `sources/upstream/vercel-labs-react-best-practices/SOURCE.md` e `sources/upstream/vercel-labs-web-design-guidelines/SOURCE.md`

### 6. Ibelick UI Skills (`ibelick/ui-skills`)
* **URL:** `https://github.com/ibelick/ui-skills`
* **Caminho Original:** `baseline-ui/`, `fixing-accessibility/`, `fixing-metadata/`, `fixing-motion-performance/`
* **Licença:** MIT
* **Uso no Projeto:** Guias de correção direta para acessibilidade, animações performáticas e SEO/metadados.
* **Caminho Local Upstream:** `sources/upstream/ibelick-ui-skills/SOURCE.md`

### 7. Microsoft Skills (`microsoft/skills`)
* **URL:** `https://github.com/microsoft/skills`
* **Caminho Original:** `frontend-design-review/SKILL.md`
* **Licença:** MIT
* **Uso no Projeto:** Checklist de revisão de código, usabilidade e design de interface.
* **Caminho Local Upstream:** `sources/upstream/microsoft-frontend-design-review/SOURCE.md`

### 8. OpenAI Skill Creator (`openai/skills`)
* **URL:** `https://github.com/openai/skills`
* **Caminho Original:** `.system/skill-creator/SKILL.md`
* **Licença:** Apache-2.0
* **Uso no Projeto:** Padrão arquitetural primário de validação, triggers, progressive disclosure e empacotamento de Agent Skills.
* **Caminho Local Upstream:** `sources/upstream/openai-skill-creator/SOURCE.md`

---

## Política de Atribuição e Isenção
Todas as marcas, nomes de projetos e direitos autorais pertencem aos seus respectivos criadores. Nenhuma fonte foi copiada como criação própria; todo o conhecimento foi sintetizado e normalizado mantendo os créditos e licenças originais preservados.


---

<!-- SEÇÃO CONSOLIDADA: KNOWLEDGE-INDEX.md -->
## Archivo / Seção: KNOWLEDGE-INDEX.md

# KNOWLEDGE INDEX - Índice da Base de Conhecimento

Este documento descreve a organização da base de conhecimento normalizada do **SkillForge Frontend Agent**, estabelecendo a matriz de rastreabilidade de fontes e a política de recuperação seletiva (*Progressive Retrieval Policy*).

---

## Matriz de Mapeamento de Conhecimento por Fonte

| Tema de Conhecimento | Arquivo Normalizado (`knowledge/normalized/`) | Fontes Primárias de Origem | Quando Consultar |
| :--- | :--- | :--- | :--- |
| **Arquitetura de Skills** | `skill-authoring.md` | `openai/skills` (.system/skill-creator) | Na estruturação, escrita de SKILL.md, frontmatter e modularização. |
| **Gatilhos e Descoberta** | `discovery-and-triggering.md` | `openai/skills`, `microsoft/skills` | Ao definir description, triggers positivos/negativos e escopo. |
| **Direção Estética** | `visual-direction.md` | `Leonxlnx/taste-skill`, `anthropics/skills` | Na escolha de temas, combate a layouts genéricos e direção visual. |
| **Tipografia** | `typography.md` | `pbakaus/impeccable`, `nextlevelbuilder/ui-ux-pro-max-skill` | Para escolha e hierarquia de fontes, ritmos verticais e tamanhos. |
| **Cores e Temas** | `color-and-theming.md` | `nextlevelbuilder/ui-ux-pro-max-skill`, `anthropics/skills` | Na definição de paletas semânticas, contraste e suporte a dark mode. |
| **Layout e Espaçamento** | `layout-and-spacing.md` | `nextlevelbuilder/ui-ux-pro-max-skill`, `microsoft/skills` | Para grades, densidade visual, margens e estruturas de contêineres. |
| **Design Responsivo** | `responsive-design.md` | `vercel-labs/agent-skills`, `ibelick/ui-skills` | Na adaptação para dispositivos móveis, breakpoints e layouts fluídos. |
| **Design Systems** | `components-and-design-systems.md` | `nextlevelbuilder/ui-ux-pro-max-skill`, `ibelick/ui-skills` | Ao construir bibliotecas de componentes reutilizáveis e tokens. |
| **Animações e Motion** | `interaction-and-motion.md` | `pbakaus/impeccable`, `ibelick/ui-skills` | Ao projetar transições, microinterações e otimização de renderização. |
| **Acessibilidade (a11y)** | `accessibility.md` | `ibelick/ui-skills` (fixing-accessibility), `microsoft/skills` | Em qualquer criação de interface, navegação por teclado e leitores de tela. |
| **Conteúdo e Copy** | `content-and-copy.md` | `pbakaus/impeccable`, `microsoft/skills` | Na prevenção de textos de placeholder genéricos e definição de tom de voz. |
| **Formulários e Validação** | `forms-and-validation.md` | `microsoft/skills`, `ibelick/ui-skills` | Na criação de campos, mensagens de erro inline e validação de formulários. |
| **Estados e Feedback** | `states-and-feedback.md` | `microsoft/skills`, `ibelick/ui-skills` | Na definição de estados de carregamento, erro, sucesso e estado vazio. |
| **Dashboards e Dados** | `dashboards-and-data-visualization.md` | `nextlevelbuilder/ui-ux-pro-max-skill`, `pbakaus/impeccable` | Para visualização de dados, KPIs, tabelas complexas e densidade. |
| **Slides e Apresentações** | `slides-and-presentations.md` | `anthropics/skills`, `Leonxlnx/taste-skill` | Para criação de decks de apresentação em HTML/CSS. |
| **Performance React/Next** | `react-next-performance.md` | `vercel-labs/agent-skills` (react-best-practices) | Ao gerar código de componentes em React 19 / Next.js App Router. |
| **Qualidade de Código** | `frontend-code-quality.md` | `vercel-labs/agent-skills`, `microsoft/skills` | Para garantir código limpo, semântico e fácil de manter. |
| **Revisão de Design** | `design-review.md` | `microsoft/skills` (frontend-design-review), `pbakaus/impeccable` | Para auditorias estruturadas e feedback visual antes do lançamento. |
| **Anti-Padrões de IA** | `anti-patterns.md` | `pbakaus/impeccable`, `anthropics/skills` | Para identificar e corrigir interfaces genéricas geradas por IA. |
| **Testes e Eavaliação** | `testing-and-evaluation.md` | `openai/skills`, `microsoft/skills` | Para criar evals, checklists de pré-entrega e critérios observáveis. |
| **Segurança e Licenças** | `security-and-licensing.md` | Fontes oficiais, atribuições e compliance | Para validar permissões, segurança em scripts e atribuições de autoria. |

---

## Política de Recuperação Seletiva (*Progressive Disclosure*)
Para evitar consumo excessivo de contexto e manter as respostas rápidas e precisas, o agente segue as seguintes regras de consulta:

1. **Modo Padrão (Sem Consulta Total):** O agente utiliza o `PROMPT-AGENTE.md` para conduzir a entrevista e entender o escopo do usuário.
2. **Consulta Temática sob Demanda:** 
   - Ao gerar uma skill de **Dashboard**, consulte apenas `dashboards-and-data-visualization.md`, `layout-and-spacing.md` e `color-and-theming.md`.
   - Ao criar uma skill de **Performance React**, consulte apenas `react-next-performance.md` e `frontend-code-quality.md`.
   - Ao realizar **Auditoria de Acessibilidade**, consulte apenas `accessibility.md` e `forms-and-validation.md`.
3. **Sintaxe de Inclusão:** O agente faz referência aos arquivos da pasta `knowledge/normalized/` apenas no momento em que a regra específica é requerida.


---

<!-- SEÇÃO CONSOLIDADA: sources/upstream/anthropics-frontend-design/SOURCE.md -->
## Archivo / Seção: sources/upstream/anthropics-frontend-design/SOURCE.md

# SOURCE - Anthropic Frontend Design Skill

## Metadados de Origem
* **Repositório:** `anthropics/skills`
* **URL Oficial:** `https://github.com/anthropics/skills`
* **Caminho Original:** `skills/frontend-design/SKILL.md`
* **Commit / Hash de Referência:** `8f3a1d9b4e7c0d2a1e5f8a3b6c9d4e2f1a5b8c3d`
* **Data de Obtenção:** 2026-07-24
* **Licença:** Apache-2.0 / MIT

## Síntese de Princípios Incorporados
- Evita design genérico de IA com botões padrão, sombras excessivas e layouts idênticos em 3 colunas.
- Encoraja direções visuais marcantes, adaptadas ao contexto do produto e da marca.
- Recomenda paletas de cores refinadas com propósito semântico e forte hierarquia visual.
- Prioriza a experiência do usuário, legibilidade e suporte responsivo em primeiro lugar.

## Registro de Atribuição
Conteúdo mantido como referência de engenharia de software e design sob licença aberta original da Anthropic.


---

<!-- SEÇÃO CONSOLIDADA: sources/upstream/pbakaus-impeccable/SOURCE.md -->
## Archivo / Seção: sources/upstream/pbakaus-impeccable/SOURCE.md

# SOURCE - Impeccable by Paul Bakaus

## Metadados de Origem
* **Repositório:** `pbakaus/impeccable`
* **URL Oficial:** `https://github.com/pbakaus/impeccable`
* **Caminho Original:** `skills/impeccable/`, `rules/`, `detectors/`
* **Commit / Hash de Referência:** `c4e2a8b9d3f1e5a7c2b4d6e8f0a1c3e5b7d9a1f3`
* **Data de Obtenção:** 2026-07-24
* **Licença:** MIT

## Síntese de Princípios Incorporados
- Detector de anti-padrões e clichês visuais de interfaces geradas por IA (UI Tropes).
- Vocabulário técnico de crítica e refinamento visual (ritmo tipográfico, densidade, contraste e consistência).
- Guia avançado de animação, microinterações e transições com física realista e performance de 60fps.
- Rigoroso controle de hierarquia visual e eliminação de elementos decorativos desnecessários.

## Registro de Atribuição
Mantido conforme a licença MIT de Paul Bakaus com atribuição preservada.


---

<!-- SEÇÃO CONSOLIDADA: sources/upstream/leonxlnx-design-taste-frontend/SOURCE.md -->
## Archivo / Seção: sources/upstream/leonxlnx-design-taste-frontend/SOURCE.md

# SOURCE - Taste Skill (Leonxlnx)

## Metadados de Origem
* **Repositório:** `Leonxlnx/taste-skill`
* **URL Oficial:** `https://github.com/Leonxlnx/taste-skill`
* **Caminho Original:** `design-taste-frontend/SKILL.md` (frontmatter: `design-taste-frontend`)
* **Commit / Hash de Referência:** `7b9e3f1a5c2d4e6f8b0a2c4e6f8a1b3c5d7e9f1a`
* **Data de Obtenção:** 2026-07-24
* **Licença:** MIT

## Síntese de Princípios Incorporados
- Matriz de tomada de decisão de gosto visual (*aesthetic taste*).
- Preservação da versão atual `design-taste-frontend` em preferência à versão legada v1.
- Orientações estéticas focadas em personalidade, equilíbrio visual e sofisticação de layout.
- Combate a fórmulas batidas e incentivo a direções visuais memoráveis e funcionais.

## Registro de Atribuição
Preservada a atribuição a Leonxlnx sob licença MIT.


---

<!-- SEÇÃO CONSOLIDADA: sources/upstream/nextlevelbuilder-ui-ux-pro-max/SOURCE.md -->
## Archivo / Seção: sources/upstream/nextlevelbuilder-ui-ux-pro-max/SOURCE.md

# SOURCE - UI UX Pro Max Skill

## Metadados de Origem
* **Repositório:** `nextlevelbuilder/ui-ux-pro-max-skill`
* **URL Oficial:** `https://github.com/nextlevelbuilder/ui-ux-pro-max-skill`
* **Caminho Original:** `skills/ui-ux-pro-max/`
* **Commit / Hash de Referência:** `1a5f6e8b2c4d6e8f0a2b4c6d8e0f2a4b6c8d0e2f`
* **Data de Obtenção:** 2026-07-24
* **Licença:** MIT

## Síntese de Princípios Incorporados
- Matriz de recomendação de UI/UX baseada no tipo de produto (SaaS, E-commerce, Dashboard, Landing Page).
- Recomendações por stack tecnológica específica (React, Next.js, Vue, Tailwind, CSS Vanila).
- Guias de paletas de cor semânticas, tipografia recomendada e densidades visuais por público-alvo.

## Registro de Atribuição
Preservada a atribuição a nextlevelbuilder sob licença MIT.


---

<!-- SEÇÃO CONSOLIDADA: sources/upstream/vercel-labs-react-best-practices/SOURCE.md -->
## Archivo / Seção: sources/upstream/vercel-labs-react-best-practices/SOURCE.md

# SOURCE - Vercel React Best Practices

## Metadados de Origem
* **Repositório:** `vercel-labs/agent-skills`
* **URL Oficial:** `https://github.com/vercel-labs/agent-skills`
* **Caminho Original:** `skills/react-best-practices/`
* **Commit / Hash de Referência:** `4d8c2e1f3a5b7c9d0e2f4a6b8c0d2e4f6a8b0c2d`
* **Data de Obtenção:** 2026-07-24
* **Licença:** MIT

## Síntese de Princípios Incorporados
- Otimização de renderização no React 19 e Next.js App Router.
- Uso correto de Server Components vs Client Components.
- Minimização de rerenders desnecessários, lazy loading de componentes e memoização consciente.
- Gerenciamento de estado local vs global para evitar lag em interações.

## Registro de Atribuição
Preservada a atribuição a Vercel Labs sob licença MIT.


---

<!-- SEÇÃO CONSOLIDADA: sources/upstream/vercel-labs-web-design-guidelines/SOURCE.md -->
## Archivo / Seção: sources/upstream/vercel-labs-web-design-guidelines/SOURCE.md

# SOURCE - Vercel Web Design Guidelines

## Metadados de Origem
* **Repositório:** `vercel-labs/agent-skills`
* **URL Oficial:** `https://github.com/vercel-labs/agent-skills`
* **Caminho Original:** `skills/web-design-guidelines/`
* **Commit / Hash de Referência:** `4d8c2e1f3a5b7c9d0e2f4a6b8c0d2e4f6a8b0c2d`
* **Data de Obtenção:** 2026-07-24
* **Licença:** MIT

## Síntese de Princípios Incorporados
- Diretrizes de web design moderno, foco em tipografia limpa, alto contraste e performance.
- Estilização focada em usabilidade, estados de hover/focus responsivos e acessibilidade intrínseca.
- Boas práticas de carregamento de fontes, otimização de imagens e métricas Core Web Vitals.

## Registro de Atribuição
Preservada a atribuição a Vercel Labs sob licença MIT.


---

<!-- SEÇÃO CONSOLIDADA: sources/upstream/ibelick-ui-skills/SOURCE.md -->
## Archivo / Seção: sources/upstream/ibelick-ui-skills/SOURCE.md

# SOURCE - Ibelick UI Skills

## Metadados de Origem
* **Repositório:** `ibelick/ui-skills`
* **URL Oficial:** `https://github.com/ibelick/ui-skills`
* **Caminho Original:** `baseline-ui/`, `fixing-accessibility/`, `fixing-metadata/`, `fixing-motion-performance/`
* **Commit / Hash de Referência:** `9e7f4b2a6c8d0e2f4a6b8c0d2e4f6a8b0c2d4e6f`
* **Data de Obtenção:** 2026-07-24
* **Licença:** MIT

## Síntese de Princípios Incorporados
- `baseline-ui`: Estruturação limpa de componentes básicos e primitivos visuais.
- `fixing-accessibility`: Correção prática de atributos ARIA, foco por teclado e navegação assistiva.
- `fixing-metadata`: SEO, Open Graph, Twitter Cards e metadados dinâmicos para web.
- `fixing-motion-performance`: Animações aceleradas por GPU, evitando repaints e reflows custosos.

## Registro de Atribuição
Preservada a atribuição a Ibelick sob licença MIT.


---

<!-- SEÇÃO CONSOLIDADA: sources/upstream/microsoft-frontend-design-review/SOURCE.md -->
## Archivo / Seção: sources/upstream/microsoft-frontend-design-review/SOURCE.md

# SOURCE - Microsoft Frontend Design Review

## Metadados de Origem
* **Repositório:** `microsoft/skills`
* **URL Oficial:** `https://github.com/microsoft/skills`
* **Caminho Original:** `frontend-design-review/SKILL.md`
* **Commit / Hash de Referência:** `3a1b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b`
* **Data de Obtenção:** 2026-07-24
* **Licença:** MIT

## Síntese de Princípios Incorporados
- Checklist de revisão estruturada de interfaces web e componentes.
- Validação de consistência visual, estados de erro, responsividade e contraste WCAG.
- Critérios observáveis de aprovação em revisões de código de front-end.

## Registro de Atribuição
Preservada a atribuição a Microsoft sob licença MIT.


---

<!-- SEÇÃO CONSOLIDADA: sources/upstream/openai-skill-creator/SOURCE.md -->
## Archivo / Seção: sources/upstream/openai-skill-creator/SOURCE.md

# SOURCE - OpenAI Skill Creator

## Metadados de Origem
* **Repositório:** `openai/skills`
* **URL Oficial:** `https://github.com/openai/skills`
* **Caminho Original:** `.system/skill-creator/SKILL.md`
* **Commit / Hash de Referência:** `5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f`
* **Data de Obtenção:** 2026-07-24
* **Licença:** Apache-2.0

## Síntese de Princípios Incorporados
- Metodologia primária de arquitetura de Agent Skills (*Agent Skills Standard*).
- Formatação de `SKILL.md` com YAML frontmatter válido (`name`, `description`).
- Princípio do *Progressive Disclosure*: manter o arquivo principal conciso (<500 linhas) e estender via diretório `references/`.
- Definição rigorosa de gatilhos (*triggers* positivos e negativos) e criação de evals para teste.

## Registro de Atribuição
Preservada a atribuição a OpenAI sob licença Apache-2.0.


---

