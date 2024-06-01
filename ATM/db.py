import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

# Function to create a connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="a12"
        )
        return connection
    except Error as e:
        messagebox.showerror("Database Connection Error", f"Error: '{e}'")
        return None

# Function to create the table
def create_table():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS accounts (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), balance DECIMAL(10, 2))")
            connection.close()
        except Error as e:
            messagebox.showerror("Database Error", f"Error: '{e}'")

# Function to add a new account
def add_account(account_id, name, balance):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO accounts (id, name, balance) VALUES (%s, %s, %s)"
            values = (account_id, name, balance)
            cursor.execute(sql, values)
            connection.commit()
            cursor.execute("SELECT LAST_INSERT_ID()")
            account_id = cursor.fetchone()[0]
            connection.close()
            return account_id
        except Error as e:
            messagebox.showerror("Database Error", f"Error: '{e}'")
            connection.rollback()
            connection.close()
    return None

# Function to remove an account
def remove_account(account_id, name):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            if get_balance(account_id, name, cursor) is not None:
                sql = "DELETE FROM accounts WHERE id = %s AND name = %s"
                values = (account_id, name)
                cursor.execute(sql, values)
                connection.commit()
                connection.close()
                return True
            connection.close()
        except Error as e:
            messagebox.showerror("Database Error", f"Error: '{e}'")
            connection.close()
    return False

# Function to get account balance
def get_balance(account_id, name, cursor=None):
    connection = None
    try:
        if cursor is None:
            connection = create_connection()
            cursor = connection.cursor()
        sql = "SELECT balance FROM accounts WHERE id = %s AND name = %s"
        values = (account_id, name)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        if connection:
            connection.close()
        return result[0] if result else None
    except Error as e:
        messagebox.showerror("Database Error", f"Error: '{e}'")
        if connection:
            connection.close()
        return None

def update_balance(account_id, name, amount):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        balance = get_balance(account_id, name, cursor)
        if balance is not None:
            new_balance = float(balance) + amount
            sql = "UPDATE accounts SET balance = %s WHERE id = %s AND name = %s"
            values = (new_balance, account_id, name)
            cursor.execute(sql, values)
            connection.commit()
            connection.close()
            return True
        connection.close()
    return False

