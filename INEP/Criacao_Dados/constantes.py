import os
import zipfile 
from pyunpack import Archive 
import subprocess
import sys  



diretorio = ["2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
zip_files = ["microdados_censo_superior_2009.zip","microdados_censo_superior_2010.zip",
             "microdados_censo_superior_2011.zip","microdados_censo_superior_2012.zip",
             "microdados_censo_superior_2013.zip","microdados_censo_superior_2014.zip",
             "microdados_censo_superior_2015.zip","microdados_censo_superior_2016.zip",
             "microdados_educacao_superior_2017.zip","microdados_educacao_superior_2018.zip",
             "microdados_educacao_superior_2019.zip"]
    


dadosInteresse = ["DM_ALUNO","DM_CURSO","DM_IES"]



sel09_16= ["CO_IES","CO_ALUNO","CO_CATEGORIA_ADMINISTRATIVA","CO_CURSO",
           "CO_NIVEL_ACADEMICO","CO_COR_RACA_ALUNO",
           "IN_SEXO_ALUNO","IN_RESERVA_ETNICO","IN_APOIO_SOCIAL"]

sel18_19= ["CO_IES","ID_ALUNO","TP_CATEGORIA_ADMINISTRATIVA","CO_CURSO",
           "TP_NIVEL_ACADEMICO","TP_COR_RACA",
           "TP_SEXO","IN_RESERVA_ETNICO","IN_APOIO_SOCIAL"]


sel17= ["CO_IES","CO_ALUNO","TP_CATEGORIA_ADMINISTRATIVA","CO_CURSO",
           "TP_NIVEL_ACADEMICO","TP_COR_RACA",
           "TP_SEXO","IN_RESERVA_ETNICO","IN_APOIO_SOCIAL"]

types1 = {'CO_GRAU_ACADEMICO': 'float64','CO_TURNO_ALUNO': 'float64',
                              'TP_GRAU_ACADEMICO': 'float64','CO_OCDE_AREA_DETALHADA': 'float64',
                               'CO_OCDE_AREA_ESPECIFICA': 'float64','CO_OCDE_AREA_GERAL': 'float64',
                               'TP_TURNO': 'float64','IN_ING_CONVENIO_PECG': 'float64' ,
                              "CO_ALUNO" :"object" , "ID_ALUNO" : "object",'ANO_INGRESSO': 'float64',
                              'CO_ALUNO_SITUACAO': 'float64','CO_COR_RACA_ALUNO': 'float64',
                              'CO_NACIONALIDADE_ALUNO': 'float64','CO_PAIS_ORIGEM_ALUNO': 'float64',
                                    'CO_SEMESTRE_REFERENCIA': 'float64',
                                    'CO_TIPO_ESCOLA_ENS_MEDIO': 'float64',
                                    'IN_ALUNO_DEF_TGD_SUPER': 'float64',
                                    'IN_APOIO_SOCIAL': 'float64',
                                    'IN_ATIVIDADE_EXTRACURRICULAR': 'float64',
                                    'IN_CONCLUINTE': 'float64',
                                    'IN_INGRESSO_TOTAL': 'float64',
                                    'IN_INGRESSO_VAGA_NOVA': 'float64',
                                    'IN_ING_AVALIACAO_SERIADA': 'float64',
                                    'IN_ING_DECISAO_JUDICIAL': 'float64',
                                    'IN_ING_ENEM': 'float64',
                                    'IN_ING_SELECAO_SIMPLIFICADA': 'float64',
                                    'IN_ING_SELECAO_VAGA_PROG_ESPEC': 'float64',
                                    'IN_ING_SELECAO_VAGA_REMANESC': 'float64',
                                    'IN_ING_TRANSF_EXOFFICIO': 'float64',
                                    'IN_ING_VESTIBULAR': 'float64',
                                    'IN_MATRICULA': 'float64',
                                    'IN_RESERVA_VAGAS': 'float64',
                                    'IN_SEXO_ALUNO': 'float64',
                                    'NU_ANO_ALUNO_NASC': 'float64',
                                    'NU_DIA_ALUNO_NASC': 'float64',
                                    'NU_IDADE_ALUNO': 'float64',
                                    'NU_MES_ALUNO_NASC': 'float64',
                                    'QT_CARGA_HORARIA_INTEG': 'float64',
                                    'QT_CARGA_HORARIA_TOTAL': 'float64' }



col_sel = ["CO_CURSO","NO_CURSO"] #criando as variaveis
types2 = {'CO_MUNICIPIO_CURSO': 'float64',
       'CO_UF_CURSO': 'float64',
       'IN_OFERECE_DISC_DISTANCIA': 'float64',
       'QT_INSCRITOS_ANO': 'float64',
       'CO_OCDE_AREA_DETALHADA': 'float64',
       'NO_MUNICIPIO_CURSO': 'object',
       'NO_REGIAO_CURSO': 'object',
       'QT_INSCRITOS_ANO_EAD': 'float64',
       'QT_VAGAS_ANUAL_EAD': 'float64',
       'SGL_UF_CURSO': 'object',
       'CO_OCDE_AREA_ESPECIFICA': 'float64',
       'CO_OCDE_AREA_GERAL': 'float64',
       'IN_GRATUITO': 'float64',
       'CO_GRAU_ACADEMICO': 'float64',
       'IN_INTEGRAL_CURSO': 'float64',
       'IN_MATUTINO_CURSO': 'float64',
       'IN_NOTURNO_CURSO': 'float64',
       'IN_VESPERTINO_CURSO': 'float64',
       'QT_CONCLUINTE_CURSO': 'float64',
       'TP_ATRIBUTO_INGRESSO': 'float64'
}

   
#@Criando as funções
def criandoenderecos(diretorios,arquivos) :
 for number in range(len(diretorios)) :
  diretorio[number] = f"./{diretorio[number]}"
  arquivos[number ] = f"./{zip_files[number]}"

def criandodiretorio(diretorio) :
  for number in range(len(diretorio)) :
    os.mkdir(diretorio[number])

def criandoarquivo(diretorio,arquivo):
 
  with zipfile.ZipFile(arquivo, 'r') as zip_ref:
    zip_ref.extractall(diretorio)


def renomear2019(dado) :
 dado_inicio = f"./2019/Microdados_Educaç╞o_Superior_2019/dados/SUP_{dado[3:]}_2019.CSV"
 dado_final = f"./2019/Microdados_Educaç╞o_Superior_2019/dados/{dado}.CSV"
 os.rename(dado_inicio,dado_final)


def descompactaArquivosRar(arquivosrarcomeco) :

  Archive(arquivosrarcomeco).extractall(arquivosrarcomeco[2:6])


def geraTodosArquivos(dados) :
 
  arc_zip =  subprocess.check_output(f"find . | grep -i {dados}.zip",shell = True).decode(sys.stdout.encoding).split("\n")
  arc_rar = subprocess.check_output(f"find . | grep -i {dados}.rar",shell= True).decode(sys.stdout.encoding).split("\n") 
  arc_zip = sorted(arc_zip)[1:]
  arc_rar = sorted(arc_rar)[1:]

  

  for i in (range(len(arc_zip))) :
    criandoarquivo (arc_zip[i][2:6], arc_zip[i])

  for i in (range(len(arc_rar))) :
    descompactaArquivosRar(arc_rar[i])
 
  arquivos =subprocess.check_output(f"find . | grep -i {dados}.csv",shell = True)
  arquivos = arquivos.decode(sys.stdout.encoding).split("\n")
  arquivos= sorted(arquivos)[1:]
  return arquivos

col_selIES1 = ['CO_IES', 'NO_IES', 'CO_MUNICIPIO_IES', 'CO_UF_IES',
        'IN_CAPITAL_IES']
col_selIES2 =  ['CO_IES', 'NO_IES', 'CO_MUNICIPIO', 'CO_UF',
        'IN_CAPITAL']
