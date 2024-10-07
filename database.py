import mysql.connector as mc
from mysql.connector import Error
def create_con():
    try:
        # Establish a connection
        conn = mc.connect(
            host="localhost",
            user="root",
            password="",  # No spaces if no password is used
            database="exam"
        )

        if conn.is_connected():  # Check if the connection was successful
            print("Connected to the database")
            return conn
        else:
            print("Not connected")
    except Error as e:
         print(e)
    

def create(conn,name,address):
    
        cursor = conn.cursor()

        # Execute a query
        query="Update detail set First_name=%s where Address=%s"
        cursor.execute(query,(name,address))

        # Fetch the result
        conn.commit()
        print(f"Updated successfully")
    


if __name__=='__main__':
    connection=create_con()

    if connection:
         create(connection,'Hari','mulpani')

