from tkinter import * # gui tkinter 사용

root = Tk()
root.title('gui title') # 제목
root.geometry('640x480') # 가로 * 세로

chkvar = IntVar() # chkvar 에 Int 형으로 값을 저장한다
chkbox = Checkbutton(root, text='오늘 하루 보지 않기', variable=chkvar) # Variable : check 여부의 값을 저장
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 처리 해제
chkbox.pack()

chkvar2 = IntVar() # chkvar 에 Int 형으로 값을 저장한다
chkbox2 = Checkbutton(root, text='일주일동안 보지 않기', variable=chkvar2) # Variable : check 여부의 값을 저장
chkbox2.pack()

def btncmd():
    # 체크박스(CheckButton) 체크 여부 값 가져오기
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()