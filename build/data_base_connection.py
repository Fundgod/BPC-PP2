import sqlite3
import sys


class DBSample():
    def start(self):
        # Connect to SQLite database (or create a new one if it doesn't exist)
        connection = sqlite3.connect("bd.db")
        # Create a cursor object to interact with the database
        cursor = self.connection.cursor()

        # Execute a SELECT statement to retrieve all rows from the "films" table
        cursor.execute('SELECT * FROM films')

        # Fetch all the rows
        rows = cursor.fetchall()

        # Commit the changes and close the connection
        connection.close()
        return rows

    
    # Ивент для отключения от БД
    def closeEvent(self, event):
        self.connection.close()