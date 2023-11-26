import threading 
import socket

alias=input("enter your alias")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',59000))

#this help in receiving and manipulating message from server and other client
def client_receive():
    while True:
        try:
         message=client.recv(1024).decode('utf-8')
         if message=="alias?":
            client.send(alias.encode('utf-8'))
         else:
            print(message)
        except:
           print("Error")
           client.close()
           break

#this also help to send message from client to another client through server
def client_send():
   while True:
      message=f'{alias}:{input("")}'
      client.send(message.encode('utf-8'))

#we create object of threading for client_receive and client_send function
threading_receive=threading.Thread(target=client_receive)
threading_receive.start()
threading_send=threading.Thread(target=client_send)
threading_send.start()
        


