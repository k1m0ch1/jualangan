from InstagramAPI import InstagramAPI

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