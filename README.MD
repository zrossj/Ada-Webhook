
Como rodar:


1. Instale as dependencias e o PostgreSQL;

-requests
-pandas
-sqlalchemy
-psycopg2

o arquivo requirements.txt possui as versoes utilizadas.

2. Criar as tabelas no banco de dados. Aqui, há duas opções: a) rodar o script 'sql_tables.sql' no CLI do postgres ou; b) rodar o script create_tables.py --> o resultado final será o mesmo. 

3. Execute o arquivo webook_coins.py --> ele precisa continuar ativo para possibilitar GET/POST;

4. O notebook coin_api_calls.ipynb possui exemplos de chamadas comuns ao Webhook --> pode ser executado para teste.


