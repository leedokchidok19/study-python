from tkinter import * # gui tkinter 사용

root = Tk()
root.title('gui title') # 제목
root.geometry('640x480') # 가로 * 세로

# Listbox - 여러가지 목록을 관리하는 위젯
listbox = Listbox(root, selectmode='extended', height=0) # selectmode='extended' 한개 또는 여러개 선택 가능, selectmode='single' 한개만 선택 가능
listbox.insert(0, '서과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박') # END 사용하면 가장 마지막 줄에 추가
listbox.insert(END, '포도')
listbox.pack()

listbox = Listbox(root, selectmode='single', height=0) # selectmode='single' 한개만 선택 가능
listbox.insert(0, '서과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박') # END 사용하면 가장 마지막 줄에 추가
listbox.insert(END, '포도')
listbox.pack()

listbox = Listbox(root, selectmode='extended', height=3) # height=0 목록 전부를 보여준다 0 이상의 숫자는 숫자만큼의 목록을 보여주고 목록을 내려야 보인다
listbox.insert(0, '서과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박') # END 사용하면 가장 마지막 줄에 추가
listbox.insert(END, '포도')
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END) # 맨 뒤에 항목 삭제
    # listbox.delete(0) # 맨 앞 항목 삭제

    # 갯수 확인
    print('리스트에는', listbox.size(), '개가 있어요')

    # 항목 확인 (시작 idx, 끝 idx)
    print('1번째부터 3번째까지의 항목 : ', listbox.get(0, 2)) # 0번재 부터 2번째까지 총 3개
    # 출력 결과 : 1번째부터 3번째까지의 항목 :  ('서과', '딸기', '바나나')

    # 선택된 항목 확인
    print('선택된 항목 : ', listbox.curselection()) # 선택한 항목의 idx로 반환한다
    # 사과, 딸기, 바나나 선택 -> 선택된 항목 :  (0, 1, 2)

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()