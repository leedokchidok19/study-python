from tkinter import * # gui tkinter 사용

root = Tk()
root.title('gui title') # 제목
root.geometry('640x480') # 가로 * 세로
''' 아무런 변화가 없다 이유는 메뉴만 설정하고 메뉴에 대한 값을 설정하지 않았다
menu = Menu(root)

root.config(menu=menu)
root.mainloop()
'''
def create_new_file():
    print('새 파일을 만듭니다.')

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='New File', command=create_new_file)
menu_file.add_command(label='New Window')
menu_file.add_separator() # 구분자
menu_file.add_command(label='Open File...')
menu_file.add_separator() # 구분자
menu_file.add_command(label='Save All', state='disable') # 비활성화
menu_file.add_separator() # 구분자
menu_file.add_command(label='Exit', command=root.quit) # 종료

menu.add_cascade(label='File', menu=menu_file)

# Edit 메뉴 (빈 값)
menu.add_cascade(label='Edit')

# Language 메뉴 (radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='Python')
menu_lang.add_radiobutton(label='Java')
menu_lang.add_radiobutton(label='C++')
menu.add_cascade(label='Language', menu=menu_lang)

# View 메뉴 (checkbutton 버튼을 통해서 여러가지 택)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='Show Minimap')
menu_view.add_checkbutton(label='Show Breadcrumbs')
menu.add_cascade(label='View', menu=menu_view)

root.config(menu=menu)
root.mainloop()