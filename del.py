from dotenv import load_dotenv, find_dotenv
import os, os.path
import sys
import day
import insta

load_dotenv(find_dotenv(), override=True)
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
BANYAK = sys.argv[1]

print "[*] Trying to login with " + USERNAME
ig = insta.login(USERNAME, PASSWORD)
insta.delete_from_last(ig, BANYAK)