import os
import json
import requests
import fileinput
from pyutil import filereplace

STEAM_AUTH_TOKEN = 'B66427A7C90E610BC6716C312199F98E'
OPENDOTA = 'https://api.opendota.com/api/matches/271145478'

def generateItemList(token):

	#GetGameItems API CALL
	URL = 'http://api.steampowered.com/IEconDOTA2_570/GetGameItems/v1?key=' + token
	items = requests.get(url = URL)
	matches = requests.get(url = OPENDOTA)
	content = json.loads(items.content.decode('utf-8').replace('\n', ''))


	outfile = open("shop_items.json",'w')

	json.dump(content,outfile)
	outfile.close


	with open('matches.txt','w') as file:
		file.write(matches.content.decode());


generateItemList(STEAM_AUTH_TOKEN)