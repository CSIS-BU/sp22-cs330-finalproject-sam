import sys
import socket
import os

SEND_BUFFER_SIZE = 2048

def getfrom(thesocket):
    getted = thesocket.recv(SEND_BUFFER_SIZE)
    if len(getted) == 0:
        raise RuntimeError("socket connection broken")
    else:
        return getted.decode('utf-8')

def sendto(thesocket, thetext):
    if thesocket.send(bytes(thetext, 'utf-8')) == 0:
        raise RuntimeError("socket connection done broke!")

def managegame(thesocket):
    while True:
        gottentext = input("Guess the letter, or type exit to quit: ")
        sendto(thesocket, gottentext)
        getted = getfrom(thesocket)
        print(getted)
        if getted == "Thanks for playing!":
            break
        

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    thesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    thesocket.connect((server_ip, server_port))
    managegame(thesocket)
    thesocket.close()
    pass


def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 clientreal.py [Server IP] [Server Port]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()