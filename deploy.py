#!/usr/bin/env python3
"""
Script para fazer deploy das Edge Functions via API REST do Supabase
Sem precisar da CLI instalada
"""

import os
import json
import base64
import sys

# Configurações
PROJECT_ID = "ruujmkanbxofxljwzvas"
FUNCTIONS = {
    "process-spreadsheet": "supabase/functions/process-spreadsheet/index.ts",
    "process-attendance": "supabase/functions/process-attendance/index.ts",
}

def read_function_code(filepath):
    """Ler o código da função"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def get_supabase_token():
    """
    Obter o access token do Supabase
    Tenta vários métodos:
    1. Variável de ambiente SUPABASE_ACCESS_TOKEN
    2. Ler de .supabase/access-token se existir
    3. Usar a chave de serviço do .env
    """
    
    # Método 1: Variável de ambiente
    if 'SUPABASE_ACCESS_TOKEN' in os.environ:
        token = os.environ['SUPABASE_ACCESS_TOKEN']
        if token and token != 'Bearer test':
            print("✓ Token obtido de: SUPABASE_ACCESS_TOKEN")
            return token
    
    # Método 2: Arquivo .supabase/access-token
    token_file = os.path.expanduser("~/.supabase/access-token")
    if os.path.exists(token_file):
        with open(token_file, 'r') as f:
            token = f.read().strip()
            if token:
                print(f"✓ Token obtido de: {token_file}")
                return token
    
    # Método 3: Ler do .env
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            for line in f:
                if 'SERVICE_ROLE_KEY' in line:
                    token = line.split('=', 1)[1].strip().strip('"')
                    if token:
                        print("✓ Token obtido de: .env (SERVICE_ROLE_KEY)")
                        return token
    
    print("⚠ Token não encontrado!")
    return None

def deploy_function_via_github(function_name, code):
    """
    Deploy via GitHub Actions (alternativa)
    Salva o código em um arquivo temporário
    """
    print(f"\n  📁 Salvando código em arquivo temporário...")
    temp_file = f"./{function_name}_deploy.ts"
    
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(code)
    
    print(f"  ✓ Código salvo em: {temp_file}")
    return temp_file

def deploy_function(function_name, code, token=None):
    """Deploy uma função"""
    
    print(f"\n🚀 Deploy de: {function_name}")
    print(f"   Tamanho do código: {len(code)} bytes")
    
    if token:
        print(f"   Método: API REST do Supabase")
        return deploy_via_api(function_name, code, token)
    else:
        print(f"   Método: Via Dashboard (manual)")
        print(f"   ⚠ Token não encontrado, você precisará fazer upload manualmente")
        print(f"   Link: https://supabase.com/dashboard/project/{PROJECT_ID}/functions")
        return False

def deploy_via_api(function_name, code, token):
    """Deploy via API REST"""
    try:
        import urllib.request
        import urllib.error
        
        # URL da API
        url = f"https://api.supabase.com/v1/projects/{PROJECT_ID}/functions/{function_name}"
        
        # Payload (base64 do código)
        payload = {
            "slug": function_name,
            "name": function_name,
            "verify_jwt": True,
            "code": base64.b64encode(code.encode()).decode(),
        }
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        
        print(f"   Enviando para: {url}")
        print(f"   Headers: Authorization: Bearer {token[:20]}...")
        
        # Fazer request
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers=headers,
            method='PATCH'
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                result = response.read().decode()
                print(f"   ✅ Status: {response.status}")
                print(f"   ✓ Deploy bem-sucedido!")
                return True
        except urllib.error.HTTPError as e:
            error_body = e.read().decode()
            print(f"   ❌ Erro HTTP {e.code}")
            print(f"   Mensagem: {error_body[:200]}")
            return False
            
    except Exception as e:
        print(f"   ❌ Erro ao fazer deploy: {e}")
        return False

def main():
    print("=" * 60)
    print("🚀 SUPABASE EDGE FUNCTIONS AUTO-DEPLOY")
    print("=" * 60)
    
    print(f"\n📋 Projeto: {PROJECT_ID}")
    print(f"📂 Diretório: {os.getcwd()}")
    
    # Obter token
    print("\n🔑 Obtendo access token...")
    token = get_supabase_token()
    
    if not token:
        print("\n⚠️  Access token não encontrado!")
        print("\n   Para fazer deploy via API, você precisa de um dos:")
        print("   1. Variável: SUPABASE_ACCESS_TOKEN")
        print("   2. Arquivo: ~/.supabase/access-token")
        print("   3. Chave no .env: SERVICE_ROLE_KEY")
        print("\n   Você pode obter em:")
        print("   → https://supabase.com/dashboard/account/tokens")
        print("\n   Ou fazer deploy manual via Dashboard:")
        print("   → https://supabase.com/dashboard/project/{PROJECT_ID}/functions")
    
    # Deploy das funções
    results = {}
    for func_name, func_path in FUNCTIONS.items():
        print(f"\n{'='*60}")
        
        # Verificar se arquivo existe
        if not os.path.exists(func_path):
            print(f"❌ Arquivo não encontrado: {func_path}")
            results[func_name] = False
            continue
        
        # Ler código
        try:
            code = read_function_code(func_path)
            print(f"✓ Arquivo lido: {func_path} ({len(code)} bytes)")
        except Exception as e:
            print(f"❌ Erro ao ler {func_path}: {e}")
            results[func_name] = False
            continue
        
        # Deploy
        results[func_name] = deploy_function(func_name, code, token)
    
    # Resumo
    print(f"\n{'='*60}")
    print("📊 RESUMO DO DEPLOY")
    print("=" * 60)
    
    success_count = sum(1 for v in results.values() if v)
    total_count = len(results)
    
    for func_name, success in results.items():
        status = "✅ Sucesso" if success else "❌ Falha"
        print(f"  {status}: {func_name}")
    
    print(f"\n  Total: {success_count}/{total_count} funções deployadas")
    
    if success_count == total_count:
        print("\n🎉 Deploy completo! Tudo pronto para testar!")
        return 0
    elif success_count > 0:
        print("\n⚠️  Deploy parcial. Algumas funções falharam.")
        return 1
    else:
        print("\n❌ Nenhuma função foi deployada.")
        print("\n💡 Próximos passos:")
        print("   1. Obtenha um access token do Supabase")
        print("   2. Execute: SUPABASE_ACCESS_TOKEN=seu_token python deploy.py")
        print("   OU use o Dashboard: https://supabase.com/dashboard")
        return 1

if __name__ == "__main__":
    sys.exit(main())
