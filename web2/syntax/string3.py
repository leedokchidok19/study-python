# 문자열 포맷팅
name = 'variable'
number = 2020
# positional formating
print('''
문자열 포맷팅중 포지셔널 포맷팅하는 방법
변수를 {} 위치에 넣어 준다. 순서대로 {}
'''.format(name, number))

# named placeholder
number = '문자열이 가능합니다.'
print("""
문자열 포맷팅중 네임 포맷팅하는 방법
변수를 {var_name} 위치에 넣어 준다. 순서대로 {var_number}
var_number에 문자열이 들어올 수 있다.
""".format(var_name=name, var_number=number))

# named placeholder
number = 2000
print("""
문자열 포맷팅중 네임 포맷팅하는 방법
변수를 {var_name} 위치에 넣어 준다. 순서대로 {var_number:d}
:d -> digit의 약자 number타입만 가능하다.
문자열이 들어오면 아래와 같은 에러가 발생한다.
ValueError: Unknown format code 'd' for object of type 'str'
""".format(var_name=name, var_number=number))