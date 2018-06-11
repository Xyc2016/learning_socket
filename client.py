import socket


point_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
point_sock.connect(('127.0.0.1',7001))
while True:
    s=point_sock.recv(1024).decode()
    print(s)
    if s=='':
        break

point_sock.close()