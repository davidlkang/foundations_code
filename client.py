import socket
import threading
import messages


HOST = "127.0.0.1"
port_number = int(input("Enter the port: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as aSocket:
    aSocket.connect((HOST, port_number))
    while True:
        messages.sending_message(aSocket)
        messages.receiving_message(aSocket)
