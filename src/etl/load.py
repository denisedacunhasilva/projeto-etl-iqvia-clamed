import os
import sys
import pandas as pd

# garante acesso ao database.py
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from database import (
    cadastrar_dim_brick,
    cadastrar_dim_filial,
    cadastrar_dim_filial_brick,
    buscar_empresa_id_por_codigo,
    buscar_endereco_nao_informado,
    buscar_filial_id_por_codigo,
    buscar_brick_id_por_codigo
)

# =========================================================
# LOAD DIM_BRICK
# =========================================================

def carregar_bricks(df: pd.DataFrame):
    df_bricks = (
        df[['cod_brick', 'nome_brick']]
        .drop_duplicates(subset=['cod_brick'])
    )

    for _, row in df_bricks.iterrows():
        cadastrar_dim_brick(
            row['cod_brick'],
            row['nome_brick']
        )

# =========================================================
# LOAD DIM_FILIAL
# =========================================================

def carregar_filiais(df: pd.DataFrame):
    empresa_id = buscar_empresa_id_por_codigo(1)   # CLAMED
    endereco_id = buscar_endereco_nao_informado()

    df_filiais = (
        df[['cod_filial', 'nome_filial']]
        .drop_duplicates(subset=['cod_filial'])
    )

    for _, row in df_filiais.iterrows():
        cadastrar_dim_filial(
            cod_filial=int(row['cod_filial']),
            nome_filial=row['nome_filial'],
            empresa_id=empresa_id,
            endereco_id=endereco_id,
            tipo_filial='FILIAL',
            status_operacao='ATIVA'
        )

# =========================================================
# LOAD DIM_FILIAL_BRICK (BRIDGE)
# =========================================================

def carregar_filial_brick(df: pd.DataFrame):
    df_rel = (
        df[['cod_filial', 'cod_brick']]
        .drop_duplicates()
    )

    for _, row in df_rel.iterrows():
        filial_id = buscar_filial_id_por_codigo(int(row['cod_filial']))
        brick_id = buscar_brick_id_por_codigo(row['cod_brick'])

        cadastrar_dim_filial_brick(
            filial_id=filial_id,
            brick_id=brick_id
        )