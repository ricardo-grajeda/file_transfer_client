#made this in 3 nights while I visited my dad who has no idea how to transfer music from his computer to his android phone.


#program will output 2 default files which were ment for debugging.
    #1."filesName.txt" which outputs all files names that were looked at for download potential
    #2."index.txt" which is just the source from the entire server("theURL" variable).


import os
import re
from urllib import request
import urllib
import requests

# ---------download source code from url-----------#
theURL = "http://192.168.1.148:8000/"
saveSpot = ("C:\\Users\\ricar\\Desktop\\store\\")
fileType = "mp3" #extention which will be downloaded from server
# theURL = input("Enter url: ")
# saveSpot = input("Enter where to save files: ")
# fileType = input("Enter file extention: ")

def index_data(website_url):
    error = 0
    errorAmount = 0
    while error == 0:
        try:
            response = request.urlopen(theURL)
            print("\n[*]SERVER FOUND[*]")
            error = 1
        except:
            print("Did not find server")

    index = response.read()
    index_string = str(index)
    lines = index_string.split("\\n")
    dest_url = saveSpot + "index.txt"
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


def DownloadFile(url, each):
    local_filename = saveSpot + each
    r = requests.get(url)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    return None


index_data(theURL)

# --------------reading index.txt and regex'ing names of mp3 files-------------#

nameOfFile = []  ###names of .mp3 files are stored in this variable then exported to file

fileR = open(saveSpot + "index.txt", "r")
fileW = open(saveSpot + "filesNames.txt", "w")

arr = []

pattern = r"(>[A-Z,a-z,0-9-\_\;\\!#\[\]'()&.\s]*.temp)"
pattern = pattern.replace("temp", fileType)
for line in fileR:

    a = (re.findall(pattern, line))
    if len(a) == 0:
        continue
    arr.append(a)
for each in arr:
    size = len(str(each))
    temp = (each[0][1:size])
    fileW.write(temp + "\n")
    nameOfFile.append(temp)

fileR.close()
fileW.close()

# ---------downloading all files specified with regex---------#
file_save = saveSpot

count = 0
#incase files have special characters not recognized by program
for each in nameOfFile:
    each = each.replace("\\xc3\\xb1", "ñ")
    each = each.replace("\\xc3\\xa1", "á")
    each = each.replace("\\xc3\\xb3", "ó")
    each = each.replace("\\xc3\\xa9", "é")
    each = each.replace("\\xc3\\x91", "Ñ")
    each = each.replace("\\xc3\\x81", "Á")
    each = each.replace("\\xc3\\x9a", "Ú")
    each = each.replace("\\xc3\\xad", "í")
    each = each.replace("\\xc3\\xba", "ú")
    each = each.replace("\\'\\'", "\'\'")
    each = each.replace("\\'", "\'")

    fullPath = str(theURL + each)
    if os.path.isfile(str(file_save + each)):
        print("found it (skipping)")
        continue
    # print(fullPath)
    print(str(each))
    count += 1
    DownloadFile(fullPath, each)
if count == 0:
    print("\n[+]everthing is up to date[+]")
elif count > 0:
    print("=== " + str(count) + " file(s) downloaded ===")