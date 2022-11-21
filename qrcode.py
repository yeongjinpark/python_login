import cv2
import pyzbar.pyzbar as pyzbar
from tkinter import messagebox
import requests
import time

used_codes = []
data_list = []


# QR코드 실행 클래스
class Qrcode:
    def __init__(self, Qrcode_publisher=False):
        print("QRcode 실행")
        
    def Qrcode_publisher(self):
        try:
            # 텍스트 파일의 qrcode 데이터 읽기
            f = open("qrbarcode.txt", "r", encoding="utf8")
            data_list = f.readlines()
        except FileNotFoundError:
            pass
        else:
            f.close()
        # 카메라 실행
        cap = cv2.VideoCapture(0)

        for i in data_list:
            used_codes.append(i.rstrip('\n'))
        k=0
        while True:
            print(k)
            k+=1
            time.sleep(0.1)
            if k==300: #QR Scan until 30s
                print("You Do Not Access Code!!")
                My_NotAccess = NotAccess()
                break
            success, frame = cap.read()
            for code in pyzbar.decode(frame):
                my_code = code.data.decode('utf-8')
                if my_code in used_codes: # QR인식 성공
                    print("인식 성공 : ", my_code)
                    messagebox.showinfo("QRCODE Login SUCCESS", "QR코드 로그인 성공했습니다.") #메시지 박스를 띄운다.
                    exit()
                else: # QR인식을 실패하는 경우
                    print("Not Identified Code!!!")
                    My_NotAccess = NotAccess()
                    time.sleep(1.0)
            #카메라 이미지 띄우기
            cv2.imshow('QRcode Barcode Scan', frame)
            cv2.waitKey(1)


# Line Notify를 실행하기 위한 함수
def NotAccess():
        try:
            TARGET_URL = 'https://notify-api.line.me/api/notify'
            TOKEN = 'C6vDaFbPof61WQoeR1QIlbxJvlunHmysq0RAhLIwxsV'	# 발급받은 토큰
            headers={'Authorization': 'Bearer ' + TOKEN}
            data={'message': 'Person NOT Access Qrcode!!'}
            response = requests.post(TARGET_URL, headers=headers, data=data)
        except Exception as ex:
            print(ex)






