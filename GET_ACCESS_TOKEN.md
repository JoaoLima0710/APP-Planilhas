# 🔑 OBTER ACCESS TOKEN DO SUPABASE

## Por que preciso de um access token?

Para fazer deploy automático das Edge Functions, preciso de autorização. Você pode gerar um token em poucos cliques!

## ✅ Passo 1: Abra a página de tokens

👉 https://supabase.com/dashboard/account/tokens

Ou manualmente:
1. Vá para: https://supabase.com/dashboard
2. Clique no seu avatar (canto superior direito)
3. Clique em: **Account Settings** (ou Configurações)
4. Menu esquerdo: **Access Tokens** (ou Tokens de Acesso)

## ✅ Passo 2: Gere um novo token

1. Clique no botão: **"Create a new token"** (ou "Novo Token")
2. Dê um nome: **"Deploy Script"** ou qualquer coisa
3. Escolha permissões:
   - ✅ **functions_deploy** (obrigatório)
   - ✅ **projects_read** (opcional mas bom ter)
4. Clique: **"Generate token"** (Gerar Token)

## ✅ Passo 3: Copie o token

**⚠️ IMPORTANTE**: O token aparece UMA VEZ APENAS!

1. Copie o token completo (Ctrl+C)
2. **NÃO feche** a página ainda!

## ✅ Passo 4: Use o token para deploy

### Opção A: PowerShell (Recomendado)
```powershell
$env:SUPABASE_ACCESS_TOKEN = 'cole_seu_token_aqui'
node deploy.mjs
```

### Opção B: Uma linha
```powershell
$env:SUPABASE_ACCESS_TOKEN = 'seu_token'; node deploy.mjs
```

### Opção C: CMD
```cmd
set SUPABASE_ACCESS_TOKEN=seu_token_aqui
node deploy.mjs
```

## 🎯 Exemplo prático

Se seu token é: `sbp_abc123def456xyz...`

```powershell
# PowerShell
$env:SUPABASE_ACCESS_TOKEN = 'sbp_abc123def456xyz'
node deploy.mjs
```

## ✅ Esperar o resultado

Você deve ver:
```
==============================================================
🚀 SUPABASE EDGE FUNCTIONS AUTO-DEPLOY
==============================================================

📋 Projeto: ruujmkanbxofxljwzvas
📂 Diretório: C:\Users\Joao\Desktop\clinic-data-atlas-main

🔑 Obtendo access token...
✓ Token de: SUPABASE_ACCESS_TOKEN

============================================================== 
🚀 Deploy: process-spreadsheet
   Tamanho: 14520 bytes
   Status HTTP: 200
   ✅ Deploy bem-sucedido!

============================================================== 
🚀 Deploy: process-attendance
   Tamanho: 12850 bytes
   Status HTTP: 200
   ✅ Deploy bem-sucedido!

==============================================================
📊 RESUMO
==============================================================
  ✅ Sucesso: process-spreadsheet
  ✅ Sucesso: process-attendance

  Total: 2/2

🎉 Deploy completo! Pronto para testar!
```

## 🔒 Segurança

- ✅ O token é temporário (só para este deployment)
- ✅ Pode ser revogado depois
- ✅ Não fica salvo em arquivo
- ✅ Não fica no histórico do terminal (use `$env:`)

## 🆘 Se der erro

Se receber um erro como:
```
❌ Erro: Unauthorized
```

Significa:
- ❌ Token expirado ou inválido
- ❌ Token não tem permissão `functions_deploy`
- ❌ Copiou parcialmente

Solução:
1. Regenere um novo token
2. Verifique se tem permissão `functions_deploy`
3. Copie o token completo (sem espaços)

---

**Pronto? Bora fazer o deploy! 💪**

