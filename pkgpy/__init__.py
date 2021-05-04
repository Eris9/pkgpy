import os
from sys import platform
def install():
	qn = input("Start install (y/n)? ")
	if qn == "n":
		break
	print("installing pkg...")
	print("starting bootstrap...")
	print("####.......... 30%")
	if platform == "linux" or platform == "linux2" or platform == darwin:
		os.system("cd / && mkdir pkg && mkdir pkg/js && mkdir pkg/py && mkdir pkg/core")
		os.system("cd /bin && curl https://pkg.he1ios.repl.co/flask/static/core -o pkg && chmod +x pkg")
		os.system("pip install pkgpy")
	elif platform == "win32" or platform == "win64:
		print("not ready yet")
def runpkg(pkg,binstatus):
	pkgname = pkg[1]
	pkgauthor = pkg[2]
	lang = pkg[3]
	inst = pkg[4]
	instf = pkg[5]
	uninst = pkg[6]
	uninstf = pkg[7]
	postinst = pkg[8]
	if lang == "js":
		os.system(f"mkdir pkg/js/{pkgname}")
		os.system(f"cd /pkg/js/{pkgname} && curl {inst} -o {instf}")
		os.system(f"cd /pkg/js/{pkgname} && curl {uninst} -o {uninstf}")
		os.system(f"cd /pkg/js/{pkgname} && curl {postinst} -o postinst.sh")
		os.system(f"cd /pkg/js/{pkgname} bash postinst.sh")
		os.system(f"cd /pkg/js/{pkgname} rm -rf postinst.sh")
	if lang == "py":
		os.system(f"mkdir pkg/py/{pkgname}")
		os.system(f"cd /pkg/py/{pkgname} && curl {inst} -o {instf}")
		os.system(f"cd /pkg/py/{pkgname} && curl {uninst} -o {uninstf}")
		os.system(f"cd /pkg/py/{pkgname} && curl {postinst} -o postinst.sh")
		os.system(f"cd /pkg/py/{pkgname} bash postinst.sh")
		os.system(f"cd /pkg/py/{pkgname} rm -rf postinst.sh")
	if lang == "js":
		run = f"cd pkg/js/{pkgname} && npm start"
	if lang == "py":
		run = f"cd pkg/js/{pkgname} && python {pkgname}.py"
	if binstatus == 1:
		os.system(f"cd /bin && touch {pkgname}")
		os.system(f"cd /bin && echo {run} > {pkgname}")
		os.system(f"chmod +x /bin/{pkgname}")
		print("done binaries assigned")
	if binstatus == 2:
		print("binaries not needed find it in pkg directory")