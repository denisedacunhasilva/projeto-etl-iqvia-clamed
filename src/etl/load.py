import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))

from src.database import cadastrar_dim_brick

import pandas as pd

def carregar_bricks_e_filiais(df_filial_brick_clean: pd.DataFrame):
    
    df_bricks = (
        df_filial_brick_clean[['cod_brick', 'nome_brick']]
        .drop_duplicates()
    )
  

    for _, row in df_bricks.iterrows():
        cadastrar_dim_brick(row['cod_brick'], 
                            row['nome_brick']
                            )