import os
from datetime import datetime
startTime = datetime.now()
print("INICIANDO TESTE!!!!")
data = "python3 dados_INEP.py;python3 dadosUnzip.py;python3 descompacta_arquivos.py;python3 cleanData.py"
os.system(data)
print("FINALIZANDO TESTE!!!!!")
tempo = (datetime.now()-startTime)
print(f'Tempo gasto no script : \n {tempo}')
