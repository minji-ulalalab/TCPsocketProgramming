#멀티 클라이언트 채팅 프로그램
from socket import *
import argparse #어떤 옵션에 따라서 파이썬 스크립트가 다르게 동작하도록 함(명령행을 통해 인자를 받음)
import threading
import time

host = "127.0.0.1"
port = 8082 #1-65535사이 숫자 가능
user_list = {} #dictionary("키":"값")

def msg_func(msg):
    print(msg)
    for con in user_list.values(): #딕셔너리의 모든 값들(유저당 반환된 소켓)
        try:
            con.send(msg.encode('utf-8'))
        except:
            print("연결이 비 정상적으로 종료된 소켓 발견")

def handle_receive(client_socket, addr, user):
    msg = "----%s님이 들어오셨습니다.----"%user
    msg_func(msg) #유저 접속문구를 msg로 msg함수에 전달해서 출력
    while 1:
        data = client_socket.recv(1024) #입력받은 채팅내용
        string = data.decode('utf-8')
        
        if "\종료" in string: #종료될때 일어나는 일
            msg = "----%s님이 나가셨습니다.----"&user
            del user_list[user] #유저목록에서 나간사람 지우기
            msg_func(msg)
            break
        string = "%s : %s"%(user, string) #유저이름과 내용을 모아서 쏴줌
        msg_func(string)
    client_socket.close() #종료클라이언트닫기

def accept_func(): #소켓생성, receive스레드 실행
    #IPv4체계, TCP타입 소켓 객체생성
    server_socket = socket(AF_INET, SOCK_STREAM)
    #setsockopt-소켓 송수신동작의 옵션제어
    #SOL_SOCKET-setsockopt() 함수의 level
    #SO_REUSEADDR-서버와 클라이언트가 연결된 상태에서 서버를 강제종료시키는 경우 서버를 재 시동했을때 발생하는 에러를 방지하기 위함(Time-wait상태에서 생기는 에러)
    #Time-wait상태에 있는 소켓의 port번호에 할당이 가능하게 해준다.(0 ->1 로 바꿔주면)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((host, port)) #'host=127.0.0.1', "port=8082"

    server_socket.listen(5)

    while 1:
        try:
            #클라이언트 함수가 접속하면 새로운 소켓을 반환한다. 그때까지 대기.
            print('%d번 포트로 접속 대기중...'%port)
            client_socket, addr = server_socket.accept()
            

        except KeyboardInterrupt: #Ctrl+C
            for user, con in user_list:
                con.close() 
            server_socket.close()
            print("Keyboard interrupt")
            break

        #접속한 유저 이름과 소켓 정보 받기
        user = client_socket.recv(1024).decode('utf-8')
        user_list[user] = client_socket

        receive_thread = threading.Thread(target=handle_receive, args=(client_socket, addr, user))#소켓정보, 주소, 유저이름
        receive_thread.daemon = True
        receive_thread.start()

if __name__=='__main__':
    #description - 인자 도움말 전에 표시할 텍스트(기본값:none)
    #help - 인자가 하는 일에 대한 간단한 설명
    parser = argparse.ArgumentParser(description="\nMin's server\n-p port\n") #ArgumentParser 객체생성
    parser.add_argument('-p', help="port") #help=디스크립션

    args = parser.parse_args() #인수를 분석
    try:
        port = int(args.p) #명령어 실행시 입력한 인자값을 받는다.
    except:
        pass
    #포트 여는 것부터 유저 받는 스레드 실행하는 것 까지하는 함수 실행
    accept_func()

    
