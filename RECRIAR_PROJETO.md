# 🆕 RECRIAR O PROJETO SUPABASE DO ZERO

## 📋 Passo 1: Criar Novo Projeto

1. **No Dashboard**, clique: **"New project"** (botão verde)

2. **Preencha os dados:**
   - **Project name**: `clinic-data-atlas` (ou outro nome)
   - **Database password**: Use uma senha segura (ex: `Senha@123!`)
   - **Region**: Escolha mais próximo de você (ex: `us-east-1` ou `eu-west-1`)
   - **Pricing Plan**: Deixe em `Free`

3. **Clique**: **"Create new project"**

4. ⏳ **Aguarde**: Pode levar 2-5 minutos para criar...

---

## 📋 Passo 2: Pegar o Project ID

Após criado, anote:
- **Project URL**: algo como `https://xxxxx.supabase.co`
- **Project ID**: a parte `xxxxx` (você vai precisar)

---

## 📋 Passo 3: Conectar ao Seu Projeto Local

Abra o arquivo `.env` no seu projeto:

```
c:\Users\Joao\Desktop\clinic-data-atlas-main\.env
```

Atualize com os valores do novo projeto:

```env
VITE_SUPABASE_PROJECT_ID="novo_project_id_aqui"
VITE_SUPABASE_PUBLISHABLE_KEY="sua_chave_publica_aqui"
VITE_SUPABASE_URL="https://novo_project_id.supabase.co"
```

Onde conseguir os valores:
1. No Dashboard, vá em: **Settings > API**
2. Copie:
   - `URL` → `VITE_SUPABASE_URL`
   - `anon key` → `VITE_SUPABASE_PUBLISHABLE_KEY`
   - Project ID → `VITE_SUPABASE_PROJECT_ID`

---

## 📋 Passo 4: Sincronizar Migrations

Agora precisa criar as tabelas do zero. Você tem 2 opções:

### Opção A: Via Supabase Local (MELHOR)

```powershell
cd c:\Users\Joao\Desktop\clinic-data-atlas-main

# Instalar Docker (se não tiver)
# Depois:
supabase start

# Depois:
supabase db pull  # Puxar schema do projeto remote
supabase db push  # Enviar para o projeto remote
```

### Opção B: Via SQL Manual

1. No Dashboard do novo projeto, vá em: **SQL Editor**

2. **Crie uma nova query** e copie/cole **TODOS** os arquivos de migration:

```
supabase/migrations/*.sql
```

Execute um por um (ou todos juntos).

---

## 📋 Passo 5: Testar Conexão

Abra o dashboard local:

```
http://localhost:8080
```

Se conseguir ver dados sem erro, ótimo! Conexão funcionando!

---

## 📋 Passo 6: Deploy das Edge Functions

Agora você pode fazer deploy das funções:

1. No novo Dashboard, vá em: **Edge Functions**

2. Siga: **DEPLOY_MANUAL.md**

3. Copie os códigos de:
   - `supabase/functions/process-spreadsheet/index.ts`
   - `supabase/functions/process-attendance/index.ts`

---

## 🎉 Pronto!

Seu projeto está recriado e atualizado!

---

## ⚠️ O que fazer com os dados antigos?

Se tinha dados no projeto anterior:
- ❌ Não há como recuperar (foi deletado)
- ✅ Mas você pode fazer upload novamente agora!

---

**Consegue criar o novo projeto?** 💪

