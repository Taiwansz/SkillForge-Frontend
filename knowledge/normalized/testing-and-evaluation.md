# Normalizado: Testes e Avaliação de Agent Skills (Testing & Evaluation)

> **Fontes Principais:** OpenAI Skill Creator (`openai/skills`), Microsoft Skills (`microsoft/skills`)

## 1. Como Avaliar uma Agent Skill
Uma skill só pode ser considerada pronta para produção se for testada contra uma suíte de evals cobrindo casos reais, casos de não-ativação e cenários limítrofes.

---

## 2. Estrutura de Teste de uma Skill (`evals/`)
Chaves de validação a testar:
1. **Acionamento do Roteador (Triggering Test):** A IA ativou a skill corretamente quando o usuário pediu o serviço?
2. **Respeito às Restrições (Constraint Compliance):** A IA seguiu as proibições e regras da skill?
3. **Qualidade do Código Gerado (Output Validation):** O código gerado é semântico, acessível e funcional?
4. **Resistência a Prompt Injection:** A skill ignora tentativas do usuário de forçar a criação de código inseguro ou desviar das regras de segurança?
