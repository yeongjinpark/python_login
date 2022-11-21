from cv2 import log
import keyboard
import mouse
import time
# 키보드 , 마우스 인식함수 5분 안에 인식되면 초기화 되는 구조
k=0
while True:
    print(k)
    k+=1
    time.sleep(0.1)
    if keyboard.is_pressed('space'):
        k=0
        print('키보드 입력 감지')
        time.sleep(0.1)
    elif keyboard.is_pressed('backspace'):
        k=0
        print('키보드 입력 감지')
        time.sleep(0.1)
    elif keyboard.is_pressed('shift'):
        k=0
        print('키보드 입력 감지')     
        time.sleep(0.1)
    elif keyboard.is_pressed('enter'):
        k=0
        print('키보드 입력 감지')
        time.sleep(0.1)
    elif keyboard.is_pressed('ctrl'):
        k=0
        print('키보드 입력 감지')
        time.sleep(0.1)
    elif mouse.is_pressed('left'):
        k=0
        print('마우스 입력 감지')
        time.sleep(0.1)
    elif mouse.is_pressed('right'):
        k=0
        print('마우스 입력 감지')
        time.sleep(0.1)
    elif k==300: # 약 5분 뒤 로그인 화면 전환용
        break


                
        
        

    


