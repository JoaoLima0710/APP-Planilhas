# 🚀 DEPLOY DAS EDGE FUNCTIONS

## 📝 O que fazer?

Fazer deploy de 2 Edge Functions (são os "servidores" que processam seus uploads).

---

## ✅ FUNÇÃO 1: process-spreadsheet

### PASSO 1: Abra Dashboard
- URL: https://app.supabase.com/project/pikskrtgivhifxpzrxyb
- Menu esquerdo: **Edge Functions**
- Botão: **Create a new function**

### PASSO 2: Dê um nome
- Nome: `process-spreadsheet`
- Clique: **Create function**

### PASSO 3: Copie o código

Abra o arquivo:
```
supabase/functions/process-spreadsheet/index.ts
```

Selecione TODO o conteúdo (Ctrl+A) e copie (Ctrl+C).

### PASSO 4: Cole no Dashboard

No editor da função no Dashboard:
- Apague o código padrão
- Cole o código (Ctrl+V)
- Clique: **Deploy**

Você verá:
```
✅ Deploying function...
✅ Function deployed!
```

---

## ✅ FUNÇÃO 2: process-attendance

### PASSO 1: Nova função
- Botão: **Create a new function** (ou vá em Edge Functions > + icon)

### PASSO 2: Dê um nome
- Nome: `process-attendance`
- Clique: **Create function**

### PASSO 3: Copie o código

Abra o arquivo:
```
supabase/functions/process-attendance/index.ts
```

Selecione TODO o conteúdo (Ctrl+A) e copie (Ctrl+C).

### PASSO 4: Cole no Dashboard

No editor:
- Apague o código padrão
- Cole (Ctrl+V)
- Clique: **Deploy**

---

## ✅ VERIFICAR DEPLOY

1. Vá em: **Edge Functions**
2. Você deve ver 2 funções:
   - ✅ process-spreadsheet
   - ✅ process-attendance

3. Clique em cada uma e verifique se tem status ✅

---

## 🎯 Próximo Passo

Após ambas estarem deployadas:

1. Volte para seu VS Code
2. Abra terminal: `npm run dev`
3. Vá em: http://localhost:5173
4. Teste fazer upload de um arquivo CSV/XLSX

Você deve ver:
- Arquivo enviado ✅
- Pacientes carregados no dashboard ✅
- Contador de pacientes atualizado ✅

---

## ⏱️ Tempo Estimado

- Deploy 1: ~1 minuto
- Deploy 2: ~1 minuto
- **Total: ~2 minutos**

---

## ❓ Dúvidas?

- Se der erro no deploy: copie o erro e vou ajudar
- Se não aparecer opção "Create a new function": recarregue a página

**Consegue fazer os deploys?** 💪

