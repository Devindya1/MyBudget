import mysql.connector
from config import config

def get_connection():
    return mysql.connector.connect(**config)

def add_category(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT IGNORE INTO category (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()    

def get_categories():   
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category_id, name FROM category")
    categories = cursor.fetchall()
    cursor.close()
    conn.close()
    return categories

def add_expense(category_id, description, amount, expense_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expense (category_id, description, amount, expense_date) VALUES (%s, %s, %s, %s)",
        (category_id, description, amount, expense_date)
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.expense_id, c.name, e.description, e.amount, e.expense_date
        FROM expense e
        JOIN category c ON e.category_id = c.category_id
        ORDER BY e.expense_date DESC
    """)
    expenses = cursor.fetchall()
    cursor.close()
    conn.close()
    return expenses

def get_summary():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.name, SUM(e.amount) AS total
        FROM expense e
        JOIN category c ON e.category_id = c.category_id
        GROUP BY c.name
        ORDER BY total DESC
    """)
    summary = cursor.fetchall() 
    cursor.close()
    conn.close()
    return summary

def delete_category(category_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM category WHERE category_id = %s", (category_id,))
    conn.commit()
    cursor.close()
    conn.close()
     