import socket, sys, time

new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname("127.0.0.1")
s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind(host_name, port)
print("Bind is successful")
print("This is your IP: " + host_name)

name = input("Enter name: ")

new_socket.listen(100)

conn, add = new_socket.accept()

print("Received connection from ", add[0])
print("Connection Estashblished. Connection from ", add[0])

client = (conn.recv(1024).decode())
print(client + " has connected.")

conn.send(name.encode())
while True:
    message = input("Me: ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ":", message)