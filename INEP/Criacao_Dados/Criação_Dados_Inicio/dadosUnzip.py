# importando bibliotecas


from constantes import diretorio,zip_files,criandoenderecos,criandodiretorio,criandoarquivo
import warnings
warnings.filterwarnings("ignore")


print("Criando as Pastas")

criandoenderecos(diretorio,zip_files) # ciranco os endereços de acesso
criandodiretorio(diretorio) #criando os diretorios
print("Unpack Data")
for i in (range(len(diretorio))) :
  criandoarquivo(diretorio[i],zip_files[i]) #unpack dos arquivos zip
