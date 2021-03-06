from socket import *
import argparse
import threading

port = 8082

def handle_receive(client_socket, user):
    while 1:
        try:
            data = client_socket.recv(1024)
        except:
            print("연결 끊김")
            break
        data = data.decode('utf-8')
        if not user in data: 
            print(data)

def handle_send(client_socket):
    while 1:
        data = input('>>>')
        client_socket.send(data.encode('utf-8'))
        if data == "/종료": 
            break

    client_socket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="\nMin's client\n-p port\n-i host\n-s string")
    parser.add_argument('-i', help = "host", required=True)
    parser.add_argument('-u', help = "user", required=True)

    args = parser.parse_args()
    host = args.i
    user = str(args.u)

    client_socket = socket(AF_INET, SOCK_STREAM)

    
    client_socket.connect((host, port))
    client_socket.send(user.encode('utf-8')) 

    receive_thread = threading.Thread(target=handle_receive, args=(client_socket, user))
    receive_thread.daemon = True
    receive_thread.start()

    send_thread = threading.Thread(target=handle_send, args=(client_socket,))
    send_thread.daemon = True
    send_thread.start()

    send_thread.join()
    receive_thread.join()