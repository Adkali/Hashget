import binary as binary
import requests
from bs4 import BeautifulSoup
import time
import random
import argparse
import subprocess
import os

def Code_Colors():
    global Yellow, Red, Normal, BM, Green, Gray
    Yellow = "\033[1;33;40m"
    Red = "\033[1;31;40m"
    Normal = "\033[0;0m"
    BM = "\033[1;35;40m"
    Green = "\033[1;32;40m"
    Gray = "\033[1;30;40m"

Code_Colors()

def BannerShow():
    print(f'''\n
    |  _____  |{Yellow}A{Normal}
    | |\ ___| | {Red}D{Normal}
    | | |   | | K
    | | |___| | {BM}A{Normal}
    \ | |____\| L
     \|_________I 
      {Green}Hashget{Normal} v1.0\n''')

BannerShow()


def Parserr(err):
    print("[!] Syntax Error!")
    print("Usage: python3 [ Script/Name ] -t [Hash type(md5/sha1/sha256/sha512] -h [hash]")
    print("Having problems? let me know!")
    exit()


# ---------- ARGS TO BE DEFINED AND GETTING INTERCATS WITH USING THE CODE'S FLAGS ----------

parser = argparse.ArgumentParser(description="Hash decrypt using scrapping source.")
parser.error = Parserr
parser.add_argument('-t', '-type', type=str, required=True, help='Hash type, for example sha1, md5, sha256, etc.')
parser.add_argument('-ha', '-hashit', type=str, required=True, help='Hash itself to decrypt.')
parser.add_argument('-p', '-proxy', type=str, required=False, help="Use proxy when sending request.")
parser.add_argument('-b', '-base64', type=str, required=False, help="use it for Base64 decoding.")
args = parser.parse_args()

def Operators():
    global hash_type, hash_itself
b64 = args.b
hash_itself = args.ha
hash_type = args.t
pro = args.p
Operators()

# ------- CHECK HASH LENGTH AND COMPARE WITH OTHER HASH -------
md5ex = '202cb962ac59075b964b07152d234b70'
sha1ex = '40bd001563085fc35165329ea1ff5c5ecbdbbeef'
sha256ex = 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'
sha512ex = '3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2'
if len(hash_itself) != len(md5ex) or hash_type != "md5":
    if len(hash_itself) != len(sha1ex) or hash_type != "sha1":
        if len(hash_itself) != len(sha256ex) or hash_type != "sha256":
            if len(hash_itself) != len(sha512ex) or hash_type != "sha512":
                def HashesList():
                    print("What happened? use the right HASH please.")
                    print("Supported hashes(lowercase):")
                    print("md5, sha1, sha256, sha512.")
                    print("Soon more will come. Try again please")
                    exit()

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
URL = f"https://hashtoolkit.com/decrypt-hash/?hash={hash_itself}"
URL2 = f"https://decrypt.tools/client-server/decrypt?type={hash_type}&string={hash_itself}"
URL3 = f"https://md5.gromweb.com/?md5={hash_itself}"
URL4 = f"https://sha1.gromweb.com/?hash={hash_itself}"
URL5 = "https://md5decrypt.net/en/"
URL6 = "https://md5decrypt.net/en/Sha1/"
URL7 = "https://md5decrypt.net/en/Sha256/"
URL8 = "https://cmd5.org/default.aspx/"
URL9 = "https://sha1.web-max.ca/index.php"
print("Pulling Out Hash Decryption, Please Wait.....\n")
time.sleep(3)

# ------- BASE64 DECODE -------
# SOON!

# ------- URL NUMBER ONE -------
  # ------- MAKE A MANUAL ERROR -------
def ErrorMessage():
    print(f"[-] HashToolKit: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

global links
try:
    r = requests.get(URL, headers=Headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.findAll("a", href=True)
    elif r.status_code == 404:
        print("Page not found, exit...")
        exit()

except ConnectionError:
    print("Something went wrong, try again please")
except Exception as e:
    print(e)

# ------ CONTINUE CODE -------

try:
    for split in links:
        L = split.get("href")
        if "/generate-hash/?text=" in L:
            L2 = L.split("/generate-hash/?text=")

    if not L2:
        ErrorMessage()
    else:
        print(f'[+]Decrypted Hash {Red}[HashToolKit]:{Normal}  [[ #H#A#S#H# ]] {Yellow}"text":"{L2[1]}"{Normal} [[ #H#A#S#H# ]]\n')

except NameError:
    ErrorMessage()
except Exception as e:
    print(e)

# ------- MAKE A MANUAL ERROR  -------
def ErrorMessage2():
    print(f"[-]Decrypt.Tools: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

# ------- CONTINUE URL NUMBER TWO -------
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

# ------- MAKE A MANUAL ERROR -------
def ErrorMessage3():
    print(f"[-]Md5.GromWeb: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")

 # ------- CONTINUE TO URL NUMBER THREE -------
   # ------- APPEND TO LIST2 [CLASS TAGS]
List2 = []
if hash_type == "md5":
    r = requests.get(URL3, params=Headers)
    try:
        if r.status_code == 200:
            md5soup = BeautifulSoup(r.content, "html.parser")
            for i in md5soup:
                md5split = md5soup.findAll("em", {"class": "long-content string"})
                for i in md5split:
                    if 'long-content string' in f"{i}":
                        List2.append(i)
    except IndexError:
        ErrorMessage3()
    except Exception as e:
        print(e)
# ------- FINISH TRY,EXCEPT AND USE [2] FOR RESULTS -------
    try:
        for i in List2[2]:
            print(f'[+]Decrypted Hash {Red}[Md5.GromWeb]:{Normal} [[ #H#A#S#H# ]] {Yellow}"text":"{i}"{Normal} [[ #H#A#S#H# ]]\n')
    except IndexError:
        ErrorMessage3()
else:

    pass

# ------- MAKE A MANUAL ERROR -------
def ErrorMessage4():
    print(f"[-]SHA1.GromWeb: {Green}{args.ha}{Normal} -- > Hash does not exist in database\n")

  # ------- CONTINUE TO URL NUMBER FOUR -------
    # ------- APPEND TO LIST3 [CLASS TAGS]
List3 = []
if hash_type == "sha1":
    r = requests.get(URL4, params=Headers)
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

 # ------- CONTINUE URL NUMBER 5 [md5decrypt/MD5] -------
recaph = "HFZXdndg5GLD85M3tSS11DSh94GxBlcT8zBQUrMjdnDz0aF3Y0EX4NFC56RDNudGlye2I8FhMUZxMYelNRIVBtIhJsOipXcB9YQ1Vqd1ROWE18VBA_TGAuLV0yYhMUYhMUGztFVDBVbjADHSg6UGIPLlZncEBGa29dNltGY3xiRXU_BntLTA9zbx94GxBidg"
a = "curl -i -k -s -X POST -d "
b = f"'hash={args.ha}&recaptchaResponse={recaph}&button_value=Decrypt'"
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

# ------- MAKE MANUAL ERROR -------
def ErrorMessage6():
    print(f"[-]MD5DECRYPT-sha1: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")
    os.system('rm -r sha1data.txt')
time.sleep(1)

 # ------- CONTINUE TO URL NUMBER 6 -------
f = "curl -i -k -s -X POST -d "
g = f"'hash={args.ha}&decrypt=Decrypt'"
h = " -H 'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'"
i = f" {URL6}"
j = f" | grep {args.ha}"
command = f + g + h + i + j

Result2 = []
if hash_type == "sha1":
    a = os.popen(f'{command} > sha1data.txt')
    time.sleep(20)

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

# ------- MAKE MANUAL ERROR -------
def ErrorMessage7():
    print(f"[-]MD5DECRYPT-SHA256: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")
    os.system('rm -r sha256data.txt')
    time.sleep(2)

# ------- CONTINUE URL NUMBER 7 [md5decrypt/Sha256]

f = "curl -i -k -s -X POST -d "
g = f"'hash={args.ha}&decrypt=Decrypt'"
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
 # ------- CONTINUE TO URL NUMBER 8 -------
List4 = []
Headers = {"User-Agent:": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
           "Accept:": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Language:": "en-US,en;q=0.5",
           "Accept-Encoding:": "gzip, deflate",
           "Content-Type:": "application/x-www-form-urlencoded",
           "Content-Length": "1995",
           "Origin": "https://www.cmd5.org",
           "Referer:": "https://www.cmd5.org/default.aspx",
           "--data-binary": f"__EVENTTARGET=Button1&__EVENTARGUMENT=&__VIEWSTATE=d51CtXEQp5Z7fG8GzCoHrIOtUp%2BFw9ouqpJwe%2BztSK3JfyfcrWVBkmZNtsNPTG%2BR1R%2BlSqP0EEWquG2pPM3NAAL4L%2FRsFOZVNpG44cP5cRkpso%2FGb0%2F%2FJHRZIjuiRaeEoFT2ke6JoCv424NC7XMVXZdpf%2F0otfpcixAWiv%2B5itLLSJMI0Xtm1%2FhvSt88yC04QfP39w%2BlRBxrxKznPdx17nVgAYSE6xT6hEm%2F0znc659wSncsfvYUVnjQdIONsM6dMbHRAoytk30cXdrA8hOodv9Fq4E6zDLK13jN%2BRaDE7xf%2B9%2BT%2FlOS4XpIdEvyVcfu374ZZfTawU0UHbvpJkRs%2BualnJ22nTzLJjnX4kuX3FoGAvKMgSdYm1oAUlRuiSSDwiz4K%2FCicq2M0BtI4EIuk5HyY1YF7wjiIyaiSUxi009oUQz8FwbeBswxgANgAgOv%2BgKjpe80VH3knQQUKAQC6gcCWpP77ElAvteydqcf%2BCtkJhpbii5e%2BVxldRClN8eCBRcwsRZCXIdRUqNkJantdGaR2WgYkEeduxGDCp1Nduap%2B%2BeOC%2FaEhkUYXXoh84q7x9kAi4TyQyg0XVMjnQNXqyqxE%2BuUyv9Itx%2F7kwNgWai%2FcsTJqbAwVvDgnG8sRD0RN6FYJVyMYp6tps63d9dS7EAEyowLmQuoB2XCXc%2FglQE6p5c0swPJoDfu%2FXFttf3QNf7Vx3w6MOW%2BsdTxz08KVJ%2FPdGxJexZh51bfWW%2FjjeY544u0YFTtgBLcNTpSJUa3sA18iBV6Q5TzirJ5uWRQBz6HWxk%2Fr4TrtrQfVZQ4svB62zn7MTSUcQDFJlXc76%2FiSzPB1Nrv9atL%2FFx9gUe%2Fq%2B9IuN2iaOvUsVRG1uF%2BNzI0k%2BuLeyATiCwbyCWkO%2BaewCNMItkJR67kvZz8Wn133SRp9F5pRrtJ4kFXyFBLRSZYuQ05TzJr4fQ4L%2FNzqf9qbLN0bQWHdoMw3yJ9gtF3uMPTUQa%2F%2BLF7XXxkuXXhuYQn3fAubKlomWcJ2hE%2F6h3zzA8K96xf4hMK9BFBq4Kmlj75tOMPGOsVWLDShbdZfOD2nB5mpjYqnB1QyE0Ey0lKcYap4ItMxkNvKBCOzbdd2nAIXfOiOGr0BA%2Fq5NM8eFYphk%2FcU%2Bz1vUpMO%2FKRCjBukXLCn59fYwOv26GAqesp94Zavf3waBLTHjv3bs6eNvFoYQatmA8Uxxi8dwaomXwc5nmAVWfr9V2%2FI%2B2EmchgYJnHT2Kfc84wIxSY7o28wjh6%2BX2Xje1NRaJovExoVacj52Jes%2BSyeujCd9K1ThmplxfUwNpzXEdQHVEAT%2FCkZxYeE6OvNNefH95OCxoiURy%2FAwzU9ScKoF0I64yCJc7eEsITktDsSa%2F1Z90fBLjGa3QOxrg5LoXhzQWjOweDV1Rq465PGKfu0Jkki9UXz3I4KdpAWLmusuCJ%2Fic9fA%3D%3D&__VIEWSTATEGENERATOR=CA0B0334&ctl00%24ContentPlaceHolder1%24TextBoxInput={hash_itself}&ctl00%24ContentPlaceHolder1%24InputHashType={hash_type}%28{hash_type}%28%24pass%29%29&ctl00%24ContentPlaceHolder1%24Button1=decrypt&ctl00%24ContentPlaceHolder1%24HiddenField1=&ctl00%24ContentPlaceHolder1%24HiddenField2=qz08XOD6pv6f52Ly0KvrN4x2r%2FZuMyKZH%2Br0xseI3KPMs2qsvRylYS67QXhX3JxR' https://www.cmd5.org/default.aspx/ | grep LabelAnswer"
           }

command = f"curl -i -s -k -X 'POST' -H 'User-Agent: {Headers['User-Agent:']}' -H 'Accept: {Headers['Accept:']}' -H 'Accept-Language: {Headers['Accept-Language:']}' -H 'Accept-Encoding: {Headers['Accept-Encoding:']}' -H 'Content-Type: {Headers['Content-Type:']}' -H 'Content-Length: {Headers['Content-Length']}' -H 'Origin: {Headers['Origin']}' -H 'Referer: {Headers['Referer:']}' --data-binary '{Headers['--data-binary']}"
time.sleep(2)
if pro == "set":
    try:
        subprocess.Popen("anonsurf start {0} >/dev/null 2>&1 &", shell=True)
    except Exception as e:
        print("Install 'kali-anonsurf' please [ sudo apt-get install kali-anonsurf -y ]")
time.sleep(3.5)
os.popen(f'{command} > cmd5.txt')
time.sleep(4)
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

# ------- MAKE MANUAL ERROR -------
def ErrorMessage9():
    print(f"[-]SHA1.WEB-MAX-: {Green}{args.ha}{Normal} -- > Hash does not exist in database.\n")
# ------- CONTINUE TO URL NUMBER 9 -------
 # ------- ADD TO LIST -------
Headers2 = {
    "User-Agent": "Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0",
    "Host": "sha1.web-max.ca",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Origin": "https://sha1.web-max.ca",
    "Referer": "https://sha1.web-max.ca/index.php",
    "Connection": "close",
    "--data-binary": f"string={hash_itself}&key=13fd&check_code=7985&hidden_code=%0C6%01l%06%3C%0Di&decode=sha1+hash+decode",
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
