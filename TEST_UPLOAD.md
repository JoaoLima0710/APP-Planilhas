# 🧪 TESTAR O SISTEMA

## ✅ Edge Functions Deployadas!

Agora vamos testar se tudo está funcionando.

---

## 🚀 PASSO 1: Iniciar o Projeto Local

```bash
cd c:\Users\Joao\Desktop\clinic-data-atlas-main
npm run dev
```

Você verá:
```
  VITE v7.2.2  ready in 1234 ms

  ➜  Local:   http://localhost:5173/
```

Abra: http://localhost:5173

---

## 📝 PASSO 2: Teste 1 - Arquivo Simples (3 Pacientes)

### Criar arquivo de teste:

Arquivo: `test-3-patients.csv`

```csv
PRONTUÁRIO,NOME,DIAS,SETOR
001,João Silva,5,Reabilitação
002,Maria Santos,10,Fisioterapia
003,Pedro Oliveira,3,Terapia Ocupacional
```

### Upload:

1. Vá para http://localhost:5173
2. Clique: **Escolher Arquivo**
3. Selecione: `test-3-patients.csv`
4. Clique: **Processar Pacientes**

### Resultado Esperado:

```json
{
  "success": true,
  "processed": 3,
  "inserted": 3,
  "errors": 0,
  "total": 3
}
```

✅ Dashboard mostra: **3 pacientes**

---

## 📊 PASSO 3: Teste 2 - Arquivo Grande (1.650 Pacientes)

### Se você tem o arquivo:

`test-multisheet-patients.xlsx` (1650 pacientes)

1. Vá para http://localhost:5173
2. Clique: **Escolher Arquivo**
3. Selecione: `test-multisheet-patients.xlsx`
4. Clique: **Processar Pacientes**

### Resultado Esperado:

```json
{
  "success": true,
  "processed": 1650,
  "inserted": 1650,
  "errors": 0,
  "total": 1650
}
```

✅ Dashboard mostra: **1650 pacientes**

---

## 📅 PASSO 4: Teste 3 - Frequência/Attendance

### Se você tem o arquivo:

`test-multisheet-attendance.xlsx` (1347 registros de frequência)

1. Vá para http://localhost:5173
2. Clique: **Escolher Arquivo**
3. Selecione: `test-multisheet-attendance.xlsx`
4. Clique: **Processar Frequência**

### Resultado Esperado:

```json
{
  "success": true,
  "processed": 1347,
  "insertedAttendance": 1347,
  "updatedPatients": 245,
  "errors": 0,
  "total": 1347
}
```

✅ Dashboard mostra pacientes com **dias de ausência**

---

## 🔍 PASSO 5: Verificar Dashboard

Após cada upload, você deve ver:

1. **Contador de Pacientes**: atualizado
2. **Gráfico**: mostrando distribuição por setor
3. **Tabela**: listando pacientes
4. **Dias de Falta**: se fez upload de frequência

---

## ❌ Se Algo Não Funcionar

### Erro: "Unauthorized"
- Faça login no app
- Verifique se o token está sendo enviado

### Erro: "Patient not found"
- Uploade arquivo de **pacientes** ANTES de **frequência**
- Os prontuários devem corresponder

### Erro: "File too large"
- Máximo: 50MB
- Divida em partes menores

### Erro: "Too many rows"
- Máximo: 50.000 linhas
- Divida em partes menores

---

## 📊 Checklist de Sucesso

- [ ] Teste 1: 3 pacientes OK
- [ ] Teste 2: 1650 pacientes OK
- [ ] Teste 3: 1347 frequências OK
- [ ] Dashboard mostra todos os dados
- [ ] Nenhum erro 403 Forbidden
- [ ] Nenhum erro de timeout

---

## 🎯 Se Tudo Passou!

```
✅ Sistema funcionando perfeitamente!
✅ Edge Functions deployadas
✅ Dados sendo salvos corretamente
✅ Dashboard mostrando dados
✅ Batch processing funcionando
✅ Multi-format support (CSV/ODS/XLSX)
```

---

## 📝 Próximas Etapas

1. Testar com seus dados reais
2. Ajustar estrutura de colunas se necessário
3. Deploy da aplicação (build)
4. Usar em produção

---

**Consegue rodar os testes?** 💪

