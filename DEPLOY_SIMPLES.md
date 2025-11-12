# 🚀 DEPLOY VERSÃO SIMPLES (FUNCIONA!)

## ⚠️ PROBLEMA

A versão complexa com npm: specifiers está dando erro ao fazer deploy.

## ✅ SOLUÇÃO

Vamos usar uma versão simples que **com certeza funciona**!

---

## 📋 PASSO 1: Copiar Código Simples

Abra o arquivo:
```
supabase/functions/process-spreadsheet/index_simples.ts
```

Copie TODO o código (Ctrl+A → Ctrl+C).

---

## 📝 PASSO 2: Fazer Deploy no Dashboard

1. Vá para: https://app.supabase.com/project/pikskrtgivhifxpzrxyb
2. Menu: **Edge Functions**
3. Clique em: **process-spreadsheet** (a que já existe)
4. Clique em: **Edit** (ou lápis)
5. Selecione TODO o código atual (Ctrl+A)
6. Delete
7. Cole o novo código (Ctrl+V)
8. Clique: **Deploy**

---

## 🧪 PASSO 3: Testar

Após deploy com sucesso:

1. Volte para http://localhost:5173
2. Faça login
3. Clique: "Escolher Arquivo"
4. Selecione: `test-simples.csv`
5. Clique: "Processar Pacientes"

---

## ✅ RESULTADO ESPERADO

```json
{
  "success": true,
  "processed": 3,
  "inserted": 3,
  "errors": 0,
  "total": 3
}
```

Dashboard deve mostrar **3 pacientes**!

---

## 🔁 REPETIR PARA process-attendance

Depois de fazer upload de pacientes, você pode fazer upload de frequência:

1. Clique: "Escolher Arquivo"
2. Selecione: `test-simples-attendance.csv`
3. Clique: "Processar Frequência"

---

**Consegue fazer o deploy da versão simples?** 💪

