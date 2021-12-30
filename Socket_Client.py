import socket
import time
import threading


class scktclnt():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 1234

    def __init__(self):
        pass

    def sckt(self):

        try:
            self.s = socket.socket()
            print(self.host, self.ip)
            time.sleep(1)
        except:
            print('unable to create a socket')

    def scktcnct(self):
        try:
            print("Trying to connect to ", self.host, self.port)
            self.s.connect((self.host, self.port))
        except:
            print("Waiting for server availability")
            time.sleep(10)
            try:
                self.s.connect((self.host, self.port))
                print("Connected to...", self.host, self.port)
            except:
                print('socket connection error')

    def send(self):
        try:
            message = input("Client: ")
            self.s.send(message.encode('utf-8'))
        except:
            print("Server is not available to receive msg")

    def receive(self):

        while True:
            try:
                mesg = self.s.recv(1024).decode('utf-8')
                print('\n'"server:{}".format(mesg))
            except:
                print("Server not available to receive msg")
                break


c = scktclnt()
c.sckt()
c.scktcnct()
recv_msg = threading.Thread(target=c.receive)
recv_msg.start()
while True:
    c.send()









