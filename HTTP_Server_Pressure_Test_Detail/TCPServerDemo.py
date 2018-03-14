import asyncore
import socket

class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8192)
        # print repr(data)
        if data and data!= '':
            self.send(data)
            print "Server: recv:", data, "\n", "-" * 50

class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr), '\n'
            handler = EchoHandler(sock)

#define	__DARWIN_FD_SETSIZE	1024
server = EchoServer("0.0.0.0", 8000)
print "\ncreate server on port 8000", "\n", "-" * 50
asyncore.loop()

