# Normalizado: Arquitetura e Escrita de Skills (Skill Authoring)

> **Fontes Principais:** OpenAI Skill Creator (`openai/skills`), Microsoft Skills (`microsoft/skills`)

## 1. Princípios da Arquitetura Agent Skills
Uma **Agent Skill** é um pacote modular de conhecimento e instruções determinísticas projetado para capacitar agentes de IA a realizarem tarefas específicas com alta precisão e consistência.

### Estrutura do Pacote
```text
minha-skill/
├── SKILL.md                 # Arquivo principal (Obrigatório, < 500 linhas)
├── references/              # Documentos de apoio aprofundados (Opcional)
├── scripts/                 # Utilitários executáveis determinísticos (Opcional)
├── assets/                  # Arquivos estáticos de apoio (Opcional)
└── evals/                   # Suíte de teste e validação (Opcional)
```

---

## 2. Padrão do Arquivo `SKILL.md`

### Frontmatter YAML
O frontmatter é o cartão de visita da skill para o roteador da IA. Deve conter:
```yaml
---
name: minha-skill-de-frontend
description: O que esta skill faz e exatamente quando deve ser ativada (com frases de gatilho).
---
```

* **Nome:** Kebab-case minúsculo, no máximo 64 caracteres, sem espaços ou símbolos especiais.
* **Description:** Deve explicar **o que** a skill faz e **quando** usá-la, incluindo gatilhos chave.

---

## 3. Diretriz do Progressive Disclosure (Divulgação Progressiva)
- Mantenha o `SKILL.md` conciso (foco em menos de 500 linhas).
- Não duplique conteúdo nem crie estruturas profundas de subpastas (`references/guia/subguia/detalhe.md` ❌).
- Mantenha links relativos diretos e rasos para fácil leitura pelo agente.

---

## 4. Critérios de Validação da Skill
- [ ] YAML Frontmatter válido e parseável.
- [ ] `SKILL.md` com extensão `.md` e menos de 500 linhas.
- [ ] Nome da pasta exatamente igual ao `name` no frontmatter.
- [ ] Ausência de segredos ou tokens hardcoded.
