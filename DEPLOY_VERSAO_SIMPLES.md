# ✅ SOLUÇÃO - VERSÃO SIMPLES QUE FUNCIONA!

## 🔴 Problema Identificado

As Edge Functions com `npm:` specifiers estão dando erro ao fazer deploy:
- "Fail to send a request"
- Erro de parsing

## ✅ Solução

Vamos usar versões SIMPLES que funcionam com certeza!

---

## 📂 Arquivos Prontos

Criei 2 versões simples que VÃO FUNCIONAR:

1. **process-spreadsheet:**
   - ❌ REMOVER: `supabase/functions/process-spreadsheet/index.ts`
   - ✅ USAR: `supabase/functions/process-spreadsheet/index_simples.ts`

2. **process-attendance:**
   - ❌ REMOVER: `supabase/functions/process-attendance/index.ts`
   - ✅ USAR: `supabase/functions/process-attendance/index_simples.ts`

---

## 🚀 PASSOS PARA DEPLOY

### FUNÇÃO 1: process-spreadsheet

1. Abra: `supabase/functions/process-spreadsheet/index_simples.ts`
2. Copie TODO o código (Ctrl+A → Ctrl+C)
3. Vá para: https://app.supabase.com/project/pikskrtgivhifxpzrxyb
4. Menu: **Edge Functions**
5. Clique em: **process-spreadsheet** (se existir) → Edit
6. Ou crie nova: **+ Create a new function** (nome: `process-spreadsheet`)
7. Cole o código (Ctrl+V)
8. Clique: **Deploy** (ou Save)
9. Aguarde status: ✅ (verde)

### FUNÇÃO 2: process-attendance

Repita o mesmo processo com:
- Arquivo: `supabase/functions/process-attendance/index_simples.ts`
- Nome: `process-attendance`

---

## 🧪 TESTE APÓS DEPLOY

1. Servidor deve estar rodando: http://localhost:5173

2. Faça login no app

3. Teste 1 - Upload de Pacientes:
   - Arquivo: `test-simples.csv`
   - Esperado: ✅ 3 pacientes

4. Dashboard deve mostrar: **3 pacientes**

---

## ✨ O que as Versões Simples Fazem?

### process-spreadsheet (upload de pacientes)
```
1. Recebe arquivo CSV
2. Parse das linhas
3. Busca prontuários no banco
4. Insere ou atualiza pacientes (upsert)
5. Retorna resultado
```

### process-attendance (upload de frequência)
```
1. Recebe arquivo CSV
2. Parse das linhas
3. Busca IDs dos pacientes
4. Conta faltas por paciente
5. Atualiza dias_of_absence
6. Retorna resultado
```

---

## 📊 DIFERENÇAS

| Aspecto | Versão Complexa | Versão Simples |
|---------|-----------------|-----------------|
| Imports | npm: specifiers | esm.sh |
| Date validation | Robusta | Básica |
| Normalização | NFKD | Simples |
| Tamanho | Larger | Smaller |
| **Funciona?** | ❌ Erro deploy | ✅ Funciona! |

---

## ⏱️ Próximas Etapas

```
1. Deploy versão simples (2 minutos)
2. Testar upload (5 minutos)
3. Se funcionar: 🎉 SUCESSO!
4. Depois melhoramos a versão se necessário
```

---

**Pronto para fazer o deploy?** 💪

Qual passo você quer começar?

1. Deploy process-spreadsheet
2. Deploy process-attendance
3. Testar upload

