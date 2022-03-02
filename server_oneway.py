#서버 소켓 세팅

from socket import *

#소켓 객체생성, 인자로 1.어드레스패밀리(AF)와 2.소켓타입 필요
#어드레스패밀리는 주소체계에 해당
serverSock = socket(AF_INET, SOCK_STREAM)
#생성한 소켓을 bind 해줘야 한다(서버 운용시 반드시 필요)
#생성된 소켓의 번호와 실제 어드레스패밀리를 연결
#bind 함수 내에 튜플로 입력!
#(ip, port)튜플 = 어드레스 패밀리
#AF_INET에서 '' = INADDR_ANY = 모든인터페이스와 연결
serverSock.bind(('', 8080))#8080번 포트에서 모든 인터페이스에게 연결하도록 한다
#상대방의 접속을 기다리는 단계
#(1)은 해당 소켓이 몇개의 동시접속을 허용할 것인지 정함
serverSock.listen(1)#한개의 접속만을 허용하겠다
#accept()는 소켓에 누군가가 접속하여 연결하였을때 비로소 결과값이 return되는 함수
#상대방이 접속함으로써 a
connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속이 확인되었습니다.')

data = connectionSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

connectionSock.send('I am a server.'.encode('utf-8'))
print('메세지를 보냈습니다.')