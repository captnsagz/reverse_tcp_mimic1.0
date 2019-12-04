import socket
import os
import platform


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
myhost = platform.uname()[1]
port = 4446
addr = "192.168.21.1"
server_addr = (addr,port)
sock.bind(server_addr)
print("starting up on {} port {}".format(*server_addr))
sock.listen(10)
ext = int(0)
while True:
         print("Waiting for a connection.......")
         connection,client_addr = sock.accept()
         try:
                print("connection from : ",client_addr)

                while True:
                        data = connection.recv(1024)
                        print("received {!r}".format(data) + "/n" + "/n")
                        if data:
                                print("1)TO SEE THE LIST OF DIRECTORIES IN CWD")
                                print("2)TO SEE A LIST OF SYSTEM INFORMATION")
                                print("3)EXIT")
                                choice=int(input("ENTER YOUR CHOICE(1-3):"))
                                if choice == 1:
                                        data = "1"
                                        connection.sendall(data)
                                        data = connection.recv(1024)
                                        print("received {!r}".format(data) + "/n" + "/n")
                                elif choice == 2:
                                        data = "2"
                                        connection.sendall(data)
                                        data = connection.recv(1024)
                                        print("received {!r}".format(data) + "/n" + "/n")
                                elif choice == 3:
                                        connection.close()
                                        sock.close()
                                        ext = ext + 1
                                else:
                                        print("Wrong choice")
                        else:
                                print('no data from', client_addr)
                                break

         finally:
                print("Closing current connection")
                connection.close()

