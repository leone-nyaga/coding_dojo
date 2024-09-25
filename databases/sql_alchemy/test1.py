from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import pymysql


# Replace 'leone' with your MySQL username, 'little rascal' with your password,
# 'localhost' with your hostname, and '3306' with your port number.
# Replace 'mydatabase' with the name of the database you want to connect to (if it already exists).
# If you don't specify a database name, it will connect to the default database.
username = 'leone'
password = 'little rascal'
hostname = 'localhost'
port = '3306'
database_name = 'testdb'

# Construct the MySQL connection string
connection_string = f'mysql://{username}:{password}@{hostname}:{port}/{database_name}'

# Create an Engine object to connect to the MySQL database
engine = create_engine(connection_string)

# Try to connect to the database
try:
    connection = engine.connect()
    print("Connection to the database successful!")
    connection.close()
except Exception as e:
    print("Error connecting to the database:", e)
