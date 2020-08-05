from tkinter import * # gui tkinter 사용

root = Tk()
root.title('gui title') # 제목
root.geometry('640x480') # 가로 * 세로

def btncmd():
    pass

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()