# README - SkillForge Frontend Agent

## Visão Geral
O **SkillForge Frontend Agent** é um agente especializado no ecossistema de criação, revisão, auditoria e evolução de **Agent Skills** focadas em desenvolvimento front-end, design systems, acessibilidade, performance e direção estética.

Este agente foi projetado para atuar como arquiteto, professor, entrevistador, revisor e gerador de skills prontas para ambientes como LibreChat, Pergunte Aí, Claude, ChatGPT e sistemas alinhados ao padrão **Agent Skills**.

---

## Objetivo do Projeto
Fornecer uma estrutura completa, modular, segura e normalizada para a criação de skills de front-end com altíssima qualidade visual, rigor técnico e total conformidade com acessibilidade, performance e licenças de software.

---

## Estrutura do Repositório (Consolidada)

O repositório é composto exclusivamente por `README.md`, `PROMPT-AGENTE.md` e 5 arquivos consolidados que contêm toda a base de conhecimento, especificações, evals, templates, licenças e ferramentas:

```text
skillforge-frontend-agent/
├── README.md                           # Visão geral e mapa da estrutura consolidada
├── PROMPT-AGENTE.md                    # Prompt de sistema principal pronto para uso
├── 01-VISUAL-DESIGN-AND-UI.md          # Consolidado: Direção estética, tipografia, cores, layout e UI
├── 02-ENGINEERING-AND-PERFORMANCE.md   # Consolidado: Design systems, a11y, performance React/Next e qualidade
├── 03-AUTHORING-TEMPLATES-EVALS.md     # Consolidado: Autoria de skills, templates e suíte de testes (Evals)
├── 04-SOURCES-AND-LICENSES.md          # Consolidado: Registro de procedência, fontes upstream e licenças
└── 05-MANIFEST-AND-TOOLING.md          # Consolidado: Manifesto de upload para IA e utilitários Python
```

---

## Instruções de Manutenção Interna

### 1. Atualização de Fontes
Para sincronizar ou atualizar fontes de referência:
```bash
python3 scripts/sync-sources.py
python3 scripts/validate-sources.py
```

### 2. Validação do Pacote do Agente
Para garantir a integridade da estrutura e validar os arquivos Markdown:
```bash
python3 scripts/validate-agent-package.py
```

### 3. Geração do Manifesto de Upload
Para atualizar o manifesto dos arquivos que devem ser anexados à base do LibreChat:
```bash
python3 scripts/generate-upload-manifest.py
```

---

## Licença e Atribuição
Todo o conteúdo original deste repositório é fornecido em conformidade com as licenças de software dos projetos de referência compilados em `SOURCES.md`. Consulte `knowledge/normalized/security-and-licensing.md` para diretrizes de compliance.
