# 📊 Especificação Técnica - Sistema de Análise de Frequência CAPS AD

## 1. Estrutura de Dados

### 1.1 Planilha de Pacientes (`PLANILHAPACIENTESCAPSAD.csv`)
```
Colunas Principais:
┌─────────────────────────────────────────────────────┐
│ PRONTUÁRIO (chave primária) → "728077"             │
│ NOMES → "ADA O CORDEIRO DE FREITAS"                │
│ DN → "09/16/65" (data de nascimento)               │
│ TERAPEUTA DE REFERÊNCIA → "GRAZILLE/BRUNO"         │
│ SETOR → "CENTRAL/NORTE" | "OESTE" | "SUL" | "LESTE"│
│ ROTINA → "NÃO INTENSIVO" | "INTENSIVO" | etc      │
│ CID → "F.10.2" (código diagnóstico)                │
│ DATA ULTIMO PCS → "8/2/2024"                       │
│ DIAS → "642" (dias em tratamento)                  │
└─────────────────────────────────────────────────────┘
```

### 1.2 Planilhas de Frequência (Ex: `CENTRALNORTENOVEMBRO.csv`)
```
Estrutura Variável:
┌──────────────────────────────────────────────────────────────────┐
│ Linhas 1-2: Descrição/metadata (pode estar vazia)               │
│ Linha 3-4: Headers (PRONTUÁRIO, NOME, SETOR, ROTINA, ...)      │
│ Colunas de Data: 4, 11, 18, 25 (dias do mês)                   │
│ Valores: P, p, F, f, ou vazio                                   │
└──────────────────────────────────────────────────────────────────┘
```

### 1.3 Estrutura de Dados em Memória
```python
{
  "pacientes": {
    "728077": {  # prontuário
      "nome": "ADA O CORDEIRO DE FREITAS",
      "setor": "CENTRAL/NORTE",
      "rotina": "NÃO INTENSIVO",
      "modalidade": "...",
      "cid": "F.10.2",
      "frequencias": [
        {"data": "2024-11-04", "presenca": True},
        {"data": "2024-11-11", "presenca": False},
        ...
      ]
    }
  },
  "resumo": {
    "728077": {
      "total_faltas": 8,
      "total_presencas": 12,
      "taxa_ausencia": 40.0
    }
  }
}
```

---

## 2. Fluxo de Processamento

### Passo 1: Upload de Arquivos
```
usuário seleciona:
  └─ 1x PLANILHAPACIENTESCAPSAD.csv (mestre)
  └─ N x CENTRALNORTENOVEMBRO.csv (frequência)
  └─ N x LESTE-NOVEMBRO.csv (frequência)
     └─ ...
```

### Passo 2: Parsing
```
Para cada arquivo:
  1. Detectar formato (CSV ou ODS)
  2. Ler com pandas.read_csv() ou odf library
  3. Normalizar nomes de colunas (maiúscula, sem espaços)
  4. Validar presença de colunas obrigatórias
```

### Passo 3: Processamento
```
1. Carregar mestre (pacientes)
   └─ Criar índice por PRONTUÁRIO
   
2. Para cada arquivo de frequência:
   └─ Identificar linhas de data (headers)
   └─ Para cada linha de dados:
       ├─ Encontrar paciente por PRONTUÁRIO
       ├─ Para cada coluna de data:
       │   └─ Registrar P/F (normalizado)
       └─ Atualizar contador de frequências
       
3. Consolidar resultados
   └─ total_faltas = count(F) por paciente
   └─ total_presencas = count(P) por paciente
   └─ taxa_ausencia = (faltas / (faltas + presencas)) * 100
```

### Passo 4: Apresentação
```
Tabela com:
  PRONTUÁRIO | NOME | SETOR | MODALIDADE | FALTAS | PRESENCAS | TAXA (%)
  ──────────────────────────────────────────────────────────────────
  728077     | ADA  | C/N   | N.INT      | 8      | 12        | 40%
  763993     | MARCO| C/N   | INT.INT    | 15     | 5         | 75% ⚠️
  ...
```

---

## 3. Cálculos

### 3.1 Taxa de Ausência
```python
taxa_ausencia = (total_faltas / (total_faltas + total_presencas)) * 100

Exemplo:
  Faltas: 8
  Presencas: 12
  Total: 20
  Taxa: (8/20)*100 = 40%
```

### 3.2 Normalização de Frequência
```python
def normalizar_frequencia(valor):
    if str(valor).upper() in ['P']:
        return True  # Presença
    elif str(valor).upper() in ['F']:
        return False  # Falta
    else:
        return None  # Ignorar
```

---

## 4. Requisitos Técnicos

### Backend
- **Framework:** FastAPI (mais moderno) ou Flask (mais simples)
- **Parsing:** pandas (CSV), openpyxl (XLSX), odf (ODS)
- **Processing:** numpy (se necessário), dict/list (padrão)
- **API Endpoints:**
  - `POST /api/upload` - Upload de arquivos
  - `POST /api/process` - Processar dados
  - `GET /api/results` - Retorna resultados em JSON

### Frontend
- **HTML5** - Estrutura
- **CSS3** - Styling (responsive)
- **Vanilla JavaScript** - Interatividade (sem framework)
- **Features:**
  - Upload múltiplo (drag & drop)
  - Barra de progresso
  - Tabela com filtros e ordenação
  - Destaque visual (cores)

### Dependências Python
```
FastAPI==0.104.1
python-multipart==0.0.6
pandas==2.1.3
openpyxl==3.10.10
odfpy==1.4.1
python-dateutil==2.8.2
```

---

## 5. Estrutura de Diretórios

```
caps-frequency-analyzer/
├── backend/
│   ├── main.py                 # Aplicação FastAPI
│   ├── requirements.txt         # Dependências
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes.py       # Endpoints
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py       # Configurações
│   │   │   └── security.py     # Validações
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── schemas.py      # Pydantic models
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── parser.py       # Parse de arquivos
│   │   │   ├── processor.py    # Processamento de dados
│   │   │   └── calculator.py   # Cálculos
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── validators.py   # Validações
│   │       └── helpers.py      # Funções auxiliares
│   └── uploads/                # Pasta temporária de uploads
│
├── frontend/
│   ├── index.html              # Página principal
│   ├── css/
│   │   └── style.css           # Estilos
│   └── js/
│       ├── main.js             # Lógica principal
│       ├── upload.js           # Upload de arquivos
│       ├── table.js            # Tabela interativa
│       └── filters.js          # Filtros e busca
│
└── README.md                   # Documentação
```

---

## 6. Fluxo de Telas

### Tela 1: Upload
```
┌───────────────────────────────────────────┐
│        CAPS AD - Análise de Frequência    │
├───────────────────────────────────────────┤
│                                           │
│  📁 Selecione as Planilhas                │
│  ┌─────────────────────────────────────┐  │
│  │ Arraste arquivos aqui ou clique    │  │
│  │ [Selecionar Arquivos]              │  │
│  └─────────────────────────────────────┘  │
│                                           │
│  Arquivos Selecionados:                   │
│  ✓ PLANILHAPACIENTESCAPSAD.csv            │
│  ✓ CENTRALNORTENOVEMBRO.csv               │
│  ✓ LESTE-NOVEMBRO.csv                     │
│                                           │
│  [Processar Dados] →                      │
│                                           │
└───────────────────────────────────────────┘
```

### Tela 2: Processando
```
┌───────────────────────────────────────────┐
│  ⏳ Processando dados...                  │
│  ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░ 45%               │
│  Lendo pacientes... ✓                     │
│  Processando frequências... →             │
│  Consolidando resultados...               │
└───────────────────────────────────────────┘
```

### Tela 3: Resultados
```
┌─────────────────────────────────────────────────────────────┐
│        Resultados - Análise de Frequência                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Filtros:                                                   │
│ [Setor ▼] [Modalidade ▼] [Buscar...] [Exportar CSV]      │
│                                                             │
│ Prontuário | Nome      | Setor   | Modalidade | Faltas |  │
│ ────────────────────────────────────────────────────────  │
│ 763993     | MARCO     | C/NORTE | INT.INTEG  | 15 | 🔴  │
│ 728077     | ADA       | C/NORTE | NÃO INT    | 8  | 🟡  │
│ 745612     | JOÃO      | LESTE   | SEMI-INT   | 3  | 🟢  │
│                                                             │
│ [Anterior] [1] [2] [Próximo]                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Legenda: 🔴 >50% absência | 🟡 25-50% | 🟢 <25%
```

---

## 7. Validações

### 7.1 Arquivo de Pacientes
```
✓ Contém coluna PRONTUÁRIO (chave primária)
✓ Contém coluna NOMES
✓ PRONTUÁRIO é único
✓ Sem linhas duplicadas
```

### 7.2 Arquivo de Frequência
```
✓ Contém coluna PRONTUÁRIO
✓ Contém coluna NOME
✓ Contém coluna SETOR
✓ Headers de data identificáveis (numéricas ou datas)
✓ Valores de frequência: P, p, F, f, ou vazio
```

### 7.3 Consolidação
```
✓ Não há pacientes sem registro mestre
✓ Não há registros de frequência sem paciente
✓ Taxa de ausência calculada corretamente
✓ Sem divisão por zero
```

---

## 8. Tratamento de Erros

```python
# Erro 1: Arquivo inválido
if not all_required_columns_present:
    return {"error": "Colunas obrigatórias não encontradas"}

# Erro 2: Paciente não encontrado
if prontuario not in pacientes_mestre:
    log(f"Prontuário {prontuario} não encontrado no mestre")
    # Opção: ignorar ou avisar

# Erro 3: Formato de data inválido
try:
    data = parse_data(valor)
except:
    log(f"Data inválida: {valor}")
    return None

# Erro 4: Divisão por zero
if total_registros == 0:
    taxa_ausencia = None  # ou 0 / 100
```

---

## 9. Próximos Passos

1. ✅ Análise concluída
2. ➡️ Implementar backend (FastAPI + services)
3. ➡️ Implementar frontend (HTML + JS)
4. ➡️ Integrar upload e processamento
5. ➡️ Testar com dados reais
6. ➡️ Deploy em servidor

---

**Status:** 🟢 Especificação Concluída - Pronto para Implementação
