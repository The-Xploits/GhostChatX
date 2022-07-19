import requests
import os
import sys

#CODE BY ALVIAN DWI SYAHPUTRA XI TKJ II

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
        log = "[+] GhostChatX Berhasil Terkirim Ke Nomer Target : {}\n".format(number)
        file_log = open("GhostChatX.log", "a")
        file_log.write(log)
        file_log.close()
    else:
        print("[!] Ghost Chat Gagal Terkirim...")
        os.exit(1)