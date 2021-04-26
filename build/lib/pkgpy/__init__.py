import os
from sys import platform
def install():
	print("installing pkgpy...")
	print("starting bootstrap...")
	print("####.......... 30%")
	if platform == "linux" or platform == "linux2" or platform == darwin:
		os.system("cd / && mkdir pkg && mkdir pkg/js && mkdir pkg/py && mkdir pkg/core")
	elif platform == "win32" or platform == "win64:
def runpkg(pkg):
	pkgname = pkg[1]
