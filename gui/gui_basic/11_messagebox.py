import tkinter.messagebox as msgbox
from tkinter import * # gui tkinter 사용
# messagebox - 에러 발생시 나오는 박스
root = Tk()
root.title('gui title') # 제목
root.geometry('640x480') # 가로 * 세로

def info():
    msgbox.showinfo('알림', '정상적으로 예매 완료되었습니다') # showinfo(title, content)

def warn():
    msgbox.showwarning('경고', '해당 좌석은 매진되었습니다')

def error():
    msgbox.showerror('에러', '결제 오류가 발생했습니다')

def okcancel():
    msgbox.askokcancel('확인 / 취소', '예매 하시겠습니까?')

def retrycancel():
    response = msgbox.askretrycancel('재시도 / 취소', '다시 시도하시겠습니까?')
    print('응답 : ', response) # True, False, None -> 예 1, 아니오 0, 그 외
    if response == 1: # 재시도
        print('재시도')
    elif response == 0: # 취소
        print('취소')

def yesno():
    msgbox.askyesno('예 / 아니오', '예매 하시겠습니까?')

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message='예매 하시겠습니까?') # 제목 삭제
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print('응답 : ', response) # True, False, None -> 예 1, 아니오 0, 그 외
    if response == 1: # 네, ok
        print('예')
    elif response == 0: # 아니오
        print('아니오')
    else: # 취소
        print('취소')

Button(root, text='알림', command=info).pack()
Button(root, text='경고', command=warn).pack()
Button(root, text='에러', command=error).pack()

Button(root, text='확인 취소', command=okcancel).pack()
Button(root, text='재시도 취소', command=retrycancel).pack()
Button(root, text='예 아니오', command=yesno).pack()
Button(root, text='예 아니오 취소', command=yesnocancel).pack()

root.mainloop()