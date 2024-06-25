# Hashget

https://github.com/Adkali/Hashget/assets/90532971/2cc991f5-1fd7-422b-afee-673b521e634b

![Maintenance Badge](https://img.shields.io/maintenance/yes/2024)
![Kali Linux Badge](https://img.shields.io/badge/Developed%20on-Kali%20Linux-blueviolet)
![Kali Linux Badge](https://img.shields.io/badge/Tested%20On-LINUX-Linux)

**Hashget** is a Python tool designed for efficient hash decryption by querying known online sources. Instead of using local wordlists to match a hash, Hashget taps into online Rainbow-Tables to rapidly fetch potential matches. Right now supports md5/sha1/sha256/sha512. while it depends on online sources, things can change.

## Features

- Retrieves hash decryptions from online databases.
- Optimized for speed and efficiency.
- Supports MD5, SHA1, SHA256, SHA512 include base64 decoding.
- Ability to send requests through a proxy server (specifically configured for anonsurf on Kali Linux).
  
## Usage
<pre>
    |  _____  |A
    | |\ ___| | D
    | | |   | | K
    | | |___| | A
    \ | |____\| L
     \|_________I 
      Hashget v1.2
Github v1.2

usage: Hashget.py [-h] -t T [-ha HA] [-hf HF] [-p P] [-b B]

Hash decrypt using scrapping source.

options:
  -h, --help            show this help message and exit
  -t T, -type T         Hash type, for example sha1, md5, sha256, etc.
  -ha HA, -hashit HA    Hash itself to decrypt.
  -hf HF, -hashfile HF  Hash itself to decrypt from a file.txt
  -p P, -proxy P        Use proxy when sending request.
  -b B, -base64 B       Use it for Base64 decoding.
</pre>

#### Examples ####
<pre>
Type: MD5 --> Hash: dc92364159da3086106f6a0c9ee68d06 --> 'SecurePassword123'
</pre>

<h2>Updates</h2>

<p><strong>1/11:</strong> Resolved 'requests.exceptions.InvalidURL: Failed to parse' error. Ensure Python is updated and run the following commands:</p>
<pre>
apt update -y
pip3 install --upgrade urllib3
</pre>

<p><strong>17/11:</strong> Some sites, such as md5decrypt, are returning zero results. I am are actively working on a solution.</p>

<p><strong>14/12:</strong> If the binary library is missing, install it using:</p>
<pre>
pip install binary
</pre>

<p><strong>17/1:</strong> Various general fixes and improvements to outputs.</p>

<p><strong>23/03:</strong> Improved result printing and added two more websites to the sources.</p>

<p><strong>12/04:</strong> Added support for Base64 and include more online sources.</p>

<p><strong>14/09:</strong> Integrated Selenium for improved web parsing capabilities. Before using this feature, ensure that you have both the `requests` library and the `chromedriver` installed. Chromedriver should be located at `/usr/bin/chromedriver`. Install the required libraries and dependencies using the following commands:</p>
<pre>
pip install requests selenium
sudo cp path_to_your_chromedriver /usr/bin/chromedriver
</pre>
