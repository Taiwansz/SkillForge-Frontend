# Normalizado: Layout, Grades e Espaçamento (Layout & Spacing)

> **Fontes Principais:** UI UX Pro Max (`nextlevelbuilder/ui-ux-pro-max-skill`), Microsoft Skills (`microsoft/skills`)

## 1. Sistema de Grade de 8px (8pt Grid System)
Todos os espaçamentos, margens, paddings e dimensões devem ser múltiplos de **8px** (ou 4px para micro-ajustes):

```css
--space-1: 0.25rem; /* 4px */
--space-2: 0.5rem;  /* 8px */
--space-3: 0.75rem; /* 12px */
--space-4: 1rem;    /* 16px */
--space-6: 1.5rem;  /* 24px */
--space-8: 2rem;    /* 32px */
--space-12: 3rem;   /* 48px */
--space-16: 4rem;   /* 64px */
```

---

## 2. Padrões de Layout

### CSS Grid para Aplicações e Dashboards
Utilize CSS Grid para estruturas de colunas com comportamento previsível:
```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-6);
}
```

### Flexbox para Alinhamento de Componentes
Utilize Flexbox para itens unidimensionais (barras de navegação, cabeçalhos, listas de ações):
```css
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
}
```

---

## 3. Densidade Visual por Tipo de Aplicação
- **Alta Densidade (Sistemas de Operação, Trading, Analytics):** Padding `8px` a `12px`, fontes `12px` a `14px`, linhas compactas.
- **Média Densidade (SaaS B2B, Gerenciadores de Tarefas):** Padding `16px`, fontes `14px` a `16px`.
- **Baixa Densidade / Editorial (Landing Pages, Consumo):** Padding `24px` a `48px`, tipografia grande, amplo espaço negativo.
