import tkinter as tk
from tkinter import *
from tkinter import messagebox
import qrcode
import os
import time


# QR code 클래스 Bring
my_qrcode = qrcode.Qrcode()
count = 0


# 타이머, 20초 마다 로그인 시도가 없을 경우 MessageBox 자동 실행.
def startTimer():
    time.sleep(1)
    global timer

    timer += 1
    timeText.configure(text=timer)
    window.after(10, startTimer)
    if timer %20 ==0:
        messagebox.showinfo("login", "로그인을 해주세요!!") #메시지 박스를 띄운다.
    elif timer == 301: #5분이 지나면 컴퓨터 자동 종료
        logout()
window = tk.Tk()

timer = 0
timeText = tk.Label(window, text=0, font=("Helvetica", 80))
timeText.pack()
startTimer()
window.mainloop


# System 종료 함수
def logout():
    return os.system('shutdown -l')


# login 함수 정의
def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    
    if uname=='' or pwd=='':
        messagebox.showinfo("login", "아무것도 입력되지 않았습니다!!") #메시지 박스를 띄운다.
        message.set("fill the empty field!!!")
    else:
        if uname=="abcd@gmail.com" and pwd=="abc":
            messagebox.showinfo("로그인 성공", "Email로 로그인이 성공되었습니다!") #메시지 박스를 띄운다.
            exit()
        else:
            global count
            count +=1
            message.set("로그인 실패 횟수 : " + str(count)) # Email 로그인실패 누적
            messagebox.showwarning("Email 로그인 실패", "로그인 실패 횟수 : " + str(count) ) #메시지 박스를 띄운다.
            if count  == 4: 
                message.set("마지막 로그인 기회입니다..")
            elif count == 5:
                messagebox.showerror("Email 로그인 횟수초과", "Email 로그인 횟수초과 되었습니다.\n 컴퓨터를 강제종료 시킵니다.")
                My_NotAccess = qrcode.NotAccess()
                time.sleep(3)
                logout()
    

# UI 실행 클래스
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# UI Start Page        
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,width="1000",height="1000",bg='white').pack(side="top", fill="x", pady=5)
        tk.Label(self, text='Auto Login System',fg='#57a1f8', bg='white',
        font=('Arial', 50, "normal")).place(x=300,y=500)
        tk.Button(self, text="Go To QRCode Access",font=('Arial', 30, "normal"),
                  fg='white', bg='#57a1f8', command=lambda: master.switch_frame(PageTwo)).place(x=1000, y=400)
        tk.Button(self, text="Go To Email Address   ",font=('Arial', 30, "normal"),
                  fg='white', bg='#57a1f8', command=lambda: master.switch_frame(PageOne)).place(x=1000, y=600)

         
# UI First Page (Email Login) 
class PageOne(tk.Frame):
    def __init__(self, master):
        global  message
        global username
        global password
        username = StringVar()
        password = StringVar()
        message=StringVar()
        tk.Frame.__init__(self, master)
        tk.Label(self, width="1000",height="1000",bg='white').pack(side="top", fill="x", pady=5)
        tk.Label(self, text="Username * ", font=('Arial', 30, "normal")).place(x=200,y=400)
        #Username textbox
        tk.Entry(self, textvariable=username,font=('Arial', 30, "normal")).place(x=500,y=400)
        #Password Label
        tk.Label(self, text="Password * ", font=('Arial', 30, "normal")).place(x=200,y=500)
        #Password textbox
        tk.Entry(self, textvariable=password ,font=('Arial', 30, "normal"),show="*").place(x=500,y=500)
        #Label for displaying login status[success/failed]
        tk.Label(self, text="",bg='gray',fg='red',textvariable=message,font=('Arial', 30, "normal")).place(x=500,y=600)
        #Login button
        tk.Button(self, text="Login", font=('Arial', 30, "normal"),width=10, height=1, bg="white",command=login).place(x=1000,y=450)
        tk.Button(self, text="Go back to start page", font=('Arial', 30, "normal"),
                  command=lambda: master.switch_frame(StartPage)).place(x=500,y=700)


# UI Second Page (QR code Login)
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, width="1000",height="1000",bg="white").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page", font=('Arial', 30, "normal"),
                  command=lambda: master.switch_frame(StartPage)).place(x=700,y=500)
        my_qrcode.Qrcode_publisher()


def main():
     #함수 1을 위한 프로세스
    while True:
        app = SampleApp()
        try:
            app.mainloop()
        # 강제 종료를 감지
        except KeyboardInterrupt:
            print("강제적인 종료 감지")
            logout()
        else:
            window.mainloop()
if __name__ == "__main__":
    main()