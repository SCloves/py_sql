import MySQLdb
import pandas as pd
from date import *

def main():
    db = MySQLdb.Connection(host='localhost', user='root', passwd='estatistica',db='Sakila_pt')
    query = ("SELECT \
    email, data_criacao, cliente.ultima_atualizacao, valor, descricao\
    FROM \
    cliente \
        INNER JOIN \
    pagamento ON cliente.cliente_id = pagamento.cliente_id \
        INNER JOIN \
    aluguel ON pagamento.aluguel_id = aluguel.aluguel_id \
        INNER JOIN \
    inventario ON aluguel.inventario_id = inventario.inventario_id \
        INNER JOIN \
    filme ON inventario.filme_id = filme.filme_id;")
    cursor = db.cursor()

    cursor.execute(query, args = None)
    rows = cursor.fetchall()
    lrows = []
    for row in rows:
        lrows.append(list(row))

    #colnames = tuple([desc[0] for desc in cursor.description])
    colnames = []
    for desc in cursor.description:
        colnames.append(desc[0])
    tuple(colnames)

    df = pd.DataFrame(lrows, columns = colnames)

    df.to_csv("data_frame", sep='\t', encoding='utf-8')

import time

def main_date():
    today = time.strftime("%Y-%m-%d")

    text_file = open("date.txt", "w")
    text_file.write("\n\n\nFile importado dia : %s\n\n" % today)

    text_file.close()

if __name__ == "__main__":
    main_date()
    main()
