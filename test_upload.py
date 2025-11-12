#!/usr/bin/env python3
"""
Test script para testar upload de pacientes
"""

import requests
import json
import os
from datetime import datetime

# ======================================
# CONFIGURAÇÃO
# ======================================

SUPABASE_URL = "https://pikskrtgivhifxpzrxyb.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBpa3NrcnRnaXZoaWZ4cHpyeHliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI4ODg2NzMsImV4cCI6MjA3ODQ2NDY3M30.s7bvipZ2lFe7bKCDp9Wwl_8y_PDP7ilj9GHh4IdJKnQ"
PROJECT_ID = "pikskrtgivhifxpzrxyb"

# URLs das Edge Functions
FUNCTION_PROCESS_PATIENTS = f"https://{PROJECT_ID}.supabase.co/functions/v1/process-spreadsheet"
FUNCTION_PROCESS_ATTENDANCE = f"https://{PROJECT_ID}.supabase.co/functions/v1/process-attendance"

# ======================================
# FUNÇÕES
# ======================================

def login_user():
    """Faz login e retorna o token"""
    print("\n📝 FAZENDO LOGIN...")
    
    url = f"{SUPABASE_URL}/auth/v1/signup"
    
    # Tenta com um email de teste
    email = f"test-{datetime.now().timestamp()}@test.com"
    password = "TestPassword123!"
    
    payload = {
        "email": email,
        "password": password
    }
    
    headers = {
        "apikey": SUPABASE_ANON_KEY,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            token = data.get('session', {}).get('access_token')
            print(f"✅ Login realizado com sucesso!")
            print(f"   Email: {email}")
            print(f"   Token: {token[:50]}...")
            return token
        else:
            print(f"❌ Erro ao fazer login: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")
        return None

def test_upload_patients(token, file_path):
    """Testa upload de pacientes"""
    print(f"\n📤 TESTANDO UPLOAD DE PACIENTES")
    print(f"   Arquivo: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ Arquivo não encontrado: {file_path}")
        return False
    
    # Ler arquivo
    with open(file_path, 'rb') as f:
        files = {'file': f}
        
        headers = {
            'Authorization': f'Bearer {token}'
        }
        
        try:
            print(f"   URL: {FUNCTION_PROCESS_PATIENTS}")
            response = requests.post(
                FUNCTION_PROCESS_PATIENTS,
                files=files,
                headers=headers,
                timeout=30
            )
            
            print(f"\n📊 RESPOSTA:")
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Sucesso!")
                print(f"   Processados: {data.get('processed', 0)}")
                print(f"   Erros: {data.get('errors', 0)}")
                print(f"   Total: {data.get('total', 0)}")
                
                if data.get('validationErrors'):
                    print(f"   Erros de validação:")
                    for error in data.get('validationErrors', [])[:5]:
                        print(f"      - {error}")
                
                return True
            else:
                print(f"   ❌ Erro: {response.status_code}")
                print(f"   Resposta: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Erro na requisição: {e}")
            return False

def main():
    print("=" * 60)
    print("🧪 TESTE DO SISTEMA - CLINIC DATA ATLAS")
    print("=" * 60)
    
    # 1. Fazer login
    token = login_user()
    if not token:
        print("\n❌ Falha ao fazer login. Abortando...")
        return
    
    # 2. Testar upload simples
    success = test_upload_patients(
        token,
        "c:\\Users\\Joao\\Desktop\\clinic-data-atlas-main\\test-simples.csv"
    )
    
    if success:
        print("\n" + "=" * 60)
        print("✅ TESTE CONCLUÍDO COM SUCESSO!")
        print("=" * 60)
        print("\n📝 Próximos passos:")
        print("   1. Abra http://localhost:5173 no navegador")
        print("   2. Faça login com o mesmo usuário")
        print("   3. Verifique se os 3 pacientes aparecem no dashboard")
    else:
        print("\n" + "=" * 60)
        print("❌ TESTE FALHOU")
        print("=" * 60)

if __name__ == "__main__":
    main()
