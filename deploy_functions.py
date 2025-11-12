"""
Script para fazer deploy das Edge Functions via Supabase Management API
"""

import subprocess
import json
import os

def get_access_token():
    """Obter access token do Supabase"""
    # Tenta via supabase cli se disponível
    try:
        result = subprocess.run(
            ["supabase", "projects", "access-token"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception as e:
        print(f"❌ Erro ao obter token via CLI: {e}")
    
    return None

def deploy_function(project_id, access_token, function_name, function_path):
    """Deploy de uma Edge Function"""
    
    # Ler o arquivo da função
    with open(function_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    print(f"\n📤 Fazendo deploy de {function_name}...")
    print(f"   Arquivo: {function_path}")
    print(f"   Tamanho: {len(code)} bytes")
    
    # API endpoint
    api_url = f"https://api.supabase.com/v1/projects/{project_id}/functions/{function_name}"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "slug": function_name,
        "name": function_name,
        "verify_jwt": True,
        "imported_libraries": [],
        "code": code
    }
    
    print(f"   URL: {api_url}")
    print(f"   Headers: {list(headers.keys())}")
    
    # Fazer request
    try:
        import urllib.request
        req = urllib.request.Request(
            api_url,
            data=json.dumps(payload).encode('utf-8'),
            headers=headers,
            method='PATCH'
        )
        
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            print(f"   ✅ Status: {response.status}")
            return True
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def main():
    print("🚀 SUPABASE EDGE FUNCTIONS DEPLOY")
    print("=" * 50)
    
    project_id = "ruujmkanbxofxljwzvas"
    
    print(f"\n📋 Project ID: {project_id}")
    
    # Obter token
    token = get_access_token()
    
    if not token:
        print("\n❌ Não foi possível obter access token do Supabase!")
        print("\n💡 Alternativas:")
        print("   1. Use o Supabase Dashboard para fazer deploy manual")
        print("   2. Instale a CLI do Supabase: https://supabase.com/docs/guides/cli")
        print("   3. Veja: DEPLOY_VIA_DASHBOARD.md")
        return
    
    print(f"✅ Access token obtido: {token[:20]}...")
    
    # Deploy das funções
    functions = [
        ("process-spreadsheet", "supabase/functions/process-spreadsheet/index.ts"),
        ("process-attendance", "supabase/functions/process-attendance/index.ts"),
    ]
    
    success_count = 0
    for func_name, func_path in functions:
        if deploy_function(project_id, token, func_name, func_path):
            success_count += 1
    
    print(f"\n📊 RESULTADO: {success_count}/{len(functions)} funções deployadas com sucesso")

if __name__ == "__main__":
    main()
