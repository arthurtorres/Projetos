from constantes import *
import shutil
import os

from datetime import datetime
startTime = datetime.now()


#a = dd.read_csv("./Dados_INEP/Aluno.csv/*",
          #      encoding="ISO-8859-1",dtype={'CO_ALUNO': 'object'})

print('Fazendo a limpeza de dados ociosos')
criandoenderecos(diretorio,zip_files) # ciranco os endereços de acesso
for data in diretorio :
    shutil.rmtree(data)
for data in zip_files :
    os.remove(data)


print("Limpeza de dados ociosos completa!")
#number = a.npartitions
#datafinal = a.get_partition(0).compute()
#print(number)
#for i in range(number - 1) :
   # i = i+1
   # partcheck = a.get_partition(i)
   # partcheck = partcheck.compute()
  #  datafinal = datafinal.merge(partcheck,how = "outer").drop_duplicates("CO_ALUNO")
 #   print(f"DROPANDO ANALISE {i} DO CODIGO")
#print(f'O NOSSO DATASET TEM AGORA {len(datafinal)} linhas. Bem mais facil de trabalar.')
