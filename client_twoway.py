#소켓 통신을 이용한 채팅프로그램 구현(클라이언트측)


from socket import *

port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('접속 완료')

#프로그램을 강제종료하지 않으면 계속 실행되게 함
#먼저 받은다음에 상대방에게 송신

while True:
    #채팅올때까지 대기, 채팅오면 출력
    recvData = clientSock.recv(1024)
    print('상대방 : ', recvData.decode('utf-8'))

    #답변 입력
    sendData = input('>>>')
    clientSock.send(sendData.encode('utf-8'))
