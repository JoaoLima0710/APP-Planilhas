import XLSX from 'xlsx';
import fs from 'fs';

console.log('📖 Gerando SQL UPDATE para atualizar pacientes com suas unidades\n');

// Lê o arquivo de pacientes
const filePath = './PLANILHA PACIENTES CAPS AD3(3).ods';

if (!fs.existsSync(filePath)) {
  console.error('❌ Arquivo não encontrado:', filePath);
  process.exit(1);
}

const workbook = XLSX.readFile(filePath);
const worksheet = workbook.Sheets['PRINCIPAL'];

if (!worksheet) {
  console.error('❌ Aba "PRINCIPAL" não encontrada');
  process.exit(1);
}

const data = XLSX.utils.sheet_to_json(worksheet, { header: 1, defval: "" });

// Headers
const headers = data[0].map(h => String(h || "").toUpperCase().trim());

// Encontrar colunas
const pronIdx = headers.findIndex(h => h.includes('PRONTUARIO'));
const ubsfIdx = headers.findIndex(h => h.includes('UBSF'));

if (pronIdx === -1 || ubsfIdx === -1) {
  console.error('❌ Colunas não encontradas');
  process.exit(1);
}

// Normalizar prontuário
const normalizeProntuario = (pront) => {
  return String(pront).trim().replace(/[^\d]/g, '').padStart(6, '0');
};

// Mapear pacientes para unidades
const updates = [];
for (let i = 1; i < data.length; i++) {
  const row = data[i];
  const prontuario = normalizeProntuario(row[pronIdx]);
  const ubsf = String(row[ubsfIdx] || "").trim();

  if (prontuario && ubsf) {
    updates.push({ prontuario, ubsf });
  }
}

// Gerar SQL com CASE statement
const caseLines = updates.map(u => {
  const ubsfEscaped = u.ubsf.replace(/'/g, "''");
  return `  WHEN '${u.prontuario}' THEN (SELECT id FROM health_units WHERE name = '${ubsfEscaped}')`;
}).join('\n');

const sqlUpdate = `UPDATE patients
SET health_unit_id = CASE prontuario
${caseLines}
  ELSE health_unit_id
END
WHERE prontuario IN (${updates.map(u => `'${u.prontuario}'`).join(',')});`;

// Salvar SQL
fs.writeFileSync('UPDATE_PACIENTES_HEALTH_UNITS.sql', sqlUpdate);

console.log('✅ SQL gerado com sucesso!\n');
console.log(`📊 Total de pacientes a atualizar: ${updates.length}\n`);
console.log('📋 Primeiros 5 updates:');
updates.slice(0, 5).forEach(u => {
  console.log(`  ${u.prontuario} → ${u.ubsf}`);
});

console.log('\n💾 Arquivo salvo: UPDATE_PACIENTES_HEALTH_UNITS.sql');
console.log('\n🚀 PRÓXIMO PASSO:');
console.log('1. Abra o arquivo UPDATE_PACIENTES_HEALTH_UNITS.sql');
console.log('2. Copie TODO o conteúdo');
console.log('3. Vá no Supabase Dashboard → SQL Editor');
console.log('4. Cole e execute\n');
