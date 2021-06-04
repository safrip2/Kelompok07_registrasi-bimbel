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


def iduser():
    from string import digits, ascii_letters
    length = 6
    num1 = random.randint(1, 99)
    num2 = random.randint(4, 9)
    symbols = ascii_letters + digits
    secure_random = random.SystemRandom()
    iduser = (f"{num1}{num2}{''.join(secure_random.choice(symbols) for i in range(length))}")
    return iduser

def cardqr():
    from PIL import Image, ImageDraw, ImageFont

    image = Image.new('RGB', (1000, 600), (66, 245, 179))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=45)

    (x, y) = (50, 50)

    message = "PROSUS SEVEN"
    company = message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=80)
    draw.text((x, y), message, fill=color, font=font)

    # adding an unique id number. You can manually take it from user
    (x, y) = (550, 70)
    idno = iduser()
    message = str('ID ' + str(idno))
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (45, 200)
    message = pilihandaftar[1]
    name = message
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (45, 300)
    message = jenis_kelamin
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (245, 300)
    message = umur
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (45, 400)
    message = ttl
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (45, 500)
    message = kelas
    color = 'rgb(255, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (45, 600)
    message = noHp_Siswa
    temp = message
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (45, 700)
    message = alamat
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)

    # save the edited image

    image.save(str(name) + '.png')

    img = qrcode.make(str(company) + str(idno))  # this info. is added in QR code, also add other things
    img.save(str(idno) + '.bmp')

    til = Image.open(name + '.png')
    im = Image.open(str(idno) + '.bmp')  # 25x25
    til.paste(im, (550, 255))
    til.save(name + '.png')
    print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))
    eval(input('\n\nPress any key to Close program...'))


print("Silahkan pilih salah satu menu di bawah ini")
pilihanawal = str()
while pilihanawal !="0" :
    header()
    pilihanawal = input("1. Informasi Umum \n2. Daftar Langsung \nMasukkan pilihan Anda (tuliskan nomor saja): ")
    if pilihanawal == "1":
        pilihaninfo = input("1. Informasi daftar hari les \n2. Informasi pembagian kelas berdasarkan nilai tes \n3. Informasi biaya les \nMasukkan pilihan anda (Tuliskan angka saja): ")
        if pilihaninfo == "1":
            print("==Informasi Daftar Hari les==")
            print("PROSUS SEVEN memiliki 2 pilihan hari les:")
            print("1. Senin, Rabu, Jumat")
            print("2. Selasa, Kamis, Sabtu")
            time.sleep(5)
        elif pilihaninfo == "2":
            print("==Informasi Pembagian Kelas Berdasarkan Nilai Tes==")
            print("Pembagian kelas berdasarkan hasil tes:")
            print("1. Apabila nilai )
            time.sleep(5)
        elif pilihaninfo == "3":
            print("==Informasi Biaya les==")
            print("Biaya bimbingan")
            time.sleep(5)
        else:
            pass
    elif pilihanawal == "2":
        pilihandaftar = list(input("Masukkan Nama,Jurusan, dan Asal SMA anda (pisahkan masing - masing data dengan koma): ").split(","))
        header()
        from soal import score
        print(f"nilai anda adalah: {score}")
        if score >= 60:
            time.sleep(5)
            print("selamat anda lolos")
            durasibimbel = input("Silakan pilih durasi belajar anda \n1. 1 semester \n2. 1 tahun \nMasukkan pilihan anda (tulis angka saja):")
            if durasibimbel == "1":
                if score >= 90:
                    kelas = "LULUS"
                    harga = 6000000
                    print(f"Anda masuk kelas {kelas}")
                    break

                elif score >= 80 and score < 90:
                    kelas = "GRADE A"
                    harga = 7500000
                    print(f"Anda masuk kelas {kelas}")
                    break
                elif score >= 70 and score < 80:
                    kelas = "GRADE B"
                    harga = 8000000
                    print(f"Anda masuk kelas {kelas}")
                    break
                elif score >= 60 and score < 70:
                    kelas = "GRADE C"
                    harga = 8500000
                    print(f"Anda masuk kelas {kelas}")
                    break
                else:
                    pass
            elif durasibimbel == "2":
                if score >= 90:
                    kelas = "LULUS"
                    harga = 11000000
                    print(f"Anda masuk kelas {kelas}")
                    break
                elif score >= 80 and score < 90:
                    kelas = "GRADE A"
                    harga = 12500000
                    print(f"Anda masuk kelas {kelas}")
                    break
                elif score >= 70 and score < 80:
                    kelas = "GRADE B"
                    harga = 13000000
                    print(f"Anda masuk kelas {kelas}")
                    break
                elif score >= 60 and score < 70:
                    kelas = "GRADE C"
                    harga = 13500000
                    print(f"Anda masuk kelas {kelas}")
                    break
                else:
                    pass
        else:
            print("maaf anda tidak lolos test")
            sys.exit()

time.sleep(3)
ttl = input("Tempat, Tanggal Lahir : ")
umur = input('masukkan umur anda: ')
jenis_kelamin = input("Jenis Kelamin : ")
agama = input("Agama : ")
alamat = input("Alamat : ")
noHp_Siswa = input("Nomor Hp Siswa : ")
email = input("Email : ")
nama_Ayah = input("Nama Ayah : ")
nama_Ibu = input("Nama Ibu : ")
noHp_Ortu = input("No Hp Orang Tua : ")
pekerjaan_Ortu = input("Pekerjaan Orang Tua : ")
pilianharibelajar = input("Silahkan pilih hari belajar yang anda inginkan \n1. Senin, Rabu, Jumat \n2. Selasa, Kamis, Sabtu \nMasukkan pilihan anda (tulis angka saja): ")
print("Biaya yang harus anda bayarkan: ", harga)
diskon = input("Apakah anda memiliki kode disekon? (ya/tidak): ")
if diskon.upper()== "YA":
    kodediskon = input("Masukkan kode diskon : ")
    if kodediskon.upper() == "BERSAMASEVENMASUKPTN":
        hargaakhir = harga * 90 / 100
    else:
        pass
elif diskon.upper()== "TIDAK":
    hargaakhir = harga
else:
    pass
print("Harga yang harus anda bayarkan: ", hargaakhir)
print("tambahan")
cardqr()


