import psycopg2

# Setting up connection
conn = psycopg2.connect(
    database="assessment", user='postgres', password='episalt', host='localhost', port='5432'
)

# Setting auto commit false
conn.autocommit = True

# Create cursor
cursor = conn.cursor()

cursor.execute('''INSERT INTO flights(flight_number, departure_time, arrival_time, departure_airport, destination_airport) 
   VALUES ('DY543', 1130, 2230, 'HYU', 'STA')''')
cursor.execute('''INSERT INTO flights(flight_number, departure_time, arrival_time, departure_airport, destination_airport) 
   VALUES ('DY793', 1330, 2130, 'BRO', 'LXA')''')
cursor.execute('''INSERT INTO flights(flight_number, departure_time, arrival_time, departure_airport, destination_airport) 
   VALUES ('DY183', 0930, 1430, 'SEZ', 'ZES')''')

# Run inserts
conn.commit()

# Verify Completion of Executes
print("Bro, your flight updates have been added.")

# Close the connection
conn.close()
