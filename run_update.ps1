[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor [System.Net.SecurityProtocolType]::Tls12

$url = 'https://pikskrtgivhifxpzrxyb.supabase.co/rest/v1/rpc/sql'
$key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBpa3NrcnRnaXZoaWZ4cHpyeHliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI4ODg2NzMsImV4cCI6MjA3ODQ2NDY3M30.s7bvipZ2lFe7bKCDp9Wwl_8y_PDP7ilj9GHh4IdJKnQ'

$sql = @"
BEGIN;
UPDATE patients
SET health_unit_id = (
  SELECT id FROM health_units ORDER BY RANDOM() LIMIT 1
)
WHERE health_unit_id IS NULL;

SELECT 
  COUNT(*) as total_patients,
  COUNT(CASE WHEN health_unit_id IS NOT NULL THEN 1 END) as with_health_unit,
  COUNT(CASE WHEN health_unit_id IS NULL THEN 1 END) as without_health_unit
FROM patients;
COMMIT;
"@

$body = @{ query = $sql } | ConvertTo-Json

Write-Host "Executando UPDATE de health_unit_id para todos os pacientes..." -ForegroundColor Cyan

try {
    $response = Invoke-RestMethod -Uri $url -Method POST -Headers @{
        'apikey' = $key
        'Authorization' = "Bearer $key"
        'Content-Type' = 'application/json'
    } -Body $body

    Write-Host "✅ UPDATE executado com sucesso!" -ForegroundColor Green
    Write-Host "Resposta:" -ForegroundColor Cyan
    $response | ConvertTo-Json -Depth 10 | Write-Host
}
catch {
    Write-Host "❌ Erro ao executar UPDATE:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host "Resposta detalhada:" -ForegroundColor Yellow
    Write-Host $_.Exception.Response -ForegroundColor Yellow
}
