# 📋 COPY & PASTE - DEPLOY SUPER RÁPIDO

## 🎯 Objetivo
Substituir o código das Edge Functions via Dashboard

---

## ✅ PASSO 1: Abra no Dashboard

Clique aqui:
👉 https://supabase.com/dashboard/project/ruujmkanbxofxljwzvas/functions

---

## ✅ PASSO 2: Deploy process-spreadsheet

### 1. Clique em: **process-spreadsheet**

Você vê a função listada. Clique nela.

### 2. Clique em: **Edit** (ícone ✏️)

Um editor vai abrir com código TypeScript.

### 3. Limpe TUDO

No editor:
- Pressione: `Ctrl + A`
- Pressione: `Delete`

Pronto, editor vazio!

### 4. Copie o código NOVO

#### Abra VS Code

Arquivo: `supabase/functions/process-spreadsheet/index.ts`

No arquivo, pressione: `Ctrl + A` (seleciona tudo)
Pressione: `Ctrl + C` (copia)

#### Volte ao Dashboard

No editor do Dashboard, pressione: `Ctrl + V` (cola)

✅ O código novo está lá!

### 5. Salve e Faça Deploy

Procure o botão **"Save and Deploy"** (canto inferior direito, azul ou verde)

Clique nele!

⏳ Aguarde ~30-60 segundos...

### 6. Verifique Sucesso

Você deve ver:
```
✅ Deployment successful
Status: Active
```

Se ver isso, parte 1 concluída! ✅

---

## ✅ PASSO 3: Deploy process-attendance

**REPITA OS PASSOS 1-6 ACIMA, MAS:**

- Na etapa 1: clique em **process-attendance** (não process-spreadsheet)
- Na etapa 4: copie de: `supabase/functions/process-attendance/index.ts`

---

## ✅ PASSO 4: Confirme Ambas

Volte à lista de funções.

Você deve ver:

```
process-spreadsheet
├─ Status: Active ✅
├─ Updated: Nov 11, 2025 at XX:XX

process-attendance
├─ Status: Active ✅
├─ Updated: Nov 11, 2025 at XX:XX
```

---

## ✅ PASSO 5: Teste

### Abra o dashboard local:
```
http://localhost:8080
```

### Recarregue:
```
Pressione: F5
```

### Upload do teste:
1. Procure por "Upload de Planilhas"
2. Clique em "Selecione um arquivo"
3. Procure por: `test-simple-pacientes.xlsx`
4. Clique em "Processar"

### Deve aparecer:
```
✅ Planilha processada! 3 pacientes atualizados
```

### Verifique a lista:
```
Pacientes Registrados
│ P0001 │ João Silva │ SUL │
│ P0002 │ Maria Santos │ OESTE │
│ P0003 │ Pedro Costa │ LESTE │
```

---

## 🎉 PRONTO!

Se conseguiu até aqui, o deploy funcionou! 🚀

Agora você pode testar com o arquivo grande:
- `test-multisheet-patients.xlsx` (1.650 pacientes)

---

## 🆘 Se der problema

### "Não consigo colar o código"
- Limpe TUDO primeiro (Ctrl+A, Delete)
- Depois cola (Ctrl+V)

### "Deployment failed"
- Verifique se copiou o arquivo correto
- Verifique se começar com: `import "https://`
- Veja os logs (botão "View logs")

### "Status não muda para Active"
- Aguarde mais tempo (pode levar 1-2 minutos)
- Recarregue a página (F5)

### "Ainda recebo 403 no upload"
- O deploy pode não ter funcionado
- Verifique se status está "Active"
- Tente fazer upload novamente

---

**Consegue fazer? Bora lá! 💪**

