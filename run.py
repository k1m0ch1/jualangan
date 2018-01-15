from InstagramAPI import InstagramAPI
from dotenv import load_dotenv, find_dotenv
import os, os.path
import datetime
import platform 
from time import sleep
import moviepy

load_dotenv(find_dotenv(), override=True)

def getDay():
	now = datetime.datetime.now()
	hari = int(now.strftime("%w"))
	if hari == 0 :
		hari = "minggu"
	elif hari == 1 :
		hari = "senin"
	elif hari == 2 :
		hari = "selasa"
	elif hari == 3 : 
		hari = "rabu"
	elif hari == 4 :
		hari = "kamis"
	elif hari == 5 :
		hari = "jumat"
	elif hari == 6 :
		hari = "sabtu"
	else:
		hari = "undefined"
	return hari

def upload(filename="", content=""):
	api = InstagramAPI(USERNAME, PASSWORD)

	if (api.login()):
	    #api.getSelfUserFeed()  # get self user feed
	    #print(api.LastJson)  # print last response JSON
	    print("Login succes!")
	else:
	    print("Can't login!")

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

SENIN = os.getcwd() + "/batch/senin/"
SELASA = os.getcwd() + "/batch/selasa/"
RABU = os.getcwd() + "/batch/rabu/"
KAMIS = os.getcwd() + "/batch/kamis/"
JUMAT = os.getcwd() + "/batch/jumat/"
SABTU = os.getcwd() + "/batch/sabtu/"
MINGGU = os.getcwd() + "/batch/minggu/"

if platform.system() == "Windows":
	SENIN = os.getcwd() + "\\batch\\senin\\"
	SELASA = os.getcwd() + "\\batch\\selasa\\"
	RABU = os.getcwd() + "\\batch\\rabu\\"
	KAMIS = os.getcwd() + "\\batch\\kamis\\"
	JUMAT = os.getcwd() + "\\batch\\jumat\\"
	SABTU = os.getcwd() + "\\batch\\sabtu\\"
	MINGGU = os.getcwd() + "\\batch\\minggu\\"

HARIINI = "KOSONG"

if getDay() == "senin":
	HARIINI = SENIN
elif getDay() == "selasa":
	HARIINI = SELASA
elif getDay() == "rabu":
	HARIINI = RABU
elif getDay() == "kamis":
	HARIINI = KAMIS
elif getDay() == "jumat":
	HARIINI = JUMAT
elif getDay() == "sabtu":
	HARIINI = SABTU
elif getDay() == "minggu":
	HARIINI = MINGGU

path, dirs, files = os.walk(HARIINI).next()
file_count = len(files)

while True:
	if file_count > 0:
		print "[*] Gathering job for today"
		a=1
		ws = []
		wss = []
		lf = []	
		txt = []
		for f in range(0, file_count/2):
			try:
				formatfile = HARIINI + str(a) + ".lol"
				fi = open(formatfile, "r")
			except OSError as e:
				print "File " + formatfile + " Ga ada pak!"				

			uy = 1
			for xx in fi:
				if uy == 1:
					lf.append(xx.rstrip())
					uy = uy + 1
				else:
					txt.append(xx.rstrip())
					uy=1

			for uye in lf:
				waktuA = datetime.datetime.strptime(str(uye), "%H:%M")
				waktuB = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M"), "%H:%M")
				waktu = waktuA - waktuB
				waktu = waktu.seconds
				waktuS = waktuB + datetime.timedelta(seconds=waktu)
				waktuS = waktuS.strftime("%H:%M")
				wss.append(waktuS)
				ws.append(int(waktu))

			a=a+1

		wss = sorted(wss)
		ws.sort(key=int)
		#print lf
		print wss

		for xy in wss :
			waktuA = datetime.datetime.strptime(str(xy), "%H:%M")
			waktuB = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M"), "%H:%M")
			waktu = waktuA - waktuB
			waktu = waktu.seconds
			if waktu >= 86400 :
				print "[*] Batch " + xy + " can't be prosessed because its already past time"
			else:
				print "[*] Next batch is " + xy + " will be posted file " 
				sleep(int(waktu)-10)
				print "[*] Batch " + xy + " will be posted 10 second from now"
				sleep(10)
				#disini posting ke instagram


		# print ws
		# print wss
		# print "[*] Waiting for the next job at " + lf[0]
		# sleep(int(waktu))
	else:
		print "[*] No job today, idle mode"
		sleep(60)
