$url = 'https://pikskrtgivhifxpzrxyb.supabase.co/functions/v1/bulk-insert-patients'
$key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBpa3NrcnRnaXZoaWZ4cHpyeHliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI4ODg2NzMsImV4cCI6MjA3ODQ2NDY3M30.s7bvipZ2lFe7bKCDp9Wwl_8y_PDP7ilj9GHh4IdJKnQ'

# Test com alguns pacientes de exemplo para ver o que volta
$testPatients = @(
    @{
        prontuario = "092153"
        name = "TESTE PATIENT"
        sector = "CAPS AD"
        health_unit = "UBSF NOVO UMUARAMA"
        days_since_last_visit = 0
    }
)

$body = @{ 
    patients = $testPatients 
} | ConvertTo-Json -Depth 5

Write-Host "Testando Edge Function com 1 paciente..." -ForegroundColor Cyan
Write-Host "Body:" -ForegroundColor Yellow
Write-Host $body -ForegroundColor Gray

try {
    $result = Invoke-RestMethod -Uri $url -Method POST -Headers @{
        'apikey' = $key
        'Authorization' = "Bearer $key"
        'Content-Type' = 'application/json'
    } -Body $body

    Write-Host "`nResposta da Edge Function:" -ForegroundColor Green
    $result | ConvertTo-Json -Depth 10 | Write-Host
}
catch {
    Write-Host "Erro: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Status: $($_.Exception.Response.StatusCode)" -ForegroundColor Red
}
