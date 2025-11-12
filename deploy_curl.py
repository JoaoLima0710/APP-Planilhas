#!/usr/bin/env python3
"""
Deploy das Edge Functions via cURL + Python
Sem precisar de CLI ou acesso ao Dashboard
"""

import subprocess
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

def deploy_with_curl(func_name, code, token):
    """Fazer deploy usando cURL"""
    
    print(f"\n🚀 Deploy de: {func_name}")
    print(f"   Tamanho: {len(code)} bytes")
    
    # Preparar payload
    payload = {
        "slug": func_name,
        "name": func_name,
        "verify_jwt": True,
        "code": base64.b64encode(code.encode()).decode(),
    }
    
    # URL
    url = f"https://api.supabase.com/v1/projects/{PROJECT_ID}/functions/{func_name}"
    
    # Headers
    headers = f"Authorization: Bearer {token}"
    
    # Preparar comando cURL
    cmd = [
        "curl",
        "-X", "PATCH",
        url,
        "-H", headers,
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload)
    ]
    
    print(f"   URL: {url}")
    print(f"   Token: {token[:20]}...")
    
    # Executar
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            response = json.loads(result.stdout)
            if "id" in response or "slug" in response:
                print(f"   ✅ Deploy bem-sucedido!")
                return True
            else:
                print(f"   ⚠️  Resposta: {result.stdout[:200]}")
                return False
        else:
            print(f"   ❌ Erro: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"   ❌ Erro ao executar cURL: {e}")
        return False

def main():
    print("=" * 60)
    print("🚀 SUPABASE EDGE FUNCTIONS DEPLOY (cURL)")
    print("=" * 60)
    
    print(f"\n📋 Projeto: {PROJECT_ID}")
    print(f"📂 Diretório: {os.getcwd()}")
    print(f"🔑 Token: {TOKEN[:20]}...")
    
    # Deploy
    results = {}
    for func_name, func_path in FUNCTIONS.items():
        print(f"\n{'='*60}")
        
        if not os.path.exists(func_path):
            print(f"❌ Arquivo não encontrado: {func_path}")
            results[func_name] = False
            continue
        
        try:
            code = read_file(func_path)
            results[func_name] = deploy_with_curl(func_name, code, TOKEN)
        except Exception as e:
            print(f"❌ Erro: {e}")
            results[func_name] = False
    
    # Resumo
    print(f"\n{'='*60}")
    print("📊 RESUMO")
    print("=" * 60)
    
    for func_name, success in results.items():
        status = "✅ Sucesso" if success else "❌ Falha"
        print(f"  {status}: {func_name}")
    
    success_count = sum(1 for v in results.values() if v)
    print(f"\n  Total: {success_count}/{len(results)}")
    
    if success_count == len(results):
        print("\n🎉 Deploy completo!")
    else:
        print("\n⚠️  Alguns deployments falharam")

if __name__ == "__main__":
    main()
