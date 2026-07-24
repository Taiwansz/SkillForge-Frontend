# Normalizado: Descoberta e Gatilhos (Discovery and Triggering)

> **Fontes Principais:** OpenAI Skill Creator (`openai/skills`), Microsoft Skills (`microsoft/skills`)

## 1. Princípios de Ativação Seletiva
Uma skill só deve ser ativada quando o pedido do usuário corresponder explicitamente ao seu escopo. Ativações falsas-positivas degradam o desempenho e consomem contexto desnecessariamente.

---

## 2. Definindo Gatilhos Positivos e Negativos

### Gatilhos Positivos (Quando Ativar)
São palavras-chave, intenções e frases típicas do usuário:
- Exemplo para Dashboard: *"Crie um painel de controle financeiro com gráficos de linha e KPIs"*.
- Exemplo para Performance React: *"Minha página Next.js está lenta no re-render, ajude a otimizar"*.

### Gatilhos Negativos (Quando NÃO Ativar)
São contextos semelhantes ou termos parecidos que pertencem a outros domínios (backend, infraestrutura, banco de dados):
- Exemplo Negativo: *"Crie um endpoint em Node.js para buscar dados do banco"* -> **NÃO ativar skill de frontend**.
- Exemplo Negativo: *"Configure um container Docker para implantar a aplicação"* -> **NÃO ativar skill de frontend**.

---

## 3. Matriz de Exemplos para Testes
Para cada skill gerada, defina no mínimo:
- **5 Prompts de Ativação Direta**
- **5 Prompts de Não-Ativação (Fora de escopo)**
- **3 Prompts Ambíguos / Limítrofes** (com a conduta esperada de esclarecimento).
