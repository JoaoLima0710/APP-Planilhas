import XLSX from 'xlsx';
import fs from 'fs';
import path from 'path';

// Procurar por arquivos de pacientes na pasta Downloads
const downloadDir = 'C:/Users/Joao/Downloads';
const files = fs.readdirSync(downloadDir)
  .filter(f => (f.endsWith('.ods') || f.endsWith('.xlsx') || f.endsWith('.xls')) && 
               (f.toLowerCase().includes('paciente') || 
                f.toLowerCase().includes('patient') ||
                f.toLowerCase().includes('sul')))
  .sort((a, b) => {
    const aTime = fs.statSync(path.join(downloadDir, a)).mtimeMs;
    const bTime = fs.statSync(path.join(downloadDir, b)).mtimeMs;
    return bTime - aTime; // Mais recente primeiro
  });

if (files.length === 0) {
  console.log('❌ Nenhum arquivo de pacientes encontrado em Downloads');
  console.log('\n📁 Arquivos disponíveis:');
  fs.readdirSync(downloadDir)
    .filter(f => f.endsWith('.ods') || f.endsWith('.xlsx') || f.endsWith('.xls'))
    .slice(0, 10)
    .forEach(f => console.log(`  - ${f}`));
  process.exit(1);
}

const patientFile = path.join(downloadDir, files[0]);
console.log(`📖 Analisando: ${files[0]}\n`);

try {
  const workbook = XLSX.readFile(patientFile);
  const firstSheet = workbook.SheetNames[0];
  
  console.log(`📊 Primeira aba: "${firstSheet}"\n`);
  
  const worksheet = workbook.Sheets[firstSheet];
  const data = XLSX.utils.sheet_to_json(worksheet, { 
    header: 1,
    defval: '',
    blankrows: false,
    raw: false,
  });

  console.log(`📋 Primeiras 5 linhas (todas as colunas):\n`);
  
  for (let row = 0; row < Math.min(5, data.length); row++) {
    const rowData = data[row] || [];
    console.log(`L${row + 1}:`);
    for (let col = 0; col < rowData.length; col++) {
      const cell = String(rowData[col] || '').substring(0, 25);
      console.log(`  Col${col}: "${cell}"`);
    }
    console.log();
  }

  // Procurar por colunas importantes
  console.log(`\n🔎 Procurando por colunas importantes:\n`);
  
  const headerRow = data[0] || [];
  const colNames = {};
  
  headerRow.forEach((header, idx) => {
    const h = String(header || '').toLowerCase().trim();
    if (h.includes('prontuário') || h.includes('prontuario') || h.includes('pront')) {
      colNames['prontuario'] = idx;
      console.log(`  ✓ Prontuário: Coluna ${idx}`);
    }
    if (h.includes('nome') || h.includes('name')) {
      colNames['nome'] = idx;
      console.log(`  ✓ Nome: Coluna ${idx}`);
    }
    if (h.includes('setor')) {
      colNames['setor'] = idx;
      console.log(`  ✓ Setor: Coluna ${idx}`);
    }
    if (h.includes('unidade') || h.includes('unit') || h.includes('ubs') || h.includes('caps')) {
      colNames['unidade'] = idx;
      console.log(`  ✓ Unidade de Saúde: Coluna ${idx}`);
    }
    if (h.includes('saúde') || h.includes('saude')) {
      colNames['saude'] = idx;
      console.log(`  ✓ Saúde: Coluna ${idx}`);
    }
  });

  // Mostrar amostra de dados
  console.log(`\n📊 Amostra de dados (primeiros 5 pacientes):\n`);
  
  for (let row = 1; row < Math.min(6, data.length); row++) {
    const rowData = data[row] || [];
    console.log(`Paciente ${row}:`);
    Object.entries(colNames).forEach(([name, colIdx]) => {
      const value = String(rowData[colIdx] || '').substring(0, 40);
      console.log(`  ${name}: "${value}"`);
    });
    console.log();
  }

} catch (error) {
  console.error('❌ Erro ao analisar arquivo:', error.message);
  process.exit(1);
}
