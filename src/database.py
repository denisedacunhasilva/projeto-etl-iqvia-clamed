import psycopg2 as pg

#Conexão com banco de dados Postgres Clamed
def connect_db(dbname, user, password, host, port):
    try:
        return pg.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
    except:
        print("Erro ao conectar ao banco de dados!\n")