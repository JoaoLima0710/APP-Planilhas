$url = 'https://pikskrtgivhifxpzrxyb.supabase.co/rest/v1/patients?select=count=exact'
$key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBpa3NrcnRnaXZoaWZ4cHpyeHliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI4ODg2NzMsImV4cCI6MjA3ODQ2NDY3M30.s7bvipZ2lFe7bKCDp9Wwl_8y_PDP7ilj9GHh4IdJKnQ'

Write-Host "Contando pacientes..." -ForegroundColor Cyan
try {
    $result = Invoke-RestMethod -Uri $url -Headers @{'apikey'=$key;'Prefer'='count=exact'} -SkipHttpErrorCheck
    Write-Host "Resposta HTTP: $($result)" -ForegroundColor Green
}
catch {
    Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n`nTentando sem count..." -ForegroundColor Cyan
$url2 = 'https://pikskrtgivhifxpzrxyb.supabase.co/rest/v1/patients?select=id,prontuario&limit=1'
try {
    $result2 = Invoke-RestMethod -Uri $url2 -Headers @{'apikey'=$key}
    Write-Host "Total retornado: $($result2.Count)" -ForegroundColor Green
    $result2 | ConvertTo-Json | Write-Host
}
catch {
    Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
}
