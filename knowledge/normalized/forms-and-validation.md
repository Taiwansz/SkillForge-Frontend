# Normalizado: Formulários e Validação (Forms & Validation)

> **Fontes Principais:** Microsoft Skills (`microsoft/skills`), Ibelick UI Skills (`ibelick/ui-skills`)

## 1. Estrutura Padrão de Campo de Formulário
Cada campo interativo deve conter rótulo claro, indicação de obrigatoriedade, campo de entrada e área dedicada para erro inline:

```html
<div class="form-group">
  <label for="email-input" class="form-label">
    E-mail profissional <span class="required" aria-hidden="true">*</span>
  </label>
  <input 
    type="email" 
    id="email-input" 
    name="email" 
    class="form-input" 
    placeholder="nome@empresa.com"
    required
    aria-invalid="false"
    aria-describedby="email-error"
  />
  <span id="email-error" class="form-error-message" role="alert"></span>
</div>
```

---

## 2. Validação Inline vs Ao Submeter
- **Ao Digitar (Debounced):** Valide regras simples de formato (e-mail, formato de telefone) após o usuário pausar a digitação.
- **Ao Perder Foco (*On Blur*):** Ideal para verificar campos obrigatórios preenchidos.
- **Ao Submeter (*On Submit*):** Dispare validação completa e posicione o foco automático no primeiro campo com erro.
