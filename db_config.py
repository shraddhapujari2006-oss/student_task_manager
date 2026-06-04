import mysql.connector

def get_db_connection():
    connection =mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user='3hSrUBSPF9bKQvi.root',
        password='asbI5myPebu2VfhG',
        database='student_task_manager',
        port='4000'
    )
    return connection