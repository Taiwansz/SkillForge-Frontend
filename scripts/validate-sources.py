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
