# 외장 함수
# glob : 경로 내의 폴더/ 파일 목록 조회 (윈도우 dir명령과 동일)
import glob
print(glob.glob("*.py")) #확장자가 py인 모든 파일검색

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) #현재 디렉토리 표시

folder = "sample_dir"

if os.path.exists(folder): # sample_dir라는 폴더가 있는지 없는지
    print("이미 존재하는 폴더 입니다")
    os.rmdir(folder) #폴더 삭제
    print(folder,"폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) #폴더생성
    print(folder,"폴더를 생성하였습니다.")

print(os.listdir())

#time : 시간관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%M-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

#timedelta : 두날짜 사이의 간격 알려줌
today = datetime.date.today()
td = datetime.timedelta(days = 100) #오늘 날짜부터 100일뒤
print("우리가 만난지 100일은", today +td)

