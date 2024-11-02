#based on notes at https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
from sqlalchemy import create_engine
import pandas as pd
import sqlite3 as db
import functions
connection = db.connect('my_db')
#create a dataframe with some data
df = pd.DataFrame.from_dict({'name' : ['Sam', 'Ravi', 'Martha'],
                             'email': ['ss@mail.com', 'hr34@mail.us', 'p3w@gbv.com'],
                             'role': ['user', 'user', 'admin']})
try:
    df.to_sql(name='users', if_exists ='replace', index=False, con=connection)
except Exception:
    print('error')
else:
    print('created table')
    df2=pd.read_sql('Select * from users', connection)
    functions.print_it('new data', df2)


