-- Criar tabela health_units se não existir
CREATE TABLE IF NOT EXISTS health_units (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Inserir as unidades encontradas
INSERT INTO health_units (name) VALUES
  ('UBSF NOVO UMUARAMA'),
  ('UBSF CANAA I'),
  ('UBS TOCANTINS'),
  ('UBS PLANALTO'),
  ('UBSF PEQUIS'),
  ('SUL') -- Para os pacientes da planilha SUL-NOVEMBRO.ods
ON CONFLICT (name) DO NOTHING;

-- Verificar inserções
SELECT id, name FROM health_units ORDER BY name;
