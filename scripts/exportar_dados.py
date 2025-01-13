import pandas as pd
import os
import sys

# Adiciona o diretório 'analise-dados/scripts' ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from scripts.conexao_postgres import conect_postgres
from scripts.consultas import consulta_alunos, consulta_responsavel

def exportar_dados(): 
    conn = conect_postgres()
    if conn is None:
        print("Não foi possível exportar os dados.")
        return
    try:
        alunos_query = consulta_alunos()
        responsavel_query = consulta_responsavel()
        
        alunos_df = pd.read_sql_query(alunos_query, conn)
        responsavel_df = pd.read_sql_query(responsavel_query, conn)
        
        os.makedirs("/home/diogo/Documentos/estacio/analise-de-dados/dados", exist_ok=True)
        alunos_df.to_csv("/home/diogo/Documentos/estacio/analise-de-dados/dados/alunos.csv", index=False, encoding="utf-8")
        responsavel_df.to_csv("/home/diogo/Documentos/estacio/analise-de-dados/dados/responsavel.csv", index=False, encoding="utf-8")
        print("Dados exportados com sucesso!")
    except Exception as e:
        print(e, "Não foi possível exportar os dados.")
    finally:
        conn.close()

if __name__ == "__main__":
    exportar_dados()