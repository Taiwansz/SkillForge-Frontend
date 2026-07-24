# Normalizado: Design Responsivo e Dispositivos (Responsive Design)

> **Fontes Principais:** Vercel Agent Skills (`vercel-labs/agent-skills`), Ibelick UI Skills (`ibelick/ui-skills`)

## 1. Abordagem Mobile-First
Desenvolva a estrutura CSS pensando primeiramente na tela mobile menor e expanda progressivamente usando media queries min-width.

```css
/* Estilo Base: Mobile (< 640px) */
.container {
  padding: 1rem;
  width: 100%;
}

/* Tablet (>= 640px) */
@media (min-width: 640px) {
  .container {
    padding: 1.5rem;
  }
}

/* Desktop (>= 1024px) */
@media (min-width: 1024px) {
  .container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 2rem;
  }
}
```

---

## 2. Breakpoints Canônicos
- **sm:** `640px` (Smartphones em modo paisagem / tablets pequenos)
- **md:** `768px` (Tablets / telas pequenas)
- **lg:** `1024px` (Laptops e desktops padrão)
- **xl:** `1280px` (Monitores de alta resolução)
- **2xl:** `1536px` (Telas ultra-wide)

---

## 3. Diretrizes Práticas de Adaptabilidade
- Evite larguras fixas em pixels (`width: 500px` ❌); prefira `max-width: 100%` ou porcentagens/rem.
- Em telas touch (mobiles/tablets), garanta que áreas clicáveis tenham no mínimo **44x44px**.
- Substitua tabelas complexas por cartões sanfonados ou scroll horizontal controlado em dispositivos móveis.
