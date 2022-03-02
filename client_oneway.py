#클라이언트 소켓 세팅
#TCP 소켓 프로그래밍
#클라이언트 & 서버 채팅 프로그램

from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080)) #127.0.0.1은 자기자신을 의미, 자기자신에게 8080번 포트로 연결하라

#send()와 recv()로 데이터 주고받기
#서버와 클라이언트가 서로 한번씩 문자열 데이터를 주고받기
print('연결확인했습니다.')
clientSock.send('I am a client'.encode('utf-8'))

print('메세지를 전송했습니다')


data = clientSock.recv(1024)
print('받은 데이터: ', data.decode('utf-8'))
