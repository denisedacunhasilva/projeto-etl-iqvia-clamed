import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))

from extract import extrair_filial_brick_data_xlsx
from transform import limpar_filial_brick_data_xlsx
from load import (
    carregar_bricks,
    carregar_filiais,
    carregar_filial_brick
)

def pipeline_bricks_e_filiais():
    df_raw = extrair_filial_brick_data_xlsx(
        '../../data/raw/filial-brick_sample.xlsx'
    )

    df_clean = limpar_filial_brick_data_xlsx(df_raw)

    carregar_bricks(df_clean)
    print('✔ Dimensão BRICK carregada')

    carregar_filiais(df_clean)
    print('✔ Dimensão FILIAL carregada')

    carregar_filial_brick(df_clean)
    print('✔ Dimensão FILIAL_BRICK carregada')

if __name__ == "__main__":
    pipeline_bricks_e_filiais()