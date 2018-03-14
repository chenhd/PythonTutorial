import socket
import time
import gevent

# HOST = '0.0.0.0'    # The remote host
HOST = '10.20.79.147'    # The remote host
PORT = 8000              # The same port as used by the server

import asyncore, socket

class HTTPClient(asyncore.dispatcher):

    def __init__(self, host):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, PORT) )
        # keep-alive!
        send_data_alive = '''\
GET / HTTP/1.1
Host: 10.20.79.147:8000
Connection: keep-alive

'''
        
        # close!
        send_data_close = '''\
GET / HTTP/1.1
Host: 10.20.79.147:8000
Connection: close

'''
        self.buffer = send_data_alive
        # self.buffer = send_data_close

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        data = self.recv(81920)
        if data != '':
            pass
            if len(data) == 192:
                self.close()


    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

if __name__ == '__main__':
    l = []
    for i in range(500): 
        g = gevent.spawn(HTTPClient, HOST)
        l.append(g)

        gevent.sleep(0.005)
    gevent.joinall(l)
    asyncore.loop()