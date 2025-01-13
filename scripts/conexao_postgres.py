import psycopg2

def conect_postgres():
    try:
        conn = psycopg2.connect(
            dbname="acmk",
            user="acmk",
            password="senha123",
            host="localhost",
            port="5432"
        )
        print ("Conexão com o banco de dados realizada com sucesso!")
        return conn
    except Exception as e:
        print (e, "Não foi possível conectar ao banco de dados.")
        return None