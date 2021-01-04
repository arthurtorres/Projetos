Coleta ,armazenamento e análise de dados da educação superior do Inep de 2009 a 2019.

A Geração dos dados inicias através do site do INEP é feita atraves de script python na pasta Criação_Dados_Inicio e ira armazenar os dados resultados na pasta Dados_INEP, que esta dentro da pasta Criação_Dados_Inicio. Foi feita uma segunda preparação, fazendo a limpeza e melhorando os dados para análise e concatenando as informações relevantes dos datasets. Este codigo foi realizado em um google notebook pois demanda mais RAM que minha maquina local possa suportar e  se encontra em Criação_Dados_Notebook dentro da Pasta Criação_Dados. Os dados resultantes deste notebook serão utilizadas numa análise mais profunda.(Em andamento)

A análise Inicial foi feita tendo como base os dados que irão ser criados na pasta Dados_INEP.Os dados utilizados na análise também estão armazenado neste [google drive](https://drive.google.com/drive/folders/1DrEowqNixud3IlHMO6YTgZqQ2PvgvTpk?usp=sharing). O notebook da análise Inicial. se encontra na pasta analise.


**AVISO :**

O código utilizado baixa os arquivos direto do INEP, utilizando os links por eles fornecidos. Entretanto, devido a grande quantidade de dados utilizada, o código
demora para compilar( cerca de 1h30 em uma máquina local)
