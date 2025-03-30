from flask import Flask, request, jsonify, render_template
import sqlite3

tool = Flask(__name__)
DATABASE = "database.db"

def get_db_connection():
    """Creates a database connection and returns the connection object."""
    conn = sqlite3.connect("database.db")
    print('connted to ')
    # To return dictionary-like results
    return conn

def process_data(query):
    """Process the query and retrieve data from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    if 'total' in query and 'sales' in query and 'region' not in query and 'month' not in query:
        cursor.execute("SELECT * FROM sales")
        data = cursor.fetchall()
        print(data)

    elif  'region' in query and 'sales' in query:
        for region in ['north', 'south', 'east', 'west']:
            if region in query:
                cursor.execute("SELECT * FROM sales WHERE region=?", (region,))
                data = cursor.fetchall()
                print("the data",data)
                break
        else:
            data = []

    elif 'total' in query and 'month' in query and '1-1-2025' in query:
        cursor.execute("SELECT * FROM sales WHERE Date=?", ('2025-01-01',))
        data = cursor.fetchall()

    else:
        data = []

    conn.close()
    return data  # Convert results to list of dictionaries

@tool.route('/get_data', methods=['POST'])
def get_data():
    """API endpoint to receive user queries and return processed results."""
    data = request.get_json()
    data = data.get("query", "")
    query= data.split()
    print(query)

    response = process_data(query)
    print(f'the response is {response}')
    return jsonify({"message":f" your {data} is ",'values':response} )  # Convert to JSON before returning

@tool.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify if the server is running."""
    return jsonify({"status": "running"})


#login functionality
@tool.route('/login',methods=['POST'])
def login():
    data = request.get_json()  # Get the JSON request
    user = data.get('username')  # Extract username
    password = data.get('password')  # Extract password


    if user=='admin' and password=='tool@1234':
        return jsonify({'message':"login successful"}),200
    else :
        return jsonify({'message':"invalid credentials"}),401


@tool.route('/admin_page')
def Ai_tool():
    """Render the home page."""
    return render_template('index.html')


@tool.route('/')
def login_page():
    return render_template('login.html')


if __name__ == '__main__':
    tool.run(debug=True)
