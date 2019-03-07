import socket

def receiving_message(connection, address=None):
    data = None
    data = connection.recv(1024).decode()
    print(address, "says:", data)


def sending_message(connection):
    message = input("You: ")
    if message != "":
        connection.send(message.encode())
