$url = 'https://pikskrtgivhifxpzrxyb.supabase.co/rest/v1/patients?select=id,prontuario,name,health_unit_id,health_units(id,name)&limit=3'
$key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBpa3NrcnRnaXZoaWZ4cHpyeHliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI4ODg2NzMsImV4cCI6MjA3ODQ2NDY3M30.s7bvipZ2lFe7bKCDp9Wwl_8y_PDP7ilj9GHh4IdJKnQ'

Write-Host "Verificando estrutura de dados de 3 pacientes..." -ForegroundColor Cyan
try {
    $result = Invoke-RestMethod -Uri $url -Headers @{'apikey'=$key}
    $result | ConvertTo-Json -Depth 5 | Write-Host
}
catch {
    Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
}
