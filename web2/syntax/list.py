var_list = [1, 'String', 6, 13, 29]
print(var_list)
print(var_list[1]) # 'String'
print(len(var_list)) # 5
var_list[1] = 12 # 'String' - > 12
print(var_list) # [1, 12, 6, 13, 29]

# list 삭제
del var_list[1]
print(var_list) # [1, 6, 13, 29]

# list 추가
var_list.append('append String')
print(var_list) # [1, 6, 13, 29, 'append String']