"""
Script para criar um arquivo XLSX super simples para teste
"""
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import os

# Criar um workbook novo
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Pacientes"

# Headers
headers = ["PRONTUÁRIO", "NOME", "DIAS", "SETOR", "UBSF", "ENDEREÇO COMPLETO", "BAIRRO", "TERAPEUTA", "CID"]
ws.append(headers)

# Adicionar alguns pacientes de teste
patients = [
    ["P0001", "João Silva", "10", "SUL", "USF Central", "Rua A, 123", "Centro", "Ana", "M79.9"],
    ["P0002", "Maria Santos", "45", "OESTE", "USF Oeste", "Rua B, 456", "Zona Oeste", "Carlos", "G20.9"],
    ["P0003", "Pedro Costa", "90", "LESTE", "USF Leste", "Rua C, 789", "Zona Leste", "Beth", "F41.1"],
]

for patient in patients:
    ws.append(patient)

# Salvar
output_path = "test-simple-pacientes.xlsx"
wb.save(output_path)

print(f"✅ Arquivo criado: {output_path}")
print(f"   Linhas: {len(patients)} pacientes + 1 header")
print(f"   Tamanho: {os.path.getsize(output_path)} bytes")
