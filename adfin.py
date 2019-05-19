#!/usr/bin/python
import sys,requests
charset="abcdefghijklmnopqrstuvwxyz1234567890"
leng=len(charset)
def cek(target):
	ree=requests.get("http://"+str(target)).status_code
	if ree == 200:
		print "[+] Found | url : "+target+" | code :",ree
		raw_input("Press Any Key To Countinue.")
	else:
		print "[-] Not Found | url : http://"+target
def crack(a,b,c,files):
	for x in range(leng):
		if b < a-1:
			crack(a,b+1,c+charset[x],files)
		else:
			cek(url+"/"+c+charset[x]+"/"+files)
if len(sys.argv) == 1:
	print """####################### | @author  : FilthyRoot
|A|D|M|I|N|F|I|N|D|E|R| | @github  : http://github.com/soracyberteam/
####################### | @version : 1.0

Usage : python adfin.py <url> <mode> [OPTION]

Mode  : -crack [Permutation]
	-brute [Wordlist]

Example : python adfin.py target.com brute /path/to/wordlist.txt
	  python adfin.py target.com crack <min> <max>"""
else:
	url=sys.argv[1]
	mode=sys.argv[2]
	if url and mode == "crack":
		b=int(sys.argv[3])
		c=int(sys.argv[4])
		files=raw_input("Files // Optional [Ex : login.php] : ")
		for i in range(b,c+1):
			crack(i,0,'',files)
	elif url and mode == "brute":
		b=sys.argv[3]
		f=open(b,'r')
		kontent=f.read()
		x=kontent.split("\n")
		for i in x:
			cek(url+"/"+i)
