import socket

def get_input(clientSocket):
   no = input("Enter Number:")
   clientSocket.send(no.encode())

clientSocket = socket.socket()
host = "192.168.120.11"
port = 8888

try:
  clientSocket.connect((host,port))

except socket.error as e:
  print(str(e))

response = clientSocket.recv(1024).decode()
print(response)

while True:

   display = clientSocket.recv(1024).decode()
   print(display)
   option = input('Your option:')
   clientSocket.send(str.encode(option))
   if option == "1":
      get_input(clientSocket)

   elif option == "2":
     get_input(clientSocket) 

   elif option == "3":
      get_input(clientSocket)

   elif option == "99":
      print("Calculator closed")
      exit(0)
  
   else:
      print("No option")
      continue

   result=clientSocket.recv(2048).decode()
   print("Output:",result)

clientSocket.close()
