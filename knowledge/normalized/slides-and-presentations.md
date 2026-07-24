# Normalizado: Apresentações e Slides em HTML/CSS (Slides & Presentations)

> **Fontes Principais:** Anthropic Skills (`anthropics/skills`), Taste Skill (`Leonxlnx/taste-skill`)

## 1. Princípios de Slides em Web
Apresentações baseadas em HTML/CSS/JS permitem animações fluídas, interatividade real e responsividade nativa sem depender de softwares proprietários.

---

## 2. Estrutura Padrão de Slide Deck (Aspect Ratio 16:9)

```html
<div class="slide-deck">
  <section class="slide current">
    <span class="slide-number">01 / 10</span>
    <h1 class="slide-title">Visão Estratégica Q3</h1>
    <p class="slide-subtitle">Transformação Digital e Arquitetura Front-end</p>
  </section>
</div>

<style>
.slide-deck {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  position: relative;
  background: var(--bg-page);
}
.slide {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4rem;
  box-sizing: border-box;
}
</style>
```

---

## 3. Navegação e Atalhos por Teclado
- Seta para Direita / Espaço: Próximo slide.
- Seta para Esquerda: Slide anterior.
- Tecla `F`: Ativar modo Tela Cheia (*Fullscreen API*).
