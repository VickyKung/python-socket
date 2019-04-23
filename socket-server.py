import socket
import  random
sk=socket.socket()
ip_port=("127.0.0.1",8888)
sk.bind(ip_port)
sk.listen(5)
while True:
    conn,address=sk.accept()
    print("正在等待连接.....")
    msg="连接成功！"
    conn.send(msg.encode())
    while True:
        data=conn.recv(1024)
        print(data.decode())
        if data == b'exit':
            break
        else:
            conn.send(data)
            conn.send(str(random.randint(1,1000)).encode())

    conn.close()