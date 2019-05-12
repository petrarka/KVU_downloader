import re as reg
import json
import requests as re
import sys, os
import multiprocessing
from tqdm import tqdm
USAGE ="""Usage: test.py ending
https://knigavuhe.org/book/anafem/   anafem - ending
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
    if len(match)!= 1:
        return 'bad data'
    match='' + match[0][match[0].find('['):match[0].find(']')] + ']'
    jsonData = json.loads(match,strict=False)
    print('download starts')
    os.makedirs(ending)
    for x in tqdm(jsonData):
        url=[x["url"],x["title"],ending]
        with open(url[2]+"/"+url[2]+' '+url[1]+".mp3", "wb") as file:
            response = re.get(url[0])
            file.write(response.content)
    print('download ends')
    return 'ok'
if len(sys.argv) != 2:
    print(USAGE)
else:
    if getData(sys.argv[1]) == 'ok':
        print('done')
    else:
        print('error')
