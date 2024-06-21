import mysql.connector
import random
import string

mysql_user = "root"
mysql_password = "12gstarz**"
mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_database = "test_db"

# Connect to MySQL
conn = mysql.connector.connect(
    host=mysql_host,
    port=mysql_port,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)
cursor = conn.cursor()

# Function to generate random string
def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Generate and insert 1 million records in batches
records = []
for i in range(1000000):
    name = random_string()
    value = random.randint(1, 100)
    records.append((name, value))
    if len(records) == 10000:
        cursor.executemany("INSERT INTO test_table (name, value) VALUES (%s, %s)", records)
        conn.commit()
        records = []

# Insert remaining records
if records:
    cursor.executemany("INSERT INTO test_table (name, value) VALUES (%s, %s)", records)
    conn.commit()

cursor.close()
conn.close()

print("1 million records inserted.")
