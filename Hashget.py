import requests
from bs4 import BeautifulSoup
import time
import argparse
import subprocess
import os
import random
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import ssl
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util.ssl_ import create_urllib3_context


########A####D####K#####A#####L#####I##########
# Hashget is an advanced tool designed to find matches for given hashes using various online services.
# It provides a seamless hash lookup experience with its user-friendly interface.
# Created to enhance your efficiency in handling multiple sources simultaneously.
# Report any issues for continuous improvement.
# Please use responsibly. [WhySoSerious?]
####H####A####S#####H####G####E#####T###########

# Usage: hashget.py -ha [HASH] -t [HASH_TYPE]
# GitHub Repository: https://github.com/Adkali/Hashget
# Want to take a part helping in maintaining it? Contact Me!


http = PoolManager(
    cert_reqs='CERT_NONE',    # Turn off certificate verification
    assert_hostname=False     # Do not verify the SSL certificate's hostname
)

urllib3.disable_warnings(InsecureRequestWarning) # Turns off warnings

# Define colors to be using
# When code runs and output results or error
def Code_Colors():
    global Yellow, Red, Normal, BM, Green, Gray
    Yellow = "\033[1;33;40m"
    Red = "\033[1;31;40m"
    Normal = "\033[0;0m"
    BM = "\033[1;35;40m"
    Green = "\033[1;32;40m"
    Gray = "\033[1;30;40m"

Code_Colors()

# Simple Adkali banner
def BannerShow():
    print(f'''\n
    |  _____  |{Yellow}A{Normal}
    | |\ ___| | {Red}D{Normal}
    | | |   | | K
    | | |___| | {BM}A{Normal}
    \ | |____\| L
     \|_________I 
      {Green}Hashget{Normal} v1.2\n{Green}Github{Normal} v1.2\n''')


BannerShow()

# Error message to be presented
def Parserr(err):
    print("[!] Syntax Error!")
    print("Usage: python3 [ Script/Name ] -t [Hash type(md5/sha1/sha256/sha512] -h [hash]")
    print("Having problems? let me know!")
    exit()

class Parserr(argparse.ArgumentParser):
    def error(self, message):
        raise Exception(message)

# ---------- ARGS TO BE DEFINED AND GETTING INTERACT WITH USING THE CODE'S FLAGS ----------

parser = argparse.ArgumentParser(description="Hash decrypt using scrapping source.")
parser.error = Parserr
parser.add_argument('-t', '-type', type=str, required=True, help='Hash type, for example sha1, md5, sha256, etc.')
parser.add_argument('-ha', '-hashit', type=str, required=False, help='Hash itself to decrypt.')
parser.add_argument('-hf', '-hashfile', type=str, required=False, help='Hash itself to decrypt from a file.txt')
parser.add_argument('-p', '-proxy', type=str, required=False, help="Use proxy when sending request.")
parser.add_argument('-b', '-base64', type=str, required=False, help="use it for Base64 decoding.")
args = parser.parse_args()

# ------- Operators & Values Usage -------

# Function to read the content of a file
def file_toread(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

# Get the arguments
b64 = args.b
hash_itself = args.ha
hash_type = args.t
pro = args.p
hashfile = args.hf

# Check if the hash itself is not provided, read from the file
if not hash_itself and hashfile:
    hash_itself = file_toread(hashfile)

# Handle the case where neither hash itself nor hash file is provided
if not hash_itself:
    parser.error("You must provide either a hash or a hash file.")

# ------- CHECK HASH LENGTH AND COMPARE WITH OTHER HASH -------

def HashesList():
    print("What happened? use the right HASH please.")
    print("Supported hashes(lowercase):")
    print("md5, sha1, sha256, sha512.")
    print("Soon more will come! Try again please.")
    exit()

md5ex = '202cb962ac59075b964b07152d234b70'
sha1ex = '40bd001563085fc35165329ea1ff5c5ecbdbbeef'
sha256ex = 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'
sha512ex = '3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2'

if len(hash_itself) != len(md5ex) or hash_type != "md5":
    if len(hash_itself) != len(sha1ex) or hash_type != "sha1":
        if len(hash_itself) != len(sha256ex) or hash_type != "sha256":
            if len(hash_itself) != len(sha512ex) or hash_type != "sha512":
                if hash_itself != "base64" and hash_type != "base64":
                    HashesList()

# ------- MAKE THE HEADERS FOR THE REQUESTS -------

agents = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:39.0) Gecko/20100101 Firefox/39.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
    "Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0"
]
he = random.choice(agents)
Headers = {'User-Agent': f'{he}'}

# ------- LIST OF SITES FOR THE DECRYPTED WANTED HASH FUNCTION -------
URL0 = f"https://www.nitrxgen.net/md5db/{hash_itself}"
URL = f"https://hashtoolkit.com/decrypt-hash/?hash={hash_itself}"
URL2 = f"https://decrypt.tools/client-server/decrypt?type={hash_type}&string={hash_itself}"
URL3 = f"https://md5.gromweb.com/?md5={hash_itself}"
URL4 = f"https://sha1.gromweb.com/?hash={hash_itself}"
URL5 = "https://md5decrypt.net/en/"
URL6 = "https://md5decrypt.net/en/Sha1/"
URL7 = "https://md5decrypt.net/en/Sha256/"
URL8 = "https://cmd5.org/default.aspx/"
URL9 = "https://sha1.web-max.ca/index.php"
URL10 = "https://md5.web-max.ca/index.php"
URL11 = "https://www.md5online.it/index.lm?key_decript="
URL12 = "https://hashes.com/en/decrypt/hash"
URL13 = "http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"
URL14 = "http://md5.rf.gd/crack.php"
URL15 = f"http://www.ttmd5.com/do.php?c=Decode&m=getMD5&md5={hash_itself}"
URL16 = "https://passwordrecovery.io/md5/"

print("Pulling Out Hash Decryption, Please Wait.....\n")
time.sleep(3)
# ---------------------------------- EACH WEB EACH ----------------------------------

# ------- BASE64 DECODE -------
if b64:
    encoding = b64
    get_string = base64.b64decode(encoding)
    decoded_string = get_string.decode('utf-8')
    print(f"Decoded string -> {decoded_string}")
    exit(0)

# ------- URL NUMBER ZERO -------
  # ------- MAKE A MANUAL ERROR -------

def ErrorMessage0():
    print(f"[-] nitrxgen: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

if hash_type == "md5":
    try:
        r = requests.get(f"{URL0}", headers=Headers).text
        if not r or r.isspace() or "0 results" in r or r == "0":
            ErrorMessage0()
        else:
            print(f'[+] Decrypted Hash {Red}[nitrxgen]:{Normal}  [[ #H#A#S#H# ]] {Yellow}"text":"{r}"{Normal} [[ #H#A#S#H# ]]\n')
    except Exception as e:
        ErrorMessage0()


# ------- URL NUMBER ONE -------
  # ------- MAKE A MANUAL ERROR -------

def ErrorMessage():
    print(f"[-] HashToolKit: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

r = requests.get(URL, headers=Headers)
soup = BeautifulSoup(r.text, "html.parser")
text_to_find = soup.findAll("h1", class_="res-header")
try:
    for word in text_to_find:
        if "Hashes for" in word.text:
            results = word.text.split()
            print(f'[+]Decrypted Hash {Red}[HashToolKit]:{Normal}  [[ #H#A#S#H# ]] {Yellow}"text":"{results[2]}"{Normal} [[ #H#A#S#H# ]]\n')
except Exception as e:
    ErrorMessage()

# ------- URL NUMBER Two -------
  # ------- MAKE A MANUAL ERROR -------
def ErrorMessage2():
    print(f"[-]Decrypt.Tools: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

r = requests.get(URL2, headers=Headers)
  # ------- APPEND TO LIST -------
List = []
try:
    if r.status_code == 200:
        links2 = BeautifulSoup(r.text, "html.parser")
        for i in links2:
            if "id" in f"[{i}]":
                links3 = i[1:50]
                List.append(links3)
            else:
                ErrorMessage2()

except Exception as e:
    print(e)

try:
    for i in List:
        a = i.split(",")
        if len(a) > 0:
            print(f'[+]Decrypted Hash {Red}[Decrypt.Tools]:{Normal} [[ #H#A#S#H# ]] {Yellow}{a[1]}{Normal} [[ #H#A#S#H# ]]\n')

except Exception as e:
    print(e)

# -------   URL NUMBER THREE -------
 # ------- MAKE A MANUAL ERROR -------
def ErrorMessage3():
    print(f"[-]Md5.GromWeb: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

# ------- APPEND TO LIST2 [CLASS TAGS]
List2 = []
r = requests.get(URL3, headers=Headers)
try:
    if r.status_code == 200:
        md5soup = BeautifulSoup(r.content, "html.parser")
        md5split = md5soup.findAll("a", {"class": "String"})
        for i in md5split:
            href_value = i['href']
            if "string" in href_value and not "no reverse string was found" in md5soup.findAll("p"):
                List2.append(href_value)
                # Append it to List2', Now split it
except Exception as e:
    print(ErrorMessage3())

# Results
try:
    print(f'[+]Decrypted Hash {Red}[MD5.GromWeb]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{List2[0].split("=")[1]}"{Normal} [[ #H#A#S#H# ]]\n')

except Exception as e:
    print(ErrorMessage3())


# -------  URL NUMBER FOUR -------
 # ------- MAKE A MANUAL ERROR -------

def ErrorMessage4():
    print(f"[-]SHA1.GromWeb: {Green}{args.ha}{Normal} -- > Hash does not exist in database\n")

List3 = []
if hash_type == "sha1":
    r = requests.get(URL4, headers=Headers)
    try:
        if r.status_code == 200:
            md5soup2 = BeautifulSoup(r.content, "html.parser")
            for i in md5soup2:
                md5split2 = md5soup2.findAll("em", {"class": "long-content string"})
                for i in md5split2:
                    if 'long-content string' in f"{i}":
                        List3.append(i)
    except IndexError:
        ErrorMessage4()
    except Exception as e:
        print(e)
# ------- FINISH TRY,EXCEPT AND USE [2] FOR RESULTS -------
    try:
        for i in List3[2]:
            print(f'[+]Decrypted Hash {Red}[SHA1.GromWeb]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{i}"{Normal} [[ #H#A#S#H# ]]\n')

    except IndexError:
        ErrorMessage4()

 # ------- MAKE MANUAL ERROR -------

def ErrorMessage5():
    print(f"[-]MD5DECRYPT: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")
    os.system('rm -r md5data.txt')

# ------- CONTINUE URL NUMBER FIVE [md5decrypt/MD5] -------
 # ------- Manual Error -------

recaph = "03AFY_a8VZPDuVaIIt12MK0HfYYHIKtB4g2VIPv3Z62PlX0yYBKQYPjfTepO_3LAHmWfuA12-l72hXhfoROa7Gv_b7wDx0xrMi5Z8P5wiU769eZwgsC8BlgnsWb_n0eJ2mzx83JoRJC5zQ7kO7Yn6OfvkatF9k9U2Honyxh3jkQnjMrGG0px9GBKzRg8L_ZSnPYG3ptTZOHg6DEQUkZFrGPn5uHk4q83bbs7FcYsFIFsGDRXSpa5Q82v6uUQ55AcqgkAeotA1r29lxpJv_tdz3CUOQWIo5A8r52jhmjehjg31hGsyewLEyD2gigHaQslc7XdNngKutXFC7krYw2WUBpzHDyDz8W32_Y8UaAIa-eZeUbju1bPYylCvnnLf93gGlTUmSlLb-P-IzerHGMsmBmCUkSwsc9NLQtATvtcnfNZfnobwzfLsAZ3E-WfprdjDgLKInW8lH1hlPrP2ez4u23xlo40aSvnujsAKbpiYWamgFxsQCBeVvlp3hVQ8I1kxRLePhXuvnzHR6-1gfBG9GY3pG0UZo4IumNH0ap2tG5_c3k_l5IklTVqeCGqL0w-_cNXaPRZk2orJ9"
a = "curl -i -k -s -X POST -d "
b = f"'hash={args.ha}&recaptchaResponse=&button_value=decrypt&decrypt=Decrypt'"
c = " -H 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0'"
d = f" {URL5}"
e = f" | grep {args.ha}"
command = a + b + c + d + e
if hash_type == "md5":
    a = os.popen(f'{command} > md5data.txt')
    time.sleep(5)

    Result = []
    try:
        with open('md5data.txt', 'r') as data:
            dataread = data.readlines()
            for i in dataread:
                if f"{args.ha}" in i:
                    spl = i.split(f"{args.ha}")

    except Exception as e:
        print(e)
    except IndexError:
        ErrorMessage5()

    try:
        if "<b>" in spl[1]:
            spl2 = spl[1].split("/b>")
            Result.append(spl2[0])
    except NameError:
        ErrorMessage5()
    except IndexError:
        ErrorMessage5()
    try:
        for i in Result:
            i = i.strip().split(": <b>")
            print(f'[+]Decrypted Hash {Red}[MD5DECRYPT]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{i[1].replace("<","")}"{Normal} [[ #H#A#S#H# ]]\n')
            os.system('rm -r md5data.txt')
    except Exception as e:
        print(e)
    except IndexError:
        ErrorMessage5()
else:
    pass

# ------- CONTINUE TO URL NUMBER SIX -------
 # ------- MAKE MANUAL ERROR -------

def ErrorMessage6():
    print(f"[-]MD5DECRYPT-sha1: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")
    os.system('rm -r sha1data.txt')
time.sleep(1)

f = "curl -i -k -s -X POST -d "
g = f"'hash={args.ha}&recaptchaResponse=&button_value=decrypt'"
h = f" -H 'User-Agent:{he}'"
i = f" {URL6}"
j = f" | grep {args.ha}"
command = f + g + h + i + j

Result2 = []

if hash_type == "sha1":
    a = os.popen(f'{command} > sha1data.txt')
    time.sleep(5)

    try:
        with open('sha1data.txt', 'r') as data2:
            dataread2 = data2.readlines()
            for i in dataread2:
                if f"{args.ha}" in i:
                    spl2 = i.split(f"{args.ha}")

                if "<b>" in spl2[1]:
                    spl3 = spl2[1].split("/b>")
                    Result2.append(spl3[0])

            for i in Result2:
                try:
                    i = i.strip().split(": <b>")
                    print(f'[+]Decrypted Hash {Red}[MD5DECRYPT-Sha1]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{i[1].replace("<","")}"{Normal} [[ #H#A#S#H# ]]\n')
                    time.sleep(1.5)
                    os.system('rm -r sha1data.txt')
                except IndexError:
                    ErrorMessage6()
    except IndexError:
        ErrorMessage6()

# ------- URL NUMBER SEVEN [md5decrypt/Sha256]
 # ------- MAKE MANUAL ERROR -------
def ErrorMessage7():
    print(f"[-]MD5DECRYPT-SHA256: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")
    os.system('rm -r sha256data.txt')
    time.sleep(2)

f = "curl -i -k -s -X POST -d "
g =f"'hash={args.ha}&recaptchaResponse=&button_value=decrypt'"
h = " -H 'User-Agent:Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0'"
i = f" {URL7}"
j = f" | grep {args.ha}"
command = f + g + h + i + j

if hash_type == "sha256":
    a = os.popen(f'{command} > sha256data.txt')
    time.sleep(2)
    Result3 = []
    try:
        with open('sha256data.txt', 'r') as data3:
            dataread3 = data3.readlines()
            for i in dataread3:
                if f"{args.ha}" in i:
                    spl3 = i.split(f"{args.ha}")

    except IndexError:
        ErrorMessage7()
    except NameError:
        ErrorMessage7()

    try:
        if "<b>" in spl3[1]:
            spl4 = spl3[1].split("/b>")
            Result3.append(spl4[0])

    except NameError:
        ErrorMessage7()
    except IndexError:
        ErrorMessage7()

    try:
        for i in Result3:
            i = i.strip().split(": <b>")
            print(f'[+]Decrypted Hash {Red}[MD5DECRYPT-Sha256]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{i[1].replace("<","")}"{Normal} [[ #H#A#S#H# ]]\n')
            os.system('rm -r sha256data.txt')
    except IndexError:
        ErrorMessage7()

# ------- MAKE MANUAL ERROR -------

def ErrorMessage8():
    print(f"[-]CMD5: {Green}{args.ha}{Normal} -- > Authentication failed, try using '-p' flag.\n")
    os.system('rm -r cmd5.txt')

# ------- CONTINUE TO URL NUMBER 8 -------
 # ------- ADD TO LIST/DICT -------
List4 = []
Headers = {"User-Agent:": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
           "Accept:": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Language:": "en-US,en;q=0.5",
           "Accept-Encoding:": "gzip, deflate",
           "Content-Type:": "application/x-www-form-urlencoded",
           "Content-Length": "1995",
           "Origin": "https://www.cmd5.org",
           "Referer:": "https://www.cmd5.org/default.aspx",
           "--data-binary": f"__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=48RqcxFUJf7FmocIwER7FW46ifSXYRCYKlIZ74sEWj3PLOqpZlGUkMrp3ZVsCR%2FcnHCWaqb2wabPWBWVN7BFHuWZmooy15NIbo8FxKp1gjHHxnCDHR%2BR0DEkn%2FrXyFRhDVxeS0iNpzWyLBrRuwsqszT6qMMCBbCLYZ8a2bu%2BvQPk32JkJHtnau%2FbYcjN9NxitVi%2FWzyRslDHJQWmD%2B6vZQ9%2FDYTyoOm3rofL9Sv5f033vPPhfYo%2BMvR7yR9%2BZRblQGk8nYKKcWyZgvqTq4BEkQO%2BWN%2BuazRBK47kbTUbJgwRgmpnJ7XxW4SBKUtlx%2BdPoMsJVwUGCekXitgtPxPsJDI6jS3AKSiHj3M6i9EpP9EtLTUw4HWS5VMtj8KZ4mRmDudoDlI1%2Bkpk9y4lYYcMeJX2kwT3kNZQJp06HsudzQNa7SSlTM5TKEVPKFrFIrEDY6gtiNGyB45b%2B7Kg8uLd7qYR9MhX1UJpeYwnwSKe6806%2B00ZRzf0PZAyA4hBxFo66NRNsCoBL%2BCyBOggzIO7wZP8rxTOpdp%2BlddG7EqZd58bBA8IGFb8riePqUyf8H23Pv%2FlzFp%2BQIWSn%2B7HlweUQqgqWtOwC86xaCmUHoX%2BpM5UpQ4JMPhJdDvFZJoG%2Fcup8qjFvaFZwy3sOr%2BlLr5h6yTk3n8%2BTRVIR8wm7n8rGCqR8Hzjx9ocsfoZWylZnLHeBMX4k98Hv4MVnjM744f%2F5yqIxwV14m6BojGa4%2Fta7Z7V4THsARbgJs0VSsrAlR7Rtz9H5lgKSxiXo6nWa2cOdNQ%2FfKCQNjLdHoZwSv8pSzGZoFBh9dJw%2BMLD3QkEnQal1eoG3R73NUiuaYewc%2F1wwlN5sWJ6AHmeemtpdxEK%2FI7FGNPHvdlL8fuldnyXXfujMrI64r6y6cnw4UX9Vy03zMDDU8OaxUoTYKuOUPvNT7EmsyNqbxUQpYMcPSPnAVZG5yC42ZInVbBAxpKWik%2FxGr6XounpB%2FMMjsmBtectd2TmJjp1ZMJofazYvKL1OYYKIjmHIIluGmxKmYzXS8ofbLhX22W4XZuxEVq4PW1gPtTpXhApS5%2BykkjDLfHyXANiaN5kLtM%2FOApDuExxNqEkpKVQANvtTTO6LTqptKbGeQLhtEhxzR6D4eXAFyzlwSnmhxshkoURo7RQ4CHqZkazldpOzwTFsp%2BFwNJ6LKMniuFTaJO5NcMHBWw%2FSIadp%2Bow1s1yadUpPABiDCz%2BS9itKU1dkbWZ%2FBUDUUqvxxaDz%2B54PidT5eTwudL6pmQdZhYOlyC%2BbcaDQKmTuvvcT1JQFIoeIUQLx%2BXaKTm3QK6H%2FiMluFz%2BCCvnRQNwy8dDKyp6%2B7P9y5OhIwIKumAI6jibGrWbtBSAxkhbVseF6dxMiEkWUOJgZZORT1EJ%2BeWbrxqnMdAVQQ1HWsZbyWHNx0Hxnl04saKlg09aJFAd3uJr0xErj5E%2BiPkLv0E2YBdyXb9Now6%2F%2FdpOATajtIvqEPWK8%2F3TownmY85Weik2WWcxIqw1FM1vawSS6%2BYnzeTS5dp95txuJ%2Bp3c3mlmWll2Kw3AyCs7gpO7A9STrUJgfZJGvcfyCWF7gLKEnQCCZFAMAwUsRltJ55bG3yCecLlNapaJt43YLQDcAsac%2FXrgJc8b59W9ePYEheW%2FDOTR18GPdiDf2I3UCZ%2BkLbA1OUmwBv97Rxcay0jf%2FwlEApzzAKUNLamPW6mV13dlnY2qy7DyvPoQ%2F35RIeAW7YlK4exSisk3Z8yYbdVF8MZtw%2BDgJc3pMaJKhrf&__VIEWSTATEGENERATOR=CA0B0334&ctl00%24ContentPlaceHolder1%24TextBoxInput=4297f44b13955235245b2497399d7a93&ctl00%24ContentPlaceHolder1%24InputHashType=md5&ctl00%24ContentPlaceHolder1%24TextBoxCode=3519&ctl00%24ContentPlaceHolder1%24Button1=decrypt&ctl00%24ContentPlaceHolder1%24HiddenField1=&ctl00%24ContentPlaceHolder1%24HiddenField2=QejRRodl%2Fso%2Fwcqlz8BYXZwdpkCW19D3zpNA0ZV7VKtYAEACqlPpXsWKibQr53cA' https://www.cmd5.org/default.aspx/ | grep LabelAnswer"
           }

command = f"curl -i -s -k -X 'POST' -H 'User-Agent: {Headers['User-Agent:']}' -H 'Accept: {Headers['Accept:']}' -H 'Accept-Language: {Headers['Accept-Language:']}' -H 'Accept-Encoding: {Headers['Accept-Encoding:']}' -H 'Content-Type: {Headers['Content-Type:']}' -H 'Content-Length: {Headers['Content-Length']}' -H 'Origin: {Headers['Origin']}' -H 'Referer: {Headers['Referer:']}' --data-binary '{Headers['--data-binary']}"
time.sleep(5)
if pro == "set":
    try:
        subprocess.Popen("anonsurf start {0} >/dev/null 2>&1 &", shell=True)
    except Exception as e:
        print("Install 'kali-anonsurf' please [ sudo apt-get install kali-anonsurf -y ]")
time.sleep(3.5)
os.popen(f'{command} > cmd5.txt')
time.sleep(1)
with open("cmd5.txt", "r") as LabelAnswer:
    try:
        for i in LabelAnswer.readlines():
            if "LabelAnswer" in i:
                labelsplit = i.split("LabelAnswer")
                for i in labelsplit:
                    z = i.split('" class="')
                for z in z:
                    List4.append(z)
        a = List4[0].split('!</span>')[0].strip().split('">')[1]
        if a == "Please log in" or "Please log in" in a:
            ErrorMessage8()
        else:
            b = a.split("</span>")
            if "<b>" in b[0]:
                ErrorMessage8()
            else:
                print(f'[+]Decrypted Hash {Red}[CMD5]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{b[0]}"{Normal} [[ #H#A#S#H# ]]\n')
                os.popen('rm -r cmd5.txt')
                subprocess.Popen("anonsurf stop {0} >/dev/null 2>&1 &", shell=True)

    except IndexError:
        ErrorMessage8()
subprocess.Popen("anonsurf stop {0} >/dev/null 2>&1 &", shell=True)
# ------- CONTINUE TO URL NUMBER 9 -------
 # ------- MAKE MANUAL ERROR -------
def ErrorMessage9():
    print(f"[-]SHA1.WEB-MAX-: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

 # ------- ADD TO LIST -------
Headers2 = {
    "User-Agent": "Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0",
    "Host": "sha1.web-max.ca",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Origin": "https://sha1.web-max.ca",
    "Referer": "https://sha1.web-max.ca/index.php",
    "Connection": "close",
    "--data-binary": f"string={hash_itself}&key=13fd&check_code=7567&hidden_code=%0Cl%0C5%00dQ%60&decode=sha1+hash+decode",
}
List5 = []
curl = f"curl -i -k -s -X 'POST' https://sha1.web-max.ca/index.php -H 'User-Agent:{Headers2['User-Agent']}' -H 'Host:{Headers2['Host']}' -H 'Accept:{Headers2['Accept']}' -H 'Accept-Language:{Headers2['Accept-Language']}' -H 'Origin:{Headers2['Origin']}' -H 'Referer:{Headers2['Referer']}' --data-binary '{Headers2['--data-binary']}'"
if hash_type == "sha1":
    os.popen(f'{curl} > curl.txt')
    time.sleep(20)
    with open('curl.txt', 'r') as curl:
        for i in curl:
            if 'string' in i:
                s = i.strip().split("https://")
        for n in s:
            if "Re-encode" in n:
                try:
                    results = (n.split("tools.web-max.ca/encode_decode.php?string=")[1].split('">')[0])
                    print(f'[+]Decrypted Hash {Red}[SHA.WEB-MAX]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{results}{Normal} [[ #H#A#S#H# ]]\n')
                    os.system('rm -r curl.txt')
                except IndexError:
                    ErrorMessage9()
                except NameError:
                    ErrorMessage9()

# ------- MAKE MANUAL ERROR -------
''' 
These lines are re-newed at the bottom. 
Code continues!
'''

# def ErrorMessage10():
#     print(f"[-]PSRECOVERY: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")
#     os.system('rm -r recovery.txt')
#
# # ------- CONTINUE TO URL NUMBER 10 -------
# # ------- ADD TO DICT --------
# Headers3 = {
#     "User-Agent": "Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0",
#     "Host": "passwordrecovery.io",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Origin": "https://passwordrecovery.io",
#     "Referer": "https://passwordrecovery.io/md5/",
#     "--data-binary": f"csrf_token=ImQ2ZDAzNGYzMDVhOTliOWM1YmE0ZGRiYTRmNDU0NWQ4NDZjNDQ0MGQi.ZBq3cQ.n-M7Xxop1D-D5LjydrH5nVBqPoE&hash={hash_itself}"
# }
#
# curl_as_command = f"curl -i -k -s -X 'POST' -H 'User-Agent: {Headers3['User-Agent']}' -H 'Host: {Headers3['Host']}' -H 'Accept-Language: {Headers3['Accept-Language']}' -H 'Accept-Encoding: {Headers3['Accept-Encoding']}' -H 'Content-Type: {Headers3['Content-Type']}' -H 'Origin: {Headers3['Origin']}' -H 'Referer: {Headers3['Referer']}' -b session='eyJjc3JmX3Rva2VuIjoiZDZkMDM0ZjMwNWE5OWI5YzViYTRkZGJhNGY0NTQ1ZDg0NmM0NDQwZCJ9.ZBq3cQ.0z5u6PENd4eQkQB-rRCK-bed1E4' --data-binary '{Headers3['--data-binary']}' --compressed https://passwordrecovery.io/query/md5 | grep 'The hash is' > recovery.txt"
# print(curl_as_command)
# os.popen(f"{curl_as_command}")
# time.sleep(3)
#
# with open('recovery.txt', 'r') as rc:
#     try:
#         for i in rc.readlines():
#             if "The hash is" in i:
#                 s = i.split("The hash is")
#                 for i in s:
#                     z = i.split("</div>")
#                 for i in z:
#                     if ":" in i:
#                         r = i.split(":")
#                         print(f'[+]Decrypted Hash {Red}[PSRECOVERY]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{r[1].strip()}" [[ #H#A#S#H# ]]\n')
#                         os.system('rm -r recovery.txt')
#                     else:
#                         pass
#             else:
#                 pass
#
#     except Exception as e:
#         ErrorMessage10()

# ------- URL NUMBER TEN -------
 # ------- MAKE MANUAL ERROR -------

def ErrorMessage11():
    print(f"[-]MD5.WEB-MAX-: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

# ------- CONTINUE  -------
 # ------- ADD TO DICT -------
Headers2 = {
    "User-Agent": f"{he}",
    "Host": "md5.web-max.ca",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Origin": "https://md5.web-max.ca",
    "Referer": "https://md5.web-max.ca/index.php",
    "Connection": "close",
}

data_to_send = {
    "string": f"{hash_itself}",
    "key": "13df",
    "check_code": "5248",
    "hidden_code": "%011%06e%06d%05%3F",
    "decode": "md5+hash+decode"
}

if hash_type == "md5":
    response = requests.post(URL10, headers=Headers2, data=data_to_send)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            for paragraph in soup.findAll("p"):
                if "String" in paragraph.text:
                    find_me = paragraph.text.split("String")[1].split(":\xa0\r\n\t\t\t\t\t")[1]
                    print(f'[+]Decrypted Hash {Red}[md5.web-max]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{find_me}"{Normal} [[ #H#A#S#H# ]]\n')
        except Exception as e:
            ErrorMessage11()

# -------  URL NUMBER ELEVEN -------
 # ------- MAKE MANUAL ERROR -------


# Suppress the InsecureRequestWarning when making unverified HTTPS requests
# This is useful in development environments but should be used with caution
urllib3.disable_warnings(InsecureRequestWarning)

def ErrorMessage12():
    # Function to display an error message when a hash is not found in the database
    print(f"[-]MD5ONLINE-: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

# Define a custom HTTPS Adapter to manage SSL/TLS settings
class DESAdapter(HTTPAdapter):
    def __init_poolmanager(self, connections, maxsize, block=False, **pool_kwargs):
        # Create an SSL context with custom settings, allowing for weaker ciphers (SECLEVEL=1)
        context = create_urllib3_context(ciphers='DEFAULT:@SECLEVEL=1')
        # Initialize the pool manager with the custom SSL context and other connection parameters
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=ssl.PROTOCOL_TLS,  # Uses the most secure version of TLS available
            ssl_context=context            # Apply the custom SSL context
        )

# Check if the hash type is MD5 before proceeding
if hash_type == "md5":
    s = requests.Session()
    # Mount the custom DESAdapter to handle all HTTPS requests
    s.mount("https://", DESAdapter())

    try:
        # Attempt to retrieve the hash from the specified URL without verifying SSL certificates
        hash_to_get = s.get(f"https://md5online.it/index.lm?key_decript={hash_itself}", verify=False)
        if hash_to_get.status_code == 200:
            # Parse the HTML content using BeautifulSoup if the request is successful
            soup = BeautifulSoup(hash_to_get.text, "html.parser")
            # Check if the hash was successfully decrypted
            if "NESSUN RISULTATO" not in soup.text:
                # Extract and clean the decrypted hash from the page content
                Gotcha_ya = soup.text.split(f"{hash_itself}")[1].strip().split("\n")[0].strip().split('")')[1]
                print(
                    f'[+]Decrypted Hash {Red}[MD5ONLINE[IT]]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{Gotcha_ya}"{Normal} [[ #H#A#S#H# ]]\n')
    except requests.exceptions.SSLError as e:
        # Handle SSL errors specifically and continue execution
        print("[!] SSL Error on MD5ONLINE[IT], continue...\n")
    except requests.exceptions.RequestException as e:
        # Handle general request exceptions
        print(f"[!] Request Exception: {str(e)}\n")


# -------  URL NUMBER Twelve -------
 # ------- MAKE MANUAL ERROR -------

def ErrorMessage13():
    print(f"[-]Hashes: {Green}{args.ha}{Normal} -- > Request blocked, continue....\n")
    os.system('rm -r hashes.txt')

csrf_token = "c8a73ae8781fda43c447715ef36d7299"
s = random.randint(1, 6)
csrf_token2 = f"c8a{s}3ae{s}78{s}fda43c{s}47715ef36d7299"

Headers4 = {
    "Host": "Hashes.com",
    "Origin": "https://hashes.com",
    "referer": f"{URL12}",
    "Cookie": f"csrf_cookie={csrf_token2}, user=",
    "--data-binary": f"csrf_token={csrf_token2}&hashes={hash_itself}&captchaIdentifier=q8ec2b75b972f1305480df03045ebd4c&captcha=VfLEzS&submitted=true"
}

if hash_type == "md5" or hash_type == "sha256":
    command2 = f"curl -s -i -k -X 'POST' -H 'Host: {Headers4['Host']}' -H 'Origin: {Headers4['Origin']}' -H 'referer: {Headers4['referer']}' -H 'Cookie: {Headers4['Cookie']}' --data-binary '{Headers4['--data-binary']}' https://hashes.com/en/decrypt/hash | grep {hash_itself} > hashes.txt"
    os.popen(command2)
    time.sleep(3)

    with open("hashes.txt", "r") as hashes:
        try:
            for hashes1 in hashes.readlines():
                if "div" in hashes1:
                    div = hashes1.split(f"{hash_itself}:")[1].split("</div></pre>")[0]
                    print(f'[+]Decrypted Hash {Red}[Hashes]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{div}"{Normal} [[ #H#A#S#H# ]]\n')
                    os.system('rm -r hashes.txt')
                else:
                    ErrorMessage13()
        except Exception as e:
            ErrorMessage13()

# ------- MAKE MANUAL ERROR -------
def ErrorMessage14():
    print(f"[-]addr-: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

# ------- CONTINUE TO URL NUMBER 13 -------

data = {
    "md5": hash_itself,
    "x": "20",
    "y": "12"
}

header = {
    "Host": "md5.my-addr.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://md5.my-addr.com",
    "Connection": "close",
    "Referer": "http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php",
    "Upgrade-Insecure-Requests": "1",
}
if hash_type == "md5":
    try:
        req = requests.post(URL13, headers=header, data=data)
        soup = BeautifulSoup(req.text, "html.parser")
        for word in soup.findAll("div", class_="white_bg_title"):
            if "Hashed" in word.text and not "not found" in word.text:
                time.sleep(2)
                print(f'[+]Decrypted Hash {Red}[addr]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{word.text.split("Hashed string")[1].split(": ")[1].strip()}"{Normal} [[ #H#A#S#H# ]]\n')
    except Exception as e:
        ErrorMessage14()

# -------  URL NUMBER FourTeen -------ls
    # ------- MAKE MANUAL ERROR -------
def ErrorMessage15():
    print(f"[-]md5.rf.gd-: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

# ------- URL NUMBER 14 ------
headers = {
    "Host": "md5.rf.gd",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": f"{he}",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

# For this, i will use chromedriver with selenium
def is_chromedriver_in_directory():
    try:
        result = os.popen("which chromedriver").read().strip()
        if "chromedriver" in result:
            return result
        else:
            return None
    except Exception as e:
        return None

chromedriver_path = is_chromedriver_in_directory()
if chromedriver_path:
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")  # Add this to fix the Chrome crash issue
    chrome_options.add_argument("--disable-dev-shm-usage")  # Add this too for the same reason

    # Use Service object
    s = Service(chromedriver_path)
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(URL14)
    input_element = driver.find_element(By.NAME, "eny2")
    input_element.send_keys(f"{hash_itself}")
    input_element.send_keys(Keys.RETURN)
    time.sleep(3)

    # Hope it will work!
    try:
        # Adjust the below line to correctly identify and extract the decrypted hash from the page.
        hash_results = driver.find_element(By.CSS_SELECTOR, ".doutput").text
        print(f'[+]Decrypted Hash {Red}[md5.rf.gd]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{hash_results.split("Found : ")[1].strip()}"{Normal} [[ #H#A#S#H# ]]\n')
    except:
        ErrorMessage15()
        driver.quit()
else:
    print(f"[!]Note Please: No chromedriver was found in the system's PATH, continue WITHOUT {Green}md5.rf{Normal} ...\n")

# -------  URL NUMBER FourTeen -------
 # ------- MAKE MANUAL ERROR -------
def ErrorMessage16():
    print(f"[-]ttmd5-: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

# ------- URL NUMBER 14 ------
headers16 = {
    "User-Agent": he
}
req = requests.get(URL15, headers=headers16)
if "plain" in req.text:
    results = req.text.split(",")[2].split('"')[3]
    print(f'[+]Decrypted Hash {Red}[ttmd5]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{results}"{Normal} [[ #H#A#S#H# ]]')
    print(f'Please {Green}Note{Normal} -->> You have to sign-in/register before shows decrypted hashes.\n')
else:
    ErrorMessage16()

# -------  URL NUMBER SixTeen -------
 # ------- MAKE MANUAL ERROR -------
if hash_type == "md5":
    def ErrorMessage15():
        print(f"[-]passwordrecovery: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

    # ------- URL NUMBER 14 ------
    # Define base headers
    headers = {
        'User-Agent': he,
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://passwordrecovery.io',
        'Referer': 'https://passwordrecovery.io/md5/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Te': 'trailers',
    }

    # Use a session to maintain cookie session as suppose
    with requests.Session() as session:
        session.headers.update(headers)

        # Sending a GET request to receive a CSRF Token
        get_response = session.get("https://passwordrecovery.io/md5/")
        soup = BeautifulSoup(get_response.content, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

        # Now, send the POST request
        data_to_send = {
            "csrf_token": csrf_token,
            "hash": f"{hash_itself}",
        }
        post_url = "https://passwordrecovery.io/query/md5"
        post_response = session.post(post_url, data=data_to_send)
        response_text = post_response.text  # Convert the entire response content to string
        try:
            spl2 = response_text.split("The hash is:")
            results2 = spl2[1].split("<")[0].strip()
            print(f'[+]Decrypted Hash {Red}[passwordrecovery]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{results2}"{Normal} [[ #H#A#S#H# ]]')
        except Exception as e:
            ErrorMessage15()


# # -------  URL NUMBER SevenTeen -------
#  # ------- MAKE MANUAL ERROR -------
# if hash_type == "md5":
#     def ErrorMessage16():
#         print(f"[-]ttmd5: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

# URL = f"http://www.ttmd5.com/do.php?c=Decode&m=getMD5&md5={hash_itself}"
# headers17 = {
#     "User-Agent": he
# }

# # Make the request, Pull the results
# ttmd5_req = requests.get(URL)
# gets_results = ttmd5_req.text.split("plain")[1].split(":")[1].split("type")[0].split(",")[0]
# if "*" in gets_results:
#     print(f"Reminder:\n[-] You have to {Red}register{Normal}- > ttmd5.com to see the results!")
# else:
#     print(f'[+]Decrypted Hash {Red}[ttmd5]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":{gets_results}{Normal} [[ #H#A#S#H# ]]')
