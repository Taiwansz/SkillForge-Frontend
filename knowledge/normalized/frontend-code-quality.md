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
