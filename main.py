import psycopg2
import matplotlib.pyplot as plt

username = 'Krakovych_Boryslav'
password = '111'
database = 'labs3-6'
host = 'localhost'
port = '5432'

query_1 = '''
create view FemaleLevelId as select level_id, count(distinct(results.student_id)) from student,results
where results.student_id in(select student_id from student where gender='female') group by level_id 
'''

query_2 = '''
create view MaleMathTest as select score, count(student_id) from results
where test_id = '1' and student_id in(select student_id from student where gender='male') group by score
'''

query_3 = '''
create view EthnicityGroups as select ethnicity, count(student_id) from student group by ethnicity order by ethnicity
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)



with conn:
    cur = conn.cursor()
    #стовпчикова діаграма
    cur.execute('DROP VIEW IF EXISTS FemaleLevelId')
    cur.execute(query_1)
    cur.execute('SELECT * FROM FemaleLevelId')
    level_id= []
    count_of_female_students = []


    for row in cur:
        level_id.append(row[0])
        count_of_female_students.append(row[1])

    x_range = range(len(level_id))
 
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, count_of_female_students, label='count')
    bar_ax.bar_label(bar, label_type='center') 
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(level_id)
    bar_ax.set_xlabel('Рівень освіти')
    bar_ax.set_ylabel('Кількість студенток')
    bar_ax.set_title('Кількість студенток, що писали тест на певний рівень освіти')

    #кругова діаграма 
    cur.execute('DROP VIEW IF EXISTS MaleMathTest')
    cur.execute(query_2)
    cur.execute('SELECT * FROM MaleMathTest')
    result = []
    count_of_students = []
    for row in cur:
        result.append(row[0])
        count_of_students.append(row[1])

    pie_ax.pie(count_of_students, labels=result, autopct='%1.1f%%',textprops={'fontsize': 8})
    pie_ax.set_title('Частка кількості студентів-чоловіків, \nщо написали тест з математики \nна певну кількість балів')

    #точковий графік залежності
    cur.execute('DROP VIEW IF EXISTS EthnicityGroups')
    cur.execute(query_3)
    cur.execute('SELECT * FROM EthnicityGroups')
    ethnicity = []
    count_of_students = []
    for row in cur:
        ethnicity.append(row[0])
        count_of_students.append(row[1])


    graph_ax.plot(ethnicity, count_of_students, marker='o')
    graph_ax.set_xlabel('Етнічна група')
    graph_ax.set_ylabel('Кількість студентів та студенток певної етнічної групи')
    graph_ax.set_title('Графік залежності кількості студентів та студенток певної етнічної групи')

    for qnt, price in zip(ethnicity, count_of_students):
        graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')


mng = plt.get_current_fig_manager()
mng.resize(2000, 800)

plt.show()
