from socket import *
from sqlite3 import connect
import threading
from datetime import *

ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'

IP = '127.1.1.1'
PORT = 30000

user_list = []
socket_list = []

try:
    with open('serverlog.txt', 'a+') as serverlog:
        curtime = datetime.now().strftime(ISOTIMEFORMAT)
        serverlog.write('\n\n-----------服务器打开时间：' + str(curtime) + '，开始记录聊天-----------\n')
except:
    print('ERROR!')

s = socket()
s.bind((IP, PORT))
s.listen()


def read_client(s, nickname):
    try:
        return s.recv(2048).decode('utf-8')
    except:
        curtime = datetime.now().strftime(ISOTIMEFORMAT)
        print(curtime)
        print(nickname + ' 离开了聊天室!')
        with open('serverlog.txt', 'a+') as serverlog:
            serverlog.write(str(curtime) + '  ' + nickname + ' 离开了聊天室!\n')
        socket_list.remove(s)
        user_list.remove(nickname)
        for client in socket_list:
            client.send(('系统消息：' + nickname + ' 离开了聊天室!').encode('utf-8'))



def socket_target(s, nickname):
    try:
        s.send((','.join(user_list)).encode('utf-8'))
        while True:
            content = read_client(s, nickname)
            if content is None:
                break
            else:
                curtime = datetime.now().strftime(ISOTIMEFORMAT)
                print(curtime)
                print(nickname + '说：' + content)
                with open('serverlog.txt', 'a+') as serverlog:
                    serverlog.write(str(curtime) + '  ' + nickname + '说：' + content + '\n')
                for client in socket_list:
                    client.send((nickname + '说:' + content).encode('utf-8'))
    except:
        print('Error!')


while True:
    conn, addr = s.accept()
    socket_list.append(conn)
    nickname = conn.recv(2048).decode('utf-8')

    if nickname in user_list:
        i = 1
        while True:
            if nickname + str(i) in user_list:
                i = i + 1
            else:
                nickname = nickname + str(i)
                break

    user_list.append(nickname)
    curtime = datetime.now().strftime(ISOTIMEFORMAT)
    print(curtime)
    print(nickname + ' 进入了聊天室!')

    with open('serverlog.txt', 'a+') as serverlog:
        serverlog.write(str(curtime) + '  ' + nickname + ' 进入了聊天室!\n')

    for client in socket_list[0:len(socket_list) - 1]:
        client.send(('系统消息：' + nickname + ' 进入了聊天室！').encode('utf-8'))


    threading.Thread(target=socket_target, args=(conn, nickname,)).start()