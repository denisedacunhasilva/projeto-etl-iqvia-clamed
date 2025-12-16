import psycopg2 as pg

# =========================================================
# Conexão
# =========================================================

def connect_db(dbname, user, password, port, host):
    return pg.connect(
        dbname=dbname,
        user=user,
        password=password,
        port=port,
        host=host
    )

# =========================================================
# LOOKUPS (resolução de SK)
# =========================================================

def buscar_empresa_id_por_codigo(cod_empresa: int) -> int:
    with connect_db('clamed', 'postgres', '@m@R3linh0', 5432, 'localhost') as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT empresa_id
                FROM dim_empresa
                WHERE cod_empresa = %s
                """,
                (cod_empresa,)
            )
            result = cur.fetchone()
            if not result:
                raise ValueError(f'Empresa {cod_empresa} não encontrada')
            return result[0]


def buscar_endereco_nao_informado() -> int:
    with connect_db('clamed', 'postgres', '@m@R3linh0', 5432, 'localhost') as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT endereco_id
                FROM dim_endereco
                WHERE rua = 'Rua Dona Francisca'
                """
            )
            result = cur.fetchone()
            if not result:
                raise ValueError('Endereço NAO INFORMADO não encontrado')
            return result[0]


def buscar_filial_id_por_codigo(cod_filial: int) -> int:
    with connect_db('clamed', 'postgres', '@m@R3linh0', 5432, 'localhost') as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT filial_id
                FROM dim_filial
                WHERE cod_filial = %s
                """,
                (cod_filial,)
            )
            result = cur.fetchone()
            if not result:
                raise ValueError(f'Filial {cod_filial} não encontrada')
            return result[0]


def buscar_brick_id_por_codigo(cod_brick: str) -> int:
    with connect_db('clamed', 'postgres', '@m@R3linh0', 5432, 'localhost') as conn:
        with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT brick_id
                    FROM dim_brick
                    WHERE cod_brick = %s
                    """,
                    (cod_brick,)
                    )
                result = cur.fetchone()
                if not result:
                    raise ValueError(f'Brick {cod_brick} não encontrado')
                return result[0]

# =========================================================
# INSERTS
# =========================================================

def cadastrar_dim_brick(cod_brick: str, nome_brick: str):
    with connect_db('clamed', 'postgres', '@m@R3linh0', 5432, 'localhost') as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO dim_brick (cod_brick, nome_brick)
                VALUES (%s, %s)
                ON CONFLICT (cod_brick) DO NOTHING
                """,
                (cod_brick, nome_brick)
            )
            conn.commit()


def cadastrar_dim_filial(
    cod_filial: int,
    nome_filial: str,
    empresa_id: int,
    endereco_id: int,
    tipo_filial: str,
    status_operacao: str
):
    with connect_db('clamed', 'postgres', '@m@R3linh0', 5432, 'localhost') as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO dim_filial (
                    cod_filial,
                    nome_filial,
                    empresa_id,
                    endereco_id,
                    tipo_filial,
                    status_operacao
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (cod_filial) DO NOTHING
                """,
                (
                    cod_filial,
                    nome_filial,
                    empresa_id,
                    endereco_id,
                    tipo_filial,
                    status_operacao
                )
            )
            conn.commit()


def cadastrar_dim_filial_brick(filial_id: int, brick_id: int):
    with connect_db('clamed', 'postgres', '@m@R3linh0', 5432, 'localhost') as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO dim_filial_brick (filial_id, brick_id)
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING
                """,
                (filial_id, brick_id)
            )
            conn.commit()

def cadastrar_fact_vendas_iqvia(row: dict):
    with connect_db('clamed', 'postgres', '@m@R3linh0', 5432, 'localhost') as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO fact_vendas_iqvia (
                    vol_concorrente_indep,
                    vol_concorrente_rede,
                    vol_marca_pp,
                    vol_total_mercado,
                    participacao_clamed,
                    cod_brick,
                    ean
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    row['vol_concorrente_indep'],
                    row['vol_concorrente_rede'],
                    row['vol_marca_pp'],
                    row['vol_total_mercado'],
                    row['participacao_clamed'],
                    int(row['cod_brick']),
                    row['ean']
                )
            )
            conn.commit()