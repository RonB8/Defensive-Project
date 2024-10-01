import socket
from Crypto.PublicKey import RSA
import threading
import data
import warnings
import threading

def handle_client(conn, addr):
    with conn:
        print('Connected by', addr)
    
        data = conn.recv(1024)
        # text = data.decode("utf-8")
        text = data
        print("Received message: " + text)
        print("Enter message ")
        reply = input()
        replydata = bytearray(reply, "utf-8")
        newdata = bytearray(1024)
        for i in range(min(len(replydata), len(newdata))):
            newdata[i] = replydata[i]
        conn.sendall(newdata)

def start_server():
    HOST = ''
    PORT = 1256 #defulte port

    file_name = "port.info"
    file_name = "ss.txt"
    try:
        f = open(file_name, 'r')
        PORT = int(f.read())
        f.close()
    except:
        warnings.warn(f'The \'{file_name}\' file does not exist')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr,))
            client_thread.start()


if __name__ == "__main__":
    start_server()
