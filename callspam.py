call.py

#/usr/bin/python

# Thanks To Aylward Hxr

# (c) Hax28dh8Sec

# modif by Mr.404


import os

import subprocess as sp

os.system('clear')

print("\033[1;33m[!] Please Wait...")

sp.call('pip install requests', shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)

import requests


def spam():

	os.system("clear")

	print("""

\033[1;32m+---------------------------------------+

\033[1;32m|\033[1;31m SPAM TELEPON \033[1;32m|

\033[1;32m|\033[1;37m CREATE BY WIDHISEC ft. Mr.404 \033[1;32m|

\033[1;32m+---------------------------------------+

(*) Ketik Enter Untuk Melewati Step""")

	no1 =input("Masukkan Nomor Telepon1 =>")

	no2 =input("Masukkan Nomor Telepon2 =>")

	no3 =input("Masukkan Nomor Telepon3 =>")

	no4 =input("Masukkan Nomor Telepon4 =>")

	no5 =input("Masukkan Nomor Telepon5 =>")

	print("[-] STATUS:")

	r1 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no1)

	print("[+] SPAM1",r1.json()["msg"])

	r2 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no2)

	print("[+] SPAM2",r2.json()["msg"])

	r3 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no3)

	print("[+] SPAM3",r3.json()["msg"])

	r4 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no4)

	print("[+] SPAM4",r4.json()["msg"])

	r5 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no5)

	print("[+] SPAM5",r5.json()["msg"])



print()

pilih = 'y'

while (pilih != 'n'):

	spam()

	pilih = input("\nspam lagi? (y/n) ")

	if pilih == 'n':

		print("Jahatt lu guys :)\n")

