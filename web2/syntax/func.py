'''
a=1
b=2
c=3
s=a+b+c
r=s/3
print(r)
'''

'''
def average():
    a=1
    b=2
    c=3
    s=a+b+c
    r=s/3
    print(r)

average()
'''

'''
#input
def average(a, b, c): # 매개변수 parameter - a, b, c 해당
    s=a+b+c
    r=s/3
    print(r)

average(10, 20, 30) # 인자 argument - 10, 20, 30 해당
'''

#하나의 함수에는 하나의 기능만 가지는게 좋다.
def average(a, b, c): # 매개변수 parameter 
    s=a+b+c
    r=s/3
    return r

print(average(10, 20, 30)) # 인자 argument