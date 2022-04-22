###############################################################################
# server-python.py
# Name: Sam Carpenter
###############################################################################

import sys
import socket
import os

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10
queuesize = 0

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    thesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    print("connecting the server to", host)
    thesocket.bind((host, server_port))
    thesocket.listen(QUEUE_LENGTH)
    while True:
        newsocket, address = thesocket.accept()
        handlenewconnection(newsocket)
    pass

def handlenewconnection(newsocket):
    gotted = []
    if os.fork() > 0:
        while True:
            getted = newsocket.recv(RECV_BUFFER_SIZE)
            #if getted == b'':
            #    raise RuntimeError("socket connection broken")
            #el
            if len(getted) == 0:
                if len(gotted) == 0:
                    raise RuntimeError("socket connection broken")
                else:
                    s = ""
                    for c in gotted:
                        s += c
                    print(s)
                    if newsocket.send(bytes("hi", 'utf-8')) == 0:
                        raise RuntimeError("socket connection done broke!")
                    break
            else:
                gotted.append(getted.decode('utf-8'))

def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()
