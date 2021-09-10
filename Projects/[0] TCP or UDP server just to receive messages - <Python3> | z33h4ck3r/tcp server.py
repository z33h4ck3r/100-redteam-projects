import socket
import sys

#take the server name and port name
host = "localhost"
port = 5000

#create tcp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port
sock.bind(("", port))

#allow maximum 1 connection to the socket
sock.listen(1)

#wait till a client accepts connection
c, addr = sock.accept()

#display client address
print("CONNECTION FROM: ", str(addr))

#send message to the client after encoding into binary string
c.send(b"Hello Friend")

#disconnect the server
sock.close()