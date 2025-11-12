import os
from supabase import create_client, Client

# Configuração do Supabase
SUPABASE_URL = "https://your-project-url.supabase.co"  # Substitua pela sua URL
SUPABASE_SERVICE_KEY = "your-service-role-key"  # Substitua pela sua service key

def clear_patients_table():
    try:
        # Criar cliente Supabase
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
        
        # Deletar todos os registros
        print("Limpando tabela patients...")
        response = supabase.from_("patients").delete().neq("id", "00000000-0000-0000-0000-000000000000").execute()
        
        print("✅ Tabela patients limpa com sucesso!")
        
        # Verificar quantos registros restam
        count_response = supabase.from_("patients").select("id", count="exact").execute()
        print(f"Registros restantes: {count_response.count}")
        
    except Exception as e:
        print(f"❌ Erro ao limpar o banco: {e}")

if __name__ == "__main__":
    print("⚠️  ATENÇÃO: Este script irá deletar TODOS os registros da tabela patients!")
    confirm = input("Deseja continuar? (sim/não): ")
    
    if confirm.lower() in ['sim', 's', 'yes', 'y']:
        clear_patients_table()
    else:
        print("Operação cancelada.")
