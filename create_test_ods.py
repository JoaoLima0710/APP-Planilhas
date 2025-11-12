#!/usr/bin/env python3
"""
Conversor de teste para validar parsing de pacientes
Cria um arquivo ODS com N pacientes para teste
"""

import os
import sys

# Tenta importar bibliotecas necessárias
try:
    from odfpy import opendocument, table, tablecell, tablerow, text
    HAS_ODF = True
except ImportError:
    HAS_ODF = False

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

def create_test_ods_with_pandas():
    """Cria arquivo ODS de teste com pandas (se disponível)"""
    if not HAS_PANDAS:
        print("❌ pandas não disponível. Use: pip install pandas openpyxl")
        return False
    
    import pandas as pd
    
    # Cria dados de teste com 200 pacientes
    data = {
        'ID': [f'{i:03d}' for i in range(1, 201)],
        'Nome': [f'Paciente {i}' for i in range(1, 201)],
        'Email': [f'paciente{i}@email.com' for i in range(1, 201)],
        'Telefone': [f'11 9876-{5000+i:04d}' for i in range(1, 201)]
    }
    
    df = pd.DataFrame(data)
    
    # Salva como XLSX (pode depois converter para ODS)
    filename = 'test-200-pacientes.xlsx'
    df.to_excel(filename, index=False, sheet_name='Pacientes')
    print(f"✅ Arquivo criado: {filename}")
    print(f"📊 Total de pacientes: {len(df)}")
    return True

def create_minimal_ods():
    """Cria um arquivo ODS mínimo com XML direto"""
    import zipfile
    import shutil
    from pathlib import Path
    
    print("🔨 Criando arquivo ODS mínimo com 200 pacientes...")
    
    # Estrutura básica do ODS
    ods_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<office:document-content
  xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
  xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0"
  xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
  xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0"
  xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"
  xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0"
  xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0"
  xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0"
  xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0"
  xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0"
  xmlns:math="http://www.w3.org/1998/Math/MathML"
  xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0"
  xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0"
  xmlns:ooo="http://openoffice.org/2004/office"
  xmlns:ooow="http://openoffice.org/2004/writer"
  xmlns:oooc="http://openoffice.org/2004/calc"
  xmlns:dom="http://www.w3.org/2001/xml-events"
  xmlns:xforms="http://www.w3.org/2002/xforms"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  office:version="1.2">
  <office:body>
    <office:spreadsheet>
      <table:table table:name="Pacientes" table:style-name="ta1">'''
    
    # Cabeçalho
    ods_xml += '''
        <table:table-row table:style-name="ro1">
          <table:table-cell table:value-type="string" office:value-type="string">
            <text:p>ID</text:p>
          </table:table-cell>
          <table:table-cell table:value-type="string" office:value-type="string">
            <text:p>Nome</text:p>
          </table:table-cell>
          <table:table-cell table:value-type="string" office:value-type="string">
            <text:p>Email</text:p>
          </table:table-cell>
          <table:table-cell table:value-type="string" office:value-type="string">
            <text:p>Telefone</text:p>
          </table:table-cell>
        </table:table-row>'''
    
    # Adiciona 200 pacientes
    for i in range(1, 201):
        ods_xml += f'''
        <table:table-row table:style-name="ro1">
          <table:table-cell table:value-type="string" office:value="ID{i:03d}">
            <text:p>ID{i:03d}</text:p>
          </table:table-cell>
          <table:table-cell table:value-type="string" office:value="Paciente {i}">
            <text:p>Paciente {i}</text:p>
          </table:table-cell>
          <table:table-cell table:value-type="string" office:value="pac{i}@email.com">
            <text:p>pac{i}@email.com</text:p>
          </table:table-cell>
          <table:table-cell table:value-type="string" office:value="11 9876-{5000+i:04d}">
            <text:p>11 9876-{5000+i:04d}</text:p>
          </table:table-cell>
        </table:table-row>'''
    
    ods_xml += '''
      </table:table>
    </office:spreadsheet>
  </office:body>
</office:document-content>'''
    
    # Cria arquivo ZIP (ODS é ZIP internamente)
    with zipfile.ZipFile('test-200-pacientes.ods', 'w', zipfile.ZIP_DEFLATED) as ods_zip:
        # META-INF/manifest.xml
        manifest = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0">
  <manifest:file-entry manifest:full-path="/" manifest:media-type="application/vnd.oasis.opendocument.spreadsheet"/>
  <manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>
  <manifest:file-entry manifest:full-path="meta.xml" manifest:media-type="text/xml"/>
  <manifest:file-entry manifest:full-path="styles.xml" manifest:media-type="text/xml"/>
</manifest:manifest>'''
        
        ods_zip.writestr('META-INF/manifest.xml', manifest)
        
        # mimetype
        ods_zip.writestr('mimetype', 'application/vnd.oasis.opendocument.spreadsheet', compress_type=zipfile.ZIP_STORED)
        
        # meta.xml
        meta = '''<?xml version="1.0" encoding="UTF-8"?>
<office:document-meta xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" office:version="1.2">
  <office:meta>
    <dc:title>Teste Pacientes</dc:title>
    <dc:description>Arquivo de teste com 200 pacientes</dc:description>
    <meta:creation-date>2024-01-01T00:00:00</meta:creation-date>
  </office:meta>
</office:document-meta>'''
        
        ods_zip.writestr('meta.xml', meta)
        
        # styles.xml
        styles = '''<?xml version="1.0" encoding="UTF-8"?>
<office:document-styles xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0">
  <office:styles/>
  <office:automatic-styles/>
</office:document-styles>'''
        
        ods_zip.writestr('styles.xml', styles)
        
        # content.xml (o principal)
        ods_zip.writestr('content.xml', ods_xml)
    
    print(f"✅ Arquivo criado: test-200-pacientes.ods")
    print(f"📊 Total de pacientes: 200")
    print(f"📁 Localização: {os.path.abspath('test-200-pacientes.ods')}")

if __name__ == '__main__':
    try:
        # Primeiro tenta com pandas
        if create_test_ods_with_pandas():
            sys.exit(0)
    except Exception as e:
        print(f"⚠️  Erro com pandas: {e}")
    
    # Se pandas falhar, cria com XML direto
    try:
        create_minimal_ods()
        print("\n✨ Agora você pode fazer upload de 'test-200-pacientes.ods' no app!")
    except Exception as e:
        print(f"❌ Erro ao criar ODS: {e}")
        sys.exit(1)
