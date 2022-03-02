#소켓 통신을 이용한 채팅프로그램 구현(서버측)

from socket import *

port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

#프로그램을 강제종료하지 않으면 계속 실행되게 함
#보낸 후에 상대방으로부터 수신을 기다림
while True:
    sendData = input('>>>')
    connectionSock.send(sendData.encode('utf-8'))

    recvData = connectionSock.recv(1024)
    print('상대방:', recvData.decode('utf-8'))