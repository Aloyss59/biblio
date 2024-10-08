import sqlite3

def CreateUser():
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_admin BOOLEAN DEFAULT 0
        )
    """)
    
    con.commit()
    con.close()

def CreateProjectShip():
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ProjectShip (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER NOT NULL,
            project_id INTEGER NOT NULL,
            status INTEGER DEFAULT pending NOT NULL,
            FOREIGN KEY (sender_id) REFERENCES User(id),
            FOREIGN KEY (receiver_id) REFERENCES User(id)
        )
    """)
    
    con.commit()
    con.close()

def CreateTable():
    CreateUser()
    CreateProjectShip()
