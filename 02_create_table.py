#based on notes at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
import pandas as pd
import sqlite3 as db
import functions
connection = db.connect('my_db')
#create a dataframe with some data
df = pd.DataFrame.from_dict({'name' : ['Sam', 'Ravi', 'Martha'],
                             'email': ['ss@mail.com', 'hr34@mail.us', 'p3w@gbv.com'],
                             'role': ['user', 'user', 'admin']})
try:
    connection.execute("""CREATE TABLE if not exists users 
                       (name text primary key, email text, role text,
                       primary key name
                       """)
    for i in range(0,3):
        insert_command = """
                        INSERT INTO users
                        (name, email, role)
                        values(:name, :email, :role)
                        """
        connection.execute(insert_command, {'name':df['name'][i], 
                                            'email':df['email'][i],
                                            'role':df['role'][i]})

    df.to_sql(name='users', if_exists ='replace', index=False, con=connection)
    #connection.execute("ALTER TABLE users ADD PRIMARY KEY ('name');")
except Exception:
    print('error')
    connection.rollback()
else:
    connection.commit()
    print('created table')
    df2=pd.read_sql('Select * from users', connection)
    functions.print_it('new data', df2)


