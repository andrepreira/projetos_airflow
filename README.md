cria e ativa ambiente virtual

- mkdir datapipeline
- cd datapipeline
- python3 -m venv .datapipeline
- source .datapipeline/bin/activate

exporta variavel de ambiente airflow

 - export AIRFLOW_HOME=$(pwd)/airflow

instalação do airflow versão 1.10.14

- pip install apache-airflow==1.10.14 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-1.10.14/constraints-3.7.txt"


inicialização das migrations do airflow

- airflow initdb

inicialização do webserver

- airflow webserver

acesse o webserver em http://localhost:8080


inicialização serviço Scheduler

- airflow scheduler
