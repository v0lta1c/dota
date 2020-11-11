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
	#content = json.loads(items.content.decode('utf-8').replace('\n', '\n'))
	#content = json.loads(items.content)

	#outfile = open("shop_items.json",'w')
	#outfile.write(json.dumps(items.content))
	#outfile.close
	#json.dump(content,outfile)
	#outfile.close
	#sorting your json output by keys so that you get your output as {"1":{}, "2":{}...}
	results_str = json.dumps(items.content.decode('utf-8').replace('\n', ''), sort_keys=True)

	#removing the outer brackets {}, now the results_str would look something like this "1":{}, "2":{}...
	results_str = results_str[1:-1]

	#splitting the string by "}," as delimiter, so results_list would look like this ["1":{, "2":{, "3":{}]
	results_list = results_str.split("},")

	#print the results to the file as per the desired format
	with open('shop_items.json', 'w') as outfile:
	    outfile.write('\n')
	    for p in results_list[:-1]:
	        print (p+'}', file=outfile)
	    print (results_list[-1], file=outfile)

	with open('matches.txt','w') as file:
		file.write(matches.content.decode());
	#with fileinput.FileInput("shop_items.json",inplace=True,backup='.bak') as file:
		#for line in file:
			#print(line.replace('\n','\\n'), end='')



generateItemList(STEAM_AUTH_TOKEN)