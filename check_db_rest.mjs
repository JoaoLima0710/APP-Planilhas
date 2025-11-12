import * as fs from 'fs';

// Carregar variáveis de ambiente
const envFile = fs.readFileSync('.env', 'utf-8');
const env = {};
envFile.split('\n').forEach(line => {
  const [key, value] = line.split('=');
  if (key && value) {
    env[key.trim()] = value.trim().replace(/^"(.*)"$/, '$1');
  }
});

const supabaseUrl = env.VITE_SUPABASE_URL;
const supabaseKey = env.VITE_SUPABASE_PUBLISHABLE_KEY;

if (!supabaseUrl || !supabaseKey) {
  console.error('❌ Variáveis de ambiente não encontradas');
  process.exit(1);
}

console.log(`🔗 URL: ${supabaseUrl}`);
console.log(`🔑 Chave (primeiros 20 chars): ${supabaseKey.substring(0, 20)}...\n`);

// Buscar via REST API
const url = `${supabaseUrl}/rest/v1/patients?limit=20&select=id,prontuario,name,days_since_last_visit`;

console.log(`📡 Fazendo requisição: ${url}\n`);

const response = await fetch(url, {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${supabaseKey}`,
    'apikey': supabaseKey,
    'Content-Type': 'application/json',
  }
});

if (!response.ok) {
  console.error(`❌ Erro HTTP ${response.status}`);
  const text = await response.text();
  console.error(text);
  process.exit(1);
}

const patients = await response.json();

if (!patients || patients.length === 0) {
  console.error('❌ Nenhum paciente encontrado');
  process.exit(1);
}

console.log(`✅ Encontrados ${patients.length} pacientes:\n`);

patients.forEach((p, i) => {
  console.log(`${(i + 1).toString().padStart(2)}. Prontuário: "${p.prontuario}" (${p.prontuario?.length} chars, tipo: ${typeof p.prontuario}) | Nome: ${p.name?.substring(0, 20)}`);
});

console.log('\n📊 Análise de formato:\n');

const formats = {
  '4dígitos': patients.filter(p => p.prontuario?.length === 4).length,
  '5dígitos': patients.filter(p => p.prontuario?.length === 5).length,
  '6dígitos': patients.filter(p => p.prontuario?.length === 6).length,
  '7dígitos': patients.filter(p => p.prontuario?.length === 7).length,
  '8dígitos': patients.filter(p => p.prontuario?.length === 8).length,
  'null/undefined': patients.filter(p => !p.prontuario).length,
};

Object.entries(formats).forEach(([fmt, count]) => {
  if (count > 0) {
    console.log(`  ${fmt}: ${count} registros`);
  }
});

console.log('\n✅ Análise concluída');
