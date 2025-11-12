$url = 'https://pikskrtgivhifxpzrxyb.supabase.co/rest/v1/patients?select=id,prontuario,name,health_unit_id&limit=5&offset=0'
$key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBpa3NrcnRnaXZoaWZ4cHpyeHliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI4ODg2NzMsImV4cCI6MjA3ODQ2NDY3M30.s7bvipZ2lFe7bKCDp9Wwl_8y_PDP7ilj9GHh4IdJKnQ'

Write-Host "Verificando 5 primeiros pacientes..." -ForegroundColor Cyan
try {
    $result = Invoke-RestMethod -Uri $url -Headers @{'apikey'=$key}
    $result | ForEach-Object {
        Write-Host "ID: $($_.id | Select-Object -First 8)... | Prontuario: $($_.prontuario) | Health Unit ID: $($_.health_unit_id)" -ForegroundColor White
    }
}
catch {
    Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`nTentando contar via query string..." -ForegroundColor Cyan
$countUrl = 'https://pikskrtgivhifxpzrxyb.supabase.co/rest/v1/patients?select=id&limit=1'
try {
    $countResult = Invoke-RestMethod -Uri $countUrl -Headers @{'apikey'=$key}
    Write-Host "Resposta obtida, total aprox: $($countResult.Count)" -ForegroundColor Green
}
catch {
    Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
}
