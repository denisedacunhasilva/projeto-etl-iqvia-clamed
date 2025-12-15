import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))

from extract import *
from transform import *
from load import *

def pipeline_bricks_e_filiais():
    #1. Extract
    df_filial_brick = extrair_filial_brick_data_xlsx('../../data/raw/filial-brick_sample.xlsx')
    print('Coleta de filiais por brick efetuada com sucesso!')

    #2. Transform
    df_filial_brick_clean = limpar_filial_brick_data_xlsx(df_filial_brick)
    print('Transformação concluída com sucesso!')
    print(df_filial_brick_clean.head())
    #3. Load
    #carregar_bricks_e_filiais(df_filial_brick_clean)
    #print('Carga concluída com sucesso!')

if __name__ == "__main__":
    pipeline_bricks_e_filiais()