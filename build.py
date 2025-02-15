import PyInstaller.__main__

try:
    PyInstaller.__main__.run([
        '--name=analisa_numero',  
        '--onefile',              
        'analisa_numero.py',     
    ])
except Exception as e:
    print(f"Ocorreu um erro: {e}")