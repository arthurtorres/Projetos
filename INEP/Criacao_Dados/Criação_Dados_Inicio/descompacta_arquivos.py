
from constantes import dadosInteresse,geraTodosArquivos,types1,types2 , col_selIES2 ,col_selIES1,col_sel,sel09_16,sel17,sel18_19,renomear2019
import warnings
warnings.filterwarnings("ignore")
import dask.dataframe as dd

arquivos= []
print("Iniciando a geração de arquivos")
for ds in dadosInteresse :
  arquivos.append(geraTodosArquivos(ds))
print("Finalizando a geração de arquivos")

datasets = []
count = 0

                     
anos = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
                
for arquivo in arquivos[0] :
  pedaco =dd.read_csv(arquivo,sep = "|",encoding="ISO-8859-1",dtype = types1)
 
  if count in [0,1,2,3,4,5,6,7] :
   pedaco = pedaco[sel09_16]
  elif count in [8] :
   pedaco = pedaco[sel17]

  else:
   pedaco = pedaco[sel18_19]


  
  pedaco["Ano"] = anos[count]
                                     
  colunas = ["CO_IES","CO_ALUNO","Cat_Adm","CO_CURSO","Nivel_Aca",
              "Cor/Raca","Genero","Cota_Racial","Apoio_Social","Ano"]
  pedaco.columns =colunas
  datasets.append(pedaco)
  count += 1

dataAluno = dd.concat(datasets)

dataAluno.Cat_Adm = dataAluno.Cat_Adm.astype("int8")
dataAluno.Nivel_Aca = dataAluno.Nivel_Aca.astype("int8")
dataAluno.Genero = dataAluno.Genero.astype("int8")
dataAluno.Cota_Racial = dataAluno.Cota_Racial.astype("bool")
dataAluno.Apoio_Social = dataAluno.Apoio_Social.astype("bool")
dataAluno["Cor/Raca"] = dataAluno["Cor/Raca"].astype("int8")



datasets = []
count = 0

                     
                
for arquivo in arquivos[1] :
   pedaco =dd.read_csv(arquivo,sep = "|",encoding="ISO-8859-1",dtype = types2)                
   pedaco = pedaco[col_sel]                                
   colunas = ["CO_CURSO","NO_CURSO"]
   pedaco.columns =colunas
   datasets.append(pedaco)
dataCurso = dd.concat(datasets)


datasets = []
count = 0

                      
                
for arquivo in arquivos[2] :
   pedaco =dd.read_csv(arquivo,sep = "|",encoding="ISO-8859-1")   
   if count <8 :             
    pedaco = pedaco[col_selIES1]
   else :
    pedaco =pedaco[col_selIES2]
   colunas = ['CO_IES', 'NO_IES', 'CO_MUNICIPIO_IES', 'CO_UF_IES',
        'IN_CAPITAL_IES']
   pedaco.columns =colunas
   datasets.append(pedaco)
   count += 1
dataIES = dd.concat(datasets)


print("Iniciando criação de dados")
dataResult =[dataAluno,dataCurso,dataIES]
dataResultName =["Aluno.csv","Curso.csv","IES.csv"]

for i in range(3) :
  print(f'Comecou a {i+1} Conversão !!!!!!' )
  dataResult[i].to_csv(f"./Dados_INEP/{dataResultName[i]}",chunksize=  50000  ,encoding="ISO-8859-1",index=False)
  print(f"FEITO A {i+1} Conversão !!!!!!")


