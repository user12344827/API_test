import pymysql

import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWOED")
DB = os.getenv("DB")

def db_init():
    db = pymysql.connect(
        host=HOST, user=USER, password=PASSWORD, port=3306, db=DB
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, cursor

# 建立使用者資料庫
def create_db_account():
    conn = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS api_class")
    cur.execute("CREATE DATABASE api_class")

    # 切換到新建立的資料庫
    cur.execute("USE api_class")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user1 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(40),
            account VARCHAR(10),
            pwd VARCHAR(20)
        )
    """)
    conn.commit()
    conn.close()

# 建立接收資料的資料庫
def create_user():
    conn = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    cur = conn.cursor()

    # 切換到新建立的資料庫
    cur.execute("USE api_class")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user2 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(40),
            gender VARCHAR(10),
            birth VARCHAR(20),
            note VARCHAR(100)
        )
    """)
    conn.commit()
    conn.close()