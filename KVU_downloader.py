import re as reg
import json
import requests as re
import sys, os
from multiprocessing.dummy import Pool
from tqdm import tqdm
from functools import partial
import time
USAGE ="""Usage: test.py ending -f "file name format" -t num_of_threads
https://knigavuhe.org/book/anafem/   anafem - ending
"{title} {num} {name}"  - format vars
"#{num} {name} - {title}" - name format example for #0 anafem - chapter 1 part 1.mp3
"""
def download(x, ending, name):
    url=[x[1]["url"],x[1]["title"],ending]
    namef = name.format(name = url[2], title = url[1], num = x[0])
    with open(url[2]+"/" + namef + ".mp3", "wb") as file:
        response = re.get(url[0])
        file.write(response.content)
    return "ok"

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
    try:
        os.makedirs(ending)
    except OSError:
        print("directory exists")
    if "-t" in sys.argv:
       index = sys.argv.index("-t") + 1
       THREADS=int(sys.argv[index])
    else:
       THREADS = 4
    p = Pool(THREADS)
    print("using {} threads".format(THREADS))
    if "-f" in sys.argv:
        index = sys.argv.index("-f") + 1
        name = sys.argv[index]
    else:
        name = "{title} {name}"
    print("using {} name format".format(name))
    d=partial(download, ending = ending, name = name)
    print('download starts')
    for _ in tqdm(p.imap_unordered(d, enumerate(jsonData)), total=len(jsonData)):
	    pass
    p.close()
    p.join()

    print('download ends')
    return 'ok'
if len(sys.argv) < 2 :
    print(USAGE)
else:
    t1 = time.time()
    status = getData(sys.argv[1])
    if status == 'ok':
        print('done for {} secs'.format(int(time.time()-t1)))
    else:
        print('error: {}').format(status)

