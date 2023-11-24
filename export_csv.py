import csv
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

with conn:
    cur = conn.cursor()

    for table_name in tables:
        cur.execute('select * from ' + table_name)
        fieldnames = [x[0] for x in cur.description]
        with open(output_file.format(table_name), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
            for row in cur:
                writer.writerow(row)
