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

// Ler com raw=true para pegar valores numéricos puros
const data = XLSX.utils.sheet_to_json(worksheet, { 
  header: 1,
  defval: '',
  blankrows: false,
  raw: true, // ← Importante: ler valores brutos
});

console.log('📊 Primeiras 10 linhas - todas as colunas (raw=true):\n');

for (let row = 0; row < Math.min(10, data.length); row++) {
  const rowData = data[row] || [];
  console.log(`L${row}: [${rowData.slice(0, 5).map((v, i) => {
    const str = String(v || '').substring(0, 15);
    return `Col${i}="${str}"`;
  }).join(', ')}]`);
}

// Tentar ler com format: 'values' para pegar tudo
console.log('\n📊 Com header=1 e raw=false:\n');

const data2 = XLSX.utils.sheet_to_json(worksheet, { 
  header: 1,
  defval: '',
  blankrows: false,
  raw: false, // ← String
});

for (let row = 0; row < Math.min(10, data2.length); row++) {
  const rowData = data2[row] || [];
  console.log(`L${row}: [${rowData.slice(0, 5).map((v, i) => {
    const str = String(v || '').substring(0, 15);
    return `Col${i}="${str}"`;
  }).join(', ')}]`);
}

// Procurar especificamente por "1102523" (que aparecia na análise anterior)
console.log('\n🔎 Procurando por "1102523":');
for (let row = 0; row < data.length; row++) {
  const rowData = data[row] || [];
  for (let col = 0; col < rowData.length; col++) {
    const cellStr = String(rowData[col] || '');
    if (cellStr.includes('1102523') || cellStr === '1102523') {
      console.log(`  ✓ Encontrado em L${row} Col${col}: "${cellStr}"`);
    }
  }
}
