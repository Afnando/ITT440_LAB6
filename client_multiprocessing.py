import socket

clientSocket = socket.socket()
host = '192.168.120.11'
port = 8888

print('Waiting for connection')

try:
  clientSocket.connect((host,port))

except socket.error as e:
  print(str(e))

response = clientSocket.recv(1024)
print(response)

while True:
  
  Input = input('say Something:')
  clientSocket.send(str.encode(Input))
  response = clientSocket.recv(1024)
  print(response.decode('utf-8'))
  
clientSocket.close()

