from tkinter import *
from datetime import *
from socket import *
import threading
import tkinter
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText

ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
s = socket()

def Login_gui_run():

    root = Tk()
    root.title("聊天室·登录")
    frm = Frame(root)
    root.geometry('300x150')
    nickname = StringVar()

    def login_in():
        name = nickname.get()
        if not name:
            tkinter.messagebox.showwarning('Warning', message='用户名为空！')
        elif len(name)>10:
            tkinter.messagebox.showwarning('Warning', message='用户名过长！最多为十个字符！')
        else:
            root.destroy()
            s.connect(('127.1.1.1', 30000))
            s.send(nickname.get().encode('utf-8'))
            Chat_gui_run()

    Button(root, text = "登录", command = login_in, width = 8, height = 1).place(x=100, y=90, width=100, height=35)
    Label(root, text='请输入昵称', font=('Fangsong',12)).place(x=10, y=20, height=50, width=80)
    Entry(root, textvariable = nickname, font=('Fangsong', 11)).place(x=100, y=30, height=30, width=180)
    root.mainloop()

def Chat_gui_run():
    window = Tk()
    window.maxsize(650, 400)
    window.minsize(650, 400)

    var1 = StringVar()
    user_list = []
    user_list = s.recv(2048).decode('utf-8').split(',')
    user_list.insert(0, '------当前用户列表------')


    nickname = user_list[len(user_list)-1]
    window.title("聊天室--"+nickname)
    var1.set(user_list)
    listbox1 = Listbox(window, listvariable=var1)
    listbox1.place(x=510, y=0, width=140, height=300)
    listbox = ScrolledText(window)
    listbox.place(x=5, y=0, width=500, height=300)

    def read_server(s):
        while True:
            content = s.recv(2048).decode('utf-8')
            curtime = datetime.now().strftime(ISOTIMEFORMAT)
            listbox.insert(tkinter.END, curtime)
            listbox.insert(tkinter.END, '\n'+content+'\n\n')
            listbox.see(tkinter.END)
            listbox.update()


            if content[0:5]=='系统消息：':
                if content[content.find(' ')+1 : content.find(' ')+3]=='进入':
                    user_list.append(content[5:content.find(' ')])
                    var1.set(user_list)
                if content[content.find(' ')+1 : content.find(' ')+3]=='离开':
                    user_list.remove(content[5:content.find(' ')])
                    var1.set(user_list)

    threading.Thread(target = read_server, args = (s,)).start()


    var2 = StringVar()
    var2.set('')
    entryInput = Entry(window, width = 140, textvariable=var2)
    entryInput.place(x=5, y=305, width = 600, height = 95)


    def sendtext():
        line = var2.get()
        s.send(line.encode('utf-8'))
        var2.set('')

    sendButton = Button(window, text = '发 送', font=('Fangsong', 18), bg = 'white', command=sendtext)
    sendButton.place(x=500, y=305, width = 150, height = 95)

    window.mainloop()

Login_gui_run()


