import pandas as pd
import numpy as np
from src.database import connect_db


def extract_filial_brick_data_xlsx(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, dtype = {
        'filial_brick_id': int,
        'filial_id': int,
        'brick_id': int,
        #'data_criacao': (datedate_format='%d%m-%Y-'),
        'ativo': bool
    })

    #return df
    print (df)



############################################################

'''

import pandas as pd
from pathlib import Path


def extract_iqvia_data(file_path: Path) -> pd.DataFrame:
    try:
        df = pd.read_excel(file_path)
        print(f"✔ IQVIA carregado | Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
        return df
    except Exception as e:
        raise RuntimeError(f"Erro na extração IQVIA: {e}")


def extract_filial_brick_data(file_path: Path) -> pd.DataFrame:
    try:
        df = pd.read_excel(file_path)
        print(f"✔ Filial-Brick carregado | Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
        return df
    except Exception as e:
        raise RuntimeError(f"Erro na extração Filial-Brick: {e}")
'''