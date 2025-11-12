# 🖥️ DEPLOY VIA SUPABASE DASHBOARD

Como o Supabase CLI não está instalado, vamos fazer o deploy pelo Dashboard web.

## ✅ Passo a Passo

### Passo 1: Abra o Dashboard
1. Vá para: https://supabase.com/dashboard
2. Faça login com sua conta
3. Selecione o projeto do Clinic Data Atlas

### Passo 2: Acesse as Edge Functions
1. No menu lateral, procure por **"Edge Functions"**
2. Você verá a lista de funções:
   - process-spreadsheet
   - process-attendance
   - send-login-notification
   - send-signup-notification

### Passo 3: Deploy da Process-Spreadsheet
1. Clique em **"process-spreadsheet"**
2. Clique no botão **"Edit"** (ou ícone de lápis)
3. **Limpe** todo o código atual
4. **Cole** o código completo do arquivo:
   - Arquivo: `supabase/functions/process-spreadsheet/index.ts`

📋 **CÓDIGO PARA COPIAR**:
```
[VEJA O ARQUIVO: supabase/functions/process-spreadsheet/index.ts]
```

5. Clique em **"Save and Deploy"** (canto inferior direito)
6. Aguarde a mensagem de sucesso (cerca de 30 segundos)

### Passo 4: Deploy da Process-Attendance
1. Volte para a lista de Edge Functions
2. Clique em **"process-attendance"**
3. Repita os passos 2-6 acima com o código:
   - Arquivo: `supabase/functions/process-attendance/index.ts`

### Passo 5: Verificar Deploy
Após ambos os deploys, você verá:
- ✅ Status "Active" ou "Deployed"
- ✅ Timestamp da última atualização recente

## 🧪 Testar Agora

1. **Recarregue o dashboard**: http://localhost:8080 (F5)
2. **Faça upload** do arquivo simples: `test-simple-pacientes.xlsx`
3. **Verifique**:
   - Deve aparecer "Planilha processada! 3 pacientes atualizados"
   - Dashboard deve mostrar 3 pacientes na lista

## ⚠️ Se der erro 403 no Dashboard

Significa que o deploy NÃO funcionou. Possíveis causas:
1. Não copiou o código completo
2. Havia erros de sintaxe
3. Não clicou em "Save and Deploy"

**Verifique**: Após clicar "Save and Deploy", aparece mensagem verde de sucesso?

## 🔍 Para Debugar

Se quiser ver o que está acontecendo:

1. Abra DevTools: F12
2. Vá para Console
3. Faça um upload
4. Veja a mensagem de erro exata
5. Me envie a mensagem completa

---

## 📝 RESUMO

| Componente | Arquivo | Status |
|-----------|---------|---------|
| Code Updates | ✅ Removido admin check | Done |
| Deploy process-spreadsheet | 📋 Via Dashboard | Pending |
| Deploy process-attendance | 📋 Via Dashboard | Pending |
| Teste simples | 📋 test-simple-pacientes.xlsx | Pending |
| Teste grande | 📋 test-multisheet-patients.xlsx | Pending |

