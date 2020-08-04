from tkinter import * # gui tkinter 사용

root = Tk()
#제목
root.title('gui title')
root.geometry('640x480') # 가로 * 세로

# text 위젯 설정 - input type='text' 느낌
txt = Text(root, width=30, height=5) # Text 만들기 Text(넣을 위치, 너비, 높이)
txt.pack()# Text 보여주기 -pack()을 사용해야 Text 보인다

# text 위젯 안에 글자를 미리 넣어주는 기능 - input placeholder 느낌
txt.insert(END, '글자를 입력하세요')

# text와 다른점은 Enter 없이 한줄로 입력하는 기능 - 아이디/비밀번호 입력 등을 할 경우 사용
e = Entry(root, width=30)
e.pack()
e.insert(0, '한줄만 입력해요') # 현재는 값이 비어 있으므로 END 를 써도 동일합니다

def btncmd():
    # 내용 출력
    print(txt.get('1.0', END)) # Text 값 가져올 때 get 쓰면 된다 - '1.0' 처음부터 끝까지 가져온다는 뜻
    print(e.get()) # Entry 값 가져오기
    # '1.0' -> 1 : 첫번째 라인 위치, 0 : 0번째 column 위치

    # 내용 삭제
    txt.delete('1.0', END)
    e.delete(0, END)

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()