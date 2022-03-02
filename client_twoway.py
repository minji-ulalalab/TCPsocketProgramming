#소켓 통신을 이용한 채팅프로그램 구현(클라이언트측)
#first commit -> 동시대화가 불가능, 서로 대화가 불가능함
#second commit -> 순서상관없이 동시적으로 동작하기 위해 스레드 사용

from socket import *
import threading
import time

#보내는 기능과 받는 기능을 함수로 구분
def send(sock):
    #프로세스가 동작하는 한 스레드가 꺼지지 않게 하기 위해서 while사용
     while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 : ', recvData.decode('utf-8'))


port = 8081

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('접속 완료')

#스레드 생성(target = 실행할함수, args= 전달할인자)
sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

#스레드 실행
sender.start()
receiver.start()

#프로그램이 꺼지지 않도록 설정
while True:
    time.sleep(1)#무한루프를 쉬어가게 하는 용도
    pass