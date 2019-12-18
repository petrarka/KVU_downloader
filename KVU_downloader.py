import re as reg
import json
import requests as re
import sys, os
import multiprocessing
from tqdm import tqdm
USAGE ="""Usage: test.py ending "file name format"
https://knigavuhe.org/book/anafem/   anafem - ending
"{title} {num} {name}"  - format vars
"#{num} {name} - {title}" - name format example for #0 anafem - chapter 1 part 1.mp3
"""
def download(url):
    #for future
    print('start '+'url[2]+' '+url[1]')
    with open("./"+url[2]+"/"+url[2]+' '+url[1], "wb") as file:
        response = re.get(url[0])
        file.write(response.content)
def getData(ending):
    BASE_URL = "https://knigavuhe.org/book/"
    r = re.get(BASE_URL + ending)
    if r.status_code != 200:
        return "bad url"
    data=r.text
    match = reg.findall( r'var player = new BookPlayer\([0-9]{1,}, \[.{1,}]', data)
    if len(match) == 0:
	    return 'bad data, player not found (litres)'
    match='' + match[1][match[1].find('['):match[1].find(']')] + ']'
    jsonData = json.loads(match,strict=False)
    print('download starts')
    try:
        os.makedirs(ending)
    except OSError:
        print("directory exists")
    for x in tqdm(list(enumerate(jsonData))):
        url=[x[1]["url"],x[1]["title"],ending]
        if len(sys.argv) == 3:
            name = sys.argv[2].format(name = url[2], title = url[1], num = x[0])
        else:
            name = "{title} {name}".format(name = url[2], title = url[1])
        with open(url[2]+"/" + name + ".mp3", "wb") as file:
            response = re.get(url[0])
            file.write(response.content)
    print('download ends')
    return 'ok'
if len(sys.argv) not in (2,3) :
    print(USAGE)
else:
    status = getData(sys.argv[1])
    if status == 'ok':
        print('done')
    else:
        print('error')
        print(status)
