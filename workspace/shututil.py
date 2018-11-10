
import shutil
import os

for i in range(1, 11):
	# 하위 디렉토리에 생성
	# name = os.getcwd() + '\9001. Module' + '\Python_Exam_' + str(i).zfill(4) + '.txt'

	# 현재 디렉토리에 생성
	name = 'Python_Exam_' + str(i).zfill(4) + '.txt'
	shutil.copy('Python_Exam.txt', name)
