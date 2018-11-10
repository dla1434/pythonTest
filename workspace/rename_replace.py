
import shutil
import os

for filename in os.listdir("."):
	if filename.startswith("Python_"):
		# print(filename)
		os.rename(filename, filename.replace("Python_", "Django_"))

for filename in os.listdir("."):
	print(filename)

