
import pandas as pd
import sqlite3

square = lambda n: n*n

# con with las conexiones se cierran automaticamente

with sqlite3.connect(r'C:\Users\flore\Sqlite\northwind.db') as conn:
    conn.create_function("square",1,square)     # creamos la funcion en sqlite 
    cursor = conn.cursor()                      # creamos el cursor que es el ejecutable de las consultas
    cursor.execute(''' SELECT *,square(price) FROM Products WHERE Price > 0''')   # query en sqlite3
    results = cursor.fetchall()                 # como python trae los datos en una forma de lista de tuplas lo convertimos a un DF
    results_df = pd.DataFrame(results)          # convertimos la lista de tuplas en un DF
                                                # con with no es necesario cerrar el cursor ni la conexion, es automatico
print(results_df)