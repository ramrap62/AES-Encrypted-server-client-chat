import socket
import pyaes
import os


key_192 = os.urandom(24)

def conn():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)
    port = 56568
    address = (ip,port)
    s.bind(address)
    s.listen(1)
    print("Started Listening on ", ip, ':', port)
    client,addr = s.accept()
    print("Got a connection from", addr[0], ':', addr[1])

    client.send(key_192)
    key_192r = client.recv(1024)
    enaes = pyaes.AESModeOfOperationOFB(key_192)
    deaes = pyaes.AESModeOfOperationOFB(key_192r)

    while True:
        msg = input("Text :")
        enmsg = enaes.encrypt(msg)
        print('encrypted :',enmsg)


        if "bye" in msg:
            print("Connection ended")
            client.send(enmsg)
            client.close()
            break

        else:
            client.send(enmsg)
            enrec = client.recv(1024)
            print('encrypted :',enrec)
            derec = deaes.decrypt(enrec).decode('utf-8')
            print("Alice :",derec)

            if "bye" in derec:
                print("Connection ended")
                client.close()
                break



def main():

    conn()

main()
