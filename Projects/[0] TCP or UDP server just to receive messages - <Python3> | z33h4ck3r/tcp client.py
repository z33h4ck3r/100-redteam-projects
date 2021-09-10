import socket

#take the server name and port name
host = "localhost"
port = 5000

#create a socket at client side using TCP/IP protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect it to server and port number on local computer
sock.connect(("127.0.0.1", port))

#receive message from server at 1024
msg = sock.recv(1024)

#repeat as long as message string is not empty
while msg:
    print("Received: " + msg.decode())
    msg = sock.recv(1024)

sock.close()
