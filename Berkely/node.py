#Berkeley algo
import socket
import sys
import time 
import threading


class Node:
    def __init__(self, port,status):
        self.port = port
        
        self.status = status
        if self.status=="server":
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(('localhost', self.port))
            self.handleServer()
        elif self.status=="client":
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(('localhost', self.port))
            self.handleClient()

    def handleClient(self):
        try:
            # Send data to the server
            message = "Hello, server!"
            self.client.sendall(message.encode())

            # Receive data from the server
            data = self.client.recv(1024)
            print("Received:", data.decode())
            self.client.close()
            self.port=int(data)
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(('localhost',self.port))
            message1 = "connected to new server"
            
            self.client.sendall(message1.encode())
            data=self.client.recv(1024)
            
            print(data.decode())
            tim=str(time.time())    
            self.client.sendall(tim.encode())
        finally:
            # Clean up the connection
            self.client.close()
    def handleServer(self):
        count=[0,0,0,0,0,0,0]
        self.server.listen(5)

        print("Server is listening on : ",self.port)

        while True:
            # Wait for a connection
            print("Waiting for a connection...")
            connection, client_address = self.server.accept()
            print("Connection from:", client_address)

            try:
                # Receive the data from the client
                while True:
                    data = connection.recv(1024)
                    
                    if not data:
                        break
                    #make a new connection specially for this request
                    reqServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    count[0]=count[0]+1
                    print("the value of count is :",count)
                    # Bind the socket to the address and let the OS choose an available port
                    reqServer.bind(('localhost', 0))
                    _, port = reqServer.getsockname()
                    print("Available port number:", port)
                    server_thread = threading.Thread(target=self.handleReq,args=(reqServer,count,count[0]))
                    server_thread.start()          
                    port=str(port)
                    # Echo back the data
                    connection.sendall(port.encode())
                    #create a thread to handle request for this specific port for specific user
                    
                    
                   
            except:
                connection.close()
                
            finally:
                # Clean up the connection
                print(count)
                connection.close()
    def handleReq(self,server,count,num):
        server.listen(5)
        connection, client_address = server.accept()
        print("second server client",client_address)
        try:
            # Receive the data from the client
            while True:
                data = connection.recv(1024)
                
                if count[0]>1:
                    break
                message='send Time' 
                while count[0]<=1:
                    continue
                print("here")
                connection.sendall(message.encode())
                data = connection.recv(1024)
                print('time : ',data.decode())
                count[num]=float(data.decode())
                
        except:
            print("in exception")
            connection.close()
            server.close()
            
        finally:
            # Clean up the connection
            connection.close()
            server.close()
    






      
def main(): 
    status=None    
    arguments = sys.argv
    if len(arguments) > 1:
        status=arguments[1]
        node =Node(12345,status)
    else:
        print("No argument passed")
        return 1
    
        
        
        
        

       


if __name__=="__main__":
    main()