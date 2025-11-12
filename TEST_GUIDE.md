# 🧪 Teste das Edge Functions com Múltiplas Abas

## Arquivos de Teste Gerados

### 1️⃣ **test-multisheet-patients.xlsx** (97 KB)
Arquivo com **3 abas** contendo **1.650 pacientes**

**Estrutura:**
```
Aba 1: "Pacientes Jan-Mar"   → P0001 a P0550 (550 pacientes)
Aba 2: "Pacientes Abr-Jun"   → P0551 a P1100 (550 pacientes)
Aba 3: "Pacientes Jul-Set"   → P1101 a P1650 (550 pacientes)
```

**Colunas:**
- Prontuário (único)
- Nome
- Dias (desde PCS)
- Setor
- Modalidade
- Rotina
- UBSF
- Endereço Completo
- Bairro
- Terapeuta
- CID

---

### 2️⃣ **test-multisheet-attendance.xlsx** (25 KB)
Arquivo com **3 abas** contendo **1.347 registros** de frequência

**Estrutura:**
```
Aba 1: "Novembro"    → 448 registros (últimos 30 dias)
Aba 2: "Outubro"     → 444 registros (30-60 dias atrás)
Aba 3: "Setembro"    → 455 registros (60-90 dias atrás)
```

**Colunas:**
- Prontuário
- Data Atendimento (YYYY-MM-DD)
- Status (P = Presente, F = Falta)

**Proporção:** ~80% Presença, ~20% Falta

---

## 🚀 Passo-a-Passo do Teste

### Fase 1: Upload de Pacientes

1. ✅ Abra o dashboard em http://localhost:8080
2. ✅ Faça login com suas credenciais
3. ✅ Clique em **"Enviar Planilha"**
4. ✅ Selecione **`test-multisheet-patients.xlsx`**
5. ✅ Clique em **"Processar"**
6. ⏳ Aguarde a mensagem de sucesso

**Resultado Esperado:**
```json
{
  "success": true,
  "processed": 1650,
  "errors": 0,
  "total": 1650,
  "validationErrors": []
}
```

**O que deve acontecer:**
- ✅ Sistema lê todas as 3 abas automaticamente
- ✅ Consolida os 1.650 pacientes em um único upload
- ✅ Dashboard mostra **1.650 pacientes** no total
- ✅ Cada paciente tem `days_since_last_visit` preenchido

---

### Fase 2: Upload de Frequência

1. ✅ Volte ao dashboard (após o primeiro upload)
2. ✅ Clique em **"Enviar Frequência"** (quando implementado)
3. ✅ Selecione **`test-multisheet-attendance.xlsx`**
4. ✅ Clique em **"Processar"**
5. ⏳ Aguarde a mensagem de sucesso

**Resultado Esperado:**
```json
{
  "success": true,
  "processed": 1347,
  "patientsUpdated": 100,
  "errors": 0,
  "total": 1347,
  "validationErrors": []
}
```

**O que deve acontecer:**
- ✅ Sistema lê todas as 3 abas (Novembro, Outubro, Setembro)
- ✅ Consolida os 1.347 registros em um único upload
- ✅ Conta as faltas para cada paciente (P0001 a P0100)
- ✅ Atualiza `days_of_absence` para cada paciente

---

## 📊 Validações

### Após Fase 1 (Pacientes)
Verifique no dashboard:
- [ ] Total de pacientes = 1.650
- [ ] Campos preenchidos: Nome, Dias, Setor, etc
- [ ] Unidades de saúde criadas automaticamente
- [ ] Sem erros na importação

### Após Fase 2 (Frequência)
Verifique no dashboard ou banco de dados:
- [ ] Tabela `attendance` tem 1.347 registros
- [ ] Pacientes P0001-P0100 têm `days_of_absence` > 0
- [ ] Distribuição de faltas é aproximadamente 20% do total

---

## 🔍 Troubleshooting

### "Erro: Arquivo muito grande"
- ❌ Seu arquivo tem mais de 50MB
- ✅ Use os arquivos de teste fornecidos

### "Erro: Prontuário não encontrado"
- ❌ Você não fez upload da planilha de pacientes primeiro
- ✅ Sempre faça Fase 1 antes da Fase 2

### "Processou 0 pacientes"
- ❌ Nomes de colunas não correspondem
- ✅ Verifique se as colunas estão em português correto
- ✅ Pode ter acentuação diferente na sua planilha

### "Abas não foram lidas"
- ❌ Arquivo está corrompido ou em formato inválido
- ✅ Regenere os arquivos de teste
- ✅ Ou teste com seus arquivos ODS/XLSX

---

## 📝 Notas

- Os arquivos são **fictícios** e para teste apenas
- Todos os prontuários e nomes são **aleatórios**
- Datas de frequência são **retroativas** (últimos 90 dias)
- Sistema consolida múltiplas abas **automaticamente**
- Não precisa separar as abas manualmente

---

## ✅ Sucesso!

Se ambas as fases funcionarem:
- ✅ Edge Functions estão operacionais
- ✅ Suporte a múltiplas abas funciona
- ✅ Sistema está pronto para seus dados reais
