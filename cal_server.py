import socket
import sys
import os
import time
import errno
from multiprocessing import Process
import math

def process_start(s_sock):

  s_sock.send(str.encode("Online Calculator"))
  while True:
    s_sock.send(str.encode("\n(1-Logarithmic 2-Square Root 3-Exponential function 99-Exit)"))

    opt = s_sock.recv(2048).decode()
    if opt == "1":
      data = s_sock.recv(2048).decode()     
      result = math.log10(float(data))
      s_sock.send(bytes(str(result),'ascii'))
    elif opt == "2":
      data = s_sock.recv(2048).decode()
      result = math.sqrt(float(data))
      s_sock.send(bytes(str(result),'ascii'))
    elif opt == "3":
      data = s_sock.recv(2048).decode()
      result = math.exp(float(data))
      s_sock.send(bytes(str(result),'ascii'))
    elif opt == "99":
      print ("\nConnection ended : ", s_addr)
      exit(0)

   # else: 
      
  s_sock.close()

if __name__ == '__main__':

  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.bind(("",8888))
  print('listening...')
  s.listen(3)

  try:
    while True:
      try:
        s_sock,s_addr = s.accept()
        print ("\nConnection from : ", s_addr)
        p = Process(target = process_start,args = (s_sock,))
        p.start()

      except socket.error:
        print('got a socket error')

  except Exception as e:
    print('an exception occured!')
    print(e)

