import socket

sk=socket.socket()
ip_port=("127.0.0.1",8888)
sk.connect(ip_port)

while True:
    data = sk.recv(1024)
    print(data.decode())
    msg = input("请输入信息：")
    sk.send(msg.encode())
    if msg == "exit":
        break
    data = sk.recv(1024)
    print(data.decode())

