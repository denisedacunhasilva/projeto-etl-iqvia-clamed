import pandas as pd #importar a biblioteca pandas que serve para manipulação de dados em dataframes
import numpy as np  #importar a biblioteca numpy que serve para manipulação de arrays e operações numéricas
import re           #importar a biblioteca de expressões regulares

#chatgpt


def limpar_filial_brick_data_xlsx(df: pd.DataFrame) -> pd.DataFrame:
# Padronizar nomes das colunas
    df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
                )


# Remover duplicatas
df = df.drop_duplicates()


# Tratar valores nulos essenciais
df = df.dropna(subset=['cod_filial', 'brick'])


# Separar coluna brick em cod_brick e nome_brick
# Exemplo: "1234 - FLORIANÓPOLIS CENTRO"
df[['cod_brick', 'nome_brick']] = df['brick'].str.split(' - ', n=1, expand=True)


# Garantir tipos corretos
df['cod_filial'] = df['cod_filial'].astype(int)
df['cod_brick'] = df['cod_brick'].astype(str)
df['nome_brick'] = df['nome_brick'].astype(str)


# Remover coluna original brick (não normalizada)
df = df.drop(columns=['brick'])


return df


'''
def limpar_filial_brick_data_xlsx(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w_]", "", regex=True)
    )

    df = df.drop_duplicates()

    return df

    '''

'''
def limpar_filial_brick_data_xlsx(df: pd.DataFrame):
    df = df.copy()

    # --------------------
    # Tratamento nome
    # --------------------
    def limpar_nome(nome):
        if pd.isna(nome) or nome.strip() == "":
            return np.nan
        
        nome = nome.strip()
        nome = re.sub(r'\s+', ' ', nome)
        nome = nome.title()
        return nome

    df_clean['nome'] = df_clean['nome'].apply(limpar_nome)
    df_clean.fillna({'nome': 'Não Informado'}, inplace=True)

'''