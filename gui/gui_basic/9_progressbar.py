import time
import tkinter.ttk as ttk # gui combobox 사용
from tkinter import * # gui tkinter 사용

root = Tk()
root.title('gui title') # 제목
root.geometry('640x480') # 가로 * 세로

'''
# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate') # 결정되지 않아서 언제 끝날지 모른다
progressbar = ttk.Progressbar(root, maximum=100, mode='determinate')
progressbar.start(10) # 10 ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop()

btn = Button(root, text='중지', command=btncmd)
btn.pack()
'''

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2 )
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1~100
        time.sleep(0.01) # 0.01 초 대기

        # progressbar2.set(i) # 끝난 결과만 보여준다
        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn2 = Button(root, text='시작', command=btncmd2)
btn2.pack()

root.mainloop()