# CONSOLIDADO 02: ENGENHARIA, DESIGN SYSTEMS E PERFORMANCE

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/components-and-design-systems.md -->
## Archivo / Seção: knowledge/normalized/components-and-design-systems.md

# Normalizado: Componentes e Design Systems (Components & Design Systems)

> **Fontes Principais:** UI UX Pro Max (`nextlevelbuilder/ui-ux-pro-max-skill`), Ibelick UI Skills (`ibelick/ui-skills`)

## 1. Arquitetura de Componentes Atomic Design
Organize os componentes em níveis claros de abstração:
- **Átomos:** Botões, Inputs, Rótulos, Badges, Ícones.
- **Moléculas:** Grupo de busca (Input + Botão), Campo de formulário (Rótulo + Input + Mensagem de erro).
- **Organismos:** Cabeçalho da página, Tabela paginada, Formulário de checkout.
- **Modelos / Páginas:** Estrutura completa montada com organismos.

---

## 2. Princípios de Reutilização e Variantes
Crie componentes com APIs limpas e suporte a variantes semânticas:

```tsx
// Exemplo em React / TypeScript
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  isLoading = false,
  children,
  className = '',
  disabled,
  ...props
}) => {
  return (
    <button
      className={`btn btn-${variant} btn-${size} ${className}`}
      disabled={disabled || isLoading}
      {...props}
    >
      {isLoading ? <Spinner className="w-4 h-4 animate-spin" /> : children}
    </button>
  );
};
```

---

## 3. Gestão de Tokens de Design
Armazene variáveis em CSS nativo ou Tailwind config de forma centralizada para que uma alteração reflita em todo o sistema.


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/accessibility.md -->
## Archivo / Seção: knowledge/normalized/accessibility.md

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


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/react-next-performance.md -->
## Archivo / Seção: knowledge/normalized/react-next-performance.md

# Normalizado: Performance React e Next.js (React/Next Performance)

> **Fontes Principais:** Vercel Agent Skills (`vercel-labs/agent-skills` - react-best-practices)

## 1. Regras do Next.js App Router (React 19)

### Server Components por Padrão
Tente manter todos os componentes como **Server Components** por padrão. Adicione a diretiva `'use client'` apenas quando houver:
- Handlers de evento (`onClick`, `onChange`, `onSubmit`).
- Hooks de estado ou efeito (`useState`, `useEffect`, `useReducer`).
- APIs exclusivas de navegador (`window`, `localStorage`).

---

## 2. Prevenção de Rerenders Desnecessários
1. **Desloque o Estado para Baixo (*Move State Down*):** Se apenas um formulário pequeno usa o estado, não coloque o `useState` no topo da página.
2. **Passe Componentes como `children`:** Evita re-renderizar a árvore inteira se o pai mudar de estado.
3. **Use `useCallback` e `useMemo` com Cautela:** Apenas para operações computacionalmente pesadas ou referências de objetos passadas a componentes memoizados.

---

## 3. Carregamento de Recursos e Fontes
- Use `next/font` para carregamento de fontes com zero Layout Shift.
- Use `next/image` para imagens responsivas, formato WebP/AVIF automático e lazy loading.


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/frontend-code-quality.md -->
## Archivo / Seção: knowledge/normalized/frontend-code-quality.md

# Normalizado: Qualidade de Código Front-end (Frontend Code Quality)

> **Fontes Principais:** Vercel Agent Skills (`vercel-labs/agent-skills`), Microsoft Skills (`microsoft/skills`)

## 1. Organização e Separação de Responsabilidades
- **Componentes Foco Único:** Um componente não deve misturar lógica de busca de API, transformação complexa de dados e renderização de 10 sub-elementos.
- **Custom Hooks:** Extraia lógica reutilizável para hooks customizados (`useAuth`, `useFormValidation`, `useMediaQuery`).

---

## 2. Padrões de Nomenclatura
- Componentes e Arquivos React: `PascalCase` (`UserProfileCard.tsx`).
- Utilitários, Hooks e Variáveis: `camelCase` (`useFetchUser`, `formatCurrency`).
- Constantes Globais: `UPPER_SNAKE_CASE` (`MAX_FILE_SIZE_BYTES`).
- Classes CSS / Tailwind: Nomes descritivos e semânticos.


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/design-review.md -->
## Archivo / Seção: knowledge/normalized/design-review.md

# Normalizado: Auditoria e Revisão de Design (Design Review)

> **Fontes Principais:** Microsoft Skills (`microsoft/skills` - frontend-design-review), Impeccable (`pbakaus/impeccable`)

## 1. Processo de Auditoria Estruturada em 4 Passos

### Passo 1: Inspeção Visual e Tipográfica
- Alinhamento de elementos na grade de 8px.
- Contraste de texto vs fundo em conformidade com WCAG AA.
- Consistência de pesos e tamanhos de fonte.

### Passo 2: Teste de Estados de Interface
- Testar o comportamento da tela sem dados (Empty State).
- Testar com textos extremamente longos (Overflow / Text Wrapping).
- Testar em estado de carregamento e estado de erro.

### Passo 3: Auditoria de Navegação e Acessibilidade
- Navegar na página usando apenas a tecla `Tab` e `Enter`.
- Verificar se o indicador de foco (*Focus Ring*) está visível.
- Validar se os atributos `aria-label` e `alt` estão presentes.

### Passo 4: Inspeção Responsiva
- Testar em viewport de `375px` (Mobile), `768px` (Tablet) e `1440px` (Desktop).
- Verificar se há barra de rolagem horizontal indesejada (*Horizontal Overflow*).


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/anti-patterns.md -->
## Archivo / Seção: knowledge/normalized/anti-patterns.md

# Normalizado: Anti-Padrões de Interface e IA (Anti-Patterns)

> **Fontes Principais:** Impeccable (`pbakaus/impeccable`), Anthropic Skills (`anthropics/skills`)

## 1. O que são Anti-Padrões de IA?
São vícios estéticos e estruturais que ocorrem quando modelos de linguagem geram código de interface sem critério visual ou contextual, resultando em soluções genéricas e repetitivas.

---

## 2. Tabela de Anti-Padrões Frequentes e Soluções

| Anti-Padrão | Sintoma Visual | Solução Correta |
| :--- | :--- | :--- |
| **Card Thrashing** | Envolver cada frase, lista ou botão em um container com borda e sombra. | Usar margens, títulos claros e divisores finos em vez de cartões em tudo. |
| **Square Icons** | Colocar um ícone pequeno dentro de um quadrado com fundo colorido. | Usar o ícone diretamente alinhado ao texto ou com tamanho e cor adequados. |
| **Purple Gradient** | Fundo escuro com gradientes em tons de roxo/azul-ciano sem justificativa. | Usar paleta semântica alinhada com a marca ou tons neutros de alto contraste. |
| **Three Column Default** | Dividir todas as seções da landing page em 3 colunas idênticas. | Variar o ritmo visual: seções de 2 colunas com imagem, listas em grade assimétrica, hero em destaque. |
| **KPI Flatness** | Dar exatamente o mesmo tamanho e destaque para 8 métricas em um dashboard. | Destacar as 2 métricas primárias (Nível 1) e organizar as secundárias em escala menor. |


---

<!-- SEÇÃO CONSOLIDADA: knowledge/normalized/security-and-licensing.md -->
## Archivo / Seção: knowledge/normalized/security-and-licensing.md

# Normalizado: Segurança, Licenciamento e Compliance (Security & Licensing)

> **Fontes Principais:** Fontes oficiais, Diretrizes de Compliance e Licenças de Código Aberto

## 1. Hierarquia de Confiança e Princípios de Segurança
Em qualquer tomada de decisão técnica ou arquitetural no SkillForge Frontend Agent, aplique estritamente a seguinte hierarquia de prioridade:

1. 🛡️ **Segurança e Licenciamento:** Respeito absoluto a licenças de software, isolamento de segredos e prevenção de código destrutivo.
2. 📋 **Instruções do Projeto / Organização:** Cumprimento rigoroso das regras globais do sistema.
3. 💬 **Solicitação Explícita do Usuário:** Atendimento aos requisitos e preferências especificadas pelo usuário.
4. 🎨 **Identidade Visual e Regras de Negócio da Empresa:** Manutenção da coerência da marca.
5. ♿ **Acessibilidade (a11y):** Garantia de usabilidade universal (WCAG AA).
6. ⚡ **Requisitos Funcionais e Técnicos:** Qualidade de código, semântica e performance.
7. 👁️ **Preferências Estéticas Secundárias de Fontes Externas.**

---

## 2. Validação de Licenças de Código Aberto
- **MIT / Apache-2.0:** Permitida reutilização e adaptação, desde que mantidos os avisos de direito autoral e o arquivo de licença original.
- **GPL / AGPL:** Exige atenção especial quanto à redistribuição de código derivado.
- **Atribuição:** Todo conhecimento externo importado deve registrar fonte, autor, repositório e commit exato no arquivo `SOURCES.md`.


---

