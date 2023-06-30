import mysql.connector

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

    def insert_record(self, table, data):
        try:
            cursor = self.connection.cursor()
            columns = ', '.join(data.keys())
            values = ', '.join(["%s"] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            cursor.execute(query, tuple(data.values()))
            self.connection.commit()
            print("Record inserted successfully")
        except mysql.connector.Error as error:
            print("Failed to insert record:", error)

    def update_record(self, table, record_id, data):
        try:
            cursor = self.connection.cursor()
            set_values = ', '.join([f"{column} = %s" for column in data.keys()])
            query = f"UPDATE {table} SET {set_values} WHERE id = %s"
            cursor.execute(query, tuple(data.values()) + (record_id,))
            self.connection.commit()
            print("Record updated successfully")
        except mysql.connector.Error as error:
            print("Failed to update record:", error)

    def recuperarDatosTabla(self, table):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            records = cursor.fetchall()
            for record in records:
                print(record)
        except mysql.connector.Error as error:
            print("Failed to retrieve records:", error)
