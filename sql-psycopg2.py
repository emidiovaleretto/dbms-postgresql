import psycopg2

conn = psycopg2.connect(database="chinook")
cursor = conn.cursor()

# query
# query = 'SELECT * FROM "Artist" WHERE "Name" = \'Queen\''
query = 'SELECT * FROM "Track" WHERE "Composer" = \'test\''
cursor.execute(query)

results = cursor.fetchall()

# results = cursor.fetchone()

conn.close()

for result in results:
    print(result)
