import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

print(todos == response.json())  # True
print(type(todos))  # <class 'list'>
print(todos[:10])  # ...
#print(response)
