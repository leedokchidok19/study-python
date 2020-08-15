from tkinter import * # gui tkinter 사용

root = Tk()
root.title('gui title') # 제목
root.geometry('640x480') # 가로 * 세로

frame = Frame(root)
frame.pack()

# 스크롤바 없는 Listbox
listbox = Listbox(frame, selectmode='extended', height=10)
for i in range(1, 32): # 1 ~ 31 일
    listbox.insert(END, str(i) + '일') # 1일, 2일, ...
listbox.pack()

# 스크롤바 있는 Listbox
scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')
# set 없으면 스크롤 내려도 다시 올라온다
listbox2 = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32): # 1 ~ 31 일
    listbox2.insert(END, str(i) + '일') # 1일, 2일, ...
listbox2.pack(side='left')

scrollbar.config(command=listbox2.yview) # 스크롤바와 listbox2 연결
root.mainloop()