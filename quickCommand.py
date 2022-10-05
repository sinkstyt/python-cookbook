import requests
import json

r = requests.get(https://jsonplaceholder.typicode.com/todos)

dict = json.loads(r.text)

# for titles only:

for user in dict:
    print(user['title'])