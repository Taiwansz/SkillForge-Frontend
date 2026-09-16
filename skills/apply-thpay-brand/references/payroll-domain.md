# THP payroll and people domain guidance

Use this reference whenever the output represents the actual ThPay product.

## Product scope

ThPay is a Brazilian payroll and people operations platform centered on continuous payroll, compliance, employee self-service and operational transparency. Relevant areas include:

- folha contínua and payroll closing readiness;
- employee directory (CLT and, where product rules allow, other contract types);
- payslip inspection and calculation anatomy;
- INSS, IRRF, FGTS and employer-cost breakdowns;
- eSocial events and rejection handling;
- benefits: VA/VR split, vale-transporte, health and dental plan options;
- employee requests/service desk with SLA and attachments;
- documents and employee profile;
- simulations for vacation, overtime, termination and salary changes;
- audit trails and compliance evidence;
- operational leaderboard/engagement views that do not expose compensation.

## Analyst experience

The payroll analyst is not assumed to be technical. Replace developer language with operational language. Show technical IDs, hashes and event codes as secondary detail, not as the main label.

Every critical screen should answer:

1. What is happening?
2. What requires attention?
3. What is the financial/operational impact?
4. What can I do next?
5. When does the change take effect?

## Employee experience

The employee sees only their own permitted data and actions. Use first-person usefulness, not HR jargon. For benefit changes, always show:

- current choice;
- allowed alternatives;
- monetary effect where applicable;
- deadline or effective competence;
- confirmation before submission;
- request status after submission.

## Payroll numbers

Use Brazilian formats by default in Portuguese contexts:

- currency: `R$ 1.234,56`;
- date: `dd/mm/aaaa`;
- competence: `MM/AAAA` or named month plus year;
- percentages with comma decimal when needed.

Do not fabricate tax/legal rates as permanent design content. Use realistic placeholders only when the task is visual, and label simulated values where ambiguity could mislead.

## Compliance UX

Compliance is communicated through evidence, not through shield-heavy decoration. Prefer clear status, timestamps, protocol IDs, validation results, event history and audit trails.

For eSocial, distinguish `Gerado`, `Validado`, `Enviado`, `Processando`, `Aceito` and `Rejeitado`. A rejection should surface the reason and remediation path.

## Service desk

Tickets must show category, status, owner/team, SLA, latest update and attachments. Employee-facing flows should avoid priority jargon unless the user can influence it.

## Friendly microcopy examples

Prefer:

- `Sua folha está quase pronta. Restam 3 pendências para conferir.`
- `Esta alteração passa a valer em 05/2027.`
- `Você pode ajustar a divisão entre alimentação e refeição dentro das regras da empresa.`
- `O eSocial recusou este evento. Veja o motivo e como corrigir.`

Avoid:

- `Erro 422 no payload.`
- `Mutation failed.`
- `Processo inválido.` without explanation.
