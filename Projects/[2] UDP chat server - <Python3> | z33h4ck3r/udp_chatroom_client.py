import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 6789

print("This is your IP address: " + ip)
server_host = input("Enter friend/'s IP address: ")
name = input("Enter friend/'s name: ")

server_host.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, " has joined...")
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me: ")
    socket_server.send(message.encode())
