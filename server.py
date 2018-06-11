import socket
from time import sleep
root_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

root_sock.bind(('127.0.0.1',7001))
root_sock.listen(5)
point_sock ,addr= root_sock.accept()

point_sock.send(b'Welcome')

s_input = input('>')
while s_input!='exit':
    point_sock.send(s_input.encode())
    s_input = input('>')

point_sock.close()
root_sock.close()