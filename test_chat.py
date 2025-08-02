import requests

message = input("You: ")
response = requests.post("http://127.0.0.1:5000/chat", json={"message": message})

if response.status_code == 200:
    print("Bot:", response.json()['response'])
else:
    print("Error:", response.status_code, response.text)
