import pandas as pd
import numpy as np
import re
import unicodedata
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))

def normalizar_coluna(col: str) -> str:
    """
    Normaliza nomes de colunas:
    - remove acentos
    - converte para lowercase
    - substitui caracteres especiais por _
    """
    col = col.strip().lower()
    col = unicodedata.normalize('NFKD', col).encode('ascii', 'ignore').decode('utf-8')
    col = re.sub(r'[^a-z0-9_]+', '_', col)
    return col


def limpar_filial_brick_data_xlsx(df_filial_brick_clean: pd.DataFrame) -> pd.DataFrame:
    # Normalizar nomes das colunas (corrige 'cód._filial' → 'cod_filial')
    df_filial_brick_clean.columns = [normalizar_coluna(col) for col in df_filial_brick_clean.columns]

    # Remover duplicatas
    df_filial_brick_clean = df_filial_brick_clean.drop_duplicates()

    # Tratar valores nulos essenciais (agora as colunas EXISTEM)
    df_filial_brick_clean = df_filial_brick_clean.dropna(subset=['brick', 'cod_filial'])

    # Separar coluna brick em cod_brick e nome_brick
    # Exemplo: "1234 - FLORIANÓPOLIS CENTRO"
    split_brick = (
        df_filial_brick_clean['brick']
        .astype(str)
        .str.split(' - ', n=1, expand=True)
    )

    df_filial_brick_clean['cod_brick'] = split_brick[0]
    df_filial_brick_clean['nome_brick'] = split_brick[1].fillna('NAO_INFORMADO')

    # Garantir tipos corretos
    df_filial_brick_clean['cod_filial'] = df_filial_brick_clean['cod_filial'].astype(int)
    df_filial_brick_clean['cod_brick'] = df_filial_brick_clean['cod_brick'].astype(str)
    df_filial_brick_clean['nome_brick'] = df_filial_brick_clean['nome_brick'].astype(str)

    # Remover coluna original brick (não normalizada)
    df_filial_brick_clean = df_filial_brick_clean.drop(columns=['brick'])

    return df_filial_brick_clean