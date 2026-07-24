# README - SkillForge Frontend Agent

## Visão Geral
O **SkillForge Frontend Agent** é um agente especializado no ecossistema de criação, revisão, auditoria e evolução de **Agent Skills** focadas em desenvolvimento front-end, design systems, acessibilidade, performance e direção estética.

Este agente foi projetado para atuar como arquiteto, professor, entrevistador, revisor e gerador de skills prontas para ambientes como LibreChat, Pergunte Aí, Claude, ChatGPT e sistemas alinhados ao padrão **Agent Skills**.

---

## Objetivo do Projeto
Fornecer uma estrutura completa, modular, segura e normalizada para a criação de skills de front-end com altíssima qualidade visual, rigor técnico e total conformidade com acessibilidade, performance e licenças de software.

---

## Estrutura do Repositório

```text
skillforge-frontend-agent/
├── README.md                          # Visão geral e instruções de manutenção
├── SOURCES.md                         # Registro de procedência, hashes e licenças
├── KNOWLEDGE-INDEX.md                 # Índice e política de recuperação de conhecimento
├── UPLOAD-MANIFEST.md                 # Manifesto de arquivos para LibreChat / Pergunte Aí
├── PROMPT-AGENTE.md                   # Prompt de sistema principal pronto para uso
├── sources/                           # Snapshots e metadados de fontes externas
│   └── upstream/                      # Registros imutáveis por repositório de origem
├── knowledge/                         # Base de conhecimento normalizada
│   ├── normalized/                    # Guias temáticos normalizados em Markdown
│   └── examples/                      # Exemplos de boas e más skills de front-end
├── templates/                         # Modelos padrão de skills
│   └── frontend-skill/                # Template de skill de front-end com SKILL.md
├── evals/                             # Cenários de teste e avaliação do agente
└── scripts/                           # Scripts utilitários em Python para validação
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
