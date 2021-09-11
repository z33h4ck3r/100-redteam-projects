import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket object
host = socket.gethostname() #get the host name
port = 8080 #ftp port
s.bind((host, port)) #bind to the host and port

f = open("hello_friend.txt", 'wb')
s.listen(5) #tell socket to listen for 5 connection
while True:
    c, addr = s.accept() #establish a connection
    print("Got connection from ", addr) #states the client address
    print("Receiving...") 
    l = c.recv(1024) 
    while (l): #while loop for file transfer to display "receiving..." before finishing 
        print("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print("Done Receiving")
    c.send(bytes("Thank you for connecting", 'UTF-8'))
    c.close()
    exit()