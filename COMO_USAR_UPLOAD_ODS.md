# 🚀 SOLUÇÃO DEFINITIVA - Upload de Arquivos ODS Grandes

## ❌ Problema
Edge Functions têm limite de memória (~128MB) que não suporta arquivos ODS/XLSX grandes mesmo com 600KB.

## ✅ Solução - Upload Local via Script Python

### Como usar:

**1. Abra o PowerShell/Terminal nesta pasta**

**2. Execute o script com seu arquivo ODS:**
```powershell
python upload_ods.py "caminho\do\seu\arquivo.ods"
```

**Exemplos:**
```powershell
# Se o arquivo está na mesma pasta
python upload_ods.py pacientes.ods

# Se está em outro lugar
python upload_ods.py "C:\Users\Joao\Downloads\lista_pacientes.ods"
```

**3. O script vai:**
- ✅ Ler o arquivo ODS localmente (sem limite de memória)
- ✅ Processar todas as linhas
- ✅ Enviar em lotes de 100 para o Supabase
- ✅ Mostrar progresso em tempo real
- ✅ Fazer UPSERT (atualizar ou inserir sem duplicar)

---

## 📋 Requisitos do Arquivo

**Colunas obrigatórias:**
- `PRONTUÁRIO` ou `PRONTUARIO` ou `PRONT`
- `NOME` ou `NAME`

**Colunas opcionais:**
- `FALTAS` ou `FALTA` (número de faltas/ausências)
- `SETOR` ou `SECTOR`

---

## 🎯 Vantagens desta Solução

✅ **Sem limite de tamanho** - Processa arquivos com milhares de linhas  
✅ **Suporta ODS e XLSX** - Ambos os formatos funcionam  
✅ **Múltiplas abas** - Processa a primeira aba ou aba "Pacientes"  
✅ **Upload incremental** - Envia em lotes pequenos  
✅ **Sem erros de memória** - Processamento local  
✅ **Progresso visual** - Vê o que está acontecendo  

---

## 📝 Exemplo de Uso

```powershell
PS C:\Users\Joao\Desktop\clinic-data-atlas-main> python upload_ods.py lista_caps.ods

📂 Lendo arquivo: lista_caps.ods
✅ Arquivo lido: 1547 linhas, 5 colunas
📋 Colunas: PRONTUÁRIO, NOME, FALTAS, SETOR, OBSERVAÇÕES

📊 Mapeamento de colunas:
   Prontuário: PRONTUÁRIO
   Nome: NOME
   Faltas: FALTAS
   Setor: SETOR

✅ 1547 pacientes válidos encontrados

🔗 Conectando ao Supabase...

📤 Enviando dados em lotes de 100...

  ✅ Lote 1/16: 100 pacientes enviados
  ✅ Lote 2/16: 100 pacientes enviados
  ...
  ✅ Lote 16/16: 47 pacientes enviados

============================================================
✅ PROCESSAMENTO CONCLUÍDO!
============================================================
   Total processado: 1547
   Inseridos/Atualizados: 1547
   Erros: 0
============================================================

📊 Total de pacientes no banco de dados: 1547
```

---

## 🔧 Primeira vez usando?

O script instalará automaticamente as dependências necessárias:
- pandas (leitura de planilhas)
- openpyxl (suporte XLSX)
- supabase (conexão com banco)

---

## 💡 Dica

Você pode executar o script quantas vezes quiser!  
Ele usa UPSERT, então:
- Se o paciente já existe → Atualiza os dados
- Se é novo → Insere no banco
- Nunca duplica registros
