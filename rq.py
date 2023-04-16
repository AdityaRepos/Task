import requests

url = 'http://localhost:3000/newpost'
data = {'title': 'My First Post', 'body': 'This is my first post.'}

response = requests.post(url, data=data)

print(response.text)