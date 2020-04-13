from datetime import datetime
from tqdm import tqdm
import requests
import re

print(r'''
______                _       _                       ______ _           
(_____ \              | |     | |                     / _____|_)_         
 _____) )___ ____   _ | | ____| | ____ ____    ___   | /      _| |_ _   _ 
|  ____/ _  |  _ \ / || |/ _  ) |/ _  ) _  |  (___)  | |     | |  _) | | |
| |   ( ( | | | | ( (_| ( (/ /| ( (/ ( ( | |         | \_____| | |_| |_| |
|_|    \_||_|_| |_|\____|\____)_|\____)_||_|          \______)_|\___)__  |
                                                                   (____/ 
                                                     [by Alex Stefan Savu]
  
  Also check Instasave: https://github.com/print-alex/root

''')

url = input("\nEnter the URL of Facebook video: ")
x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)

if x:
    html = requests.get(url).content.decode('utf-8')
else:
    print("Not related with Facebook domain")
    exit()

_qualityhd = re.search('hd_src:"https', html)
_qualitysd = re.search('sd_src:"https', html)
_hd = re.search('hd_src:null', html)
_sd = re.search('sd_src:null', html)

list = []
_thelist = [_qualityhd, _qualitysd, _hd, _sd]
for id,val in enumerate(_thelist):
    if val != None:
        list.append(id)

try:
    if len(list) == 2:
        if 0 in list and 1 in list:
            _input_1 = str(input("\nPress 'A' to download the video in HD quality.\nPress 'B' to download the video in SD quality\n: ")).upper()
            if _input_1 == 'A':
                print("\nDownloading the video in HD quality")
                video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("Video downloaded successfully")   

            if _input_1 == 'B':
                print("\nDownloading the video in SD quality")
                video_url = re.search(r'sd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("Video downloaded successfully")   

    if len(list) == 2:
        if 1 in list and 2 in list:
            _input_2 = str(input("Oops! The video is not available in HD quality. Would you like to download it? ('Y' or 'N'): ")).upper()
            if _input_2 == 'Y':
                print("\nDownloading the video in SD quality")
                video_url = re.search(r'sd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("Video downloaded successfully")
            if _input_2 == 'N':
                exit()

    if len(list) == 2:
        if 0 in list and 3 in list:
            _input_2 = str(input("Oops! The video is not available in SD quality. Would you like to download it? ('Y' or 'N'): \n")).upper()
            if _input_2 == 'Y':
                print("\nDownloading the video in HD quality")
                video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("Video downloaded successfully")
            if _input_2 == 'N':
                exit()
except(KeyboardInterrupt):
    print("\nProgramme Interrupted")
    
