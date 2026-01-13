import requests
import random
import matplotlib.pyplot as plt

url = "https://jsonplaceholder.typicode.com/users"


response =  requests.get(url)
data=response.json()

# for user in data[:5]:
#     score=random.randint(60,100)
#     print(user["id"],user["name"],user["email"],score)

name=[]
score=[]
for user in data:
    name.append(user["name"])
    score.append(random.randint(60,100))
print("Average score of all students:",sum(score)/len(score))

plt.figure()
plt.bar(name,score)
plt.title("Student Scores")
plt.xticks(rotation=90)
plt.xlabel("Students")
plt.ylabel("Score")

plt.tight_layout()
plt.show()