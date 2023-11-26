import threading 
import socket

host='127.0.0.1'
port=59000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))  #this bind the server object
server.listen()  #this is listening the port

clients=[]
aliases=[]

#this provide message for all the clients
def broadcast(message):
    for client in clients:
        client.send(message)



#this provide handling feature of all client where using  server  clients can talk to eachother 
def handle_client(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            alias=aliases[index]
            broadcast(f'{alias} has left the chat '.encode('utf-8'))
            aliases.remove(alias)
            break


#this is main funtion for run server 
def receive():
    while True:
        print('server is listening and running')
        client,addr=server.accept()
        print(f'connetion is established to address {str(addr)}')
        client.send('alias?'.encode('utf-8'))
        alias=client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'the alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'the alias name {alias} is joined our chat'.encode('utf-8'))
        client.send('you are now connected'.encode('utf-8'))
        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()

if __name__=="__main__":
    receive()