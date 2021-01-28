import sqlite3

#connecting database
conn=sqlite3.connect("./database/food.db")
cur=conn.cursor()

cur.execute("select * from food where food='순두부찌개'")
result=cur.fetchall()


print(result)



query="insert into account(id, pw) values(?,?)"
cur.execute(query, ("testuser", "123"))

cur.execute("select * from account")
result=cur.fetchall()


print(result)
conn.commit()
conn.close()