# ⚡ DEPLOY RÁPIDO - COPY & PASTE

## 🎯 Objetivo
Fazer deploy das 2 Edge Functions atualizadas

## ✅ Passo 1: Abra o Dashboard
```
https://supabase.com/dashboard/project/ruujmkanbxofxljwzvas/functions
```

## ✅ Passo 2: Deploy process-spreadsheet

1. Clique em **process-spreadsheet** na lista
2. Clique em **Edit** (ícone de lápis)
3. **Limpe TUDO** (Ctrl+A, Delete)
4. **COPIE** todo o código abaixo (de "import" até o final):

---

### 📋 CÓDIGO para process-spreadsheet:

[LEIA O ARQUIVO: supabase/functions/process-spreadsheet/index.ts E COPIE TUDO]

---

5. **Cole** no editor (Ctrl+V)
6. Clique **"Save and Deploy"** (botão verde, canto inferior direito)
7. ⏳ Aguarde mensagem verde de sucesso (~30 segundos)

## ✅ Passo 3: Deploy process-attendance

Repita os passos 1-7 acima, mas:
- Clique em **process-attendance** (não process-spreadsheet)
- **COPIE** todo o código de: supabase/functions/process-attendance/index.ts

---

### 📋 CÓDIGO para process-attendance:

[LEIA O ARQUIVO: supabase/functions/process-attendance/index.ts E COPIE TUDO]

---

## ✅ Passo 4: Verifique o Status

Após os 2 deploys, ambas as funções devem estar com status **"Active"** e um timestamp recente.

## 🧪 Passo 5: Teste

1. Abra http://localhost:8080
2. Recarregue (F5)
3. Faça upload de: **test-simple-pacientes.xlsx**
4. Deve aparecer: ✅ "Planilha processada! 3 pacientes atualizados"

## 💪 Está pronto!

Após confirmar que funcionou com o arquivo simples, teste com:
- **test-multisheet-patients.xlsx** (1.650 pacientes)

---

## ❓ Dúvidas

**P: Qual arquivo copiar?**
R: `supabase/functions/process-spreadsheet/index.ts` (todo o conteúdo)

**P: Pode deixar comentários no código?**
R: Sim! Comentários em TypeScript são permitidos.

**P: O código é muito grande, como copiar?**
R: Abra o arquivo no VS Code, selecione tudo (Ctrl+A), copie (Ctrl+C), cole no Dashboard (Ctrl+V)

**P: E se der erro ao colar?**
R: Pode ser erro de sintaxe. Verifique se copiou tudo, sem quebras.

**P: Quanto tempo leva para fazer deploy?**
R: De 20-60 segundos. Aguarde a mensagem verde.

