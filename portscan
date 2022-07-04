#!/bin/python

import sys
import socket
from datetime import datetime   # for timestamp

# Define your target IP address and port
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # gethostbyname converts hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 portscanner.py <ip>")
    sys.exit()

# Begin the scan
print ("Time initalized: " + str(datetime.now()))
print ("Scanning: " + target)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print ("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print ("\nScan terminated.")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print ("Couldn't make a connection.")
    sys.exit()
