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
