import socket

client = socket.socket()

client.connect(("127.0.0.1",
                        5000))

message = "sending message to the server"
client.send(message.encode())
print("message to server:", message)

reply = client.recv(1024).decode()
print("Server's reply:", reply)

client.close()
print("Client connection is now closed.")
