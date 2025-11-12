# 🖥️ DEPLOY VIA DASHBOARD (SOLUÇÃO ALTERNATIVA)

## ✅ Como fazer deploy manualmente (sem CLI)

A conta Supabase free não tem permissão para deploy via API.
Vamos usar o Dashboard web, que é super simples!

---

## 📋 Passo 1: Abra o Dashboard

👉 https://supabase.com/dashboard/project/ruujmkanbxofxljwzvas/functions

Ou manualmente:
1. https://supabase.com/dashboard
2. Selecione: **ruujmkanbxofxljwzvas**
3. Menu esquerdo: **Edge Functions**

---

## 📋 Passo 2: Deploy process-spreadsheet

### Localize a função
- Procure por: **process-spreadsheet**
- Clique nela

### Clique em Edit
- Você vê um botão ✏️ ou "Edit"
- Clique para abrir o editor

### Limpe o código antigo
- Dentro do editor, pressione: **Ctrl + A** (seleciona tudo)
- Pressione: **Delete**

### Cole o novo código

**Abra o arquivo**: `supabase/functions/process-spreadsheet/index.ts` no seu VS Code

Copie TUDO (Ctrl+A, Ctrl+C)

Volta ao Dashboard e cole (Ctrl+V)

### Salve e faça deploy
- Procure o botão: **"Save and Deploy"** (azul ou verde)
- Clique nele
- ⏳ Aguarde 30-60 segundos

### Você deve ver
```
✅ Deployment successful
Status: Active
Updated: Nov 11, 2025 at 21:XX
```

---

## 📋 Passo 3: Deploy process-attendance

Repita o Passo 2, mas:
- Função: **process-attendance**
- Arquivo: `supabase/functions/process-attendance/index.ts`

---

## ✅ Confirme o Resultado

Ambas devem estar assim:

```
process-spreadsheet ✅ Active
├─ Updated: Nov 11, 2025 at 21:XX

process-attendance ✅ Active
├─ Updated: Nov 11, 2025 at 21:XX
```

---

## 🧪 Teste Agora

1. Abra: http://localhost:8080
2. Recarregue: F5
3. Upload: **test-simple-pacientes.xlsx** (3 pacientes)
4. Deve aparecer: ✅ "Planilha processada! 3 pacientes atualizados"

---

## 💡 Dicas

- ✅ Pode deixar comentários no código
- ✅ O editor detecta erros de sintaxe (linha vermelha)
- ✅ Botão "Save and Deploy" fica na parte inferior
- ✅ Pode levar até 1 minuto para fazer deploy

---

## 🎯 Resumo

| Passo | O que fazer | Tempo |
|-------|------------|-------|
| 1 | Abrir Dashboard | 30 seg |
| 2 | Deploy process-spreadsheet | 1 min |
| 3 | Deploy process-attendance | 1 min |
| 4 | Testar upload | 1 min |
| **Total** | | **~3-4 min** |

---

**Consegue fazer? É igual copiar um arquivo!** 💪

Se precisar de ajuda, me manda screenshot do que aparecer!

