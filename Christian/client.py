import socket
import time
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data to the server
    message = "Hello, server!"
    print("Sending:", message)
    timeStart=time.time()
    client_socket.sendall(message.encode())

    # Receive data from the server
    data = client_socket.recv(1024)
    print("Received:", data.decode())
    client_socket.close()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost',int(data)))
    message = "time please"
    client_socket.sendall(message.encode())
    data=client_socket.recv(1024)
    print("TIME ON SERVER",data.decode())
    timeEnd=time.time()
    print("RTT FOR THIS SERVER: ",timeEnd-timeStart)
    print("SYNCRONISED TIME IS :",float(data.decode())+timeEnd-timeStart)
finally:
    # Clean up the connection
    client_socket.close()
