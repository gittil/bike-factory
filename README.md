# Repositório do Projeto BikeFactory

## O problema: 

O presente problema se refere aos dados de uma empresa que produz bicicletas.

O objetivo deste desafio é compreender os seus conhecimentos e experiência analisando os seguintes aspectos:

1.	Fazer a modelagem conceitual dos dados;
2.	Criação da infraestrutura necessária;
3.	Criação de todos os artefatos necessários para carregar os arquivos para o banco criado;
4.	Desenvolvimento de SCRIPT para análise de dados;
5.	(opcional) Criar um relatório em qualquer ferramenta de visualização de dados.

Os seguintes arquivos devem ser importados (ETL) para o banco de dados de sua escolha: 

-	Sales.SpecialOfferProduct.csv
-	Production.Product.csv
-	Sales.SalesOrderHeader.csv
-	Sales.Customer.csv
-	Person.Person.csv
-	Sales.SalesOrderDetail.csv

Explicar qual arquitetura foi escolhida e porque?
<br></br>

# Resolução

## Escolha da arquitetura e provedor de serviço de Cloud: 
Para solução do problema proposto foi utilizado a Google Cloud Plataform (GCP), em especial 4 serviços:
- Cloud Storage para criação do DataLake;
- Dataproc para processamento dos dados;
- BigQuery para armazenamento dos dados na camada analítica;
- Data Studio para geração de gráficos.

O DataLake foi dividido em 4 partes:

1. Landing area: Essa é a pasta local onde os arquivos recebidos por email foram salvos e ficaram ali até o final do projeto.

2. Raw Stage: Essa camada do DataLake é a primeira camada na GCP. Ela recebeu todos os arquivos CSV de forma ainda bruta. <br>
Para carregar os arquivos locais na camada RAW, foi utilizado o seguinte scritp: [Load Raw to GCP](https://github.com/gittil/bike-factory/blob/main/ETL/1-raw-load/1-load-raw.ipynb)

3. Refined Stage: A camada REFINED recebeu todos os arquivos tratados que foram carregados a partir da camara RAW. <br>
Foi utilizado a biblioteca Pandas para fazer a manipulação dos dados (limpezas e tranformações, alteração de tipos, etc).<br>
Os notebooks com os tratamentos e todo detalhamento estão disponíveis em: [REFINED](https://github.com/gittil/bike-factory/tree/main/ETL/2-refined-transformation)

4. Curated Stage: Os dados carregados na camada CURATED vieram da camada Refined e receberam algum tipo de processamento mais complexo, como por exemplo JOIN´s e agregações.<br>
Essa será a camada do DataLake que poderá ser disponibilizada para DS's, DA's e BI's trabalharem modelos analíticos, tirar insigths, produzirem Dashboards, etc. <br>
Para processar os dados que foram carregados nessa camada foi utlizado o framework Spark com a interface PySpark e Spark SQL. <br>
O notebook com os códigos pode ser acessado aqui: [CURATED](https://github.com/gittil/bike-factory/blob/main/ETL/3-load-curated/load-curated.ipynb)









<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
Fazer passo a passo:

OK 01 - Criar projeto (print)

OK 02- Criar Cloud Storage com a estrutura de pastas (print)

OK 03 - Carregar arquivos da landing area para bucket/RAW

04 - Ler arquivos do bucket/RAW

05 - Criar cluster DATAPROC (print)

06 - Conectar localmente no DATAPROC

07 - Iniciar o tratamento dos arquivos