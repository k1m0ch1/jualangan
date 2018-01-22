from dotenv import load_dotenv, find_dotenv
import os, os.path
import datetime
import platform 
from time import sleep
import moviepy
import json
from pygments import highlight, lexers, formatters
from collections import namedtuple
import day
import insta

load_dotenv(find_dotenv(), override=True)
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
LOGGEDIN = False

print "[*] Trying to login with " + USERNAME
ig = insta.login(USERNAME, PASSWORD)

def development():
	# api = InstagramAPI(USERNAME, PASSWORD)
	# if api.login():
	# 	api.getSelfUserFeed()
		#api.deleteMedia("1694574687916317986")
		#api.mediaInfo("BUlxQgtjEUFS9FH-txgE2NkJb_CsJbiW6JqwO40")
		#jSon = str(api.LastJson)
		# formatted_json = json.dumps(jSon, indent=4)
		# colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
		# print(colorful_json)
		#jSon = json.dumps(jSon, indent=4)
		#print jSon
		# for items in jSon.values()[3]:
		# 	print items.values()
		# a, b = zip(*jSon.items())
		# print b
		# jSon = namedtuple("jSon", jSon.keys())(*jSon.values())
		# items = []
		# caption = []
		# for getitems in jSon.items:
		# 	items.append(namedtuple("items", getitems.keys())(*getitems.values()))
		# jSon = json.loads(jSon)

		# for items in jSOn['items']:
		# 	print items

		# for getcaption in items:
		# 	for ggetcaption in getcaption.caption:
		# 		print ggetcaption.values()
				#caption.append(namedtuple("caption", ggetcaption.keys())(*ggetcaption.values()))
			#print getcaption.caption.keys()
			#caption.append(namedtuple("caption", getcaption.caption.keys())(*getcaption.caption.values()))

		# getcaption = namedtuple("hasil", getcaption.caption.keys())(*getcaption.caption.values())
		# print getcaption.created_at
	return ""

#development()

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

akhir = False
while True:
	if akhir == False:
		print "[*] Gathering job for today (" + day.getDay() + ")"

	if day.getDay() == "senin":
		HARIINI = SENIN
	elif day.getDay() == "selasa":
		HARIINI = SELASA
	elif day.getDay() == "rabu":
		HARIINI = RABU
	elif day.getDay() == "kamis":
		HARIINI = KAMIS
	elif day.getDay() == "jumat":
		HARIINI = JUMAT
	elif day.getDay() == "sabtu":
		HARIINI = SABTU
	elif day.getDay() == "minggu":
		HARIINI = MINGGU

	path, dirs, files = os.walk(HARIINI).next()
	file_count = len(files)

	if file_count > 0 and akhir == False:
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
				print "[*] File " + formatfile + " Ga ada pak!"				

			uy = 1
			for xx in fi:
				if uy == 1:
					lf.append(xx.rstrip())
					uy = uy + 1
				else:
					txt.append(xx.rstrip())
					uy=1

			a=a+1

		for uye in lf:
			waktuA = datetime.datetime.strptime(str(uye), "%H:%M")
			waktuB = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M"), "%H:%M")
			waktu = waktuA - waktuB
			waktu = waktu.seconds
			waktuS = waktuB + datetime.timedelta(seconds=waktu)
			waktuS = waktuS.strftime("%H:%M")
			wss.append(waktuS)
			ws.append(int(waktu))

		wss = sorted(wss)
		ws.sort(key=int)
		#print lf
		#print wss
		#print txt
		files.sort(key=lambda f: int(filter(str.isdigit, f)))
		print files
		a=1
		for xy in wss :
			waktuA = datetime.datetime.strptime(str(xy), "%H:%M")
			waktuB = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M"), "%H:%M")
			waktuC = datetime.datetime.strptime(str("00:00"), "%H:%M")
			waktu = waktuA - waktuB
			waktu = waktu.seconds
			waktuAwal = waktuB - waktuC
			waktuAkhir = waktuB - waktuA
			# print waktuAwal.seconds
			# print waktuAkhir.seconds
			# print waktu
			if int(waktuAkhir.seconds) <= int(waktuAwal.seconds) :
				print "[*] Batch " + xy + " can't be prosessed because its already past time"
			else:
				print "[*] Next batch is " + xy + " will be posted file " + str(HARIINI + files[a*2-2])
				sleep(int(waktu)-10)
				print "[*] Batch " + xy + " will be posted 10 second from now"
				sleep(10)
				insta.upload(ig, HARIINI + files[a*2-2], txt[a-1])
				#disini posting ke instagram
			a = a +1

		akhir = True

		# print ws
		# print wss
		# print "[*] Waiting for the next job at " + lf[0]
		# sleep(int(waktu))
	else:
		print "[*] No job today, idle mode for " + str(os.environ.get("IDLE")) + " seconds"
		sleep(int(os.environ.get("IDLE"))-10)
		print "[*] 10 seconds more will do re-check the job"
		sleep(10)
		akhir = False
