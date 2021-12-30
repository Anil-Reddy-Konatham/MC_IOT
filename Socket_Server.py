import threading
import socket


class scktsrvr():

    def __init__(self):
        pass

    def sckt(self):
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)
        self.port = 1234

        try:
            self.s = socket.socket()
            self.s.bind((self.host, self.port))
            print(self.host, self.ip)
            self.s.listen(1)
            print("Waiting for incoming connections...")

        except:
            print('unable to create a socket')

    def scktcnct(self):
        try:
            self.conn, self.addr = self.s.accept()
            print ("Received connection from ", self.addr)
        except:
            print('socket connection error')

    def send(self):
        try:
            message = input("server: ")
            self.conn.send(message.encode('utf-8'))
        except:
            print('unable to send message')

    def receive(self):
        while True:
            try:
                mesg = self.conn.recv(1024).decode('utf-8')
                print('\n'"Client:{}".format(mesg))
            except:
                print("Client Disconnected")
                break


s = scktsrvr()
s.sckt()
s.scktcnct()

rec_msg = threading.Thread(target=s.receive)
rec_msg.start()
while True:
    s.send()






