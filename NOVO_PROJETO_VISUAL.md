# ✅ CRIAR NOVO PROJETO - GUIA VISUAL

## 🎯 Resumo

Seu projeto foi deletado. Solução: criar um novo!

**Tempo**: ~5 minutos

---

## 📋 PASSO 1: Clique "New project"

No Dashboard, você vê:

```
┌─────────────────────────────┐
│ Projects                    │
├─────────────────────────────┤
│ No projects                 │
│                             │
│ ┌─────────────────────────┐ │
│ │ [+ New project] (verde) │ │
│ └─────────────────────────┘ │
└─────────────────────────────┘
```

Clique no botão verde **"New project"** ou **"+ New project"**

---

## 📋 PASSO 2: Preencha o Formulário

Você vai ver:

```
┌─────────────────────────────┐
│ Create a new project        │
├─────────────────────────────┤
│ Project name:               │
│ [clinic-data-atlas________] │
│                             │
│ Database password:          │
│ [Senha123!______________]   │
│                             │
│ Region:                     │
│ [United States (us-east-1)] │
│                             │
│ [Create new project]        │
└─────────────────────────────┘
```

### Preenchimento:

1. **Project name**: `clinic-data-atlas`
2. **Database password**: Uma senha forte (ex: `Clinic@2025!`)
3. **Region**: Deixe como está (ou escolha perto de você)

Clique: **"Create new project"**

---

## 📋 PASSO 3: Aguarde Criação

```
⏳ Creating your project...
   └─ Setting up database...
   └─ Configuring...
   
(Pode levar 2-5 minutos)
```

Quando pronto, você vê um Dashboard novo!

---

## 📋 PASSO 4: Copie os Valores

Abra: **Settings > API**

```
┌──────────────────────────────┐
│ Settings > API               │
├──────────────────────────────┤
│ URL:                         │
│ https://xxxxx.supabase.co    │ ← Copie
│                              │
│ anon key:                    │
│ eyJhbGc...........................│ ← Copie
│                              │
│ service_role key:            │
│ eyJhbGc...........................│
└──────────────────────────────┘
```

Copie:
- URL
- anon key

---

## 📋 PASSO 5: Atualizar .env

**Abra o arquivo**: `c:\Users\Joao\Desktop\clinic-data-atlas-main\.env`

**Mude para:**

```env
VITE_SUPABASE_PROJECT_ID="xxxxx"
VITE_SUPABASE_PUBLISHABLE_KEY="eyJhbGc...."
VITE_SUPABASE_URL="https://xxxxx.supabase.co"
```

Substituindo:
- `xxxxx` = seu novo project ID
- `eyJhbGc....` = anon key (copie inteira)
- `https://xxxxx.supabase.co` = URL que copiou

---

## 📋 PASSO 6: Criar Tabelas

No novo Dashboard, vá em: **SQL Editor**

Copie/cole os SQL de:
```
supabase/migrations/
```

(Tem vários arquivos .sql lá)

Rode um por um ou todos juntos.

---

## 📋 PASSO 7: Deploy das Edge Functions

Agora faça deploy:

1. No Dashboard, vá em: **Edge Functions**
2. Siga o DEPLOY_MANUAL.md

---

## 🎉 Pronto!

Seu novo projeto está pronto!

Teste:
- http://localhost:8080 (F5)
- Upload: test-simple-pacientes.xlsx
- Deve aparecer: ✅ "3 pacientes atualizados"

---

**Consegue criar?** 💪

