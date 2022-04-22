###############################################################################
# client-python.py
# Name: Sam Carpenter
###############################################################################

import sys
import socket

SEND_BUFFER_SIZE = 2048

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    gottentext = input("Say something to the server: ")
    gttable = list(gottentext)
    thesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    thesocket.connect((server_ip, server_port))
    sent = 0
    while sent < len(gttable):
        t = ""
        for i in range(0, SEND_BUFFER_SIZE):
            if i + sent >= len(gttable):
                break
            else:
                t += gttable[i + sent]
        sendcheck = thesocket.send(bytes(t, 'utf-8'))
        if sendcheck == 0:
            raise RuntimeError("socket connection done broke!")
        sent += sendcheck
    thesocket.close()
    pass


def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()
