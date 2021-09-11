import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
c_port = 8080
s.connect((host, c_port))

s.send(bytes("Hello Friend", 'UTF-8'))
f = open("hello_friend.txt", 'rb')
print("Sending...")
 
l = f.read(1024)
while (l):
    print("Sending...")
    s.send(l)
    l = f.read(1024)
f.close()
print("Done sending")
s.close()