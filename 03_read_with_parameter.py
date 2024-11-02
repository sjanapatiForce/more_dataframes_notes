import pandas as pd
import sqlite3 as db
import functions
connection = db.connect('my_db')
cursor = connection.cursor()
user_input = input('Enter user name: ')
#results = pd.read_sql(f"select * from users where name = '{user_name}'", connection)
#functions.print_it('with parameter: ', results)

def get_result(connection, user_input: str)-> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT * from users WHERE 
                       name = %(name)s""", {'name':user_input})
    result = cursor.fetchall()
    return result
rows = get_result(connection, user_input)
functions.print_it('Using parameters:', rows)
#df2=pd.read_sql('Select * from users', connection)
#functions.print_it('new data', df2)
