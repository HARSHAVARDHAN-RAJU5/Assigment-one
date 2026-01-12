import requests

BASE="http://localhost:3000"

def GET():
    response = requests.get(f"{BASE}/user")
    print(response.json())
def CREATE():
    data = {
        "name":"harsha",
        "email":"harsha@gmail.com"
    }
    response = requests.post(f"{BASE}/user",json=data)
    print(response.json())
def CHANGE(id):
    data={
        "name":"kavi",
        "email":"kavi@gmail.com"
    }
    response = requests.put(f"{BASE}/user/{id}",json=data)
    print(response.json())
def UPDATE(id):
    data={
        "email":"kavi1@gmail.com"
    }
    response = requests.patch(f"{BASE}/user/{id}",json=data)
    print(response.json())    
def DELETE(id):
    response = requests.delete(f"{BASE}/user/{id}")
    print(response.json())

if __name__ == "__main__":
    GET()
    CREATE()
    CHANGE(1)
    UPDATE(1)
    DELETE(1)