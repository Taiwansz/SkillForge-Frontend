# Normalizado: Diretrizes de Acessibilidade (Accessibility / a11y)

> **Fontes Principais:** Ibelick UI Skills (`ibelick/ui-skills` - fixing-accessibility), Microsoft Skills (`microsoft/skills`)

## 1. Princípios Fundamentais (WCAG 2.1 AA)
A acessibilidade deve ser incorporada desde a concepção da interface, e não como uma etapa posterior de correção.

---

## 2. Checklist Essencial de Acessibilidade

### HTML Semântico
- Use elementos corretos: `<main>`, `<nav>`, `<header>`, `<footer>`, `<section>`, `<article>`, `<button>`, `<a href="...">`.
- Nunca use `<div onClick="...">` para criar botões; prefira `<button type="button">`.

### Navegação por Teclado e Foco Visível
- Todos os elementos interativos devem ser alcançáveis por `Tab`.
- Preserve e estilize o indicador visual de foco (*Focus Ring*):
  ```css
  :focus-visible {
    outline: 2px solid var(--brand-accent);
    outline-offset: 2px;
  }
  ```

### Atributos ARIA (Accessible Rich Internet Applications)
- Use `aria-expanded="true|false"` para menus sanfonados e modais.
- Use `aria-live="polite"` para notificações dinâmicas.
- Use `aria-label="..."` em botões que contêm apenas ícones.

### Imagens e Mídia
- Todas as imagens informativas devem possuir `alt="..."` descritivo.
- Imagens puramente decorativas devem ter `alt=""` e `aria-hidden="true"`.
