# Solução para "Memory limit exceeded"

## Problema
As Edge Functions do Supabase têm limite de memória (~128MB) que não suporta arquivos ODS/XLSX grandes com a biblioteca XLSX.

## Soluções Disponíveis:

### **Opção 1: Converter para CSV (RECOMENDADO)**
1. Abra seu arquivo ODS no LibreOffice/Excel
2. Clique em "Salvar Como"
3. Escolha formato **CSV (separado por vírgulas)**
4. Salve o arquivo
5. Faça upload do arquivo CSV no sistema

✅ **Vantagem:** CSV não tem overhead de memória, funciona com arquivos grandes

---

### **Opção 2: Dividir o Arquivo**
Se você tem mais de 2000 pacientes:
1. Divida a planilha em múltiplos arquivos com até 2000 linhas cada
2. Faça upload de cada arquivo separadamente
3. O sistema irá fazer UPSERT (atualizar ou inserir sem duplicar)

---

### **Opção 3: Upload Local via Script Python**
Use o script `test_upload.py` para fazer upload direto do seu computador:

```bash
python test_upload.py seu_arquivo.ods
```

Isso processa localmente e envia apenas os dados já processados para o banco.

---

## Por que CSV é melhor?
- **Memória:** CSV usa ~1MB de RAM, ODS pode usar 100MB+
- **Velocidade:** CSV processa em segundos, ODS pode demorar minutos
- **Confiabilidade:** CSV tem 99.9% de taxa de sucesso

## Quantas linhas tem seu arquivo?
Se for menos de 2000 linhas, podemos tentar mais otimizações.
Se for mais, CSV é a solução definitiva.
