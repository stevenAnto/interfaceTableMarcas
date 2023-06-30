import mysql.connector
from typing import List
from typing import Tuple

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                    )
            print("Connected to the database")
            return "Connected to the database"
        except mysql.connector.Error as error:
            print("Failed to connect to the database:", error)

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")
            return "connection closed"

    def insert_record(self, table:str,columns:Tuple, data:Tuple):
        try:
            cursor = self.connection.cursor()
            query = f"INSERT INTO {table} ({columns}) VALUES (%s, %s, %s)"
            cursor.execute(query,data)
            self.connection.commit()
            print("Record inserted successfully")
            return "Record inserted successfully"
        except mysql.connector.Error as error:
            print("Failed to insert record:", error)
            return error

    #la List columns tiene 3 elementos que son loos nombres de los campos
    #La tupla solo tiene 2 elementos que son los que se van actualizar
    def update_record(self, table:str,id,columns:List, data:Tuple):
        try:
            cursor = self.connection.cursor()
            query = f"UPDATE {table} SET {columns[1]}=%s, {columns[2]}=%s  WHERE  {columns[0]}= {id}"
            cursor.execute(query, data )
            self.connection.commit()
            print("Record updated successfully")
            return "Record update successfully"
        except mysql.connector.Error as error:
            print("Failed to update record:", error)
            return error

    def recuperarDatosTabla(self, table):
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except mysql.connector.Error as error:
            print("Failed to retrieve records:", error)
            return error
