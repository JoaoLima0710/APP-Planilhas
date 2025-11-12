# 🧪 TESTE RÁPIDO COM cURL

## 1️⃣ ABRA O APP

```
http://localhost:5173
```

---

## 2️⃣ FAÇA LOGIN

Use qualquer email/senha (vai criar novo usuário)

---

## 3️⃣ TESTE UPLOAD SIMPLES

Você já tem um arquivo de teste:
```
test-simples.csv
```

**No Dashboard:**
1. Clique: "Escolher Arquivo"
2. Selecione: `test-simples.csv`
3. Clique: "Processar Pacientes"

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

Dashboard deve mostrar:
- ✅ **3 Pacientes**
- ✅ Distribuição por setor
- ✅ Tabela de pacientes

---

## 🔍 SE HOUVER ERRO

### Erro 401 Unauthorized
- Faça login no app
- Copie o token do navegador (F12 → Application → Supabase)

### Erro 403 Forbidden
- ❌ Admin role check (já removido, mas verifique)

### Erro 500
- Verifique logs da Edge Function no Dashboard

---

## 📊 PRÓXIMO PASSO

Se o teste simples passar:
1. Teste com arquivo grande (`test-1600-patients.csv`)
2. Teste frequência (`test-multisheet-attendance.xlsx`)

**Pronto?** 💪

