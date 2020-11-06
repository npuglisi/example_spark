### Nathália Regina Puglisi de Souza

## Instruções
Para a execução deste teste, existem alguns itens que precisam ser executados inicialmente, sendo:
- Instalação do Java Oracle
- Instalação do Python
- Instalação do Spark

## Instalações
###  Instalação do Java Oracle
A instalação do Java Oracle é necessária para a execução dos comandos pyspark, visto que o Spark foi desenvolvido em Scala mas é executado em um ambiente virtual Java.
Para o download https://java.com/en/download/
Após a instalação, é preciso incluir uma linha nova nas variaveis de ambiente do Windows, sendo o nome da variável JAVA_HOME e o caminho é onde o Java está instalado

###  Instalação do Python
A instalação do Python é necessária para a utilização da linguagem e desenvolvimento do teste.
Para o download https://www.python.org/downloads/
Após a instalação, é preciso incluir uma linha nova em Path nas variaveis de ambiente do Windows, sendo o caminho é onde o Python está instalado

### Instalação do Spark/Hadoop
A instalação do Spark é necessária para a utilização do framework, neste passo o download é feito do Spark e Hadoop juntos.
Para o download do Spark http://spark.apache.org/downloads.html
Para o download do winutils.exe (este arquivo deve ser baixado pois o Spark precisa dele para a instalação do Hadoop, ele pode ser incluido em C:/Hadoop/bin/)
https://github.com/steveloughran/winutils/blob/master/hadoop-2.7.1/bin/winutils.exe
Após a instalação, é preciso incluir duas linhas novas nas variaveis de ambiente do Windows, sendo uma com nome da variável HADOOP_HOME e o caminho é onde o winutils.exe está, e a outra é SPARK_HOME com o caminho de onde o Spark está instalado

## Arquivos datasets
### Por uma limitação do github, nao foi possível subir os arquivos json pois ultrapassam 25MB, portanto é necessário pegar os arquivos por fora e incluir na basta "dataset" que esta dentro do projeto

## Desenvolvimento

### Foi utilizado as ferramentas Spark e Python, ou seja, pyspark, como pede o enunciado.
Para organização do código, foi utilizado a idéia de design pattern Clean, pois ele utiliza SOLID e traz a clareza das responsabilidades de cada item, deixando o código limpo e organizado.
Para o desenvolvimento da aplicação, foi utilizado como IDE o VS Code.

### Para os testes, era possível criar classes de testes unitários, a idéia é muito conhecida por mim e eu saberia implementar, mas infelizmente não consegui fazer a tempo. Portanto, para a validação das informações, utilizei do Terminal do VS Code, executando comandos como "print()" e "show()" com dados limitados a 100, e após validado, a limitação e os "debuggers" foram retirados.

### Os arquivos e pastas foram organizados baseado na responsabilidade de cada operação, sendo
- reading = responsavel pela leitura dos dados
- pre processing = responsavel pela limpeza dos dados
- transformation = responsavel pela transformação do dado, como convertendo tabelas, ajustando valores ou criando colunas
- metrics = responsavel pela função analitica dos dados, ou seja, qual o resultado expor
- writing = responsavel pela escrita dos dados, neste caso, em arquivo
- objects = responsavel pelos objetos utilizados no desenvolvimento


## Utilização da Aplicação
### Ao iniciar a aplicação executando o comando "python3 app.py" pelo terminal, terá uma tela no console com as opções de agrupamento, ao selecionar uma delas, a aplicação irá criar um arquivo json com as informações agrupadas como solicitado

