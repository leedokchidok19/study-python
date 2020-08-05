from tkinter import * # gui tkinter 사용

root = Tk()
# 제목
root.title('gui title')

btn1 = Button(root, text='버튼1') # Button 만들기 Button(넣을 위치, 버튼 Text)
btn1.pack() # button 보여주기 -pack()을 사용해야 버튼이 보인다
# 버튼 크기 설정
btn2 = Button(root, padx=5, pady=10, text='버튼의 크기가 늘어나면 버튼 크기가 늘어난다')
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text='버튼3')
btn3.pack()

btn4 = Button(root, width=10, height=5, text='버튼의 크기와 상관없이 고정된 크기를 갖는다')
btn4.pack()

# 버튼 색상
btn5 = Button(root, fg='red', bg='yellow', text='fg=text 색상, bg 버튼 배경색')
btn5.pack()

# 버튼 이미지 넣기 - 이미지 경로 오류
# photo = PhotoImage(fiie='gui/buttonImg.png')
# btn6 = Button(root, image=photo)
# btn6.pack()

def btncmd():
    print('버튼이 클릭되었어요!')

# 버튼 이벤트
btn7 = Button(root, text='동작하는 버튼', command=btncmd)
btn7.pack()

root.mainloop()