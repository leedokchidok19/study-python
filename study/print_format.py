# print('문자열')
print('hello Python')
print("hello Python")

# print('문자열', '문자열')
print('hello','python')
print("hello","python")

# print('''긴 문장''')
print('''여러 줄을
출력합니다.''')
print("""
따옴표 안에 넣어주세요.
""")

# 숫자, 문자
print('%d월' % 7)
print("%d일" % 2)
print('%s요일' % '목')
print("%s" % '구름IDE')
print('%c단어' % '한')
print("%c" % "일")
print("%d년%d월%d일 입니다." % (2020,7,2))
print("언어 : %s 툴 :%s" % ('파이썬','구름IDE'))
print("%c요일 %c%c" % ('목','공','부'))

# format
print('언어 : {} 툴 : {}'.format('Python', '구름IDE'))
print("툴 : {} 언어 : {}".format("Python", "구름IDE"))
print('언어 : {0} 툴 : {1}'.format('Python', '구름IDE'))
print("툴 : {1} 언어 : {0}".format("Python", "구름IDE"))
print('언어 : {language} 툴 : {tool}'.format(language='Python',tool='구름IDE'))
print("툴 : {tool} 언어 : {language}".format(language="Python", tool="구름IDE"))

# 파이썬 3.6이상
variable = '파이썬 3.6'
print(f'{variable}부터 가능합니다.')
print(f"{variable}부터 가능합니다.")
