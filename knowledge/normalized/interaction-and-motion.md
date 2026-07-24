# Normalizado: Animação e Microinterações (Interaction & Motion)

> **Fontes Principais:** Impeccable (`pbakaus/impeccable`), Ibelick UI Skills (`ibelick/ui-skills`)

## 1. Princípios de Animação Performática
Animações na web devem ser rápidas, intencionais e aceleradas por GPU.

### Propriedades Seguras (Aceleração por GPU)
- ✅ `transform` (`translate3d`, `scale`, `rotate`)
- ✅ `opacity`

### Propriedades Perigosas (Causam Layout Thrashing / Reflow)
- ❌ `width`, `height`, `margin`, `padding`
- ❌ `top`, `left`, `right`, `bottom`

---

## 2. Durabilidade e Curvas de Transição (*Easings*)
- **Microinterações rápidas (Hover em botões, seleção):** `150ms` a `200ms` (`ease-out`).
- **Transições de modal e gavetas:** `250ms` a `300ms` (`cubic-bezier(0.16, 1, 0.3, 1)`).
- **Animações decorativas ou entrada de página:** `300ms` a `400ms`.

---

## 3. Respeito às Preferências do Usuário (Reduced Motion)
Sempre inclua suporte para usuários que desativaram animações no sistema operacional:

```css
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
