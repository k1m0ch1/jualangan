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

LOGGEDIN = False
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

print "[*] Trying to login with " + USERNAME
ig = insta.login(USERNAME, PASSWORD)