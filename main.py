import psycopg2 as pg
import pandas as pd

#Conexão com banco de dados
def connect_db(dbname, user, password, port, host):
    try:
        return pg.connect(
            dbname=dbname,
            user=user,
            password=password,
            port=port,
            host=host
        )
    except:
        print("Erro: Falha ao conectar com o banco de dados!")
