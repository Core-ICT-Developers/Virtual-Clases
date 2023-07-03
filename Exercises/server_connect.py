import psycopg2
connection = psycopg2.connect(dbname="exercise", user="postgres", password="1234", host="127.0.0.1")

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS exercise;')

cursor.execute('''
  CREATE TABLE exercise (
    id INTEGER PRIMARY KEY,
    fname VARCHAR(200) NULL,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO exercise (id, completed) VALUES (%i, %s);', (1, True))

SQL = 'INSERT INTO exercise (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)


cursor.execute('SELECT * from exercise;')
result = cursor.fetchone()
print('fetchone ' , result)

mymanyrecordsresult = cursor.fatchall()
#complete it to loop all the records
#complete it...

connection.commit()

connection.close()
cursor.close()


