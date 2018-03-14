import socket

HOST = '10.20.98.66'    # The remote host
PORT = 8000              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall('Hello, world')
data = s.recv(1024)

s.close()

print 'Client: Received', repr(data)
