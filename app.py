from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': '12gstarz**',
    'host': 'localhost',
    'database': 'test_db'
}

@app.route('/data', methods=['GET'])
def get_data():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    # Assuming you have a table named 'your_table' with data
    cursor.execute('SELECT * FROM test_table LIMIT 100')  # Adjust the query as needed
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(rows)

if __name__ == '__main__':
    app.run(port=5000)
