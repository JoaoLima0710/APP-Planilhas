# 🖥️ PASSO A PASSO COM SCREENSHOTS

## Passo 1: Gerar Token

### Abra essa URL:
```
https://supabase.com/dashboard/account/tokens
```

### Você vê isso:
```
┌────────────────────────────────────────────┐
│ Account tokens                             │
├────────────────────────────────────────────┤
│                                            │
│ ┌──────────────────────────────────────┐   │
│ │ Create a new token          [Botão]  │   │
│ └──────────────────────────────────────┘   │
│                                            │
│ (lista de tokens antigos)                  │
└────────────────────────────────────────────┘
```

### Clique no botão azul: "Create a new token"

### Preencha o formulário:
```
Token name:  [Deploy Script_____________]
Description: [Deploy automático das funções]

Scopes:
  ☑ functions_deploy          ← MARCAR ISSO!
  ☑ projects_read
  ☐ organizations_read
```

### Clique: "Generate token"

### Você vê:
```
┌────────────────────────────────────┐
│ Token created!                     │
├────────────────────────────────────┤
│                                    │
│ sbp_abc123def456xyz789...          │
│                                    │
│ [Copiar] [Fechar]                  │
└────────────────────────────────────┘
```

### COPIE O TOKEN!
- Não feche a página
- Copie com Ctrl+C
- Guarde em lugar seguro por agora

---

## Passo 2: Executar Deploy

### Abra PowerShell

Pressione: `Windows + R`
Digite: `powershell`
Pressione: `Enter`

Você vê:
```
PS C:\Users\Joao>
```

### Digite os comandos:

```powershell
cd c:\Users\Joao\Desktop\clinic-data-atlas-main
```

Pressione Enter. Você vê:
```
PS C:\Users\Joao\Desktop\clinic-data-atlas-main>
```

### Defina o token (SUBSTITUA seu_token_aqui):

```powershell
$env:SUPABASE_ACCESS_TOKEN = 'seu_token_aqui'
```

Pressione Enter. Você vê:
```
PS C:\Users\Joao\Desktop\clinic-data-atlas-main>
```

(Nada de errado, é normal)

### Execute o deploy:

```powershell
node deploy.mjs
```

Pressione Enter.

---

## Passo 3: Ver Resultado

### Se funcionou (Token correto):

```
============================================================
🚀 SUPABASE EDGE FUNCTIONS AUTO-DEPLOY
============================================================

📋 Projeto: ruujmkanbxofxljwzvas
📂 Diretório: C:\Users\Joao\Desktop\clinic-data-atlas-main

🔑 Obtendo access token...
✓ Token de: SUPABASE_ACCESS_TOKEN

============================================================
🚀 Deploy: process-spreadsheet
   Tamanho: 16242 bytes
   Status HTTP: 200
   ✅ Deploy bem-sucedido!

============================================================
🚀 Deploy: process-attendance
   Tamanho: 15503 bytes
   Status HTTP: 200
   ✅ Deploy bem-sucedido!

============================================================
📊 RESUMO
============================================================
  ✅ Sucesso: process-spreadsheet
  ✅ Sucesso: process-attendance

  Total: 2/2

🎉 Deploy completo! Pronto para testar!
```

### Se der erro (Token inválido ou expirado):

```
❌ Erro: Unauthorized
```

**Solução**: Gere um novo token e tente novamente.

---

## Passo 4: Testar no Dashboard

### Abra o dashboard:
```
http://localhost:8080
```

### Recarregue:
```
Pressione: F5
```

### Localize o upload:
- Procure por: "Upload de Planilhas"
- Veja o botão azul: "Processar"

### Upload do arquivo:
- Clique em: "Selecione um arquivo"
- Procure por: `test-simple-pacientes.xlsx`
- Selecione e abra

### Você vê:
```
Arquivo selecionado: test-simple-pacientes.xlsx
[Processar]
```

### Clique em "Processar":
- Aguarde 3-5 segundos

### Se funcionou, você vê:
```
✅ Planilha processada! 3 pacientes atualizados
```

### E na lista de pacientes, aparecem:
```
Pacientes Registrados

│ P0001 │ João Silva      │ SUL     │
│ P0002 │ Maria Santos    │ OESTE   │
│ P0003 │ Pedro Costa     │ LESTE   │
```

---

## 🎉 Pronto!

Se chegou até aqui, o deploy funcionou! 🚀

---

## 🆘 Troubleshooting

### "Token não encontrado"
→ Você não definiu a variável de ambiente
→ Execute: `$env:SUPABASE_ACCESS_TOKEN = 'seu_token'`

### "Erro: Unauthorized"
→ Token errado ou expirado
→ Gere um novo em: https://supabase.com/dashboard/account/tokens

### "Comando 'node' não encontrado"
→ Node.js não está instalado
→ Instale em: https://nodejs.org

### "Arquivo não encontrado"
→ Você está no diretório errado
→ Execute: `cd c:\Users\Joao\Desktop\clinic-data-atlas-main`

### "Ainda mostra 0 pacientes"
→ O deploy pode ter falhado
→ Verifique a mensagem de erro exata
→ Me mande screenshot ou copie a mensagem

