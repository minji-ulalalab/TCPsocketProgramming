#소켓 통신을 이용한 채팅프로그램 구현(서버측)
#first commit -> 동시대화가 불가능, 서로 대화가 불가능함
#second commit -> 순서상관없이 동시적으로 동작하기 위해 스레드 사용

from socket import *
import threading
import time

#보내는 기능과 받는 기능을 함수로 구분
#데이터 소켓을 인자로 받음

#보내는함수
def send(sock):
    while True:
        #프로세스가 동작하는 한 스레드가 꺼지지 않게 하기 위해서 while사용
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

#받는함수  
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 : ', recvData.decode('utf-8'))
        

        

if __name__ == "__main__":
    port = 8081

    serverSock = socket(AF_INET, SOCK_STREAM)#AF_INEF -> IP4v, SOCK_STREAM -> TCP 
    serverSock.bind(('', port))
    serverSock.listen(1)

    print('%d번 포트로 접속 대기중...'%port)

    #client에서 접속할때까지 대기
    connectionSock, addr = serverSock.accept()#새로운소켓, 상대방의 AF

    #client에서 접속하면 접속한 주소 출력 되면서 연결
    print(str(addr), '에서 접속되었습니다.')

    #스레드 생성(target = 실행할함수, args= 전달할인자)
    sender = threading.Thread(target=send, args=(connectionSock,))
    receiver = threading.Thread(target=receive, args=(connectionSock,))

    #스레드 실행
    sender.start()
    receiver.start()

    #sender.join()
    #receiver.join()

    #while True:
    #    time.sleep(1)
    #    pass
