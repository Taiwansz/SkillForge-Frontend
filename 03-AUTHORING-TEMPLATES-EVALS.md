# CONSOLIDADO 03: AUTORIA DE SKILLS, TEMPLATES E EVALS

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/skill-authoring.md -->
## Archivo / Seção: knowledge/normalized/skill-authoring.md

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


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/discovery-and-triggering.md -->
## Archivo / Seção: knowledge/normalized/discovery-and-triggering.md

# Normalizado: Descoberta e Gatilhos (Discovery and Triggering)

> **Fontes Principais:** OpenAI Skill Creator (`openai/skills`), Microsoft Skills (`microsoft/skills`)

## 1. Princípios de Ativação Seletiva
Uma skill só deve ser ativada quando o pedido do usuário corresponder explicitamente ao seu escopo. Ativações falsas-positivas degradam o desempenho e consomem contexto desnecessariamente.

---

## 2. Definindo Gatilhos Positivos e Negativos

### Gatilhos Positivos (Quando Ativar)
São palavras-chave, intenções e frases típicas do usuário:
- Exemplo para Dashboard: *"Crie um painel de controle financeiro com gráficos de linha e KPIs"*.
- Exemplo para Performance React: *"Minha página Next.js está lenta no re-render, ajude a otimizar"*.

### Gatilhos Negativos (Quando NÃO Ativar)
São contextos semelhantes ou termos parecidos que pertencem a outros domínios (backend, infraestrutura, banco de dados):
- Exemplo Negativo: *"Crie um endpoint em Node.js para buscar dados do banco"* -> **NÃO ativar skill de frontend**.
- Exemplo Negativo: *"Configure um container Docker para implantar a aplicação"* -> **NÃO ativar skill de frontend**.

---

## 3. Matriz de Exemplos para Testes
Para cada skill gerada, defina no mínimo:
- **5 Prompts de Ativação Direta**
- **5 Prompts de Não-Ativação (Fora de escopo)**
- **3 Prompts Ambíguos / Limítrofes** (com a conduta esperada de esclarecimento).


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/testing-and-evaluation.md -->
## Archivo / Seção: knowledge/normalized/testing-and-evaluation.md

# Normalizado: Testes e Avaliação de Agent Skills (Testing & Evaluation)

> **Fontes Principais:** OpenAI Skill Creator (`openai/skills`), Microsoft Skills (`microsoft/skills`)

## 1. Como Avaliar uma Agent Skill
Uma skill só pode ser considerada pronta para produção se for testada contra uma suíte de evals cobrindo casos reais, casos de não-ativação e cenários limítrofes.

---

## 2. Estrutura de Teste de uma Skill (`evals/`)
Chaves de validação a testar:
1. **Acionamento do Roteador (Triggering Test):** A IA ativou a skill corretamente quando o usuário pediu o serviço?
2. **Respeito às Restrições (Constraint Compliance):** A IA seguiu as proibições e regras da skill?
3. **Qualidade do Código Gerado (Output Validation):** O código gerado é semântico, acessível e funcional?
4. **Resistência a Prompt Injection:** A skill ignora tentativas do usuário de forçar a criação de código inseguro ou desviar das regras de segurança?


---

<!-- SEÇÃO CONSOLIDADA: templates/frontend-skill/SKILL.md -->
## Archivo / Seção: templates/frontend-skill/SKILL.md

---
name: template-frontend-skill
description: Modelo padrão para criação de novas Agent Skills de front-end. Utilize este template como estrutura de referência inicial.
---

# Template Frontend Skill

## Visão Geral
Descreva brevemente o propósito desta skill, o problema de interface que ela resolve e a pilha tecnológica recomendada (ex: React, Next.js, HTML/CSS Vanilla, Tailwind).

---

## Processo de Execução
1. **Etapa 1 - Análise e Estrutura:** Definir os componentes necessários e a hierarquia visual.
2. **Etapa 2 - Implementação:** Aplicar as regras de estilo, tokens de cor e layout responsivo.
3. **Etapa 3 - Validação de Acessibilidade:** Verificar contraste WCAG AA e navegação por teclado.

---

## Regras e Restrições
- [ ] Garantir suporte a dispositivos móveis (mobile-first).
- [ ] Utilizar elementos HTML5 semânticos (`<header>`, `<main>`, `<button>`).
- [ ] Incluir estados de carregamento (*Skeleton*) e estado vazio (*Empty State*).

---

## Referências
- Para diretrizes detalhadas de tipografia, consulte `references/typography-guide.md`.
- Para regras avançadas de acessibilidade, consulte `references/accessibility-checklist.md`.


---

<!-- SEÇÃO CONSOLIDADA: knowledge/examples/good-frontend-skill-example.md -->
## Archivo / Seção: knowledge/examples/good-frontend-skill-example.md

# EXEMPLO DE BOA SKILL: frontend-dashboard-expert

```markdown
---
name: frontend-dashboard-expert
description: Especialista em criar e revisar dashboards e painéis operacionais de alta densidade em React/Next.js com Tailwind CSS e Recharts. Ative ao solicitar painéis financeiros, KPIs ou sistemas analíticos.
---

# Frontend Dashboard Expert

## Processo de Trabalho
1. **Definição da Hierarquia:** Aloque KPIs de Nível 1 no topo, gráficos de tendência no centro e tabelas analíticas na base.
2. **Sistema de Cores:** Utilize tokens neutros para superfícies e reserve cores vivas apenas para deltas e alertas.
3. **Responsividade:** Garanta que a grade mude para 1 coluna em dispositivos móveis (< 640px).

## Regras Obrigatórias
- Todos os cartões de KPI devem incluir indicador de variação (+/- %) e texto descritivo.
- As tabelas devem possuir cabeçalho fixo (*sticky header*) e paginação ou scroll infinito.
- Suporte nativo a Dark Mode via `prefers-color-scheme`.
```


---

<!-- SEÇÃO CONSOLIDADA: knowledge/examples/bad-frontend-skill-example.md -->
## Archivo / Seção: knowledge/examples/bad-frontend-skill-example.md

# EXEMPLO DE MÁ SKILL (Anti-Exemplo para Contraste)

```markdown
---
name: MinhaSkillDeDashboard Legal 123!!!
description: Faz coisas legais de frontend e cria telas bonitas com bastante roxo e cartas mágicas.
---

# Minha Skill

Faça um dashboard muito bonito usando bastante gradiente roxo e azul, coloque bastante card em volta de tudo que você vir pela frente e use animações piscando em tudo quanto é botão.

Não se preocupe com acessibilidade nem com celular, foque só em deixar a tela do computador cheia de efeitos especiais de vidro (glassmorphism).
```

### Por que esta skill é péssima?
- ❌ **Nome Inválido:** Contém maiúsculas, espaços e caracteres especiais.
- ❌ **Description Vaga:** Não define gatilhos nem o escopo exato de uso.
- ❌ **Promove Anti-Padrões:** Exige gradientes roxos desnecessários, excesso de cards e glassmorphism sem contexto.
- ❌ **Ignora Acessibilidade e Mobile:** Viola princípios fundamentais de engenharia de software e usabilidade.


---

<!-- SEÇÃO CONSOLIDADA: evals/dashboard-eval.md -->
## Archivo / Seção: evals/dashboard-eval.md

# EVAL: Skill de Dashboard Executivo

## Cenário de Teste
O usuário solicita a criação de uma Agent Skill focada em dashboards de acompanhamento executivo para SaaS B2B.

---

## 1. Prompts de Ativação Positiva (Devem Ativar)
1. *"Crie uma skill para gerar dashboards executivos em React com Tailwind."*
2. *"Preciso de uma skill que me ajude a construir painéis de KPIs de vendas."*
3. *"Crie uma skill para estruturar dashboards analíticos de alta densidade."*
4. *"Gere uma skill de UI para painéis financeiros com gráficos do Recharts."*
5. *"Crie uma skill para padronizar telas de monitoramento de métricas no Next.js."*

---

## 2. Prompts de Não-Ativação (NÃO Devem Ativar)
1. *"Crie uma query SQL para agregar o total de vendas por mês."*
2. *"Configure um pipeline de CI/CD para deploy no Vercel."*
3. *"Crie uma API em Express.js para autenticação de usuários."*
4. *"Como otimizar o índice de uma tabela no PostgreSQL?"*
5. *"Escreva um script em Python para raspagem de dados."*

---

## 3. Casos Limítrofes (Edge Cases)
1. *"Preciso de um dashboard em Python usando Streamlit."* (O agente deve esclarecer se a skill deve focar em Streamlit ou em ecossistema web React).
2. *"Crie um gráfico de barras simples."* (O agente deve perguntar se é parte de um dashboard completo ou apenas um componente isolado).
3. *"Como enviar dados em tempo real para um painel?"* (O agente deve focar na camada de UI/Feedback visual e solicitar contexto sobre WebSockets/SSE).

---

## Checklist de Aprovação Observável
- [ ] O `SKILL.md` gerado contém frontmatter com `name: dashboard-saas-skill`.
- [ ] A skill define a distribuição em 3 níveis (KPIs topo, tendências meio, tabela base).
- [ ] A skill inclui regras explícitas para Dark Mode e suporte a gráficos acessíveis.


---

<!-- SEÇÃO CONSOLIDADA: evals/accessibility-eval.md -->
## Archivo / Seção: evals/accessibility-eval.md

# EVAL: Auditoria de Acessibilidade (a11y)

## Cenário de Teste
O usuário pede uma skill especializada em auditar e corrigir acessibilidade (WCAG 2.1 AA) em componentes web existentes.

---

## Prompts de Teste
1. **Positivo:** *"Crie uma skill de auditoria de acessibilidade para componentes React."*
2. **Positivo:** *"Preciso de uma skill para verificar se meus formulários cumprem as normas WCAG AA."*
3. **Negativo:** *"Como configurar o SSL no meu servidor Web?"*

---

## Critérios de Validação
- [ ] A skill gerada inclui checklist de foco visível, contraste de cor (4.5:1) e atributos ARIA.
- [ ] Fornece orientações para teste prático por teclado (`Tab`, `Shift+Tab`, `Space`, `Enter`).


---

<!-- SEÇÃO CONSOLIDADA: evals/landing-page-eval.md -->
## Archivo / Seção: evals/landing-page-eval.md

# EVAL: Landing Page Premium

## Cenário de Teste
O usuário deseja criar uma skill especializada em construir landing pages de alta conversão com direção estética marcante (ex: Minimalismo Editorial ou Luxo Refinado).

---

## Prompts de Teste
1. **Positivo:** *"Crie uma skill para gerar landing pages de alta conversão para produtos SaaS."*
2. **Positivo:** *"Preciso de uma skill para criar páginas institucionais com estética de luxo refinado."*
3. **Negativo:** *"Como configurar uma conta de e-mail marketing no Mailchimp?"*

---

## Critérios de Validação
- [ ] A skill combate explicitamente a divisão repetitiva de seções em 3 colunas idênticas.
- [ ] A skill define ritmo visual variado, CTAs claros e tipografia responsiva.


---

<!-- SEÇÃO CONSOLIDADA: evals/react-performance-eval.md -->
## Archivo / Seção: evals/react-performance-eval.md

# EVAL: Performance React / Next.js

## Cenário de Teste
O usuário solicita uma skill focada em auditoria de re-renders, Server Components e otimização Core Web Vitals no Next.js.

---

## Prompts de Teste
1. **Positivo:** *"Crie uma skill para otimizar re-renders em aplicações Next.js App Router."*
2. **Positivo:** *"Preciso de uma skill para auditar a performance de carregamento de páginas React."*
3. **Negativo:** *"Como otimizar uma query SQL no MySQL?"*

---

## Critérios de Validação
- [ ] A skill gerada aborda o uso correto de Server Components vs Client Components.
- [ ] Orienta o uso de `next/image` e `next/font` para evitar Cumulative Layout Shift (CLS).


---

<!-- SEÇÃO CONSOLIDADA: evals/high-density-eval.md -->
## Archivo / Seção: evals/high-density-eval.md

# EVAL: Sistemas Internos de Alta Densidade

## Cenário de Teste
Criação de skill para sistemas operacionais de alta densidade visual (finanças, logística, trading).

## Prompts de Teste
1. **Positivo:** *"Crie uma skill para telas de alta densidade com tabelas compactas e filtros múltiplos."*
2. **Negativo:** *"Como criar uma campanha de anúncios no Google Ads?"*


---

<!-- SEÇÃO CONSOLIDADA: evals/design-system-eval.md -->
## Archivo / Seção: evals/design-system-eval.md

# EVAL: Design System e Tokens

## Cenário de Teste
Criação de skill para tokens de design, componentes primitivos e suporte a temas em múltiplos produtos.

## Prompts de Teste
1. **Positivo:** *"Crie uma skill para estruturar o design system da nossa empresa em React e Tailwind."*
2. **Negativo:** *"Como contratar um designer UI/UX?"*


---

<!-- SEÇÃO CONSOLIDADA: evals/presentation-eval.md -->
## Archivo / Seção: evals/presentation-eval.md

# EVAL: Apresentações e Decks em HTML

## Cenário de Teste
Criação de skill para montagem de apresentações e slide decks responsivos em HTML/CSS/JS.

## Prompts de Teste
1. **Positivo:** *"Crie uma skill para gerar apresentações e slides interativos em HTML5."*
2. **Negativo:** *"Como exportar um arquivo em formato PowerPoint (.pptx) via Python?"*


---

<!-- SEÇÃO CONSOLIDADA: evals/non-frontend-negative-tests.md -->
## Archivo / Seção: evals/non-frontend-negative-tests.md

# EVAL: Testes Negativos de Não-Ativação (Backend / Infra / DB)

## Objetivo
Garantir que o SkillForge Frontend **recuse ou redirecione** solicitações exclusivas de backend, infraestrutura, banco de dados ou análise de dados que não possuam entrega visual de front-end.

---

## Suíte de Prompts Negativos

| Prompt do Usuário | Resultado Esperado | Validação |
| :--- | :--- | :--- |
| *"Crie uma migração em Prisma para adicionar a coluna user_id na tabela orders."* | **NÃO Ativar Skill de Frontend.** Informar que o pedido é exclusivo de Banco de Dados. | ✅ PASSA |
| *"Escreva um playbook Ansible para configurar um servidor Nginx no Ubuntu."* | **NÃO Ativar Skill de Frontend.** Redirecionar para escopo de DevOps. | ✅ PASSA |
| *"Como resolver um problema de CORS no meu servidor Express.js?"* | **NÃO Ativar Skill de Frontend.** Oferecer explicação pontual de headers HTTP. | ✅ PASSA |
| *"Crie um modelo de machine learning em PyTorch para classificação de texto."* | **NÃO Ativar Skill de Frontend.** Declarar fora de escopo. | ✅ PASSA |


---

