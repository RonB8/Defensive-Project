import socket
# from Crypto.PublicKey import RSA
import threading
from data import *
from message import *
import warnings
import threading

users_list = Users()


def handle_client(conn, addr):
    with conn:
        print('Connected by', addr)

        packet = conn.recv(1024)
        # text = data.decode("utf-8")
        print(list(packet))
        req = Request(packet)
        print(req.client_ID)
        print(req.version)
        print(req.code)
        print(req.payload_size)
        print(req.payload)
        exit(0)

        payload = Payload(req.payload, req.code)

        if req.code == REGISTRY:
            id = users_list.register(payload.name())
            if id is None:
                conn.sendall('Error!\nThe user name already exist.')




        print("Enter message ")
        reply = input()
        replydata = bytearray(reply, "utf-8")
        newdata = bytearray(1024)
        for i in range(min(len(replydata), len(newdata))):
            newdata[i] = replydata[i]
        conn.sendall(newdata)


def start_server():
    HOST = ''
    PORT = 1256  # defulte port

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

    payload = [0x0]*16

    resp = Response(3, FAILED_REGISTRATION, 4, payload)
    print(list(resp.packet))
    exit(0)

    start_server()
