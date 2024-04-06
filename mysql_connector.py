import mysql.connector

def connect_to_database(host, user, password, database_name=None):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )
        print("Connected to MySQL database successfully")
        return connection
    except mysql.connector.Error as err:
        print(f"Failed to connect to MySQL database: {err}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

def create_database(connection, database_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created successfully")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def create_table(connection, table_name, columns):
    try:
        cursor = connection.cursor()

        # Construct the CREATE TABLE query
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for column_name, data_type in columns.items():
            query += f"{column_name} {data_type}, "
        query = query[:-2]  # Remove the last comma and space
        query += ")"

        cursor.execute(query)
        print(f"Table '{table_name}' created successfully")
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")

def insert_data(connection, table_name, data):
    try:
        cursor = connection.cursor()

        # Construct the INSERT INTO query
        query = f"INSERT INTO {table_name} ("
        for column_name, value in data.items():
            query += f"{column_name}, "
        query = query[:-2]  # Remove the last comma and space
        query += ") VALUES ("
        for value in data.values():
            if isinstance(value, str):
                query += f"'{value}', "
            else:
                query += f"{value}, "
        query = query[:-2]  # Remove the last comma and space
        query += ")"

        cursor.execute(query)
        connection.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print("Failed inserting data: {}".format(err))
        connection.rollback()
    

def show_tables(connection):
    try:
        cursor = connection.cursor()

        # Query to fetch table names
        query = "SHOW TABLES"

        # Executing the query
        cursor.execute(query)

        # Fetching all tables
        tables = cursor.fetchall()

        # Printing the table names
        print("Tables in the database:")
        for table in tables:
            print(table[0])

    except mysql.connector.Error as error:
        print("Failed to show tables:", error)


def max_column(connection, table_name, column_name):
    query = f"SELECT MAX({column_name}) FROM {table_name};"
    result = execute_query(connection, query)
    if result:
        print("Maximum:", result[0][0])
    else:
        print("Error: Unable to find maximum.")

def min_column(connection, table_name, column_name):
    query = f"SELECT MIN({column_name}) FROM {table_name};"
    result = execute_query(connection, query)
    if result:
        print("Minimum:", result[0][0])
    else:
        print("Error: Unable to find minimum.")
        
def average_column(connection, table_name, column_name):
    query = f"SELECT AVG({column_name}) FROM {table_name};"
    result = execute_query(connection, query)
    if result:
        print("Average:", result[0][0])
    else:
        print("Error: Unable to compute average.")
        
def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as error:
        print("Failed to execute query:", error)
        return None

        
