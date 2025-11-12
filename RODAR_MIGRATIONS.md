# 🗄️ RODAR MIGRATIONS - VIA DASHBOARD

## 📋 O que são migrations?

São scripts SQL que criam as tabelas do banco de dados.

Você tem 7 arquivos que precisam ser executados em ordem.

---

## ✅ PASSO 1: Abra SQL Editor

1. Vá para: https://app.supabase.com/project/pikskrtgivhifxpzrxyb
2. Menu esquerdo: **SQL Editor**
3. Clique: **New query** (botão azul)

---

## ✅ PASSO 2: Copie Primeira Migration

### Abra o arquivo:
```
supabase/migrations/20251111014613_185d9885-76d2-44f1-a99c-7fa1f554a974.sql
```

### Copie TODO o conteúdo:
- Ctrl+A (seleciona tudo)
- Ctrl+C (copia)

### Cole no SQL Editor do Dashboard:
- Clique no editor (janela SQL)
- Ctrl+V (cola)

---

## ✅ PASSO 3: Execute

Clique o botão: **"Run"** (ou Ctrl+Enter)

Você vai ver:
```
✅ Query successful
Rows: 0
Time: 1.234s
```

---

## ✅ PASSO 4: Repita para os Próximos Arquivos

Faça o mesmo com TODOS os arquivos em ordem:

```
1. 20251111014613_185d9885-76d2-44f1-a99c-7fa1f554a974.sql
2. 20251111014635_e665d22d-bfd0-4b6a-a4a9-0fefae079d66.sql
3. 20251111092509_fe24e844-f33a-44b1-b23f-444e050bbf00.sql
4. 20251111094927_27d14458-6bda-4bed-8c71-26882862d70e.sql
5. 20251111095432_5035915a-b20e-4be6-8f77-c0edbe48ce55.sql
6. 20251111121439_f8dcaeb1-3af4-4e8f-8f9b-5fabc05a1610.sql
7. 20251111203000_add_days_of_absence.sql
```

---

## ✅ PASSO 5: Verifique Sucesso

Após rodar TODOS:

1. Vá em: **Database** (menu esquerdo)
2. Procure por: **public** (schema)
3. Você deve ver as tabelas:
   - patients
   - health_units
   - attendance
   - user_roles
   - profiles
   - upload_logs

Se vê todas, ótimo! ✅

---

## 🎯 Próximo Passo

Após rodar todas as migrations:

1. Deploy das Edge Functions (DEPLOY_MANUAL.md)
2. Testar upload no dashboard local

---

## ⏱️ Tempo Estimado

- Cada migration: 1-2 segundos
- Total: ~15 segundos

---

**Consegue rodar as migrations?** 💪

