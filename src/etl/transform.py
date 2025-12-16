import pandas as pd
import re
import unicodedata

# -------------------------------
# Utilitário
# -------------------------------

def normalizar_coluna(col: str) -> str:
    col = col.strip().lower()
    col = unicodedata.normalize('NFKD', col).encode('ascii', 'ignore').decode('utf-8')
    col = re.sub(r'[^a-z0-9_]+', '_', col)
    return col

# -------------------------------
# Transform FILIAL x BRICK
# -------------------------------

def limpar_filial_brick_data_xlsx(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = [normalizar_coluna(col) for col in df.columns]

    split_brick = (
        df['brick']
        .astype(str)
        .str.split(' - ', n=1, expand=True)
    )

    df['cod_brick'] = split_brick[0].str.strip()
    df['nome_brick'] = split_brick[1].fillna('NAO INFORMADO').str.strip()

    df['nome_filial'] = 'DADO NAO INFORMADO'

    df = df.dropna(subset=['cod_filial', 'cod_brick'])

    df['cod_filial'] = df['cod_filial'].astype(int)
    df['cod_brick'] = df['cod_brick'].astype(str)

    df = df.drop(columns=['brick'])

    return df.reset_index(drop=True)