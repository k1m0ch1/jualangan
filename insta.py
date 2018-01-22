from InstagramAPI import InstagramAPI
import datetime
import time
from time import sleep
from random import randint

def upload(api="",filename="", content=""):
	photo_path = filename
	caption = content
	print "[*] Processing to upload " + filename
	api.uploadPhoto(photo_path, caption=caption)
	print "[*] File Uploaded"

def login(USERNAME="", PASSWORD=""):
	api = InstagramAPI(USERNAME, PASSWORD)

	if(api.login()):
		print "[*] Success Login"
	else:
		print "[*] Can't Login, check again username dan password"

	return api

def delete_from_last(api="", BANYAK=0):
	print "[*] Processing to gather data profile ( this will took a long time and don't close this process )"
	mulai = time.time()
	jSon = api.getTotalSelfUserFeed()
	beres = time.time()
	lama = beres - mulai
	lama = int(lama)
	print "[*] It tooks " + str(lama) + " second to processing gathering all user feed"
	print "[*] Gathering data finished"
	sleep(3)
	ljSon = len(jSon)
	ajSon = int(ljSon) - int(BANYAK)
	awal = jSon[ljSon-1]['caption']['created_at']
	awal = str(datetime.datetime.fromtimestamp(int(awal)).strftime('%d %B %Y %H:%M:%S'))
	akhir = jSon[ajSon-1]['caption']['created_at']
	akhir = str(datetime.datetime.fromtimestamp(int(akhir)).strftime('%d %B %Y %H:%M:%S'))
	print "[*] Dari " + str(ljSon) + " post, akan hapus " + str(BANYAK) + " post terakhir dimulai tanggal " + awal + " s/d " + akhir
	for x in range(ajSon, ljSon):
		sleep(int(randint(5, 15))) #this random to prefent spam detection, tested for 100 request.
		media_id = str(jSon[x]['caption']['media_id'])
		tanggal = jSon[x]['caption']['created_at']
		bTanggal = str(datetime.datetime.fromtimestamp(int(tanggal)).strftime('%d %B %Y %H:%M:%S'))
		if api.deleteMedia(media_id) :
			print "[*][" + str(media_id) + "] Delete post from " + bTanggal + " Success "
		else:
			print "[*][" + str(media_id) + "] Delete post from " + bTanggal + " Fail "

	print "[*] Delete Success"
