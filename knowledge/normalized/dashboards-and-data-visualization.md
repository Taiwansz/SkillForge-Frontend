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
