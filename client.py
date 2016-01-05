import socket

sock = socket.socket()
host = socket.gethostname()
port = 1337

sock.connect(('endor.solidarray.com',port))
print(sock.recv(1024))
sock.close
