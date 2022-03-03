from socket import *
import argparse
import threading

port = 8082 #접속하고싶은 포트입력 내가 들어가고 싶은 서버로 연결된 포트!!

def handle_receive(client_socket, user):
    while 1:
        try:
            data = client_socket.recv(1024)
        except:
            print("연결 끊김")
            break
        data = data.decode('utf-8')
        if not user in data: #유저이름을 보내주는 데이터와 구분
            print(data) #받은 채팅내용을 출력합니다.

def handle_send(client_socket):
    while 1:
        data = input()
        client_socket.send(data.encode('utf-8'))
        if data == "/종료": #/종료 입력하면 클라이언트 종료
            break

    client_socket.close()

if __name__ == '__main__':
    #프로그램 실행시 옵션으로 포트와 ip주소 유저명을 입력받는다.
    #required-명령행 옵션을 생략할 수 있는지 아닌지
    parser = argparse.ArgumentParser(description="\nMin's client\n-p port\n-i host\n-s string")
    parser.add_argument('-i', help = "host", required=True)
    parser.add_argument('-u', help = "user", required=True)

    args = parser.parse_args()
    host = args.i
    user = str(args.u)

    client_socket = socket(AF_INET, SOCK_STREAM)

    #지정된 host와 port로 서버에 접속
    client_socket.connect((host, port))
    client_socket.send(user.encode('utf-8')) #유저명을 보내준다. 접속유저 리스트생성

    #받는함수를 실행할 스레드 생성
    receive_thread = threading.Thread(target=handle_receive, args=(client_socket, user))
    receive_thread.daemon = True
    receive_thread.start()

    #보내는 함수를 실행할 스레드 생성
    send_thread = threading.Thread(target=handle_send, args=(client_socket,))
    send_thread.daemon = True
    send_thread.start()

    send_thread.join()
    receive_thread.join()

