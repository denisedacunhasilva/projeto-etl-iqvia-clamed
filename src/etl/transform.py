import pandas as pd
import numpy as np
import re
import unicodedata


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


def limpar_filial_brick_data_xlsx(df: pd.DataFrame) -> pd.DataFrame:
    # Normalizar nomes das colunas (corrige 'cód._filial' → 'cod_filial')
    df.columns = [normalizar_coluna(col) for col in df.columns]

    # Remover duplicatas
    df = df.drop_duplicates()

    # Tratar valores nulos essenciais (agora as colunas EXISTEM)
    df = df.dropna(subset=['brick', 'cod_filial'])

    # Separar coluna brick em cod_brick e nome_brick
    # Exemplo: "1234 - FLORIANÓPOLIS CENTRO"
    split_brick = (
        df['brick']
        .astype(str)
        .str.split(' - ', n=1, expand=True)
    )

    df['cod_brick'] = split_brick[0]
    df['nome_brick'] = split_brick[1].fillna('NAO_INFORMADO')

    # Garantir tipos corretos
    df['cod_filial'] = df['cod_filial'].astype(int)
    df['cod_brick'] = df['cod_brick'].astype(str)
    df['nome_brick'] = df['nome_brick'].astype(str)

    # Remover coluna original brick (não normalizada)
    df = df.drop(columns=['brick'])

    return df
