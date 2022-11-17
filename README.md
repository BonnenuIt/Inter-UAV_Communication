# Inter-UAV_Communication
Raspberry Pis

## Setup

1. 连接电池
2. ？
3. `client.py` 和 `SentFile.txt` 都放到`client`机上去。`SentFile.txt`是每一次发送的文件，大小1kB。 由于`socket.sendall()`和`socket.recv()`函数容易截断不读缓冲区数据，每次只收发1kB的数据。5000次收发即5000kB数据。`SentFile.py`用于从`共产党宣言`中截取数据到`SentFile.txt`中。
4. `server.py` 放到`server`机上去。
5. 注意server IP和端口号的一致性。

## Result
Round Trip Time ( 5000  times ) =  11.896782875061035  second
Round Trip Time ( 5000  times ) =  13.502812385559082  second
Round Trip Time ( 5000  times ) =  12.280096530914307  second
Round Trip Time ( 10000  times ) =  28.968437671661377  second
Round Trip Time ( 10000  times ) =  23.09668803215027  second
Round Trip Time ( 10000  times ) =  24.112331867218018  second
总速率为收发来回的平均，800kB左右
