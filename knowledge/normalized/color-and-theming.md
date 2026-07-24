# Normalizado: Cores, Temas e Paletas Semânticas (Color & Theming)

> **Fontes Principais:** UI UX Pro Max (`nextlevelbuilder/ui-ux-pro-max-skill`), Anthropic Skills (`anthropics/skills`)

## 1. Arquitetura Semântica de Cores
Evite definir cores no CSS usando nomes brutos como `blue-500` diretamente nos componentes. Utilize **tokens semânticos**:

```css
:root {
  /* Cores Básicas da Marca */
  --brand-primary: #0f172a;
  --brand-accent: #2563eb;

  /* Cores Semânticas de Superfície */
  --bg-page: #f8fafc;
  --bg-surface: #ffffff;
  --bg-muted: #f1f5f9;

  /* Cores de Texto */
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #94a3b8;

  /* Cores de Estado */
  --status-success: #16a34a;
  --status-warning: #d97706;
  --status-error: #dc2626;
  --status-info: #0284c7;
}

/* Suporte Automático a Dark Mode */
@media (prefers-color-scheme: dark) {
  :root {
    --bg-page: #090d16;
    --bg-surface: #1e293b;
    --bg-muted: #334155;
    --text-primary: #f8fafc;
    --text-secondary: #cbd5e1;
    --text-muted: #64748b;
  }
}
```

---

## 2. Proporção da Regra 60-30-10
- **60% Cor Dominante:** Fundos de página e superfícies neutras.
- **30% Cor Secundária:** Cartões, menus, estrutura de suporte e divisores.
- **10% Cor de Destaque (*Accent*):** Botões de ação primária (CTA), indicadores ativos e elementos focais.

---

## 3. Diretrizes de Contraste e Acessibilidade
- Verifique se a combinação de texto e fundo possui taxa de contraste conforme WCAG 2.1 AA (`4.5:1` para texto padrão).
- Nunca transmita informação **apenas através da cor**; adicione ícone, texto ou padrão visual auxiliar.
