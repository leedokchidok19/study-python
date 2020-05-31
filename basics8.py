# pickle
print("pickle")

import pickle
"""
# 이름.pickle w는 파일입출력과 같다, b는 바이너리를 나타낸다. 인코딩은 필요 없다.
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "언어":["자바", "파이썬", "자바스크립트"]}
print(profile)
pickle.dump(profile, profile_file)    # profile에 있는 정보를 file(profile_file)에 저장
profile_file.close()
"""
# r : read 파일입출력과 같다, b는 바이너리를 나타낸다.
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)    # file(profile_file)에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
