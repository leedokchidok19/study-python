from tkinter import * # gui tkinter 사용

root = Tk()
root.title('gui title') # 제목
root.geometry('640x480') # 가로 * 세로

Label(root, text='메뉴를 선택해 주세요.').pack(side='top')
Button(root, text='주문하기.').pack(side='bottom')

# 햄버거 프에임
frame_burger = Frame(root, relief = 'solid', bd=1) # relief 외곽선, bd 표시
frame_burger.pack(side='left', fill='both', expand= True) # side='lefr' 왼쪽에 위치, fill='both' 크기를 꽉 채운다

Button(frame_burger, text='햄버거').pack()
Button(frame_burger, text='치즈버거').pack()
Button(frame_burger, text='치킨버거').pack()

# 음료 프레임 - 제목이 있는 프레임
frame_drink = LabelFrame(root, text='음료')
frame_drink.pack(side='right', fill='both', expand= True)

Button(frame_drink, text='콜라').pack()
Button(frame_drink, text='사이다').pack()

root.mainloop()