// Script para debugar processamento de XLSX
import * as XLSX from 'https://deno.land/x/xlsx@0.17.0/mod.ts';
import { readFileSync } from 'node:fs';

const filePath = './test-multisheet-patients.xlsx';

try {
  console.log('📂 Lendo arquivo:', filePath);
  const buffer = readFileSync(filePath);
  console.log('✅ Buffer lido:', buffer.byteLength, 'bytes');

  const workbook = XLSX.read(buffer, { type: 'array' });
  console.log('✅ Workbook lido');
  console.log('📋 Abas:', workbook.SheetNames);

  let totalRows = 0;
  for (const sheetName of workbook.SheetNames) {
    const worksheet = workbook.Sheets[sheetName];
    const sheetData = XLSX.utils.sheet_to_json(worksheet, { defval: '' });
    console.log(`  Aba "${sheetName}": ${sheetData.length} linhas`);
    totalRows += sheetData.length;

    // Mostrar primeiras 2 linhas de cada aba
    if (sheetData.length > 0) {
      console.log(`    Primeira linha:`, JSON.stringify(sheetData[0]).substring(0, 100));
    }
  }

  console.log(`\n📊 Total: ${totalRows} linhas`);
  console.log('✅ Arquivo processado com sucesso!');
} catch (error) {
  console.error('❌ Erro:', error);
}
