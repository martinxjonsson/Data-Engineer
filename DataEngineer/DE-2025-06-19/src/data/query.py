import psycopg2

# Setting up connection
conn = psycopg2.connect(
    database="assessment", user='postgres', password='episalt', host='localhost', port='5432'
)

# Setting auto commit false
conn.autocommit = True

# Create a cursor
cursor = conn.cursor()

# View Data
cursor.execute('''SELECT * FROM flights ORDER BY departure_time''')

# Fetching all data and display in pretty rows
result = cursor.fetchall()
for row in result:
    print(row)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
