# import sqlite3

# conn=sqlite3.connect("book.db")

# cur=conn.cursor()

# cur.execute("""
# CREATE TABLE book(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT,
#             author TEXT,
#             published TEXT
# )
# """)

# conn.commit()
# conn.close()
# print("done")

import sqlite3

conn = sqlite3.connect("book.db")
cur = conn.cursor()

cur.execute("SELECT * FROM book")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
