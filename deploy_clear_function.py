"""
Deploy da Edge Function clear-database via Management API
Execute: python deploy_clear_function.py
"""
import requests
import os

# Suas credenciais do Supabase
SUPABASE_ACCESS_TOKEN = "sbp_seu_token_aqui"  # Pegue em: https://supabase.com/dashboard/account/tokens
PROJECT_REF = "ruujmkanbxofxljwzvas"

# Ler o código da função
with open("supabase/functions/clear-database/index.ts", "r", encoding="utf-8") as f:
    function_code = f.read()

# Fazer deploy via API
url = f"https://api.supabase.com/v1/projects/{PROJECT_REF}/functions/clear-database"

headers = {
    "Authorization": f"Bearer {SUPABASE_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "slug": "clear-database",
    "name": "clear-database",
    "verify_jwt": True,
    "import_map": False,
    "entrypoint_path": "index.ts",
    "body": function_code
}

print("📤 Fazendo deploy da função clear-database...")
response = requests.post(url, json=payload, headers=headers)

if response.status_code in [200, 201]:
    print("✅ Deploy realizado com sucesso!")
    print(response.json())
else:
    print(f"❌ Erro no deploy: {response.status_code}")
    print(response.text)
