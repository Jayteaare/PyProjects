#!/bin/python

import sys
import socket
from os import mkdir 
from datetime import datetime
from time import sleep   # for timestamp

# Define your target IP address and port
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # gethostbyname converts hostname to IPv4
else:
    print("Invalid amount of arguments.") # If no arguments are given, print error
    print("Syntax: python3 portscanner.py <ip>") # Syntax
    sys.exit() 

# Begin the scan
print ("We're getting everything ready.") 
mkdir (target) # Create a directory for the scan
sleep (5) # Wait 5 seconds
print ("Time initalized: " + str(datetime.now())) # Print the time
print ("Scanning: " + target) # Print the target
open (target + "/" + target + "_scanresults" + ".txt", "w") # Create a file for the scan results

try:
    for port in range(1, 65535): # Scan all ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket
        socket.setdefaulttimeout(1) # Set the timeout to 1 second
        result = s.connect_ex((target, port)) # Try to connect to the port
        if result == 0: # If the port is open
            print ("Port {} is open".format(port))
        s.close() # Close the socket

except KeyboardInterrupt: # If the user interrupts the program
    print ("\nScan terminated.")
    sys.exit()

except socket.gaierror: # If the hostname is invalid
    print ("Hostname could not be resolved.")
    sys.exit()

except socket.error: # If the port is invalid
    print ("Couldn't make a connection.")
    sys.exit()
