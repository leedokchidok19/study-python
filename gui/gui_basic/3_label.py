from tkinter import * # gui tkinter 사용

root = Tk()
# 제목
root.title('gui title')
root.geometry('640x480')

# label : 글자 혹은 이미지만 보여준다 - button(X)
label1 = Label(root, text='안녕하세요') # Label 만들기 Label(넣을 위치, 레이블(Label) Text)
label1.pack() # Label 보여주기 -pack()을 사용해야 레이블(Label) 보인다

# Label 이미지 넣기 - 이미지 경로 오류
# photo = PhotoImage(fiie='gui/buttonImg.png')
# label2 = Label(root, image=photo)
# label2.pack()

def change():
    label1.config(text='또 만나요')

    # global photo2 # global(전역 변수) 설정을 안 하면 함수가 실행된 후 메모리에서 삭제된다 - global 없으면 이미지 안 나온다
    # photo2 = PhotoImage(fiie='gui/buttonImg2.png')
    # label2.config(image=photo)

btn = Button(root, text='클릭', command=change)
btn.pack()

root.mainloop()