"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""

import bluetooth
    
# hciconfig
# myMACaddress = '00:1f:e1:dd:08:3d'
serverMACAddress = '88:53:2e:2e:bf:4d'


# file: rfcomm-client.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a client application that uses RFCOMM sockets
#       intended for use with rfcomm-server
#
# $Id: rfcomm-client.py 424 2006-08-24 03:35:54Z albert $

from bluetooth import *
import sys

addr = serverMACAddress
# addr = None

# if len(sys.argv) < 2:
#     print("no device specified.  Searching all nearby bluetooth devices for")
#     print("the SampleServer service")
# else:
#     addr = sys.argv[1]
#     print("Searching for SampleServer on %s" % addr)

# search for the SampleServer service
uuid = "023f3c7f-af05-4299-bd2d-52487cb6cef7"
service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))

print("connected.  type stuff")
while True:
    data = str(raw_input()).encode()
    if len(data) == 0: break
    sock.send(data)
    print(sock.recv(2048))

sock.close()
