import socket

server = socket.socket()

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s 
# s.bind((HOST, PORT))

server.bind(("127.0.0.1", 5000))

#     s.listen()

server.listen(1)
print("Server is now running and waiting for the client.")

connectionToClient, address = server.accept()
print("Client connected:", address)

message = connectionToClient.recv(1024).decode()
print("Message from the client:", message)

reply = "Server has received message!"
connectionToClient.send(reply.encode())

connectionToClient.close()
server.close()
print("Server is now closed.")


