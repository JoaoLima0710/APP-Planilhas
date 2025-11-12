#!/usr/bin/env python3
"""Gerar arquivo CSV de teste com 1600 pacientes

Formato esperado:
- Prontuário: Identificador único do paciente
- Nome: Nome completo
- Dias: Dias desde o último PCS (Procedimento/Consulta)
- Setor: Área de atendimento
- Modalidade: Tipo de atendimento (Individual/Grupo)
- Rotina: Frequência de atendimento
- UBSF: Unidade Básica de Saúde
- Endereço Completo: Logradouro
- Bairro: Bairro/Distrito
- Terapeuta: Profissional responsável
- CID: Código de diagnóstico
"""

import csv
from pathlib import Path

# Nome do arquivo de saída
output_file = Path(__file__).parent / "test-1600-patients.csv"

# Headers - IMPORTANTE: "Dias" refere-se aos dias desde o ÚLTIMO PCS, não dias de falta
headers = ["Prontuário", "Nome", "Dias", "Setor", "Modalidade", "Rotina", "UBSF", "Endereço Completo", "Bairro", "Terapeuta", "CID"]

# Dados
sectors = ["Psicologia", "Fisioterapia", "Fonoaudiologia", "Terapia Ocupacional"]
modalities = ["Individual", "Grupo", "Dupla"]
routines = ["Semanal", "Quinzenal", "Mensal"]
ubsfs = ["USF Centro", "USF Norte", "USF Sul", "USF Leste", "USF Oeste"]
neighborhoods = ["Centro", "Norte", "Sul", "Leste", "Oeste", "Zona Industrial", "Vila Nova"]
therapists = ["João Silva", "Maria Santos", "Pedro Costa", "Ana Paula", "Carlos Mendes", "Lucia Ferreira"]
cids = ["F41.1", "M54.0", "F32.9", "F80.0", "F41.0", "M25.9", "F43.1", "F80.1", "F41.2", "M54.1"]

# Gerar 1600 linhas
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    
    for i in range(1, 1601):
        prontuario = f"P{i:04d}"
        nome = f"Paciente {i:04d}"
        # Dias desde o último PCS (varia de 0 a 365)
        dias = (i * 7) % 365
        setor = sectors[i % len(sectors)]
        modalidade = modalities[i % len(modalities)]
        rotina = routines[i % len(routines)]
        ubsf = ubsfs[i % len(ubsfs)]
        endereco = f"Rua {'ABCDEFGHIJKLMNOPQRST'[i % 20]}, {100 + (i % 900)}"
        bairro = neighborhoods[i % len(neighborhoods)]
        terapeuta = therapists[i % len(therapists)]
        cid = cids[i % len(cids)]
        
        writer.writerow([prontuario, nome, dias, setor, modalidade, rotina, ubsf, endereco, bairro, terapeuta, cid])

print(f"✅ Arquivo gerado: {output_file}")
print(f"📊 Total de linhas: 1600 pacientes")
print(f"📝 Coluna 'Dias' = Dias desde o último PCS (Procedimento/Consulta)")
