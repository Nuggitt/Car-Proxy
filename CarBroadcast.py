from socket import *
import json

serverName = '255.255.255.255'
serverPort = 10100
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    cars = {
        "id": 28,
        "brand": "Ferrari",
        "model": "Monza SP1",
        "horsepower": 810,
    }
    
    message = json.dumps(cars)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    print("Car broadcasted")
    break

clientSocket.close()