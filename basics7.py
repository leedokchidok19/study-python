# 파일 입출력
print("파일 입출력")
"""
# open("파일이름.확장자", "w" 쓰기 목적, 인코딩)
score_file = open("score_file.txt", "w", encoding="utf-8")    # w : 파일이 기존에 있다면 덥어쓰기가 된다.
print("수학 : 0", file=score_file)
print("영아 : 50", file=score_file)
# 항상 닫아줘야 한다.
score_file.close()
"""
"""
# a : append 수정
score_file = open("score_file.txt", "a", encoding="utf-8")
score_file.write("과학 : 80")        # print와 달리 줄바꿈 기능이 없다.
score_file.write("\n코딩 : 100")
score_file.close()
"""
"""
# r : read 읽기
score_file = open("score_file.txt", "r", encoding="utf-8")
print(score_file.read())
score_file.close()
"""
"""
# 한 줄씩 읽어오기
score_file = open("score_file.txt", "r", encoding="utf-8")
print(score_file.readline(), end="")    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동한다.
print(score_file.readline(), end="")    # readline이 줄바꿈도 해준다.
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
"""
# 총 몇줄인지 모를 때 전부 읽어오는 방법
# 방법 1 : while
score_file = open("score_file.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# 방법 2 : for
score_file = open("score_file.txt", "r", encoding="utf-8")
lines = score_file.readlines()    # readlines로 모두 불러오고 lines에 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()






