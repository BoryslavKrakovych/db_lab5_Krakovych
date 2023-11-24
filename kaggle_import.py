import csv
import decimal
import psycopg2

username = 'Krakovych_Boryslav'
password = '111'
database = 'labs3-6'
host = 'localhost'
port = '5432'
INPUT_CSV_FILE = 'StudentsPerformance.csv'



query_1 = '''
INSERT INTO Results (Score, Test_ID, Level_ID, Student_ID) VALUES (%s, %s, %s, %s)
'''

query_2 = '''
INSERT INTO Student(Student_ID, Gender, Ethnicity) VALUES (%s, %s, %s)
'''

query_3 = '''
INSERT INTO TestID_TestName(Test_ID, Test_name) VALUES (%s, %s)
'''

query_4 = '''
INSERT INTO LevelID_LevelName(Level_ID, Level_name) VALUES (%s, %s)
'''

query_5 = '''
DELETE FROM Results
'''
query_6 = '''
DELETE FROM Student
'''
query_7 = '''
DELETE FROM TestID_TestName
'''
query_8 = '''
DELETE FROM LevelID_LevelName
'''

def test_definition(strng):
    if strng in row['math score']:
        return 1
    if strng in row['reading score']:
        return 2
    if strng in row['writing score']:
        return 3
    else: return 0

def level_definition(strng):
    if strng == 'master\'s degree':
        return 1
    elif strng == 'bachelor\'s degree':
        return 2
    elif strng == 'associate\'s degree':
        return 3
    elif strng == 'some college':
        return 4
    elif strng == 'high school':
        return 5
    elif strng == 'some high school':
        return 6
    else: return 0

    


conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_5)
    cur.execute(query_6)
    cur.execute(query_7)   
    cur.execute(query_8)   
    values=(1, 'master\'s degree')
    cur.execute(query_4, values)
    values=(2, 'bachelor\'s degree')
    cur.execute(query_4, values)
    values=(3, 'associate\'s degree')
    cur.execute(query_4, values)
    values=(4, 'some college degree')
    cur.execute(query_4, values)
    values=(5, 'high school')
    cur.execute(query_4, values)
    values=(6, 'some high school')
    cur.execute(query_4, values)
    values=(1, 'math score')
    cur.execute(query_3, values)
    values=(2, 'reading score')
    cur.execute(query_3, values) 
    values=(3, 'writing score')
    cur.execute(query_3, values)    

    with open(INPUT_CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)


        for idx, row in enumerate(reader):
            values = (idx + 1, row['gender'], row['race/ethnicity']) 
            cur.execute(query_2, values)

            level= level_definition(row['parental level of education'])



            values = (row['math score'], 1, level, idx + 1) 
            cur.execute(query_1, values)
            values = (row['reading score'], 2, level, idx + 1) 
            cur.execute(query_1, values)
            values = (row['writing score'], 3, level, idx + 1) 
            cur.execute(query_1, values)


    conn.commit()