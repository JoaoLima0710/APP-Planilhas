# 🎯 Próximo Passo: Processamento de Presença

## Estrutura da Planilha de Presença
- **Arquivo**: `SUL-NOVEMBRO.ods`
- **Abas**: Segunda, Terça, Quarta, Quinta, Sexta (e outras)
- **Formato**: Prontuários nas colunas (4, 5, 6, 7, 8, etc.)
- **Finalidade**: Rastrear quem compareceu cada dia da semana

## Próximos Passos

### 1. **Upload da Planilha de Presença**
- Criar seção adicional no frontend
- Permitir upload de arquivo ODS/XLSX de presença
- Chamar novo Edge Function: `process-weekly-attendance`

### 2. **Processamento no Backend**
- Ler arquivo ODS/XLSX
- Extrair prontuários que compareceram cada dia
- Comparar com pacientes no banco:
  - Se compareceu na semana → `days_since_last_visit = 0`
  - Se não compareceu → `days_since_last_visit += 7`

### 3. **Atualização do Frontend**
- Mostrar resultados do processamento:
  - ✅ Pacientes com presença
  - ❌ Pacientes ausentes
  - ⚠️ Pacientes não encontrados

## Dados da Planilha
```
Segunda-feira: 
  Col 4: 1102523 (presente)
  Col 5: 921539 (presente)
  Col 6: 706957 (presente)
  ... e mais

Terça-feira: (mesmo padrão)
```

## Tabela de Atualização Esperada

| Prontuário | Nome | Dias Antes | Presença Esta Semana | Dias Depois |
|------------|------|-----------|-------------------|------------|
| 1102523 | XXX | 7 | ✅ Segunda | 0 |
| 921539 | XXX | 14 | ✅ Quarta | 0 |
| 706957 | XXX | 0 | ❌ Ausente | 7 |

## O que Precisa Ser Feito:

1. ✅ Estrutura do arquivo analisada
2. ⚠️ Edge Function para processar presença (requer revisão do código existente)
3. ⚠️ UI para upload de planilha de presença
4. ⚠️ Atualização de `days_since_last_visit` baseado na presença

## Estrutura Esperada do JSON de Entrada:
```json
{
  "Segunda": ["1102523", "921539", "706957", ...],
  "Terça": ["1102523", "123456", ...],
  "Quarta": [...],
  ...
}
```

## Próximo: Vamos implementar o processamento de presença?
