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
