import requests

url = "https://www.googleapis.com/books/v1/volumes"

params = {
    "q":"python programming",
    "maxresults":5
}

response = requests.get(url, params=params)

data=response.json()

# print(data)
print(response)
for item in data.get("items", []):
    info = item.get("volumeInfo", {})
    print("Title:", info.get("title"))
    print("Authors:", info.get("authors"))
    print("Published:", info.get("publishedDate"))