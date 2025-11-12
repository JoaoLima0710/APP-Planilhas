import { createClient } from '@supabase/supabase-js';
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

console.log(`🔗 Conectando ao Supabase: ${supabaseUrl}`);

const supabase = createClient(supabaseUrl, supabaseKey);

// Buscar primeiros pacientes
console.log('\n📋 Buscando primeiros 20 pacientes da base de dados...\n');

const { data: patients, error } = await supabase
  .from('patients')
  .select('id, prontuario, name, days_since_last_visit')
  .limit(20);

if (error) {
  console.error('❌ Erro ao buscar:', error);
  process.exit(1);
}

if (!patients || patients.length === 0) {
  console.error('❌ Nenhum paciente encontrado');
  process.exit(1);
}

console.log(`✅ Encontrados ${patients.length} pacientes:\n`);

patients.forEach((p, i) => {
  console.log(`${(i + 1).toString().padStart(2)}. Prontuário: "${p.prontuario}" (${p.prontuario?.length} chars) | Nome: ${p.name?.substring(0, 30)} | Dias: ${p.days_since_last_visit}`);
});

console.log('\n📊 Análise de formato:\n');

const formats = {
  '4dígitos': patients.filter(p => p.prontuario?.length === 4).length,
  '5dígitos': patients.filter(p => p.prontuario?.length === 5).length,
  '6dígitos': patients.filter(p => p.prontuario?.length === 6).length,
  '7dígitos': patients.filter(p => p.prontuario?.length === 7).length,
  '8dígitos': patients.filter(p => p.prontuario?.length === 8).length,
};

Object.entries(formats).forEach(([fmt, count]) => {
  if (count > 0) {
    console.log(`  ${fmt}: ${count} registros`);
  }
});

// Buscar TODOS os pacientes para contar
console.log('\n📊 Contando TODOS os pacientes na base...\n');

const { count, error: countError } = await supabase
  .from('patients')
  .select('*', { count: 'exact', head: true });

if (countError) {
  console.error('❌ Erro ao contar:', countError);
} else {
  console.log(`✅ Total de pacientes na base: ${count}`);
}

console.log('\n✅ Análise concluída');
