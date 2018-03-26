import sqlite3
import csv
# import pandas as pd

# db = sqlite3.connect('Cookies')
# table_name = 'cookies'
# table = pd.read_sql_query("SELECT * from " + table_name, db)
# table.to_csv(table_name + '.csv', index_label='index')


# with DbManager(#MY DATA BASE INFO) as db:
#     SQLview = 'SELECT * FROM mytable;'
#     cursor = db.cursor()
#     cursor.execute(SQLview)
#     with open('output.csv', 'w') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([ i[0] for i in cursor.description ]) 
#         writer.writerows(cursor.fetchall())

db = sqlite3.connect('Cookies')
cursor = db.cursor()
cursor.execute('SELECT * FROM cookies')
with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    print [i[0] for i in cursor.description]
    # writer.writerow([ i[0] for i in cursor.description ]) 
    # print cursor.fetchall()
