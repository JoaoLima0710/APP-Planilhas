import XLSX from 'xlsx';
import fs from 'fs';

// Fazer download do arquivo do Supabase ou usar local
// Por enquanto, vou criar um debug que mostra os headers

console.log('🔍 Script de debug para headers do arquivo XLSX\n');

// Para quando você fazer upload, verifique os console.logs do navegador
// A função processSpreadsheet log os headers assim:
// console.log('Headers:', headers);
// console.log('Headers JSON:', JSON.stringify(headers));

console.log('Quando você fizer upload, verifique no console do navegador (F12):');
console.log('1. Procure por "Headers:"');
console.log('2. Procure por "Headers JSON:"');
console.log('3. Procure por "ubsfRaw" para ver o valor extraído\n');

// Se o UBSF estiver como vazio, pode ser que:
console.log('✓ Possíveis causas:');
console.log('  1. Header da coluna não é exatamente "UBSF"');
console.log('  2. Coluna UBSF está em posição diferente da 14');
console.log('  3. Arquivo tem estrutura diferente da esperada\n');

console.log('💡 Solução: Faça o upload e abra o console do navegador (F12)');
console.log('   Procure pelos logs acima e diga qual é o header real da coluna UBSF');
