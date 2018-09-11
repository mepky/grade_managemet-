import sqlite3

def connect():
        conn=sqlite3.connect("students.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY ,name text,user_name text, email_id text,password text)")
        conn.commit()
        conn.close()

def insert(name, user_name, email_id, password):
        conn=sqlite3.connect("students.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO data VALUES(NULL,?,?,?,?)",(name,user_name,email_id,password))
        conn.commit()
        conn.close()

def view():
        conn=sqlite3.connect("students.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM data")
        rows=cur.fetchall()
        conn.close()
        return rows

def search(name=" ",user_name=" ",email_id=" ",password=" "):
        conn=sqlite3.connect("students.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM data WHERE name=? OR user_name=? OR email_id=? OR password=?" (name,user_name,email_id,password))
        row=cur.fetchall()
        conn.close()
        return row


def update(name,user_name,email_id,password):
        conn = sqlite3.connect('books.db')
        cur = conn.cursor()
        cur.execute("UPDATE  data SET  name=? OR user_name=? OR email_id=? OR password=?", (name,user_name,email_id, password))
        conn.commit()
        conn.close()

        



connect()
insert("navin","singh","kumarpraveen7393@gmail.com","Royrebel11")
print(view())
#print(search(user_name="rebel"))
                        
