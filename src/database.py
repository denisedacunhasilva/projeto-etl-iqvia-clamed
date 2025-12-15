import psycopg2 as pg

#Conexão com banco de dados
def connect_db(dbname, user, password, port, host):
    try:
        return pg.connect(
            dbname=dbname,
            user=user,
            password=password,
            port=port,
            host=host
        )
    except:
        print("Erro: Falha ao conectar com o banco de dados!\n")

def cadastrar_dim_brick(cod_brick: str, nome_brick: str):
    '''
        Cadastra um novo brick no banco de dados.

        Parâmetros:
            - cod_brick: str
            - nome_brick: str
    '''
    with connect_db('clamed', 'postgres', '@m@R3linh0', 5432, 'localhost') as conn:
        with conn.cursor() as cur:
            try:
                cur.execute('INSERT INTO dim_brick(cod_brick, nome_brick) VALUES (%s, %s)',
                            (cod_brick, nome_brick))
            except Exception as e:
                print('Error: Falha ao cadastrar dim_brick! ', e)

    