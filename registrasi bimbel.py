import random
import datetime
import qrcode
import time
import sys
import threading
score = 0
def header():
    d_date = datetime.datetime.now()
    reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\tPROSUS SEVEN\t\t\t\t\t  %I:%M:%S %p")
    print(
        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(reg_format_date)
    print(
        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

header()

print("Silahkan pilih salah satu menu di bawah ini")
pilihanawal = input("1. Informasi Umum \n2. Daftar Langsung \nMasukkan pilihan Anda (tuliskan nomor saja): ")
if pilihanawal == "1":
    pilihaninfo = input("1. Informasi daftar hari les \n2. Informasi pembagian kelas berdasarkan nilai tes \n3. Informasi biaya les \nMasukkan pilihan anda (Tuliskan angka saja): ")
    if pilihaninfo == "1":
        print("informasi daftar hari les")
    elif pilihaninfo == "2":
        print("informasi pembagian kelas berdasarkan nilai tes")
    elif pilihaninfo == "3":
        print("informasi biaya les")
    else:
        pass
elif pilihanawal == "2":
    pilihandaftar = input("Masukkan Nama,Jurusan, dan Asal SMA anda (pisahkan masing - masing data dengan koma): ")
    pilihandaftar_list = pilihandaftar.split(",")
    print("\n")
    from soal import score
    print(f"nilai anda adalah: {score}")
    if score >= 60:
        time.sleep(5)
        print("selamat anda lolos")


