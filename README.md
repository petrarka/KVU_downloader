# KVU_downloader
Simple audiobook downloader for knigavuhe.ru

## Install:
```
git clone https://github.com/petrarka/KVU_downloader
pip3 install requests tqdm
cd KVU_downloader
```

## Usage:
```
python3 KVU_downloader.py ending "file name format"
```

for https://knigavuhe.ru/book/anafem/
```
python3 KVU_downloader.py anafem
```
## File name format:
"{title} {num} {name}"  - format vars

"#{num} {name} - {title}" - name format example for #0 anafem - chapter 1 part 1.mp3

