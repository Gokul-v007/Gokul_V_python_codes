# import mysql.connector
# from mysql.connector import Error
# def dbconnector():
#     try:
#         conn=mysql.connector.connect(
#             host='localhost',
#             database='gokul',
#             username='root',
#             password='root123'
#         )
#         if conn.is_connected():
#             print("connected Established")
#             return conn
#     except Error as e:
#         print(f"connection failed:(e)")
#     return None
# def insert_users(conn):
#     if conn is None:
#         print("No database connection available.")
#         return
        
#     cursor = conn.cursor()
#     username = input("Enter username: ")
#     passwords = input("Enter password: ")
#     namee = input("Enter name: ")
#     email = input("Enter email: ")
    
#     query = "INSERT INTO users (username, passwords, namee, email) VALUES (%s, %s, %s, %s)"
#     try:
#         cursor.execute(query, (username, passwords, namee, email))
#         conn.commit()  # Fixed: Changed con.commit() to conn.commit()
#         print("User inserted successfully")
#     except Error as e:
#         print(f"Error: {e}") # Fixed: Changed (e) to {e} to see the real SQL error
#     finally:
#         cursor.close()
      


# # Main execution (Removed the extra duplicate dbconnector() call from your original script)
# con = dbconnector()
# if con:
#     insert_users(con)
#     con.close() # Good practice to close the connection when completely done


import mysql.connector
from mysql.connector import Error


def dbconnector():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="gokul",
            user="root",
            password="root123"
        )

        if conn.is_connected():
            print("Connection Established")
            return conn

    except Error as e:
        print(f"Connection failed: {e}")

    return None


def insert_users(conn):
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")
    name = input("Enter name: ")
    email = input("Enter email: ")

    query = """
    INSERT INTO users (username, password, name, email)
    VALUES (%s, %s, %s, %s)
    """

    try:
        cursor.execute(query, (username, password, name, email))
        conn.commit()
        print("User inserted successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()


def view_users(conn):
    cursor = conn.cursor()

    query = "SELECT * FROM users"
    cursor.execute(query)

    rows = cursor.fetchall()

    if rows:
        print("\nAll Users:")
        for row in rows:
            print(row)
    else:
        print("No Users Found")

    cursor.close()


def update_password(conn):
    cursor = conn.cursor()

    username = input("Enter username: ")
    new_password = input("Enter new password: ")

    query = "UPDATE users SET password=%s WHERE username=%s"

    try:
        cursor.execute(query, (new_password, username))
        conn.commit()

        if cursor.rowcount > 0:
            print("Password updated successfully!")
        else:
            print("Username not found!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()


# Main Program
con = dbconnector()

if con:
    view_users(con)

    print("\n1. Insert User")
    print("2. Update Password")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_users(con)

    elif choice == 2:
        update_password(con)

    else:
        print("Invalid Choice")

    con.close()
    print("Connection Closed")

def delete_user(con):
    cursor=con.cursor()
    username=input("enter the username:")
    query="delete from users where username=%s"
    cursor.execute(query,(username,))
    con.commit()
    if cursor.rowcount>0:
        print("user deleted sucessfully")
    else:
        print("user not found")
    cursor.close()
#delete_user(con)    
    
def menu():
    con=dbconnector()
    if not con:
        print("connection not established")
        return
    while True:
        print("1.Insert")
        print("2.update")
        print("3.delete")
        print("4.view")
        print("5.Exit")
        choice=int(input("enter the choice:"))
        if choice==1:
            insert_users(con)
        elif choice==2:
            update_password(con)
        elif choice==3:
            delete_user(con)
        elif choice==4:
            view_users(con)
        elif choice==5:
            print("thanks for using")
            con.close()
            break
        else:
            print("Invalid choice")
menu()