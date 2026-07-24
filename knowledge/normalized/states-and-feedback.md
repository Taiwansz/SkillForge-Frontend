# Normalizado: Estados de UI e Feedback (States & Feedback)

> **Fontes Principais:** Microsoft Skills (`microsoft/skills`), Ibelick UI Skills (`ibelick/ui-skills`)

## 1. Os 5 Estados Obrigatórios de uma UI
Toda tela ou componente assíncrono deve contemplar explicitamente os 5 estados:

1. **Estado Inicial / Vazio (*Empty State*):** Exibido antes de haver dados. Deve explicar o motivo e oferecer um CTA claro (*"Nenhum relatório encontrado. Criar primeiro relatório"*).
2. **Estado de Carregamento (*Loading State*):** Prefira *Skeletons* (estruturas fantasma) em vez de spinners centralizados para manter a percepção de velocidade.
3. **Estado de Sucesso (*Success State*):** Feedback visual claro de que a ação foi concluída.
4. **Estado de Erro (*Error State*):** Mensagem amigável com opção de tentar novamente (*Retry button*).
5. **Estado Parcial / Paginado (*Partial State*):** Exibição de dados parciais durante o carregamento de mais itens.
