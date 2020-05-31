"""
import package.thailand # .뒤에는 모듈 or 패키지만 가능하다. class, def는 사용 불가
# import package.thailand.ThailandPackage    # ModuleNotFoundError: No module named 'package.thailand.ThailandPackage'; 'package.thailand' is not a package
trip_to = package.thailand.ThailandPackage()
trip_to.detail()
"""
'''
from package.thailand import ThailandPackage # 모듈, 패키지, 클래스, 함수 가능하다.
trip_to = ThailandPackage()
trip_to.detail()
'''
"""
from package import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
"""

from package import * # 패키지 *로 패키지 아래 파일들을 가져올 것 같지만 에러 발생 NameError: name 'vietnam' is not defined
# 사용 방법 __init__에 파일들의 공개범위 설정
#trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 모듈, 패키지 위치 확인
import inspect
import random
print(inspect.getfile(random))    # /usr/local/lib/python3.7/random.py
print(inspect.getfile(thailand))  # /workspace/studyPython/module/package/thailand.py

# pip install
# pypi 검색, https://pypi.org/ 사이트에서 검색 해서 사용
# pip list <- 현재 설치된 목록
# pip show 패키지이름 <- 설치된 패키지 정보를 보여준다.
# pip install --upgrade 패키지이름 <- 설치된 패키지 업데이트
# pip uninstall 패키지이름 <- 설치된 패키지 삭제

# 내장 함수
# input : 사용자 입력을 받는 함수
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
print(dir())
print(dir(random))

# list of python builtins // https://docs.python.org/ko/3/library/functions.html

# 외장 함수 : 직접 import해서 사용
# list of python modules // https://docs.python.org/ko/3/py-modindex.html
# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())    # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):    # sample_dir 이름의 폴더가 있으면 True
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)    # 폴더 삭제
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)    # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir()) # glob처럼 디렉토리 파일 확인

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())
# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(day=100) # 100일 저장
print("우리가 만난지 100일은", today+td) # 오늘부터 100일 후
