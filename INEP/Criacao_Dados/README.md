Para que o script execute precisa-se seguir os seguintes passos :


1 - Executar pip3 install -r requirements.txt

2 = Executrar pip3 install dask

3 - Executar python3 dadosTeste.py

O codigo então se encarregara de baixar os dados, descompactar os arquivos, unir os dados e limpar os dados sobresalentes. Ao final dessas etapas o codigo mostrára o tempo demorado para executar tais tarefas, que pode demorar devido a utilização de wget em links https.
O script criará 3 pastas dentro da pasta Dados_INEP, um referente a Alunos, outro referente a Cursos e um último referente a IES, todos em formato .csv para que possa facilmente ser utilizado em biliotecas de análise de dados como o Pandas.


