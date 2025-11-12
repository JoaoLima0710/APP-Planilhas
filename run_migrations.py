#!/usr/bin/env python3
"""
Script para rodar as migrations do Supabase
Cria todas as tabelas necessárias
"""

import os
import subprocess
import sys

PROJECT_ID = "pikskrtgivhifxpzrxyb"
PROJECT_URL = "https://pikskrtgivhifxpzrxyb.supabase.co"
SERVICE_ROLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBpa3NrcnRnaXZoaWZ4cHpyeHliIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2Mjg4ODY3MywiZXhwIjoyMDc4NDY0NjczfQ.z5bx3NlAvbGJbAl8FVkZflkc-1zof0PckdquluBTVs0"

MIGRATIONS_DIR = "supabase/migrations"

def read_migration_files():
    """Ler todos os arquivos de migration"""
    migrations = []
    
    if not os.path.exists(MIGRATIONS_DIR):
        print(f"❌ Diretório não encontrado: {MIGRATIONS_DIR}")
        return migrations
    
    files = sorted([f for f in os.listdir(MIGRATIONS_DIR) if f.endswith('.sql')])
    
    for file in files:
        path = os.path.join(MIGRATIONS_DIR, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            migrations.append({
                'name': file,
                'path': path,
                'content': content
            })
    
    return migrations

def run_migration(migration, project_url, service_role_key):
    """Rodar uma migration via Supabase SQL"""
    
    print(f"\n📝 Executando: {migration['name']}")
    print(f"   Tamanho: {len(migration['content'])} bytes")
    
    # Usar psql via Supabase connection string
    # Format: postgresql://postgres:password@host:5432/postgres
    
    # Extrair password da service_role_key não é direto
    # Melhor usar SQL API via Python
    
    import urllib.request
    import urllib.error
    import json
    
    # URL para executar SQL
    url = f"{project_url}/rest/v1/rpc/exec_sql"
    
    payload = {
        "sql": migration['content']
    }
    
    headers = {
        "Authorization": f"Bearer {service_role_key}",
        "Content-Type": "application/json",
    }
    
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        
        with urllib.request.urlopen(req, timeout=30) as response:
            print(f"   ✅ Status: {response.status}")
            return True
            
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"   ⚠️  HTTP {e.code}")
        
        # A função exec_sql pode não existir, então tentamos outra abordagem
        return False
        
    except Exception as e:
        print(f"   ⚠️  Erro: {e}")
        return False

def run_via_psql(migrations, project_url, password):
    """Rodar migrations via psql direto"""
    
    print("🔄 Tentando via psql...")
    
    # Extrair host da URL
    host = project_url.replace("https://", "").replace(".supabase.co", "")
    
    # Connection string
    connection = f"postgresql://postgres:{password}@db.{host}.supabase.co:5432/postgres"
    
    for migration in migrations:
        print(f"\n📝 Executando: {migration['name']}")
        
        try:
            # Usar psql
            proc = subprocess.run(
                ["psql", connection, "-f", migration['path']],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if proc.returncode == 0:
                print(f"   ✅ Sucesso!")
            else:
                print(f"   ⚠️  Erro: {proc.stderr[:200]}")
                
        except FileNotFoundError:
            print(f"   ❌ psql não está instalado")
            return False
        except Exception as e:
            print(f"   ⚠️  Erro: {e}")
            return False
    
    return True

def main():
    print("=" * 60)
    print("🗄️  SUPABASE MIGRATIONS RUNNER")
    print("=" * 60)
    
    print(f"\n📋 Projeto: {PROJECT_ID}")
    print(f"🌐 URL: {PROJECT_URL}")
    print(f"📂 Migrations: {MIGRATIONS_DIR}")
    
    # Ler migrations
    print("\n🔍 Procurando migrations...")
    migrations = read_migration_files()
    
    if not migrations:
        print("❌ Nenhuma migration encontrada!")
        return 1
    
    print(f"✅ {len(migrations)} migrations encontradas:")
    for m in migrations:
        print(f"   • {m['name']}")
    
    print("\n⚠️  Para executar as migrations, você tem 2 opções:")
    print("\n📋 OPÇÃO 1: SQL Editor do Dashboard (recomendado)")
    print("   1. Abra o Dashboard: https://app.supabase.com/project/pikskrtgivhifxpzrxyb")
    print("   2. Vá em: SQL Editor")
    print("   3. Crie uma nova query")
    print("   4. Copie/cole o conteúdo de CADA arquivo em: supabase/migrations/")
    print("   5. Execute um por um")
    
    print("\n📋 OPÇÃO 2: Via Terminal (precisa de psql)")
    print("   1. Instale: PostgreSQL (inclui psql)")
    print("   2. Execute este script novamente")
    
    print("\n💡 Recomendação: Use a OPÇÃO 1 (Dashboard)")
    print("   É mais simples e não requer instalação extra")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
