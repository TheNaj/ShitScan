import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

#Banner
print("-" * 50)
print(" ____  _     _ _   ____")                  
print("/ ___|| |__ (_) |_/ ___|  ___ __ _ _ __")  
print("\___ \| '_ \| | __\___ \ / __/ _` | '_ \\") 
print(" ___) | | | | | |_ ___) | (_| (_| | | | |")
print("|____/|_| |_|_|\__|____/ \___\__,_|_| |_|")                   
print('\n')
print("Made by Naji.")     
print('\n')
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))    
print("-" * 50)



try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting program.")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
    
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
    

