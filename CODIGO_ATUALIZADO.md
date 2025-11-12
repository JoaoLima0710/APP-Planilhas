# Código Atualizado para o Supabase Dashboard

Cole este código completo no Supabase Dashboard para a função `process-spreadsheet`:

**URL**: https://supabase.com/dashboard/project/ruujmkanbxofxljwzvas/functions/process-spreadsheet

---

```typescript
import { createClient } from "npm:@supabase/supabase-js@2.81.0";
import * as XLSX from "npm:xlsx@0.18.5";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};

const BATCH_SIZE = 200;

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders });
  }

  try {
    const authHeader = req.headers.get("Authorization");
    if (!authHeader) {
      return new Response(
        JSON.stringify({ success: false, error: "Unauthorized" }),
        { status: 401, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const supabaseServiceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");

    if (!supabaseUrl || !supabaseServiceKey) {
      throw new Error("Missing Supabase config");
    }

    const supabase = createClient(supabaseUrl, supabaseServiceKey);

    const formData = await req.formData();
    const file = formData.get("file") as File;

    if (!file) {
      return new Response(
        JSON.stringify({ success: false, error: "No file provided" }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    console.log(`Processing file: ${file.name}, type: ${file.type}`);

    let rows: any[] = [];
    const fileName = file.name.toLowerCase();

    if (fileName.endsWith('.csv')) {
      const text = await file.text();
      rows = parseCSV(text);
    } else if (fileName.endsWith('.xlsx') || fileName.endsWith('.xls') || fileName.endsWith('.ods')) {
      const arrayBuffer = await file.arrayBuffer();
      const workbook = XLSX.read(new Uint8Array(arrayBuffer), { type: 'array' });

      let sheetName = workbook.SheetNames[0];
      const patientsSheet = workbook.SheetNames.find(name => 
        name.toLowerCase().includes('paciente') || name.toLowerCase().includes('patient')
      );
      if (patientsSheet) sheetName = patientsSheet;

      console.log(`Using sheet: ${sheetName}`);
      const worksheet = workbook.Sheets[sheetName];
      const jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

      if (jsonData.length < 2) {
        throw new Error("Planilha vazia ou sem dados");
      }

      const headers = (jsonData[0] as any[]).map((h: any) => String(h || "").toUpperCase().trim());
      console.log(`Headers: ${headers.join(", ")}`);

      for (let i = 1; i < jsonData.length; i++) {
        const rowData = jsonData[i] as any[];
        if (!rowData || rowData.length === 0) continue;

        const row: any = {};
        headers.forEach((header, idx) => {
          row[header] = rowData[idx] !== undefined && rowData[idx] !== null ? String(rowData[idx]).trim() : "";
        });

        if (Object.values(row).some(v => v)) {
          rows.push(row);
        }
      }
    } else {
      throw new Error("Formato de arquivo não suportado. Use CSV, XLSX, XLS ou ODS");
    }

    console.log(`Parsed ${rows.length} rows`);

    function parseCSV(text: string): any[] {
      const parsedRows: any[] = [];
      let lines = text.split(/\r?\n/);
      while (lines.length > 0 && !lines[lines.length - 1].trim()) lines.pop();
      if (lines.length < 2) return parsedRows;

      function parseCSVLine(line: string): string[] {
        const result: string[] = [];
        let current = "";
        let insideQuotes = false;
        for (let i = 0; i < line.length; i++) {
          const char = line[i];
          if (char === '"') {
            if (insideQuotes && line[i+1] === '"') { current += '"'; i++; }
            else insideQuotes = !insideQuotes;
          } else if (char === ',' && !insideQuotes) {
            result.push(current.trim().replace(/^"|"$/g, ""));
            current = "";
          } else {
            current += char;
          }
        }
        result.push(current.trim().replace(/^"|"$/g, ""));
        return result;
      }

      const headerLine = lines[0];
      const headers = parseCSVLine(headerLine).map(h => String(h).toUpperCase().trim());

      for (let i = 1; i < lines.length; i++) {
        const line = lines[i].trim();
        if (!line) continue;
        const values = parseCSVLine(line);
        if (values.some(v => v)) {
          const row: any = {};
          headers.forEach((header, idx) => { row[header] = values[idx] || ""; });
          parsedRows.push(row);
        }
      }
      return parsedRows;
    }

    const patientsToUpsert: any[] = [];
    const rowErrors: { rowIndex: number; message: string }[] = [];

    rows.forEach((row, idx) => {
      const prontuarioRaw = row["PRONTUÁRIO"] || row["PRONTUARIO"] || row["PRONT"] || "";
      const prontuario = String(prontuarioRaw).toUpperCase().trim();
      const name = String(row["NOME"] || row["NAME"] || "").trim();
      const faltas = parseInt(String(row["FALTAS"] || row["FALTA"] || "0")) || 0;
      const sector = String(row["SETOR"] || row["SECTOR"] || "").trim();

      if (!prontuario || !name) {
        rowErrors.push({ rowIndex: idx + 2, message: "Missing prontuário or name" });
        return;
      }

      patientsToUpsert.push({
        prontuario,
        name,
        days_since_last_visit: faltas,
        sector: sector || null,
      });
    });

    let inserted = 0;
    let errors = rowErrors.length;
    const errorDetails: string[] = rowErrors.map(e => `Linha ${e.rowIndex}: ${e.message}`);

    for (let i = 0; i < patientsToUpsert.length; i += BATCH_SIZE) {
      const batch = patientsToUpsert.slice(i, i + BATCH_SIZE);
      try {
        const { data: upserted, error } = await supabase.from("patients").upsert(batch, { onConflict: "prontuario" });
        if (error) {
          console.error("Batch upsert error:", error);
          for (const p of batch) {
            try {
              const { data: singleData, error: singleErr } = await supabase.from("patients").upsert(p, { onConflict: "prontuario" });
              if (singleErr) {
                errors++;
                errorDetails.push(`Patient ${p.prontuario}: ${singleErr.message}`);
              } else {
                inserted += (singleData && singleData.length) ? singleData.length : 1;
              }
            } catch (e) {
              errors++;
              errorDetails.push(`Patient ${p.prontuario}: ${e instanceof Error ? e.message : String(e)}`);
            }
          }
        } else {
          inserted += upserted && upserted.length ? upserted.length : batch.length;
        }
      } catch (e) {
        console.error("Unexpected batch error:", e);
        for (const p of batch) {
          try {
            const { data: singleData, error: singleErr } = await supabase.from("patients").upsert(p, { onConflict: "prontuario" });
            if (singleErr) {
              errors++;
              errorDetails.push(`Patient ${p.prontuario}: ${singleErr.message}`);
            } else {
              inserted += (singleData && singleData.length) ? singleData.length : 1;
            }
          } catch (e2) {
            errors++;
            errorDetails.push(`Patient ${p.prontuario}: ${e2 instanceof Error ? e2.message : String(e2)}`);
          }
        }
      }
    }

    console.log(`Completed. Inserted: ${inserted}, Errors: ${errors}`);
    if (errorDetails.length > 0) console.log("Error details:", errorDetails.slice(0, 50));

    let dbCount: number | null = null;
    let sample: any[] | null = null;
    try {
      const { count } = await supabase.from('patients').select('*', { count: 'exact' });
      dbCount = count ?? null;
      const { data: sampleData } = await supabase.from('patients').select('prontuario,name').limit(5);
      sample = sampleData ?? null;
    } catch (e) {
      console.error('Error fetching confirmation data:', e);
    }

    return new Response(
      JSON.stringify({
        success: true,
        processed: rows.length,
        inserted,
        errors,
        errorDetails: errorDetails.length ? errorDetails : undefined,
        total: rows.length,
        db_count: dbCount,
        sample,
      }),
      { headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  } catch (error) {
    console.error("Error:", error);
    return new Response(
      JSON.stringify({
        success: false,
        error: error instanceof Error ? error.message : "Unknown error",
      }),
      { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  }
});
```

---

## Mudanças feitas:
✅ Substituído `Buffer.from(arrayBuffer)` por `new Uint8Array(arrayBuffer)`
✅ Mudado `type: 'buffer'` para `type: 'array'`
✅ Agora compatível com Deno

Copie todo o código acima e cole no Supabase Dashboard, depois clique em "Deploy".
