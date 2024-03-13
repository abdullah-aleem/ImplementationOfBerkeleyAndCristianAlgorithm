#Berkeley algo
import socket
import sys
import time 
import threading

barrier = threading.Barrier(6)
class Node:
    def __init__(self, port,status):
        self.port = port
        self.threads=[]
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

        while count[0]<6:
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
                    
                    print("the value of count is :",count)
                    # Bind the socket to the address and let the OS choose an available port
                    reqServer.bind(('localhost', 0))
                    _, port = reqServer.getsockname()
                    print("Available port number:", port)
                    currentuser=count[0]+1
                    server_thread = threading.Thread(target=self.handleReq,args=(reqServer,count,currentuser,))
                    self.threads.append(server_thread)
                    server_thread.start()          
                    port=str(port)
                 
                    connection.sendall(port.encode())
                    #this time is to syncronise the thread together so that both run the function together
                    time.sleep(3)
                    count[0]=currentuser
                    
                    
                    
                   
            except:
                connection.close()
                
            finally:
                # Clean up the connection
                print(count)
                connection.close()
        #so that it waits for all the threads to complete
        for thread in self.threads:
            thread.join()

        print("value of count : ",count)
    def handleReq(self,server,count,num):
        server.listen(5)
        connection, client_address = server.accept()
        print("Connection Number is :", num)
        try:
            # Receive the data from the client
            while True:
                data = connection.recv(1024)
                
                if not data:
                    break
                message='send Time' 
                while count[0]<=5:
                
                    continue
                barrier.wait()
                connection.sendall(message.encode())
                data = connection.recv(1024)
                print('time : ',data.decode())
                count[num]=float(data.decode())
                print('this is true count:',count)
                
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