import pandas as pd

def extrair_filial_brick_data_xlsx(path: str) -> pd.DataFrame:
    return pd.read_excel(path)

def extrair_vendas_iqvia_xlsx(path: str) -> pd.DataFrame:
    return pd.read_excel(path)