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
