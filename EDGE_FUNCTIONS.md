# Edge Functions - Clinic Data Atlas

## Formatos Suportados

- ✅ **CSV** (.csv)
- ✅ **ODS** (.ods) - LibreOffice Calc **com suporte a múltiplas abas**
- ✅ **XLSX/XLS** (.xlsx, .xls) - Excel/Calc **com suporte a múltiplas abas**

### Limite de Tamanho
- **CSV**: até 10MB
- **ODS/XLSX**: até 50MB (para acomodar múltiplas abas)

---

## 1. process-spreadsheet

Processa a planilha inicial de pacientes com dados de PCS (Procedimento/Consulta).

**Arquivo:** `supabase/functions/process-spreadsheet/index.ts`

### Características
- Suporta **múltiplas abas** em ODS/XLSX
- Processa automaticamente todas as abas
- Normaliza nomes de colunas (espaços e maiúsculas)
- Detecta delimitadores em CSV

### Formato Esperado

| Coluna | Descrição | Obrigatória |
|--------|-----------|------------|
| Prontuário | Identificador único | ✅ Sim |
| Nome | Nome completo | ✅ Sim |
| Dias | Dias desde o último PCS | ❌ Não |
| Setor | Área de atendimento | ❌ Não |
| Modalidade | Individual/Grupo | ❌ Não |
| Rotina | Frequência de atendimento | ❌ Não |
| UBSF/Unidade | Unidade de Saúde | ❌ Não |
| Endereço Completo | Logradouro | ❌ Não |
| Bairro | Bairro/Distrito | ❌ Não |
| Terapeuta | Profissional responsável | ❌ Não |
| CID | Código de diagnóstico | ❌ Não |

### Resposta

```json
{
  "success": true,
  "processed": 1600,
  "errors": 0,
  "total": 1600,
  "validationErrors": []
}
```

---

## 2. process-attendance

Processa a planilha de frequência/ausências dos pacientes.

**Arquivo:** `supabase/functions/process-attendance/index.ts`

### Características
- Suporta **múltiplas abas** em ODS/XLSX
- Processa todas as abas automaticamente
- Conta automaticamente dias de falta
- Normaliza nomes de colunas

### Formato Esperado

| Coluna | Descrição | Valores |
|--------|-----------|---------|
| Prontuário | Identificador do paciente | P0001, P0002, etc |
| Data Atendimento | Data do atendimento | YYYY-MM-DD |
| Status | Presença ou Falta | P, F, Presente, Falta |

### Função

- **Lê os registros de frequência** da planilha (todas as abas)
- **Identifica faltas (F)** e conta quantas cada paciente tem
- **Atualiza campo `days_of_absence`** para cada paciente
- **Registra na tabela `attendance`** para histórico

### Resposta

```json
{
  "success": true,
  "processed": 450,
  "patientsUpdated": 100,
  "errors": 0,
  "total": 450,
  "validationErrors": []
}
```

---

## 3. Fluxo Esperado

1. **Fazer login** no dashboard
2. **Upload da planilha de pacientes** (`process-spreadsheet`)
   - Suporta CSV, ODS ou XLSX
   - Se múltiplas abas, lê todas automaticamente
   - Popula tabela `patients`
   - Define `days_since_last_visit` (dias desde PCS)
3. **Upload da planilha de frequência** (`process-attendance`)
   - Suporta CSV, ODS ou XLSX
   - Se múltiplas abas, lê todas automaticamente
   - Registra na tabela `attendance`
   - Atualiza `days_of_absence` em `patients`

---

## 4. Autorização

Ambas as functions requerem:
- ✅ **Usuário autenticado**
- ✅ **Role de admin**

---

## 5. Campos do Banco de Dados

### Tabela: patients

- `id`: UUID (chave primária)
- `prontuario`: TEXT UNIQUE (obrigatório)
- `name`: TEXT (obrigatório)
- `sector`: TEXT
- `days_since_last_visit`: INTEGER (dias desde PCS)
- `days_of_absence`: INTEGER (dias de falta)
- `health_unit_id`: UUID (referência)
- `address`: TEXT
- `therapist`: TEXT
- `cid`: TEXT
- Outros...

### Tabela: attendance

- `id`: UUID
- `patient_id`: UUID (referência)
- `prontuario`: TEXT
- `attendance_date`: DATE
- `status`: TEXT ('P' ou 'F')
- `created_at`: TIMESTAMP

---

## 6. Tratamento de Erros

### Erros Comuns

- **"Prontuário ou nome ausente"** → Verifique se as colunas estão corretas
- **"Paciente com prontuário X não encontrado"** → Faça upload da planilha de pacientes primeiro
- **"Arquivo muito grande"** → Máximo 50MB para ODS/XLSX ou 10MB para CSV
- **"Muitas linhas"** → Máximo 50.000 linhas (process-attendance) ou 10.000 (process-spreadsheet)
- **"Erro ao processar arquivo"** → Verifique formato do arquivo ODS/XLSX

---

## 7. Delimitadores Suportados (CSV)

Detecta automaticamente:
- `,` (vírgula) - padrão
- `;` (ponto-e-vírgula)
- `\t` (tab)

---

## 8. Múltiplas Abas (ODS/XLSX)

As functions processam **automaticamente todas as abas** do arquivo:

```
Arquivo.ods
├── Aba 1: Pacientes...  (50 linhas)
├── Aba 2: Pacientes...  (100 linhas)
└── Aba 3: Pacientes...  (200 linhas)
↓
Total processado: 350 linhas
```

O sistema:
- Lê sequencialmente todas as abas
- Normaliza os cabeçalhos de cada aba
- Consolida em uma única lista
- Processa como se fossem uma única tabela

---

## 9. Logs

Os uploads são registrados na tabela `upload_logs` com:
- `user_id`: Usuário que fez upload
- `filename`: Nome do arquivo
- `records_processed`: Linhas processadas
- `records_failed`: Erros
- `created_at`: Data/hora
