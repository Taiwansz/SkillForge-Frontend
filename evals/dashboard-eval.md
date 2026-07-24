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
