from pathlib import Path
import shutil

# print(Path.cwd())

caminho = Path(r'Python/projeto_integracao-pastas/Arquivos_Lojas')
arquivos = caminho.iterdir()
for arquivo in arquivos:
    print(arquivo)

# Criando uma pasta
Path('Python/projeto_integracao-pastas/Pasta Auxiliar/pasta2').mkdir()

# Criando uma cópia de um arquivo

shutil.copy2(Path("Python/projeto_integracao-pastas/Arquivos_Lojas/201802_Ibirapuera_SP.csv"), Path("Python\projeto_integracao-pastas\Pasta Auxiliar/201802_Ibirapuera_SP.csv"))

# Movendo o arquivo de uma pasta pra outra

shutil.move(Path("Python/projeto_integracao-pastas/Pasta Auxiliar/201802_Ibirapuera_SP.csv"), Path("Python/projeto_integracao-pastas/Pasta Auxiliar/pasta2/201802_Ibirapuera_SP.csv"))
