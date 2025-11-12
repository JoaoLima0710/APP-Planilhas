#!/usr/bin/env node
/**
 * Script de deploy das Edge Functions
 * Uso: node deploy.mjs
 * Com token: SUPABASE_ACCESS_TOKEN=seu_token node deploy.mjs
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PROJECT_ID = "ruujmkanbxofxljwzvas";

const FUNCTIONS = {
  "process-spreadsheet": "supabase/functions/process-spreadsheet/index.ts",
  "process-attendance": "supabase/functions/process-attendance/index.ts",
};

async function getAccessToken() {
  // Método 1: Variável de ambiente
  if (process.env.SUPABASE_ACCESS_TOKEN) {
    console.log("✓ Token de: SUPABASE_ACCESS_TOKEN");
    return process.env.SUPABASE_ACCESS_TOKEN;
  }

  // Método 2: Arquivo ~/.supabase/access-token
  const homeDir = process.env.HOME || process.env.USERPROFILE;
  const tokenFile = path.join(homeDir, ".supabase", "access-token");

  try {
    if (fs.existsSync(tokenFile)) {
      const token = fs.readFileSync(tokenFile, "utf-8").trim();
      console.log(`✓ Token de: ${tokenFile}`);
      return token;
    }
  } catch (e) {
    // Arquivo não existe
  }

  return null;
}

async function deployFunction(funcName, code, token) {
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

    console.log(`   Status HTTP: ${response.status}`);

    if (response.ok) {
      console.log(`   ✅ Deploy bem-sucedido!`);
      return true;
    } else {
      const error = await response.text();
      console.log(`   ❌ Erro: ${error.substring(0, 300)}`);
      return false;
    }
  } catch (e) {
    console.log(`   ❌ Erro de conexão: ${e.message}`);
    return false;
  }
}

async function main() {
  console.log("=".repeat(60));
  console.log("🚀 SUPABASE EDGE FUNCTIONS AUTO-DEPLOY");
  console.log("=".repeat(60));

  console.log(`\n📋 Projeto: ${PROJECT_ID}`);
  console.log(`📂 Diretório: ${process.cwd()}`);

  // Obter token
  console.log("\n🔑 Obtendo access token...");
  const token = await getAccessToken();

  if (!token) {
    console.log("\n⚠️  Access token não encontrado!");
    console.log("\n   Para fazer deploy automático:");
    console.log("   1. Gere um token em: https://supabase.com/dashboard/account/tokens");
    console.log("   2. Execute: set SUPABASE_ACCESS_TOKEN=seu_token (Windows)");
    console.log("   3. Execute: node deploy.mjs");
    console.log("\n   OU use o Dashboard:");
    console.log(
      `   → https://supabase.com/dashboard/project/${PROJECT_ID}/functions`
    );

    // Ainda assim, tentaremos fazer um deploy "simulado"
    console.log("\n⚠️  Tentando deploy sem token (pode não funcionar)...");
  }

  // Deploy das funções
  const results = {};

  for (const [funcName, funcPath] of Object.entries(FUNCTIONS)) {
    console.log(`\n${"=".repeat(60)}`);

    try {
      const fullPath = path.join(__dirname, funcPath);

      if (!fs.existsSync(fullPath)) {
        console.log(`❌ Arquivo não encontrado: ${funcPath}`);
        results[funcName] = false;
        continue;
      }

      const code = fs.readFileSync(fullPath, "utf-8");
      console.log(`✓ Arquivo lido: ${funcPath} (${code.length} bytes)`);

      if (token) {
        results[funcName] = await deployFunction(funcName, code, token);
      } else {
        console.log(`⚠️  Pulando deploy (sem token)`);
        results[funcName] = false;
      }
    } catch (e) {
      console.log(`❌ Erro: ${e.message}`);
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

  if (successCount === totalCount && successCount > 0) {
    console.log("\n🎉 Deploy completo! Pronto para testar!");
  } else {
    console.log("\n💡 Se quiser deploy automático:");
    console.log("   1. Token: https://supabase.com/dashboard/account/tokens");
    console.log("   2. Windows: set SUPABASE_ACCESS_TOKEN=seu_token");
    console.log("   3. PowerShell: $env:SUPABASE_ACCESS_TOKEN='seu_token'");
    console.log("   4. Execute: node deploy.mjs");
  }
}

main().catch(console.error);
