#!/usr/bin/env python3
"""Gerar arquivo CSV de teste com frequência/ausências de 100 pacientes

Formato esperado:
- Prontuário: Identificador único do paciente
- Data Atendimento: Data do atendimento (YYYY-MM-DD)
- Status: P (Presente) ou F (Falta)
"""

import csv
from datetime import datetime, timedelta
from pathlib import Path
import random

# Nome do arquivo de saída
output_file = Path(__file__).parent / "test-attendance.csv"

# Headers
headers = ["Prontuário", "Data Atendimento", "Status"]

# Data inicial (últimos 30 dias)
today = datetime.now()
start_date = today - timedelta(days=30)

# Gerar registros de frequência
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    
    # Para cada paciente (P001 a P100)
    for patient_num in range(1, 101):
        prontuario = f"P{patient_num:04d}"
        
        # Cada paciente tem múltiplos registros (4-5 atendimentos)
        num_records = random.randint(4, 5)
        
        for _ in range(num_records):
            # Data aleatória nos últimos 30 dias
            days_ago = random.randint(0, 30)
            date = today - timedelta(days=days_ago)
            data_atendimento = date.strftime("%Y-%m-%d")
            
            # 80% de presença, 20% de falta
            status = "P" if random.random() < 0.8 else "F"
            
            writer.writerow([prontuario, data_atendimento, status])

print(f"✅ Arquivo gerado: {output_file}")
print(f"📊 Registros de frequência para primeiros 100 pacientes")
print(f"📝 Status: P (Presente) ou F (Falta)")
print(f"📅 Período: últimos 30 dias")
