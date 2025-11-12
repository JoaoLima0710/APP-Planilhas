# 🖥️ DEPLOY VIA DASHBOARD - GUIA VISUAL

## 🔗 Link Direto

Clique aqui para ir direto ao Dashboard:
👉 https://supabase.com/dashboard/project/ruujmkanbxofxljwzvas/functions

Ou:
1. Vá para https://supabase.com/dashboard
2. Selecione projeto: **ruujmkanbxofxljwzvas**
3. Menu esquerdo: **Edge Functions**

---

## 📝 O que você vai ver

```
┌─────────────────────────────────────┐
│ Edge Functions                       │
├─────────────────────────────────────┤
│ □ process-spreadsheet   Active ✓    │
│ □ process-attendance    Active ✓    │
│ □ send-login-notification           │
│ □ send-signup-notification          │
└─────────────────────────────────────┘
```

---

## 🎯 Passo 1: Editar process-spreadsheet

### Localizar
- Na lista, procure por: **process-spreadsheet**
- À direita, tem 3 pontinhos (⋮) ou um ícone de editar

### Clicar
- Clique em qualquer lugar da linha para abrir
- OU clique no ícone de editar (✏️)
- OU clique nos 3 pontinhos (⋮) > Edit

### Ver o Editor
Você vai ver:
```
┌─────────────────────────┐
│ process-spreadsheet     │
├─────────────────────────┤
│ [  CÓDIGO TYPESCRIPT   ]│
│ [                      ]│
│ [                      ]│
│ └─────────────────────┘ │
│   [ Save & Deploy ]     │
└─────────────────────────┘
```

---

## 🖊️ Passo 2: Copiar o Novo Código

### Abra o arquivo no seu PC
- Abra: `supabase/functions/process-spreadsheet/index.ts`
- Em VS Code (ou editor)

### Selecione TUDO
- Pressione: **Ctrl + A** (seleciona tudo)

### Copie
- Pressione: **Ctrl + C**

### Verifique a clipboard
- Abra terminal PowerShell
- Digite: `Get-Clipboard | Measure-Object -Line`
- Deve mostrar muitas linhas (ex: 440 lines)

---

## 📌 Passo 3: Colar no Dashboard

### Limpe o editor
- Clique dentro do editor (onde está o código)
- Pressione: **Ctrl + A** (seleciona tudo)
- Pressione: **Delete** (apaga tudo)

### Cole o novo código
- Pressione: **Ctrl + V** (cola)
- Espere 1-2 segundos (pode ficar lento)

### Verifique
- O código novo deve estar lá
- Deve começar com: `import "https://deno.land/x/xhr@0.1.0/mod.ts";`
- Deve terminar com: `});`

---

## 💾 Passo 4: Salvar e Deploy

### Procure o botão
- Canto inferior direito do editor
- Deve ter um botão **"Save and Deploy"** (azul ou verde)

### Clique
- 1 clique no botão **"Save and Deploy"**

### Aguarde
- Pode levar 20-60 segundos
- A página pode ficar carregando
- Você vai ver mensagem:
  - ✅ "Deployment successful" (SUCESSO!)
  - ❌ "Deployment failed" (erro)

### Se der sucesso
- Página volta ao normal
- Status muda para "Active" com timestamp recente

---

## 🔁 Passo 5: Repita para process-attendance

Volte à lista de Edge Functions:
1. Clique em **process-attendance**
2. Repita Passos 2-4 acima
3. Mas desta vez copie do arquivo: `supabase/functions/process-attendance/index.ts`

---

## ✅ Confirme o Deploy

Ambas as funções devem estar assim:

```
process-spreadsheet
├─ Status: Active ✓
└─ Updated: Nov 11, 2025 at 21:XX

process-attendance  
├─ Status: Active ✓
└─ Updated: Nov 11, 2025 at 21:XX
```

---

## 🧪 Pronto para Testar!

Após o deploy de AMBAS:

1. Abra o dashboard: http://localhost:8080
2. Recarregue: F5
3. Upload: teste-simples-pacientes.xlsx
4. Deve aparecer: ✅ "Planilha processada! 3 pacientes atualizados"

---

## 🆘 Se der erro

### Erro: "Deployment failed"
- Clique em **"View logs"**
- Veja a mensagem exata
- Me envie a mensagem

### Erro: 403 Forbidden
- Significa que o código antigo ainda está lá
- Verifique se copiou o arquivo correto
- Verifique se colou TUDO (começa com `import "https://...`)

### Erro: Blank page
- Recarregue a página (F5)
- Tente novamente

---

## 📞 Precisa de Ajuda?

Se não conseguir, me mande:
1. Screenshot do erro (se tiver)
2. Mensagem exata de erro (se houver logs)
3. Qual função deu erro (process-spreadsheet ou process-attendance?)

