import XLSX from 'xlsx';
import fs from 'fs';
import path from 'path';

// Procurar por arquivos de pacientes na pasta Downloads
const downloadDir = 'C:/Users/Joao/Downloads';
const files = fs.readdirSync(downloadDir)
  .filter(f => (f.endsWith('.ods') || f.endsWith('.xlsx') || f.endsWith('.xls')) && 
               (f.toLowerCase().includes('paciente') || 
                f.toLowerCase().includes('patient') ||
                f.toLowerCase().includes('1600')))
  .sort((a, b) => {
    const aTime = fs.statSync(path.join(downloadDir, a)).mtimeMs;
    const bTime = fs.statSync(path.join(downloadDir, b)).mtimeMs;
    return bTime - aTime; // Mais recente primeiro
  });

if (files.length === 0) {
  console.log('❌ Nenhum arquivo com 1600 pacientes encontrado em Downloads');
  process.exit(1);
}

const patientFile = path.join(downloadDir, files[0]);
console.log(`📖 Analisando: ${files[0]}\n`);

try {
  const workbook = XLSX.readFile(patientFile);
  const firstSheet = workbook.SheetNames[0];
  
  const worksheet = workbook.Sheets[firstSheet];
  const data = XLSX.utils.sheet_to_json(worksheet, { 
    header: 1,
    defval: '',
    blankrows: false,
    raw: false,
  });

  console.log(`📊 Total de linhas: ${data.length}\n`);

  // Procurar coluna UBSF (col 14 na estrutura anterior, mas pode variar)
  const headerRow = data[0] || [];
  let ubsfColIdx = -1;
  
  for (let col = 0; col < headerRow.length; col++) {
    const h = String(headerRow[col] || '').toLowerCase().trim();
    if (h.includes('ubsf') || h.includes('unidade')) {
      ubsfColIdx = col;
      console.log(`✓ Coluna UBSF encontrada em posição: ${col}\n`);
      break;
    }
  }

  if (ubsfColIdx < 0) {
    console.error('❌ Coluna UBSF não encontrada');
    console.log('Headers encontrados:');
    headerRow.forEach((h, i) => console.log(`  Col${i}: ${h}`));
    process.exit(1);
  }

  // Extrair todas as unidades únicas
  const unidades = new Set();
  const unitCount = new Map();
  
  for (let row = 1; row < data.length; row++) {
    const rowData = data[row] || [];
    const ubsf = String(rowData[ubsfColIdx] || '').trim();
    
    if (ubsf && ubsf.length > 0) {
      unidades.add(ubsf);
      unitCount.set(ubsf, (unitCount.get(ubsf) || 0) + 1);
    }
  }

  console.log(`📊 Total de unidades únicas: ${unidades.size}\n`);
  console.log(`📋 Lista de todas as unidades:\n`);

  // Ordenar por frequência
  const sorted = Array.from(unitCount.entries())
    .sort((a, b) => b[1] - a[1]);

  sorted.forEach(([unit, count], idx) => {
    console.log(`${(idx + 1).toString().padStart(3)}. "${unit}" (${count} pacientes)`);
  });

  // Gerar SQL INSERT
  console.log(`\n\n💾 SQL para inserir no Supabase:\n`);
  console.log('INSERT INTO health_units (name) VALUES');
  
  const sqlLines = sorted.map(([unit]) => `  ('${unit.replace(/'/g, "''")}')`);
  console.log(sqlLines.join(',\n'));
  console.log('ON CONFLICT (name) DO NOTHING;');

  // Salvar em arquivo
  const sqlContent = `-- Auto-generated SQL from analyzing patient file: ${files[0]}
-- Total de unidades: ${unidades.size}
-- Total de pacientes: ${data.length - 1}

INSERT INTO health_units (name) VALUES
${sqlLines.join(',\n')}
ON CONFLICT (name) DO NOTHING;

-- Verificar inserções
SELECT id, name FROM health_units ORDER BY name;
`;

  fs.writeFileSync('insert_health_units.sql', sqlContent);
  console.log(`\n\n✅ SQL salvo em: insert_health_units.sql`);

} catch (error) {
  console.error('❌ Erro ao analisar arquivo:', error.message);
  process.exit(1);
}
