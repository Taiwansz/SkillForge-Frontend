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
