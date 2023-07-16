import mysql.connector
from typing import List
from typing import Tuple
from typing import Dict

class Connection:
    def __init__(self, host:str, user:str, password:str, database:str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self)->str:
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
            return error

    def close(self)->str:
        if self.connection:
            self.connection.close()
            print("Connection closed")
            return "connection closed"

    #insercion por didcionario
    def insert_record(self, table:str, data:Dict)->str:
        try:
            cursor = self.connection.cursor()
            columns = ', '.join(data.keys())
            values = ', '.join(["%s"]*len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            cursor.execute(query, tuple(data.values()))
            self.connection.commit()
            print("Record inserted successfully")
            return "Record inserted successfully"
        except mysql.connector.Error as error:
            print("Failed to insert record:", error)
            return error

    #la List columns tiene 3 elementos que son loos nombres de los campos
    #La tupla solo tiene 2 elementos que son los que se van actualizar
    def update_record(self, table:str,nomCod:str,cod:int,data:Dict)->str:
        try:
            cursor = self.connection.cursor()
            set_values = ', '.join([f"{column} = %s" for column in data.keys()])
            query = f"UPDATE {table} SET {set_values} WHERE {nomCod} = {cod}"
            cursor.execute(query, tuple(data.values()))
            self.connection.commit()
            print("Record updated successfully")
            return "Record update successfully"
        except mysql.connector.Error as error:
            print("Failed to update record:", error)
            return error

    def recuperarDatosTabla(self, table:str)->List:
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except mysql.connector.Error as error:
            print("Failed to retrieve records:", error)
            return error

    def get_zonas_activas(self, query: str) -> List:
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            zonas = cursor.fetchall()
            return zonas
        except mysql.connector.Error as error:
            print("Failed to retrieve active zones:", error)
            return []
