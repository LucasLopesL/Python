from pathlib import Path
import shutil

caminho = Path(r"Python/projeto_integracao-pastas/Arquivos_Lojas")
arquivos = caminho.iterdir()

# Dividir os relatórios dos estados de AM, GO, MG, RJ, SP

estados = ["AM", "SP", "GO", "MG", "RJ"]

for estado in estados:
    Path(rf"Python/projeto_integracao-pastas/Pasta Auxiliar/{estado}").mkdir()

for arquivo in arquivos:
    nome_arquivo = arquivo.name
    print(nome_arquivo)
    if nome_arquivo[-6:-4] == "AM":
        shutil.copy2(Path(rf"Python/projeto_integracao-pastas/Arquivos_Lojas/{arquivo}"), Path(rf"Python/projeto_integracao-pastas/Pasta Auxiliar/AM/{arquivo}"))
    elif nome_arquivo[-6:-4] == "_GO":
        shutil.copy2(Path(rf"Python/projeto_integracao-pastas/Arquivos_Lojas/{arquivo}"), Path(rf"Python/projeto_integracao-pastas/Pasta Auxiliar/GO/{arquivo}"))
    elif nome_arquivo[-6:-4] == "_MG":
        shutil.copy2(Path(rf"Python/projeto_integracao-pastas/Arquivos_Lojas/{arquivo}"), Path(rf"Python/projeto_integracao-pastas/Pasta Auxiliar/MG/{arquivo}"))
    elif nome_arquivo[-6:-4] == "_RJ":
        shutil.copy2(Path(rf"Python/projeto_integracao-pastas/Arquivos_Lojas/{arquivo}"), Path(rf"Python/projeto_integracao-pastas/Pasta Auxiliar/RJ/{arquivo}"))
    elif nome_arquivo[-6:-4] == "_SP":
        shutil.copy2(Path(rf"Python/projeto_integracao-pastas/Arquivos_Lojas/{arquivo}"), Path(rf"Python/projeto_integracao-pastas/Pasta Auxiliar/SP/{arquivo}"))
    else:
        pass
