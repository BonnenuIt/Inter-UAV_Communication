# python3 server.py 运行
import socket
import time

HOST = '192.168.1.105' # server IP
PORT = 8033 # server Port (non-privileged ports are > 1023)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET for IPv4   SOCK_STREAM socket type for TCP
sock.bind((HOST, PORT))
sock.listen(5) # 侦听socket
print(HOST, 'is listening.')
ListenStart = time.time()

connection, address = sock.accept() # 等待客户端连接
try:
    connection.settimeout(10)
    buf = connection.recv(1024)
    connection.sendall(buf)
    RepeatTimes = int(buf.decode())
    print('RepeatTimes = ', RepeatTimes)
    
    for i in range(RepeatTimes):
        buf = connection.recv(1024)
        connection.sendall(buf)
        # print(buf.decode())
    time.sleep(2)

    connection.send(b'Welcome to server!')
    print('Connection success!')
except socket.timeout:
    print('time out')
connection.close()
