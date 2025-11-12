$url = 'https://pikskrtgivhifxpzrxyb.supabase.co/rest/v1/patients?select=id,prontuario,name,health_unit_id&limit=10'
$key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBpa3NrcnRnaXZoaWZ4cHpyeHliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI4ODg2NzMsImV4cCI6MjA3ODQ2NDY3M30.s7bvipZ2lFe7bKCDp9Wwl_8y_PDP7ilj9GHh4IdJKnQ'

Write-Host "Verificando 10 primeiros pacientes..." -ForegroundColor Cyan
$result = Invoke-RestMethod -Uri $url -Headers @{'apikey'=$key}
$result | ConvertTo-Json -Depth 3

Write-Host "`nContando pacientes com/sem health_unit_id..." -ForegroundColor Cyan
$countUrl = 'https://pikskrtgivhifxpzrxyb.supabase.co/rest/v1/rpc/sql'
$countSql = "SELECT COUNT(*) as total, COUNT(CASE WHEN health_unit_id IS NOT NULL THEN 1 END) as com_unit FROM patients;"
$countBody = @{ query = $countSql } | ConvertTo-Json

$countResult = Invoke-RestMethod -Uri $countUrl -Method POST -Headers @{
    'apikey' = $key
    'Authorization' = "Bearer $key"
    'Content-Type' = 'application/json'
} -Body $countBody

$countResult | ConvertTo-Json -Depth 5
