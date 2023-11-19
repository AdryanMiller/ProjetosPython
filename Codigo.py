#Bibliotecas

from pathlib import Path
import shutil as sh

# Criar a pasta onde ira ficar as outras pastas

"""Para não ter que criar uma pasta de cada vez use uma lista ex
    estados = ['MG','SP','RJ','GO','AM']
    for estado in estados:
        path(f'Pastas_Estados/{estado}').mkdir"""

# Path('Pastas_Estados').mkdir()

# Emcontrar a pasta onde esta os arquivos

caminho = Path('Arquivos_Lojas')

#Percorre os itens da pasta
arquivo = caminho.iterdir()

for arquivos in arquivo:
    name = arquivos.name
#     print(arquivos)
    print(name)

#Ver se item e de que estado

#Descobrir estado
    nome_estado = name[-6:-4]
'''PARA EU QUE NN ENDENDI, EU USEI UMA MANEIRA MAIS RAPIDA DE VER OS ESDADOS USANDO UMA FORMA DE FORMATAÇÃO DE STRING PEGANDO 
DA PARTE -6 A PARTE -4 O QUE PEGARIA AS ULTIMAS LETRAS'''
    print(nome_estado)
#     if '_MG' in name:
#         arquivo_copiar_mg = Path(f'Arquivos_Lojas/{name}')
#         arquivo_colar_mg = Path(f'Pastas_Estados/MG/{name}')
#         sh.copy2(arquivo_copiar_mg, arquivo_colar_mg)
    
#     elif '_SP' in name:
#         arquivo_copiar_sp = Path(f'Arquivos_Lojas/{name}')
#         arquivo_colar_sp = Path(f'Pastas_Estados/SP/{name}')
#         sh.copy2(arquivo_copiar_sp, arquivo_colar_sp)
        
#     elif '_RJ' in name:
#         arquivo_copiar_rj = Path(f'Arquivos_Lojas/{name}')
#         arquivo_colar_rj = Path(f'Pastas_Estados/RJ/{name}')
#         sh.copy2(arquivo_copiar_rj, arquivo_colar_rj)
        
#     elif '_GO' in name:
#         arquivo_copiar_go = Path(f'Arquivos_Lojas/{name}')
#         arquivo_colar_go = Path(f'Pastas_Estados/GO/{name}')
#         sh.copy2(arquivo_copiar_go, arquivo_colar_go)
        
#     elif '_AM' in name:
#         arquivo_copiar_am = Path(f'Arquivos_Lojas/{name}')
#         arquivo_colar_am = Path(f'Pastas_Estados/AM/{name}')
#         sh.copy2(arquivo_copiar_am, arquivo_colar_am)
        
        
    #Pode ter esse jeito aqui 
    
    if '.csv' in name:
        arquivo_copiar2 = Path(f'Arquivos_Lojas/{name}')
        arquivo_colar2 = Path(f'Pastas_Estados/{nome_estado}/{name}')
        sh.copy2(arquivo_copiar2, arquivo_colar2)
