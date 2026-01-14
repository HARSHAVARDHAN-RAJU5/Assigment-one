import requests
import sqlite3

url = "https://www.googleapis.com/books/v1/volumes"

params = {
    "q":"python programming",
    "maxresults":5
}

response = requests.get(url, params=params)
data=response.json()

conn=sqlite3.connect("book.db")
cur=conn.cursor()

for item in data.get("items", []):
    info = item.get("volumeInfo", {})
    title= info.get("title")
    authors= ", ".join(info.get("authors",[]))
    published=info.get("publishedDate")

cur.execute(
    "INSERT INTO book (title, author, published) VALUES (?,?,?)",
    (title, authors, published)
)

conn.commit()
conn.close()

print("Data stored")