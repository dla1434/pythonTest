
import os

# getcwd() : 현재작업디렉토리(current working directory)를 나타내는 스트링을 리턴
print(os.getcwd())

# __file__ : 파일의 path를 저장
print(os.path.realpath(__file__))

# realpath() : file이 symbolic link인 경우 원본 위치를 찾아줌
print(os.path.dirname(os.path.realpath(__file__)))
