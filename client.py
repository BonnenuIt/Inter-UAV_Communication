# python3 client.py 运行
import socket
import time

def LongWordsFunc(file_path = 'SentFile.txt'):
    with open(file_path, "r") as file:
        LongWords = ''
        for line in file:
            LongWords = LongWords + line
    return LongWords, len(LongWords)

LongWords, LongWords_len = LongWordsFunc()
LongWords = bytes(LongWords, encoding="utf8")[0:1024]

HOST = '192.168.1.105' # server IP
PORT = 8033 # server Port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
time.sleep(2)

sock.sendall(b'10000') # RepeatTimes
RepeatTimes = int(sock.recv(1024).decode())
print('RepeatTimes = ', RepeatTimes)
print("Connection Succeed")

SendStart = time.time()
for i in range(RepeatTimes):
    sock.sendall(LongWords)
    sock.recv(1024)
    # print(sock.recv(1024).decode())
SendEnd = time.time()
print("Round Trip Time (", RepeatTimes, " times ) = ", SendEnd - SendStart, " second")
print(sock.recv(1024).decode())
sock.close()
