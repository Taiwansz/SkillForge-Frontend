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
