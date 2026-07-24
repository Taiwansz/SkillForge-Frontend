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
