import sys
import socket
import os

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10
queuesize = 0

def getfrom(thesocket):
    getted = thesocket.recv(RECV_BUFFER_SIZE)
    if len(getted) == 0:
        raise RuntimeError("socket connection broken")
    else:
        return getted.decode('utf-8')
        
def sendto(thesocket, thetext):
    if thesocket.send(bytes(thetext, 'utf-8')) == 0:
        raise RuntimeError("socket connection done broke!")

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
    gotted = ""
    if os.fork() > 0:
        while True:
            getted = getfrom(newsocket)
            print(getted)
            s = "hi"
            if getted == "exit":
                s = "bye"
            sendto(newsocket, s)
            if getted == "exit":
                break

def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python serverreal.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()