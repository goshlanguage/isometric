import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1337))
server.listen(5)

while(True):
  (clientsocket, address) = server.accept()
  clientsocket.send('Thank you')
  clientsocket.close()
  #ct = client_thread(clientsocket)
  #print(clientsocket)
  #print(dir(clientsocket))
  #ct.run()
