import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))

from extract import (
    extrair_filial_brick_data_xlsx,
    extrair_vendas_iqvia_xlsx
)

from transform import (
    limpar_filial_brick_data_xlsx,
    transformar_vendas_iqvia
)

from load import (
    carregar_bricks,
    carregar_filiais,
    carregar_filial_brick,
    carregar_fact_vendas_iqvia
)

def pipeline_completo():
    # ==============================
    # DIMENSÕES
    # ==============================
    df_filial_brick = extrair_filial_brick_data_xlsx(
        '../../data/raw/filial-brick_sample.xlsx'
    )

    df_dim = limpar_filial_brick_data_xlsx(df_filial_brick)

    carregar_bricks(df_dim)
    carregar_filiais(df_dim)
    carregar_filial_brick(df_dim)

    print('✔ Dimensões carregadas')

    # ==============================
    # FACT
    # ==============================
    df_iqvia_raw = extrair_vendas_iqvia_xlsx(
        '../../data/raw/MS_12_2022_sample.xlsx'
    )

    df_fact = transformar_vendas_iqvia(df_iqvia_raw)
    carregar_fact_vendas_iqvia(df_fact)

    print('✔ Fact vendas IQVIA carregada')

if __name__ == "__main__":
    pipeline_completo()