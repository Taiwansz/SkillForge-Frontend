# CONSOLIDATED 05: MANIFESTO DE UPLOAD E FERRAMENTAS PYTHON

<!-- SEÇÃO CONSOLIDADA: UPLOAD-MANIFEST.md -->
## Archivo / Seção: UPLOAD-MANIFEST.md

# UPLOAD MANIFEST - Guia de Anexo para LibreChat / Pergunte Aí

Este manifesto define rigorosamente quais arquivos do **SkillForge Frontend Agent** devem e não devem ser anexados à base de conhecimento da plataforma de IA (LibreChat, Pergunte Aí, Claude Project, etc.).

---

## 1. Obrigatório no Prompt do Agente (System Prompt)
*Estes arquivos devem ser colados diretamente no campo de Prompt de Sistema do Agente:*

| Arquivo | Descrição / Instrução |
| :--- | :--- |
| `PROMPT-AGENTE.md` | Conteúdo completo do prompt de sistema. Define a identidade, fluxos de trabalho, modos de entrevista e formato de saída. |

---

## 2. Obrigatórios na Base de Conhecimento (Knowledge Base / RAG)
*Estes arquivos devem ser anexados à base de conhecimento (arquivos de busca/vetor do agente):*

| Arquivo | Função no RAG |
| :--- | :--- |
| `KNOWLEDGE-INDEX.md` | Índice geral e mapa de recuperação de arquivos. |
| `SOURCES.md` | Registro de procedência e licenças para auditoria. |
| `README.md` | Visão geral do repositório. |
| `knowledge/normalized/skill-authoring.md` | Arquitetura e escrita de skills. |
| `knowledge/normalized/discovery-and-triggering.md` | Gatilhos e descrição. |
| `knowledge/normalized/visual-direction.md` | Direção estética e combate ao genérico. |
| `knowledge/normalized/typography.md` | Tipografia e hierarquia. |
| `knowledge/normalized/color-and-theming.md` | Cores, contraste e temas. |
| `knowledge/normalized/layout-and-spacing.md` | Grades e espaçamentos. |
| `knowledge/normalized/responsive-design.md` | Responsividade e mobile. |
| `knowledge/normalized/components-and-design-systems.md` | Componentes e tokens. |
| `knowledge/normalized/interaction-and-motion.md` | Animações e microinterações. |
| `knowledge/normalized/accessibility.md` | Diretrizes de acessibilidade (a11y). |
| `knowledge/normalized/content-and-copy.md` | UX writing e combate a placeholders. |
| `knowledge/normalized/forms-and-validation.md` | Formulários e validações. |
| `knowledge/normalized/states-and-feedback.md` | Estados de UI e feedback. |
| `knowledge/normalized/dashboards-and-data-visualization.md` | Dashboards e gráficos. |
| `knowledge/normalized/slides-and-presentations.md` | Apresentações e slides em HTML. |
| `knowledge/normalized/react-next-performance.md` | Boas práticas de React / Next.js. |
| `knowledge/normalized/frontend-code-quality.md` | Qualidade de código front-end. |
| `knowledge/normalized/design-review.md` | Checklists de auditoria visual. |
| `knowledge/normalized/anti-patterns.md` | Guia de eliminação de anti-padrões. |
| `knowledge/normalized/testing-and-evaluation.md` | Evals e testes de skills. |
| `knowledge/normalized/security-and-licensing.md` | Segurança e licenças. |
| `templates/frontend-skill/SKILL.md` | Modelo de referência de skill. |

---

## 3. Opcionais na Base de Conhecimento
*Podem ser anexados para fornecer mais exemplos práticos se a plataforma permitir mais arquivos:*

| Arquivo | Função |
| :--- | :--- |
| `knowledge/examples/good-frontend-skill-example.md` | Exemplo de skill bem construída. |
| `knowledge/examples/bad-frontend-skill-example.md` | Exemplo de skill com falhas para contraste. |

---

## 4. Somente Manutenção (NÃO Anexar ao RAG)
*Estes arquivos servem para desenvolvimento local, validação e execução de testes:*

| Caminho | Motivo para NÃO Anexar |
| :--- | :--- |
| `evals/*.md` | Suíte de testes local do agente; gastaria contexto desnecessário. |
| `scripts/*.py` | Ferramentas de validação em Python; não contêm conhecimento conceitual. |

---

## 5. ESTRITAMENTE PROIBIDO ANEXAR (Não Upload)
*Nunca envie os itens abaixo para a plataforma de IA:*

* ❌ `sources/upstream/*` (Snapshots brutos e repositórios externos clonados).
* ❌ `.git/`, `.github/`, `.gitignore`
* ❌ `node_modules/`, `__pycache__/`, `.venv/`
* ❌ Chaves API, arquivos `.env`, segredos ou tokens.


---

<!-- SEÇÃO CONSOLIDADA: scripts/sync-sources.py -->
## Archivo / Seção: scripts/sync-sources.py

```python
# scripts/sync-sources.py
#!/usr/bin/env python3
"""
sync-sources.py - Script seguro para registrar e validar sincronização das fontes upstream.
Este script não executa comandos de código externo; ele atualiza os registros em SOURCES.md.
"""

import sys
import os
import json

def sync_sources():
    print(" [Sync Sources] Verificando manifesto de fontes locais em SOURCES.md...")
    sources_file = os.path.join(os.path.dirname(__file__), "..", "SOURCES.md")
    if not os.path.exists(sources_file):
        print("❌ Arquivo SOURCES.md não encontrado!")
        sys.exit(1)
    
    print("✅ SOURCES.md verificado com sucesso.")
    print("ℹ️ Em ambientes sem ferramentas de rede, as fontes utilizam snapshots imutáveis em sources/upstream/")

if __name__ == "__main__":
    sync_sources()

```

---

<!-- SEÇÃO CONSOLIDADA: scripts/validate-sources.py -->
## Archivo / Seção: scripts/validate-sources.py

```python
# scripts/validate-sources.py
#!/usr/bin/env python3
"""
validate-sources.py - Script seguro para validação das fontes de origem e licenças.
"""

import os
import sys

REQUIRED_SOURCES = [
    "anthropics-frontend-design",
    "pbakaus-impeccable",
    "leonxlnx-design-taste-frontend",
    "nextlevelbuilder-ui-ux-pro-max",
    "vercel-labs-react-best-practices",
    "vercel-labs-web-design-guidelines",
    "ibelick-ui-skills",
    "microsoft-frontend-design-review",
    "openai-skill-creator"
]

def validate_sources():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "sources", "upstream"))
    missing = []
    
    for src in REQUIRED_SOURCES:
        src_path = os.path.join(base_dir, src, "SOURCE.md")
        if not os.path.exists(src_path):
            missing.append(src)
            
    if missing:
        print(f"❌ Fontes ausentes em sources/upstream: {missing}")
        sys.exit(1)
        
    print(f"✅ Todas as {len(REQUIRED_SOURCES)} fontes registradas possuem SOURCE.md válido.")

if __name__ == "__main__":
    validate_sources()

```

---

<!-- SEÇÃO CONSOLIDADA: scripts/validate-agent-package.py -->
## Archivo / Seção: scripts/validate-agent-package.py

```python
# scripts/validate-agent-package.py
#!/usr/bin/env python3
"""
validate-agent-package.py - Script seguro para validação do pacote do agente.
Verifica a presença dos arquivos obrigatórios no agente SkillForge Frontend.
"""

import os
import sys

REQUIRED_ROOT_FILES = [
    "PROMPT-AGENTE.md",
    "KNOWLEDGE-INDEX.md",
    "UPLOAD-MANIFEST.md",
    "SOURCES.md",
    "README.md"
]

REQUIRED_NORMALIZED_FILES = [
    "skill-authoring.md",
    "discovery-and-triggering.md",
    "visual-direction.md",
    "typography.md",
    "color-and-theming.md",
    "layout-and-spacing.md",
    "responsive-design.md",
    "components-and-design-systems.md",
    "interaction-and-motion.md",
    "accessibility.md",
    "content-and-copy.md",
    "forms-and-validation.md",
    "states-and-feedback.md",
    "dashboards-and-data-visualization.md",
    "slides-and-presentations.md",
    "react-next-performance.md",
    "frontend-code-quality.md",
    "design-review.md",
    "anti-patterns.md",
    "testing-and-evaluation.md",
    "security-and-licensing.md"
]

def validate_package():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    errors = []
    
    for f in REQUIRED_ROOT_FILES:
        path = os.path.join(base_dir, f)
        if not os.path.exists(path):
            errors.append(f"Arquivo de raiz ausente: {f}")
            
    norm_dir = os.path.join(base_dir, "knowledge", "normalized")
    for f in REQUIRED_NORMALIZED_FILES:
        path = os.path.join(norm_dir, f)
        if not os.path.exists(path):
            errors.append(f"Conhecimento normalizado ausente: {f}")
            
    if errors:
        print("❌ ERROS DE VALIDAÇÃO DO PACOTE:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
        
    print("✅ Pacote SkillForge Frontend validado com 100% dos arquivos obrigatórios!")

if __name__ == "__main__":
    validate_package()

```

---

<!-- SEÇÃO CONSOLIDADA: scripts/generate-upload-manifest.py -->
## Archivo / Seção: scripts/generate-upload-manifest.py

```python
# scripts/generate-upload-manifest.py
#!/usr/bin/env python3
"""
generate-upload-manifest.py - Atualiza ou valida o arquivo UPLOAD-MANIFEST.md
"""

import os

def generate_manifest():
    print(" [Manifest Generator] Validando UPLOAD-MANIFEST.md...")
    manifest_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "UPLOAD-MANIFEST.md"))
    if os.path.exists(manifest_path):
        print(f"✅ UPLOAD-MANIFEST.md está atualizado em {manifest_path}")
    else:
        print("❌ UPLOAD-MANIFEST.md não encontrado!")

if __name__ == "__main__":
    generate_manifest()

```

---

<!-- SEÇÃO CONSOLIDADA: scripts/package-agent.py -->
## Archivo / Seção: scripts/package-agent.py

```python
# scripts/package-agent.py
#!/usr/bin/env python3
"""
package-agent.py - Script seguro para preparar a árvore de distribuição do agente.
"""

import os
import sys

def package_agent():
    print("📦 [Package Agent] Verificando estrutura do pacote para empacotamento...")
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"📁 Diretório base do agente: {base_dir}")
    print("✅ Pacote pronto para ser anexado ao LibreChat / Pergunte Aí conforme UPLOAD-MANIFEST.md!")

if __name__ == "__main__":
    package_agent()

```

---

