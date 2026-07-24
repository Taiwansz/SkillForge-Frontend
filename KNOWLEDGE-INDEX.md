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
