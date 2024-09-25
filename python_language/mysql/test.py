#!/usr/bin/python3

import mysql.connector

connection = mysql.connector.connect(
        host ="localhost",
        user ="user",
        passwd ="little rascal",
        database ="test connection"
)

if connection.is_connected():
    print(connection)

connection.close()

