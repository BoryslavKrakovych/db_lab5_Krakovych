import json
import psycopg2

username = 'Krakovych_Boryslav'
password = '111'
database = 'labs3-6'
host = 'localhost'
port = '5432'

output_file = 'Krakovych_DB_{}.csv'

tables = [
    'Results',
    'Student',
    'TestID_TestName',
    'LevelID_LevelName',
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


data = {}
with conn:

    cur = conn.cursor()
    
    for table in tables:
        cur.execute('select * from ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('lab5.json', 'w') as outf:
    json.dump(data, outf, default = str)