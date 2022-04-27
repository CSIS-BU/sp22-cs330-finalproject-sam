import sys
import socket
import os
import random

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

def handlenewconnection(thesocket):
    if os.fork() > 0:
        gotted = ""
        letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        #print(letter)
        guesses = 1
        winned = False
        while True:    
            gotted = getfrom(thesocket)
            gotted = gotted.lower()
            print(gotted)
            if gotted == "exit":
                sendto(thesocket, "Thanks for playing!")
                break
            elif gotted == "retry":
                letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
                #print(letter)
                guesses = 1
                winned = False
                sendto(thesocket, "Letter reset! Good luck!")
            elif winned:
                sendto(thesocket, "Type retry to retry, or exit to quit!")
            elif len(gotted) != 1:
                sendto(thesocket, "Make sure guesses are exactly one character long!")
            elif gotted[0] == letter:
                winned = True
                if guesses == 1:
                    sendto(thesocket, "You guessed the correct letter in only one guess! Wow!\nType retry to retry, or exit to quit!")
                else:
                    sendto(thesocket, "You guessed the correct letter in " + str(guesses) + " guesses!\nType retry to retry, or exit to quit!!")
            else:
                sendto(thesocket, "Incorrect... Try again!")
                guesses = guesses + 1

def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python serverreal.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()