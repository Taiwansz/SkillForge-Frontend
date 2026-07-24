# EVAL: Testes Negativos de Não-Ativação (Backend / Infra / DB)

## Objetivo
Garantir que o SkillForge Frontend **recuse ou redirecione** solicitações exclusivas de backend, infraestrutura, banco de dados ou análise de dados que não possuam entrega visual de front-end.

---

## Suíte de Prompts Negativos

| Prompt do Usuário | Resultado Esperado | Validação |
| :--- | :--- | :--- |
| *"Crie uma migração em Prisma para adicionar a coluna user_id na tabela orders."* | **NÃO Ativar Skill de Frontend.** Informar que o pedido é exclusivo de Banco de Dados. | ✅ PASSA |
| *"Escreva um playbook Ansible para configurar um servidor Nginx no Ubuntu."* | **NÃO Ativar Skill de Frontend.** Redirecionar para escopo de DevOps. | ✅ PASSA |
| *"Como resolver um problema de CORS no meu servidor Express.js?"* | **NÃO Ativar Skill de Frontend.** Oferecer explicação pontual de headers HTTP. | ✅ PASSA |
| *"Crie um modelo de machine learning em PyTorch para classificação de texto."* | **NÃO Ativar Skill de Frontend.** Declarar fora de escopo. | ✅ PASSA |
