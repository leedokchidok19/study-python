import tkinter.ttk as ttk # gui combobox 사용
from tkinter import * # gui tkinter 사용

root = Tk()
root.title('gui title') # 제목
root.geometry('640x480') # 가로 * 세로

values = [str(i) + '일' for i in range(1, 32)] # 1~31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values) # height :보여지는 목록 수
combobox.pack()
combobox.set('카드 결제일') # 최초 목록 제목 설정 및 버튼 클릭을 통한 값도 설정 가능

readonly_combobox = ttk.Combobox(root, height=10, values=values, state='readonly') # 읽기 전용 - state='readonly'
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get()) # 선택된 값 표시

btn = Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop()