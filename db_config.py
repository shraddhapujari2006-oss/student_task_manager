import mysql.connector

def get_db_connection():
    connection =mysql.connector.connect(
        host='localhost',
        user='root',
        password='2709',
        database='student_task_manager'
    )
    return connection