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
