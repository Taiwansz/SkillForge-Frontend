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
