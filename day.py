import datetime

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