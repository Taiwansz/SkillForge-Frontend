# UPLOAD MANIFEST - Guia de Anexo para LibreChat / Pergunte Aí

Este manifesto define rigorosamente quais arquivos do **SkillForge Frontend Agent** devem e não devem ser anexados à base de conhecimento da plataforma de IA (LibreChat, Pergunte Aí, Claude Project, etc.).

---

## 1. Obrigatório no Prompt do Agente (System Prompt)
*Estes arquivos devem ser colados diretamente no campo de Prompt de Sistema do Agente:*

| Arquivo | Descrição / Instrução |
| :--- | :--- |
| `PROMPT-AGENTE.md` | Conteúdo completo do prompt de sistema. Define a identidade, fluxos de trabalho, modos de entrevista e formato de saída. |

---

## 2. Obrigatórios na Base de Conhecimento (Knowledge Base / RAG)
*Estes arquivos devem ser anexados à base de conhecimento (arquivos de busca/vetor do agente):*

| Arquivo | Função no RAG |
| :--- | :--- |
| `KNOWLEDGE-INDEX.md` | Índice geral e mapa de recuperação de arquivos. |
| `SOURCES.md` | Registro de procedência e licenças para auditoria. |
| `README.md` | Visão geral do repositório. |
| `knowledge/normalized/skill-authoring.md` | Arquitetura e escrita de skills. |
| `knowledge/normalized/discovery-and-triggering.md` | Gatilhos e descrição. |
| `knowledge/normalized/visual-direction.md` | Direção estética e combate ao genérico. |
| `knowledge/normalized/typography.md` | Tipografia e hierarquia. |
| `knowledge/normalized/color-and-theming.md` | Cores, contraste e temas. |
| `knowledge/normalized/layout-and-spacing.md` | Grades e espaçamentos. |
| `knowledge/normalized/responsive-design.md` | Responsividade e mobile. |
| `knowledge/normalized/components-and-design-systems.md` | Componentes e tokens. |
| `knowledge/normalized/interaction-and-motion.md` | Animações e microinterações. |
| `knowledge/normalized/accessibility.md` | Diretrizes de acessibilidade (a11y). |
| `knowledge/normalized/content-and-copy.md` | UX writing e combate a placeholders. |
| `knowledge/normalized/forms-and-validation.md` | Formulários e validações. |
| `knowledge/normalized/states-and-feedback.md` | Estados de UI e feedback. |
| `knowledge/normalized/dashboards-and-data-visualization.md` | Dashboards e gráficos. |
| `knowledge/normalized/slides-and-presentations.md` | Apresentações e slides em HTML. |
| `knowledge/normalized/react-next-performance.md` | Boas práticas de React / Next.js. |
| `knowledge/normalized/frontend-code-quality.md` | Qualidade de código front-end. |
| `knowledge/normalized/design-review.md` | Checklists de auditoria visual. |
| `knowledge/normalized/anti-patterns.md` | Guia de eliminação de anti-padrões. |
| `knowledge/normalized/testing-and-evaluation.md` | Evals e testes de skills. |
| `knowledge/normalized/security-and-licensing.md` | Segurança e licenças. |
| `templates/frontend-skill/SKILL.md` | Modelo de referência de skill. |

---

## 3. Opcionais na Base de Conhecimento
*Podem ser anexados para fornecer mais exemplos práticos se a plataforma permitir mais arquivos:*

| Arquivo | Função |
| :--- | :--- |
| `knowledge/examples/good-frontend-skill-example.md` | Exemplo de skill bem construída. |
| `knowledge/examples/bad-frontend-skill-example.md` | Exemplo de skill com falhas para contraste. |

---

## 4. Somente Manutenção (NÃO Anexar ao RAG)
*Estes arquivos servem para desenvolvimento local, validação e execução de testes:*

| Caminho | Motivo para NÃO Anexar |
| :--- | :--- |
| `evals/*.md` | Suíte de testes local do agente; gastaria contexto desnecessário. |
| `scripts/*.py` | Ferramentas de validação em Python; não contêm conhecimento conceitual. |

---

## 5. ESTRITAMENTE PROIBIDO ANEXAR (Não Upload)
*Nunca envie os itens abaixo para a plataforma de IA:*

* ❌ `sources/upstream/*` (Snapshots brutos e repositórios externos clonados).
* ❌ `.git/`, `.github/`, `.gitignore`
* ❌ `node_modules/`, `__pycache__/`, `.venv/`
* ❌ Chaves API, arquivos `.env`, segredos ou tokens.
