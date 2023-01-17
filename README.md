# Hashget
<img src="https://img.shields.io/badge/Maintained%3F-Yes-96c40f"> <img src="https://img.shields.io/badge/Developed%20on-kali%20linux-blueviolet">
<h4>Pull Hashes Decryption From Online Source Using Python.</h4>Hashget takes hash as argument using '-ha' flag and '-t' as type of hash, and pulling the decryption from the given URL's. Hashget uses as a hash puller instead of using wordlists for the given hash to find a match when does. Online service keeps hashes in some Rainbow-Table and when hash is givven, the results come more faster, and millions of hashes are over there, so i made this tool for my own convenience when using them at once.

# Usage
<pre>
    |  _____  |A
    | |\ ___| | D
    | | |   | | K
    | | |___| | A
    \ | |____\| L
     \|_________I 
      Hashget v1.2
</pre>

Hashget is very easy to use.<br>using the '-t' (type) argument with '-ha' (hash itself) will give results.<br>Soon i will add the option of using a wordlist of hashes so the code could read from a TXT file, and send the hashes inside with each request in a loop time. for now, the supported hashes are MD5, SHA1, SHA256, SHA512. 

<pre>
  -h, --help          show this help message and exit
  -t T, -type T       Hash type, for example sha1, md5, sha256, etc.
  -ha HA, -hashit HA  Hash to decrypt
  -p P, -proxy P      Use proxy when sending request
</pre>

# Examples
Type: MD5 -- > Hash: dc92364159da3086106f6a0c9ee68d06 -- > 'SecurePassword123'

![2](https://user-images.githubusercontent.com/90532971/198870035-49749cc6-07fd-45b0-840d-2b08573d3542.png)<br>
as you can see from above, the hash seems to be public for now only in 1 site - MD5.GROMWEB. using the code would give you the results much more faster instead of using the browser to look for the hashes decryption. Now, make a use of the '-p-' flag with "set", would give you the option of sending request through proxy server only if you have anonsurf on you machine [ kali ]. making the code run again on same hash with '-p', results in pulling the hash ( if it does in the public database ) :<br>

![3](https://user-images.githubusercontent.com/90532971/198870319-31e1444a-5bd6-4860-a552-948df0469595.png)

# Updates
For now, supported hash are MD5, SHA1, SHA256, SHA512.Hope you will find this tool useful and a shortime maker. if you have any problems or might going some wrong request, please make an issue. make sure you install re req file before runing the code.
# Notes
1/11 - for some having problems while run the code, and gets error like 'requests.exceptions.InvalidURL: Failed to parse', make sure python is updated or use the following commands. if you having another problems, please let me know.<br>
1. apt update -y
2. pip3 install --upgrade urllib3
<br>
<br>
<b>17/11 - recap result in nothing from some sites, which gives zero results back.i will trying to make it work soon i believe. thanks for updating me! current site: md5decrypt. beside that, seems everything else still working as it should. DM me if you have any problems.</b><br><br>
<b>14/12 - if binary is missing, use "pip install binary".</b><br><br>
<b>17/1 - General Fix & Ouputs.</b>
