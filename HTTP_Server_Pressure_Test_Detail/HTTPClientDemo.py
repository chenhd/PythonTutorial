import socket
import time

HOST = '10.20.98.32'    # The remote host
PORT = 8000              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

send_data = '''\
GET / HTTP/1.1
Host: 0.0.0.0:8000
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8

'''

send_data = send_data.replace("\n", "\r\n")

s.sendall(send_data)
time.sleep(1)
data = s.recv(10240)

s.close()

print 'Client: Received:'
print data