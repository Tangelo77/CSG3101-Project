import pyodbc

SERVER_NAME = 'DESKTOP-Q6P1DJ6'
DATABASE_NAME = 'DATABASE8'

cursor = ''
def Connect_To_Database():
    global cursor
    try:
        connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={SERVER_NAME};'
            f'DATABASE={DATABASE_NAME};'
            f'TRUSTED_CONNECTION=yes;'
        )

        # Connection established successfully
        cursor = connection.cursor()

        # Execute SQL queries or other database operations here
        print("Connected")


    except pyodbc.Error as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_cursor():
    return cursor