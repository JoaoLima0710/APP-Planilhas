# Clinic Data Atlas - Sistema de Gestão de Pacientes

Sistema web para gerenciar dados de pacientes, frequência de atendimentos e análise de indicadores clínicos.

## 📋 Formato de Importação

### Formatos Suportados

- ✅ **CSV** (.csv) - vírgula, ponto-e-vírgula ou tab
- ✅ **ODS** (.ods) - LibreOffice Calc **com múltiplas abas**
- ✅ **XLSX/XLS** (.xlsx, .xls) - Excel **com múltiplas abas**

### Múltiplas Abas

Se sua planilha tem vários abas/sheets, o sistema lê **todas automaticamente** e consolida os dados:

```
Planilha.ods
├── Aba: "Pacientes Jan-Mar"   (500 pacientes)
├── Aba: "Pacientes Abr-Jun"   (600 pacientes)
└── Aba: "Pacientes Jul-Set"   (500 pacientes)
↓
Total processado: 1.600 pacientes
```

---

### Planilha 1: Pacientes (process-spreadsheet)

A coluna **"Dias"** refere-se aos **dias desde o último PCS (Procedimento/Consulta)**, NÃO aos dias de falta.

**Exemplo:**
| Prontuário | Nome | Dias | Setor | ... |
|-----------|------|------|-------|-----|
| P001 | Paciente 001 | 45 | Psicologia | ... |
| P002 | Paciente 002 | 60 | Fisioterapia | ... |

**Colunas Aceitas:**
- **Prontuário**: Identificador único ✅ Obrigatório
- **Nome**: Nome completo ✅ Obrigatório
- **Dias**: Dias desde o último PCS
- **Setor**: Área de atendimento
- **Modalidade**: Individual/Grupo
- **Rotina**: Frequência de atendimento
- **UBSF/Unidade**: Unidade de Saúde
- **Endereço Completo**: Logradouro
- **Bairro**: Bairro/Distrito
- **Terapeuta**: Profissional responsável
- **CID**: Código de diagnóstico

### Planilha 2: Frequência (process-attendance)

Registra presença ou falta de cada paciente em um período.

**Colunas Aceitas:**
- **Prontuário**: ID do paciente ✅ Obrigatório
- **Data Atendimento**: Data (YYYY-MM-DD)
- **Status**: P (Presente), F (Falta) ✅ Obrigatório

**Exemplo:**
| Prontuário | Data Atendimento | Status |
|-----------|------------------|--------|
| P001 | 2025-11-10 | P |
| P001 | 2025-11-09 | F |
| P002 | 2025-11-10 | P |

**Múltiplas Abas:**
Se a planilha de frequência tem abas por mês (Jan, Fev, Mar, etc), o sistema processa todas:

```
Frequência.ods
├── Aba: "Novembro"   (450 registros)
├── Aba: "Outubro"    (480 registros)
└── Aba: "Setembro"   (500 registros)
↓
Total processado: 1.430 registros de frequência
Pacientes atualizados com dias de falta
```

---

## 📚 Documentação Completa das Edge Functions

Veja o arquivo [EDGE_FUNCTIONS.md](./EDGE_FUNCTIONS.md) para mais detalhes sobre:
- Formatos esperados
- Respostas da API
- Tratamento de erros
- Campos do banco de dados

## Project info

**URL**: https://lovable.dev/projects/f00c1929-bff5-4e62-b265-bf9f3bbd3dbe

## How can I edit this code?

There are several ways of editing your application.

**Use Lovable**

Simply visit the [Lovable Project](https://lovable.dev/projects/f00c1929-bff5-4e62-b265-bf9f3bbd3dbe) and start prompting.

Changes made via Lovable will be committed automatically to this repo.

**Use your preferred IDE**

If you want to work locally using your own IDE, you can clone this repo and push changes. Pushed changes will also be reflected in Lovable.

The only requirement is having Node.js & npm installed - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)

Follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone <YOUR_GIT_URL>

# Step 2: Navigate to the project directory.
cd <YOUR_PROJECT_NAME>

# Step 3: Install the necessary dependencies.
npm i

# Step 4: Start the development server with auto-reloading and an instant preview.
npm run dev
```

**Edit a file directly in GitHub**

- Navigate to the desired file(s).
- Click the "Edit" button (pencil icon) at the top right of the file view.
- Make your changes and commit the changes.

**Use GitHub Codespaces**

- Navigate to the main page of your repository.
- Click on the "Code" button (green button) near the top right.
- Select the "Codespaces" tab.
- Click on "New codespace" to launch a new Codespace environment.
- Edit files directly within the Codespace and commit and push your changes once you're done.

## What technologies are used for this project?

This project is built with:

- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS

## How can I deploy this project?

Simply open [Lovable](https://lovable.dev/projects/f00c1929-bff5-4e62-b265-bf9f3bbd3dbe) and click on Share -> Publish.

## Can I connect a custom domain to my Lovable project?

Yes, you can!

To connect a domain, navigate to Project > Settings > Domains and click Connect Domain.

Read more here: [Setting up a custom domain](https://docs.lovable.dev/features/custom-domain#custom-domain)
