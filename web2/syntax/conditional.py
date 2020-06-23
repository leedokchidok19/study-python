# if문
user_id = input('id? ')
user_password = input('password? ')

'''
if user_password == '1234':
    print('환영합니다.')
else:
    print('비밀번호 확인')
'''
if user_id.lower() == 'python': # string.lower() 대소문자 상관없이 소문자로 만들어준다.

    if user_password == '1234':
        print('환영합니다.')
    else:
        print('비밀번호 확인')

else:
    print('아이디 확인')
