import socket
from Crypto.PublicKey import RSA
import threading
import data




# def func1(n=0):
#     print(22)

# t1 = threading.Thread(target=func1, args=(4,))
# t1.start()
# t1.join()
r1 = data.Request(1,1,1,1,1)
print(r1.REGISTRY)

print("Stam Bdika")
exit(0)


HOST = ''
PORT = 1234



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            text = data.decode("utf-8")
            print("Received message: " + text)
            print("Enter message ")
            reply = input()
            replydata = bytearray(reply, "utf-8")
            newdata = bytearray(1024)
            for i in range(min(len(replydata), len(newdata))):
                newdata[i] = replydata[i]
            conn.sendall(newdata)
