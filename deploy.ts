#!/usr/bin/env bun
/**
 * Script para fazer deploy das Edge Functions via Supabase Management API
 * Usando Bun (mais rápido que Node)
 */

const PROJECT_ID = "ruujmkanbxofxljwzvas";
const SUPABASE_URL = "https://supabase.com";

const FUNCTIONS = {
  "process-spreadsheet": "supabase/functions/process-spreadsheet/index.ts",
  "process-attendance": "supabase/functions/process-attendance/index.ts",
};

async function readFile(path: string): Promise<string> {
  const file = Bun.file(path);
  return await file.text();
}

async function getAccessToken(): Promise<string | null> {
  // Tentar ler de .supabase/access-token
  const homeDir = process.env.HOME || process.env.USERPROFILE;
  const tokenFile = `${homeDir}/.supabase/access-token`;
  
  try {
    const file = Bun.file(tokenFile);
    if (await file.exists()) {
      const token = (await file.text()).trim();
      console.log("✓ Token obtido de: ~/.supabase/access-token");
      return token;
    }
  } catch (e) {
    // Token file não existe
  }

  // Tentar ler de SUPABASE_ACCESS_TOKEN
  if (process.env.SUPABASE_ACCESS_TOKEN) {
    console.log("✓ Token obtido de: SUPABASE_ACCESS_TOKEN");
    return process.env.SUPABASE_ACCESS_TOKEN;
  }

  return null;
}

async function deployFunction(
  funcName: string,
  code: string,
  token: string
): Promise<boolean> {
  console.log(`\n🚀 Deploy: ${funcName}`);
  console.log(`   Tamanho: ${code.length} bytes`);

  const url = `https://api.supabase.com/v1/projects/${PROJECT_ID}/functions/${funcName}`;

  const payload = {
    slug: funcName,
    name: funcName,
    verify_jwt: true,
    code: Buffer.from(code).toString("base64"),
  };

  try {
    const response = await fetch(url, {
      method: "PATCH",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (response.ok) {
      console.log(`   ✅ Status: ${response.status}`);
      console.log(`   ✓ Deploy bem-sucedido!`);
      return true;
    } else {
      const error = await response.text();
      console.log(`   ❌ Erro HTTP ${response.status}`);
      console.log(`   ${error.substring(0, 200)}`);
      return false;
    }
  } catch (e) {
    console.log(`   ❌ Erro: ${e}`);
    return false;
  }
}

async function main() {
  console.log("=".repeat(60));
  console.log("🚀 SUPABASE EDGE FUNCTIONS DEPLOY");
  console.log("=".repeat(60));

  console.log(`\n📋 Projeto: ${PROJECT_ID}`);
  console.log(`📂 Diretório: ${process.cwd()}`);

  // Obter token
  console.log("\n🔑 Obtendo access token...");
  const token = await getAccessToken();

  if (!token) {
    console.log("\n⚠️  Access token não encontrado!");
    console.log("\n   Para fazer deploy automático, você precisa de:");
    console.log("   1. Variável: SUPABASE_ACCESS_TOKEN");
    console.log("   2. Arquivo: ~/.supabase/access-token");
    console.log("\n   Ou use o Dashboard manualmente:");
    console.log(
      `   → https://supabase.com/dashboard/project/${PROJECT_ID}/functions`
    );
    process.exit(1);
  }

  console.log(`   Token: ${token.substring(0, 20)}...`);

  // Deploy das funções
  const results: { [key: string]: boolean } = {};

  for (const [funcName, funcPath] of Object.entries(FUNCTIONS)) {
    console.log(`\n${"=".repeat(60)}`);

    try {
      const code = await readFile(funcPath);
      console.log(`✓ Arquivo lido: ${funcPath}`);

      results[funcName] = await deployFunction(funcName, code, token);
    } catch (e) {
      console.log(`❌ Erro ao processar ${funcName}: ${e}`);
      results[funcName] = false;
    }
  }

  // Resumo
  console.log(`\n${"=".repeat(60)}`);
  console.log("📊 RESUMO");
  console.log("=".repeat(60));

  const successCount = Object.values(results).filter((v) => v).length;
  const totalCount = Object.keys(results).length;

  for (const [funcName, success] of Object.entries(results)) {
    const status = success ? "✅ Sucesso" : "❌ Falha";
    console.log(`  ${status}: ${funcName}`);
  }

  console.log(`\n  Total: ${successCount}/${totalCount}`);

  if (successCount === totalCount) {
    console.log("\n🎉 Deploy completo! Pronto para testar!");
    process.exit(0);
  } else {
    console.log(
      "\n❌ Deploy incompleto. Tente fazer manual via Dashboard."
    );
    process.exit(1);
  }
}

main();
