from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

MYSQL_CONFIG = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'datable',
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

@app.route('/execute_sql', methods=['POST'])
def execute_sql():
    sql_query = request.json.get('query')
    if not sql_query:
        return jsonify({'error': 'No query provided'}), 400

    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({'error': 'Failed to connect to database'}), 500

        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.close()

        return jsonify({'results': results})
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

if __name__ == '__main__':
    app.run(debug=True)