import pandas as pd
import numpy as np
import os
import sys
from src.database import connect_db

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))

def extrair_filial_brick_data_xlsx(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, dtype = {
        'brick': str,
        'cod_filial': int
    })

    return df