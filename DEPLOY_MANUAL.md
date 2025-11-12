# 🚀 DEPLOY MANUAL VIA DASHBOARD - ÚLTIMO PASSO!

## ⚡ Resumo Rápido

**Problema**: API deploy requer conta Pro+
**Solução**: Deploy manual via Dashboard (mesma coisa!)
**Tempo**: 3-4 minutos

---

## 🔗 Link Direto

👉 **https://supabase.com/dashboard/project/ruujmkanbxofxljwzvas/functions**

Abra esse link e segue os passos abaixo!

---

## 📋 PASSO 1: process-spreadsheet

### No Dashboard, procure por:
```
process-spreadsheet
├─ Status: Active (ou outra)
└─ [Ícone de editar ou ⋮]
```

### Clique para abrir

### Clique em: "Edit"

Um editor com código vai abrir.

### Selecione TUDO e delete

```
Ctrl + A  (seleciona tudo)
Delete    (apaga)
```

### Copie o código novo

**No seu PC, abra**:
```
supabase/functions/process-spreadsheet/index.ts
```

**Copie tudo**:
```
Ctrl + A  (seleciona tudo)
Ctrl + C  (copia)
```

### Cole no Dashboard

```
Ctrl + V  (cola)
```

✅ Código novo aparece no editor!

### Clique: "Save and Deploy"

Botão azul ou verde, canto inferior direito.

⏳ Aguarde... ~30-60 segundos

### Você vai ver:

```
✅ Deployment successful

Status: Active
Updated: Nov 11, 2025 at XX:XX
```

**PRONTO! Part 1 concluída! ✅**

---

## 📋 PASSO 2: process-attendance

**REPITA EXATAMENTE O PASSO 1, MAS**:

- Procure por: **process-attendance** (não process-spreadsheet)
- Arquivo: `supabase/functions/process-attendance/index.ts`

**Resultado final**:

```
✅ Deployment successful

Status: Active
Updated: Nov 11, 2025 at XX:XX
```

**PRONTO! Part 2 concluída! ✅**

---

## 📋 PASSO 3: Confirme Ambas

Volte à lista de funções.

Procure por:

```
process-spreadsheet ✅ Active (Nov 11, 21:XX)
process-attendance ✅ Active (Nov 11, 21:XX)
```

Se ambas têm ✅ e Status "Active", o deploy funcionou!

---

## 🧪 PASSO 4: Teste Agora

### Abra o dashboard local:
```
http://localhost:8080
```

### Recarregue a página:
```
F5
```

### Localize "Upload de Planilhas"

Procure pelo card/seção com titulo "Upload de Planilhas"

### Clique em "Selecione um arquivo"

### Navegue até:
```
test-simple-pacientes.xlsx
```

(Arquivo com 3 pacientes de teste)

### Clique em "Processar"

### Aguarde 3-5 segundos...

### Você deve ver uma mensagem VERDE:

```
✅ Planilha processada! 3 pacientes atualizados
```

### Verifique a lista de pacientes:

Deve aparecer 3 pacientes:

```
P0001 │ João Silva │ SUL │ 10 dias │
P0002 │ Maria Santos │ OESTE │ 45 dias │
P0003 │ Pedro Costa │ LESTE │ 90 dias │
```

---

## 🎉 SUCESSO!

Se chegou até aqui, tudo funcionou!

Agora você pode testar com o arquivo grande:

```
test-multisheet-patients.xlsx
(1.650 pacientes em 3 abas)
```

---

## 💡 Dicas Importantes

### ✅ Copie sempre TUDO do arquivo
- Não deixe linhas de fora
- Começa com: `import "https://...`
- Termina com: `});`

### ✅ Aguarde o deploy completar
- Pode levar até 1 minuto
- Não feche a página
- Se tomar muito tempo, recarregue

### ✅ Se der erro no "Save and Deploy"
- Clique em "View logs"
- Veja a mensagem de erro
- Me mande a mensagem

### ✅ Se o status não mudar para "Active"
- Recarregue a página (F5)
- Tente fazer o deploy novamente
- Verifique se código está correto

---

## 🆘 Troubleshooting

| Problema | Solução |
|----------|---------|
| "Deployment failed" | Veja logs, verifica se copiou tudo |
| "Status não muda" | Recarregue (F5), tente novamente |
| "Ainda recebo 403" | O deploy pode ter falhado, verifique status |
| "Upload não funciona" | Certifique que ambas estão com status Active |

---

## 📞 Precisa de Ajuda?

Se der qualquer problema:
1. Verifique o arquivo que copiou
2. Verifique os logs do Dashboard
3. Me mande screenshot ou mensagem de erro

---

**Consegue fazer agora? É só copiar e colar! 💪**

Abra o Dashboard:
👉 https://supabase.com/dashboard/project/ruujmkanbxofxljwzvas/functions

