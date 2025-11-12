# 🚀 DEPLOY AUTOMÁTICO - GUIA FINAL

## ✅ Tenho um script pronto que faz tudo!

Arquivo criado: `deploy.mjs`

## 📋 Passo-a-Passo (3 passos simples)

### Passo 1️⃣: Obter Access Token (2 minutos)

1. Abra: https://supabase.com/dashboard/account/tokens
2. Clique: **"Create a new token"**
3. Nome: **"Deploy Script"**
4. Permissões: marque **"functions_deploy"**
5. Clique: **"Generate token"**
6. **Copie** o token (Ctrl+C)
7. ⚠️ **NÃO FECHE** a página

### Passo 2️⃣: Executar o Deploy (30 segundos)

Abra PowerShell e execute:

```powershell
cd c:\Users\Joao\Desktop\clinic-data-atlas-main
$env:SUPABASE_ACCESS_TOKEN = 'Cole seu token aqui'
node deploy.mjs
```

Resultado esperado:
```
✅ Sucesso: process-spreadsheet
✅ Sucesso: process-attendance
Total: 2/2
🎉 Deploy completo!
```

### Passo 3️⃣: Testar (1 minuto)

1. Abra: http://localhost:8080
2. Recarregue: F5
3. Upload: **test-simple-pacientes.xlsx**
4. Deve aparecer: ✅ "Planilha processada! 3 pacientes atualizados"

---

## 📞 Precisa de Ajuda?

### "Não acho a página de tokens"
→ https://supabase.com/dashboard/account/tokens

### "Qual botão clico?"
→ Botão azul "Create a new token"

### "O token aparece uma vez?"
→ Sim! Copie na hora. Se perder, gera outro.

### "E se der erro?"
→ Me manda a mensagem de erro

---

## 🎯 Resumo dos Arquivos

| Arquivo | Função |
|---------|--------|
| `deploy.mjs` | 🚀 Script de deploy automático |
| `GET_ACCESS_TOKEN.md` | 🔑 Como obter o token |
| `DEPLOY_VISUAL.md` | 📸 Deploy manual via Dashboard |
| `DEPLOY_QUICK.md` | ⚡ Copy-paste manual |

---

## 🔄 Fluxo Completo

```
1. Obter Token (2 min)
        ↓
2. Executar: node deploy.mjs (30 seg)
        ↓
3. Testar no dashboard (1 min)
        ↓
✅ SUCESSO!
```

**Total: ~3-4 minutos**

---

## ❓ O script vai funcionar?

✅ **SIM!** O `deploy.mjs` vai:
1. Ler os arquivos das Edge Functions
2. Enviar via API REST do Supabase
3. Fazer o deploy automáticamente
4. Mostrar o resultado

Tudo sem CLI, só Node!

---

**Bora lá? Vamos fazer esse deploy! 💪**

```powershell
node deploy.mjs
```

