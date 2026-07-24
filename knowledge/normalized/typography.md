# Normalizado: Tipografia e Hierarquia Vertical (Typography)

> **Fontes Principais:** Impeccable (`pbakaus/impeccable`), UI UX Pro Max (`nextlevelbuilder/ui-ux-pro-max-skill`)

## 1. Princípios de Tipografia Front-end
A tipografia representa mais de 80% do design de interface na web. Uma boa hierarquia garante escaneabilidade e reduz o cansaço visual.

---

## 2. Escalas Tipográficas Recomendadas

```css
/* Escala de Tipo Modular recomendada (Rácio 1.25 - Major Third) */
--text-xs: 0.75rem;   /* 12px - Legendas secundárias */
--text-sm: 0.875rem;  /* 14px - Textos auxiliares e dados */
--text-base: 1rem;    /* 16px - Corpo de texto padrão */
--text-lg: 1.125rem;  /* 18px - Subtítulos pequenos */
--text-xl: 1.25rem;   /* 20px - Títulos de cartões */
--text-2xl: 1.5rem;   /* 24px - Títulos de seção */
--text-3xl: 1.875rem; /* 30px - Títulos de página */
--text-4xl: 2.25rem;  /* 36px - Destaques / Decks */
```

---

## 3. Emparelhamento de Fontes (*Font Pairing*)
- **Moderna / Tecnológica:** Inter + JetBrains Mono
- **Editorial / Elegante:** Playfair Display + Inter
- **Corporativa / Robusta:** Roboto / Open Sans + Fira Code
- **Industrial / Utilitária:** Space Grotesk + Space Mono

---

## 4. Regras de Ouro
1. **Comprimento de Linha (*Measure*):** Limite parágrafos entre 45 e 75 caracteres por linha para leitura ideal.
2. **Altura de Linha (*Line Height*):** 
   - Títulos grandes (`h1`, `h2`): `1.1` a `1.2`.
   - Corpo de texto: `1.5` a `1.6`.
3. **Contraste Mínimo:** Atender WCAG AA (mínimo `4.5:1` para texto normal e `3:1` para texto grande).
