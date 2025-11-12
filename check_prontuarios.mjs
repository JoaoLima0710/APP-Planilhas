import XLSX from 'xlsx';
import fs from 'fs';

const attendanceFile = 'C:/Users/Joao/Downloads/SUL-NOVEMBRO.ods';

if (!fs.existsSync(attendanceFile)) {
  console.error('❌ Arquivo não encontrado');
  process.exit(1);
}

const workbook = XLSX.readFile(attendanceFile);
const firstSheet = workbook.SheetNames[0];
const worksheet = workbook.Sheets[firstSheet];
const data = XLSX.utils.sheet_to_json(worksheet, { 
  header: 1,
  defval: '',
  blankrows: false,
  raw: false,
});

console.log('📊 Analisando formato de prontuários na planilha:\n');

// Encontrar linha com prontuários
let prontuarioRowIdx = -1;
for (let rowIdx = 0; rowIdx < Math.min(5, data.length); rowIdx++) {
  const rowData = data[rowIdx] || [];
  for (let colIdx = 0; colIdx < rowData.length; colIdx++) {
    const cellStr = String(rowData[colIdx] || "").trim();
    if (/^\d{4,8}$/.test(cellStr)) {
      prontuarioRowIdx = rowIdx;
      break;
    }
  }
  if (prontuarioRowIdx >= 0) break;
}

if (prontuarioRowIdx < 0) {
  console.error('❌ Nenhuma linha com prontuários encontrada');
  process.exit(1);
}

console.log(`Prontuários encontrados na linha ${prontuarioRowIdx}\n`);
console.log('Prontuários extraídos da planilha:\n');

const prontuariosFromFile = [];
for (let rowIdx = prontuarioRowIdx + 1; rowIdx < data.length && prontuariosFromFile.length < 15; rowIdx++) {
  const rowData = data[rowIdx] || [];
  const prontuarioStr = String(rowData[0] || "").trim();
  
  if (/^\d{4,8}$/.test(prontuarioStr)) {
    prontuariosFromFile.push(prontuarioStr);
    console.log(`  ${prontuariosFromFile.length.toString().padStart(2)}. "${prontuarioStr}" (${prontuarioStr.length} dígitos)`);
  }
}

console.log('\n✅ Agora compare esses prontuários com os da base de dados');
console.log('   Digite os prontuários do banco de dados para comparação');
console.log('\nFormatos esperados na base:');
console.log('  - 6 dígitos com leading zeros: "092153"');
console.log('  - 7 dígitos: "1102523"');
console.log('  - Ou sem padding: "92153", "1102523"');
