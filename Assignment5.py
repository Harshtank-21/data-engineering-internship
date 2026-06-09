# Assignment 5
import csv, sqlite3

with open("address_book.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name","Address","Mobile","Email"])
    for _ in range(2):
        writer.writerow([input("Name:"),input("Address:"),input("Mobile:"),input("Email:")])

conn=sqlite3.connect("demo.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER,name TEXT)")
cur.execute("INSERT INTO students(name) VALUES ('Harsh')")
print(cur.execute("SELECT * FROM students").fetchall())
cur.execute("UPDATE students SET name='John' WHERE id=1")
cur.execute("DELETE FROM students WHERE id=1")
conn.commit()
conn.close()
