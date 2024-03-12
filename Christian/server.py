import socket
import threading
import time


def handleReq(server):
    server.listen(5)
    connection, client_address = server.accept()
    print("second server client",client_address)
    try:
        # Receive the data from the client
        while True:
            data = connection.recv(1024)
            
            if not data:
                break
            time.sleep(3)
            tim=str(time.time())    
            connection.sendall(tim.encode())
            #create a thread to handle request for this specific port for specific user
            
    except:
        print("in exception")
        connection.close()
        server.close()
        
    finally:
        # Clean up the connection
        connection.close()
        server.close()
        

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening on {}:{}".format(*server_address))

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()
    print("Connection from:", client_address)

    try:
        # Receive the data from the client
        while True:
            data = connection.recv(1024)
            
            if not data:
                break
            #make a new connection specially for this request
            reqServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Bind the socket to the address and let the OS choose an available port
            reqServer.bind(('localhost', 0))
            _, port = reqServer.getsockname()
            print("Available port number:", port)
            server_thread = threading.Thread(target=handleReq,args=(reqServer,))
            server_thread.start()
            print(data)            
            port=str(port)
            # Echo back the data
            connection.sendall(port.encode())
            #create a thread to handle request for this specific port for specific user
  
            
    except:
        
        connection.close()
        
    finally:
        # Clean up the connection
        connection.close()
        # server_socket.close()
