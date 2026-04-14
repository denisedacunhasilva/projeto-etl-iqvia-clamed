import pandas as pd
import re
import unicodedata


# =================================================
# Função utilitária
# =================================================

def normalizar_coluna(col: str) -> str:
    col = col.strip().lower()
    col = unicodedata.normalize('NFKD', col).encode('ascii', 'ignore').decode('utf-8')
    col = re.sub(r'[^a-z0-9_]+', '_', col)
    return col


# =================================================
# TRANSFORMAÇÃO: FILIAL x BRICK (DIMENSÕES)
# =================================================

def transformar_filial_brick(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Normalizar colunas
    df.columns = [normalizar_coluna(c) for c in df.columns]

    # -----------------------------------------
    # Separar cod_brick e nome_brick
    # Ex: "1147 - CAMPO GRANDE - CENTRO"
    # -----------------------------------------
    split_brick = (
        df['brick']
        .astype(str)
        .str.split(' - ', n=1, expand=True)
    )

    df['cod_brick'] = split_brick[0].str.strip().astype(int)
    df['nome_brick'] = split_brick[1].fillna('NAO INFORMADO').str.strip()

    # -----------------------------------------
    # Nome da filial NÃO existe no arquivo
    # -----------------------------------------
    df['nome_filial'] = 'DADO NAO INFORMADO'

    # Tipos
    df['cod_filial'] = df['cod_filial'].astype(int)
    df['nome_brick'] = df['nome_brick'].astype(str)

    # Remover registros inválidos
    df = df.dropna(subset=['cod_filial', 'cod_brick'])

    return df.reset_index(drop=True)


# =================================================
# ALIAS (compatibilidade com pipeline antigo)
# =================================================

def limpar_filial_brick_data_xlsx(df: pd.DataFrame) -> pd.DataFrame:
    return transformar_filial_brick(df)


# =================================================
# TRANSFORMAÇÃO: FACT_VENDAS_IQVIA
# =================================================

def transformar_vendas_iqvia(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Normalizar colunas
    df.columns = [normalizar_coluna(c) for c in df.columns]

    # -----------------------------------------
    # Identificar coluna de BRICK no IQVIA
    # -----------------------------------------
    if 'cod_brick' not in df.columns:
        if 'brick' in df.columns:
            df['cod_brick'] = df['brick']
        else:
            raise KeyError(
                f'Coluna de brick não encontrada no arquivo IQVIA. '
                f'Colunas disponíveis: {list(df.columns)}'
            )

    # -----------------------------------------
    # Tratar cod_brick
    # Ex: "1147 - CAMPO GRANDE - CENTRO"
    # -----------------------------------------
    df['cod_brick'] = (
        df['cod_brick']
        .astype(str)
        .str.extract(r'(\d+)')[0]
        .astype(int)
    )

    # -----------------------------------------
    # Tratar cod_filial
    # -----------------------------------------
    if 'cod_filial' not in df.columns:
        raise KeyError('Coluna cod_filial não encontrada no arquivo IQVIA')

    df['cod_filial'] = df['cod_filial'].astype(int)

    # -----------------------------------------
    # Colunas numéricas (se existirem)
    # -----------------------------------------
    colunas_numericas = [
        'vol_clamed',
        'vol_concorrente',
        'vol_total',
        'valor_clamed',
        'valor_concorrente',
        'valor_total'
    ]

    for col in colunas_numericas:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    # -----------------------------------------
    # Validações finais
    # -----------------------------------------
    if df['cod_brick'].isna().any():
        raise ValueError('Existem registros de vendas sem cod_brick válido')

    if df['cod_filial'].isna().any():
        raise ValueError('Existem registros de vendas sem cod_filial válido')

    return df.reset_index(drop=True)
