import ftplib,os,os.path,sys,zipfile,socket
host="host"
username="username"
password="password"

curdir=os.getcwd()

try:
	ftp=ftplib.FTP(host,username,password)
	print("[#] Connected to       : %s"%(str(ftp.host)))
	print("[#] Server current Dir : %s"%(ftp.pwd()))
	print("[#] Current Device Dir : %s"%(curdir))
	print("[#] Server IP          : %s"%(socket.gethostbyname(ftp.host)))
	print("[#] Current IP         : %s"%(socket.gethostbyname(socket.gethostname())))
	files=[i for i in ftp.nlst()]
except Exception as e:
	print("[x] Cant Connect Right now!")
	print("[X] %s"%(e))
	exit(0)


def send(file):
	fname=file.split("\\")[::-1][0]

	if os.path.isdir(file.split(file.split("\\")[::-1][0])[0])==True:
		os.chdir(file.split(file.split("\\")[::-1][0])[0])

	if os.path.exists(fname)==True:
		zipfile.ZipFile(str(fname.split(".")[0])+".zip",mode="w").write(fname)
		ftp.storbinary("STOR "+str(str(fname.split(".")[0])+".zip"),open(str(str(fname.split(".")[0])+".zip"), 'rb'))
		print("\n[#] Done Uploading\n");print(ftp.nlst())
		os.chdir(curdir)
 

if int(len(sys.argv))==int(2):
	send(sys.argv[1])
	exit(0)

while True:
	f1=os.path.normpath(input("\nEnter File Path To Upload -: "))
	if os.path.exists(f1)==True:
		send(f1)
	else:
		print("\n[X] Cant Find The File Speefied! ")



