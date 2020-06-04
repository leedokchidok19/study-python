# with
"""
import pickle

# 파일입출력, pickle과 같은 기능을 좀 더 편하게 사용할 수 있게한다.
# with open("파일이름.pickle", "권한") as 담을 변수명
# profile_file.close()를 할 필요 없이 with에서 처리 해준다.
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
"""
"""
# with 파일입출력 - 생성
with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 공부하고 있습니다.")
"""
# with 파일입출력 - 읽기
with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())
