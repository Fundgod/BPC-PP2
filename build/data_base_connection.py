import sqlite3


class DBSample():
    def get_all_lines(self):
        # Connect to SQLite database (or create a new one if it doesn't exist)
        with sqlite3.connect('bd.db') as connection:
            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Execute a SELECT statement to retrieve all rows from the "films" table
            cursor.execute('SELECT * FROM films')

            # Fetch all the rows
            rows = cursor.fetchall()
        return rows
    
    def create_new_row(self, title, author, year, rate):
        # Connect to SQLite database
        with sqlite3.connect('bd.db') as connection:
            cursor = connection.cursor()

            # Use placeholders to prevent SQL injection
            cursor.execute('INSERT INTO films (title, author, year, rate) VALUES (?, ?, ?, ?)', (title, author, year, rate))

            # Commit the changes and close the connection
            connection.commit()

    def select_from_entry(self, entry_line):
        with sqlite3.connect('bd.db') as connection:
            cursor = connection.cursor()
            if not entry_line.strip():
                # If the search line is blank, retrieve all rows
                query = "SELECT * FROM films"
                cursor.execute(query)
            else:
                # If the search line is not blank, search in all columns
                query = """
                    SELECT * 
                    FROM films 
                    WHERE ID = ? OR Title = ? OR Author = ? OR Year = ? OR Rate = ?
                """
                # Execute the query with the line_data as parameters
                cursor.execute(query, (entry_line, entry_line, entry_line, entry_line, entry_line))
            
            # Fetch all the results
            results = cursor.fetchall()

        return results