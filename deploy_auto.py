#!/usr/bin/env python3
"""
Deploy das Edge Functions via Python + urllib
Sem dependências externas
"""

import urllib.request
import urllib.error
import json
import base64
import os

PROJECT_ID = "ruujmkanbxofxljwzvas"
TOKEN = "sbp_2fd717aadfd154a265a5d6e34e067a67bcad7451"

FUNCTIONS = {
    "process-spreadsheet": "supabase/functions/process-spreadsheet/index.ts",
    "process-attendance": "supabase/functions/process-attendance/index.ts",
}

def read_file(path):
    """Ler arquivo"""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def deploy_function(func_name, code, token):
    """Deploy via urllib (Python puro)"""
    
    print(f"\n🚀 Deploy: {func_name}")
    print(f"   Tamanho: {len(code)} bytes")
    
    # URL
    url = f"https://api.supabase.com/v1/projects/{PROJECT_ID}/functions/{func_name}"
    
    # Payload
    payload = {
        "slug": func_name,
        "name": func_name,
        "verify_jwt": True,
        "code": base64.b64encode(code.encode()).decode(),
    }
    
    # Headers
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    # Request
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers=headers,
            method='PATCH'
        )
        
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode())
            print(f"   ✅ Status: {response.status}")
            print(f"   ✓ Deploy bem-sucedido!")
            print(f"   ID: {result.get('id', 'N/A')}")
            return True
            
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"   ❌ Erro HTTP {e.code}")
        
        try:
            error_json = json.loads(error_body)
            print(f"   Mensagem: {error_json.get('message', error_body[:100])}")
        except:
            print(f"   Resposta: {error_body[:200]}")
        
        return False
        
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def main():
    print("=" * 60)
    print("🚀 SUPABASE EDGE FUNCTIONS DEPLOY")
    print("=" * 60)
    
    print(f"\n📋 Projeto: {PROJECT_ID}")
    print(f"📂 Diretório: {os.getcwd()}")
    print(f"🔑 Token: {TOKEN[:20]}...\n")
    
    # Deploy
    results = {}
    for func_name, func_path in FUNCTIONS.items():
        print("=" * 60)
        
        if not os.path.exists(func_path):
            print(f"❌ Arquivo não encontrado: {func_path}")
            results[func_name] = False
            continue
        
        try:
            code = read_file(func_path)
            results[func_name] = deploy_function(func_name, code, TOKEN)
        except Exception as e:
            print(f"❌ Erro ao processar: {e}")
            results[func_name] = False
    
    # Resumo
    print(f"\n{'='*60}")
    print("📊 RESUMO")
    print("=" * 60)
    
    for func_name, success in results.items():
        status = "✅ Sucesso" if success else "❌ Falha"
        print(f"  {status}: {func_name}")
    
    success_count = sum(1 for v in results.values() if v)
    total = len(results)
    print(f"\n  Total: {success_count}/{total}")
    
    if success_count == total:
        print("\n🎉 Deploy completo! Pronto para testar!")
        return 0
    else:
        print("\n⚠️  Alguns deployments falharam")
        return 1

if __name__ == "__main__":
    exit(main())
