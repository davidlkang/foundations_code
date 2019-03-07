import socket
import threading
import messages


HOST = "127.0.0.1"
port_number = int(input("Enter the port: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as aSocket:
    aSocket.bind((HOST, port_number))
    print("Server started at address %s on port %i" % (HOST, port_number))
    aSocket.listen()
    connection, address = aSocket.accept() ## accept incoming connection
    print("Client connected from: ", address)
    with connection:
        while True:
            messages.receiving_message(connection, address)
            messages.sending_message(connection)
