"""
 Implements a simple socket server

"""

import socket


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

# Wait for client connections
while True:

    client_connection, client_address = server_socket.accept()

    while True:
        # Print message from client
        msg = client_connection.recv(1024).decode()
        print('Received:', msg)

        if msg == "exit":
            break

        try:
            res = eval(msg)
            msgString = str(res)
            client_connection.send(msgString.encode())
        except:
            msgString = "Erro"
            client_connection.send(msgString.encode())

        # Send message back to client
        #print(msgString)
        #client_connection.send(msgString.encode())

    client_connection.close()  # Close client connection

# Close socket
# server_socket.close()
