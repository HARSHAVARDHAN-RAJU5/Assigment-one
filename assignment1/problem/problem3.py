import sqlite3
import pandas as pd

# conn = sqlite3.connect("user.db")
# cur = conn.cursor()

# cur.execute("""
# CREATE TABLE user(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             email TEXT,
#             country TEXT)

# """
# )

# conn.commit()
# conn.close()
# print("done")

df = pd.read_csv("users.csv")

conn = sqlite3.connect("user.db")
cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO user (name,email,country) VALUES (?,?,?)",
        (row["name"], row["email"], row["country"])
    )

cur.execute("SELECT * FROM user")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
print("done")
