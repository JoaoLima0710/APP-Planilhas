import XLSX from 'xlsx';
import * as fs from 'fs';
import * as path from 'path';

const attendanceFile = 'C:/Users/Joao/Downloads/SUL-NOVEMBRO.ods';

console.log(`📖 Analisando arquivo: ${attendanceFile}`);
console.log('='.repeat(80));

try {
  // Verificar se arquivo existe
  if (!fs.existsSync(attendanceFile)) {
    // Procurar por arquivos .ods na pasta Downloads
    const downloadDir = 'C:/Users/Joao/Downloads';
    const files = fs.readdirSync(downloadDir).filter(f => f.endsWith('.ods'));
    
    if (files.length === 0) {
      console.error('❌ Nenhum arquivo .ods encontrado');
      process.exit(1);
    }
    
    console.warn(`⚠️  Arquivo padrão não encontrado, usando: ${files[0]}`);
    attendanceFile = path.join(downloadDir, files[0]);
  }

  // Ler arquivo
  const workbook = XLSX.readFile(attendanceFile, { cellFormula: false, cellStyles: false });
  const sheets = workbook.SheetNames;

  console.log(`\n📊 Arquivo tem ${sheets.length} abas:\n`);
  sheets.forEach(sheet => console.log(`  • ${sheet}`));

  console.log('\n' + '='.repeat(80));
  
  // Analisar primeira aba
  const firstSheet = sheets[0];
  console.log(`\n🔍 Analisando primeira aba: "${firstSheet}"\n`);
  
  const worksheet = workbook.Sheets[firstSheet];
  const data = XLSX.utils.sheet_to_json(worksheet, { 
    header: 1,
    defval: '',
    blankrows: false,
    raw: false,
  });

  console.log(`Aba tem ${data.length} linhas\n`);

  // Mostrar primeiras 10 linhas x 15 colunas
  console.log('Primeiras 10 linhas x 15 colunas:\n');
  
  // Header com números de coluna
  process.stdout.write('    ');
  for (let col = 0; col < Math.min(15, data[0]?.length || 0); col++) {
    process.stdout.write(`Col${col.toString().padStart(2, '0')}  `);
  }
  console.log();
  console.log('    ' + '-'.repeat(70));

  // Dados
  for (let row = 0; row < Math.min(10, data.length); row++) {
    process.stdout.write(`L${(row + 1).toString().padStart(2, '0')} | `);
    const rowData = data[row] || [];
    for (let col = 0; col < Math.min(15, rowData.length); col++) {
      const cell = String(rowData[col] || '').substring(0, 5).padEnd(5);
      process.stdout.write(`${cell}  `);
    }
    console.log();
  }

  console.log('\n' + '='.repeat(80));

  // Procurar por prontuários (4-8 dígitos)
  console.log('\n🔎 Procurando por prontuários (números 4-8 dígitos)...\n');

  let prontuarioCount = 0;
  for (let row = 0; row < data.length; row++) {
    const rowData = data[row] || [];
    for (let col = 0; col < rowData.length; col++) {
      const cellStr = String(rowData[col] || '').trim();
      if (/^\d{4,8}$/.test(cellStr)) {
        if (prontuarioCount < 10) {
          console.log(`  ✓ Prontuário "${cellStr}" em L${row + 1} Col${col + 1}`);
        }
        prontuarioCount++;
      }
    }
  }
  console.log(`  ... total de ${prontuarioCount} células que parecem prontuários`);

  // Procurar por P/F
  console.log('\n🔎 Procurando por status (P ou F)...\n');

  let statusCount = 0;
  for (let row = 0; row < data.length; row++) {
    const rowData = data[row] || [];
    for (let col = 0; col < rowData.length; col++) {
      const cellStr = String(rowData[col] || '').trim().toUpperCase();
      if (cellStr === 'P' || cellStr === 'F') {
        if (statusCount < 10) {
          console.log(`  ✓ Status "${cellStr}" em L${row + 1} Col${col + 1}`);
        }
        statusCount++;
      }
    }
  }
  console.log(`  ... total de ${statusCount} células com P/F`);

  console.log('\n' + '='.repeat(80));
  console.log('\n✅ Análise concluída\n');

} catch (error) {
  console.error('❌ Erro:', error.message);
  process.exit(1);
}
