#!/bin/python

import sys
import socket
import os
from termcolor import cprint
from pyfiglet import figlet_format
from datetime import datetime
from time import sleep   # for timestamp

# Define your target IP address and port
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # gethostbyname converts hostname to IPv4
else:
    print ("Invalid amount of arguments.") # If no arguments are given, print error
    print ("Syntax: python3 portscanner.py <ip>") # Syntax
    sys.exit() 

# Begin the scan
cprint (figlet_format("SimpleScan", font="starwars"), color="red", attrs=["bold"])
print ("We're getting everything ready.") 
if not os.path.exists(target): # If the target directory doesn't exist, create it
    os.mkdir (target) # Create a directory for the scan
    open (target + "/" + target + "_scanresults" + ".txt", "w") # Create a file for the scan results
sleep (5) # Wait 5 seconds
print ("Time initalized: " + str(datetime.now())) # Print the time
print ("Scanning: " + target) # Print the target
print ("----------------------------------------------------")

try:
    for port in range(1, 65535): # Scan all ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket
        socket.setdefaulttimeout(1) # Set the timeout to 1 second
        result = s.connect_ex((target, port)) # Try to connect to the port
        if result == 0: # If the port is open
            print ("Port {} is open".format(port)) # Print the port
            x=open (target + "/" + target + "_scanresults" + ".txt", "a") # Open the file for writing
            x.write ("Port {} is open\n".format(port)) # Write the port to the file
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

print ("----------------------------------------------------")
print ("Scan completed at: " + str(datetime.now())) # Print the time
print ("Scan results saved to " + target + "/" + target + "_scanresults" + ".txt") # Print the file location
