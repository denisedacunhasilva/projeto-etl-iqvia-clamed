import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))

from src.database import cadastrar_aluno 

import pandas as pd

def carregar_alunos_db(df: pd.DataFrame):

    for _, row in df.iterrows():
        cadastrar_aluno(row['nome'], row['email'], row['senha'], row['telefone'])


"""
load.py
Responsável por carregar os dados no PostgreSQL.


import psycopg2
from psycopg2.extras import execute_batch


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="clamed",
        user="postgres",
        password="postgres",
        port=5432
    )


def load_dim_filial_brick(df):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO dim_filial_brick (codigo_filial, brick, uf)
        VALUES (%s, %s, %s)
    """

    data = df[["codigo_filial", "brick", "uf"]].values.tolist()
    execute_batch(cur, query, data)

    conn.commit()
    cur.close()
    conn.close()


def load_fact_vendas_iqvia(df):
    conn = get_connection()
    cur = conn.cursor()

    query = """
   """     INSERT INTO fact_vendas_iqvia (
            ean,
            brick,
            vol_concorrente_indep,
            vol_concorrente_rede,
            vol_clamed_pp,
            vol_total_mercado,
            participacao_clamed
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
"""
    #data = df[
        [
            "ean",
            "brick",
            "vol_concorrente_indep",
            "vol_concorrente_rede",
            "vol_clamed_pp",
            "vol_total_mercado",
            "participacao_clamed",
        ]
    ].values.tolist()

    execute_batch(cur, query, data)

    conn.commit()
    cur.close()
    conn.close()
"""