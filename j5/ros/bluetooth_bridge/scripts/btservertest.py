# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $

import time
import select
from bluetooth import *

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = '023f3c7f-af05-4299-bd2d-52487cb6cef7'

advertise_service( server_sock, "LidarServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ]
                   )

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

client_sock.setblocking(0)

try:
    while True:
        ready = select.select([client_sock], [], [], 0.01)
        if ready[0]:
            data = client_sock.recv(1024)
            if len(data) == 0: break
            print("received [%s]" % data)
            client_sock.send("my data".encode('UTF-8'))
        else:
            print("no data recieved")
            time.sleep(0.25)
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
