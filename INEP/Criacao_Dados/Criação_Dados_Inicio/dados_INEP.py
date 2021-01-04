import os
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
startTime = datetime.now()
def DownloadData(url) :
   import os 
   os.system(f'wget {url}')



urls  = ["http://download.inep.gov.br/microdados/microdados_censo_superior_2009.zip",
         "http://download.inep.gov.br/microdados/microdados_censo_superior_2010.zip",
         "http://download.inep.gov.br/microdados/microdados_censo_superior_2011.zip",
         "http://download.inep.gov.br/microdados/microdados_censo_superior_2012.zip",
         "http://download.inep.gov.br/microdados/microdados_censo_superior_2013.zip",
         "http://download.inep.gov.br/microdados/microdados_censo_superior_2014.zip",
         "http://download.inep.gov.br/microdados/microdados_censo_superior_2015.zip",
         "http://download.inep.gov.br/microdados/microdados_censo_superior_2016.zip",
         "http://download.inep.gov.br/microdados/microdados_educacao_superior_2017.zip",
         "http://download.inep.gov.br/microdados/microdados_educacao_superior_2018.zip",
         "http://download.inep.gov.br/microdados/microdados_educacao_superior_2019.zip"]


for i in (range(len(urls))):
  DownloadData(urls[i])


tempoDownload = (datetime.now() - startTime)




