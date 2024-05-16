from socket import *
import requests

serverPort = 10100
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ('', serverPort)

api_address = "https://carrestapi20240417213626.azurewebsites.net/api/cars"
headersArray = { "Content-Type": "application/json" }

serverSocket.bind(serverAddress)
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(f"Received message: {message.decode()} from {clientAddress}")
    
    response = requests.post(api_address, data=message, headers=headersArray)
    print(f"Response: {response.text}")