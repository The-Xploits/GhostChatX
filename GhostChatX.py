import requests
import os
import sys

def optional():
    print("\n\nSCRIPT BY THE EXPLOIT V1.0\n\nCARA PEMAKAIAN:\n\n[?] Number WhatsApp : +628xxxx\n[?] Jumplah Spam : 3\n\n\n")
    os.system("echo -ne '\033]0;Ghost ChatX V1.0\007'")

url = "https://aink-sanz.herokuapp.com/api/free-tutorial-spam-wa"

optional()
number = raw_input("[?] Number WhatsApp : ")
spam = input("[?] Jumplah Spam : ")

data = {
    "nomor":number
}

for i in range(spam):
    TheXploit = requests.get(url, params=data)
    if "Berhasil Ngab ! .. Subrek Yt FREE TUTORIAL." in TheXploit.text:
        print("[+] Ghost Chat Berhasil Terkirim...")
    else:
        print("[!] Ghost Chat Gagal Terkirim...")
        os.system("echo -ne '\033]0;Tunggu 30 Menit\007'")
        os.exit(1)