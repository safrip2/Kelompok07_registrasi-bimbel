import random
import datetime
import qrcode
import time
import sys
import csv
import os
import smtplib
# untuk email dan password memang disembunyikan di environment system, maka kalian perlu men setting dulu melalui control panel
EMAIL_ADDRESS = os.environ.get('DB_USER')
EMAIL_PASSWORD = os.environ.get('DB_PASS')

# pre defined
score = 0
hargaakhir = 0
ttl = str
umur = str
jeniskelamin = str
agama = str
phone = str
alamat = str
email = str
nama_ayah = str
nama_ibu = str
haribelajar = str


# fungsi header
def header():
    d_date = datetime.datetime.now()
    reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\tPROSUS SEVEN\t\t\t\t\t  %I:%M:%S %p")
    print('+' * 79)
    print(reg_format_date)
    print('+' * 79)


# membuat nomor identitas siswa
def iduser():
    from string import digits, ascii_letters
    length = 6
    num1 = random.randint(1, 99)
    num2 = random.randint(4, 9)
    symbols = ascii_letters + digits
    secure_random = random.SystemRandom()
    idsiswa = f"{num1}{num2}{''.join(secure_random.choice(symbols) for i in range(length))}"
    return idsiswa


# masukkan data diri siswa yang kemudian untuk fungsi cardqr dan di store ke database
def inputdata():
    global ttl
    global umur
    global jeniskelamin
    global agama
    global phone
    global alamat
    global nama_ayah
    global nama_ibu
    global harga
    global hargaakhir
    global haribelajar
    global pilihanharibelajar
    time.sleep(3)
    if not os.path.exists('database.csv'):
        # jika file database.csv tidak ada, program akan melakukan write file
        with open("database.csv", "w") as newfile:
            fieldnames = ['nama', 'jurusan', 'asal sma', 'kelasbimbel',
                          'phone', 'email', 'jenis kelamin', 'alamat',
                          'ttl', 'umur', 'agama', 'nama ayah', 'nama ibu', 'no hp ortu', 'ID Siswa']
            csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames)
            csv_writer.writeheader()
            newfile.close()
    with open('database.csv', 'a') as f:  # jika ada, program tinggal menabahkan data baru
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        nama = datanama
        jurusan = datajurusan
        asalsma = datasma
        kelasbimbel = kelas
        phone = input("Nomor Hp Siswa : ")
        jeniskelamin = input("Jenis Kelamin: ")
        alamat = input("Alamat: ")
        ttl = input("Tempat, Tanggal Lahir : ")
        umur = input('masukkan umur anda: ')
        agama = input("Agama : ")
        nama_ayah = input("Nama Ayah : ")
        nama_ibu = input("Nama Ibu : ")
        no_hp_ortu = input("Nomor Hp salah satu Orang Tua : ")
        w.writerow([nama, jurusan, asalsma, kelasbimbel, phone, email,
                    jeniskelamin, alamat, ttl, umur, agama, nama_ayah,
                    nama_ibu, no_hp_ortu, nomorid])
        f.close()
    time.sleep(3)
    pilianharibelajar = input(
        "\n\t\t\t==========H A R I  B E L A J A R==========\t\t\t\nSilahkan pilih hari belajar yang anda inginkan \n1. Senin, Rabu, Jumat \n2. Selasa, Kamis, Sabtu \nMasukkan pilihan anda (tulis angka saja): ")
    if pilianharibelajar == 1:
        haribelajar = "senin, rabu, jumat"

    elif pilianharibelajar == 2:
        haribelajar = "selasa, kamis, sabtu"

    print()
    print(80 * '=')
    print(f"Biaya yang harus anda bayarkan: Rp.{harga}")
    print(80 * '=')
    print()
    diskon = input("Apakah Anda Memiliki Kode Diskon? (ya/tidak): ")
    if diskon.upper() == "YA":
        kodediskon = input("Masukkan Kode Diskon : ")
        if kodediskon.upper() == "BERSAMASEVENMASUKPTN":
            hargaakhir = harga * 90 / 100
        else:
            print("kode yang anda masukkan salah!")
            hargaakhir = harga
    elif diskon.upper() == "TIDAK":
        hargaakhir = harga
    else:
        hargaakhir = harga
    print(f"Harga Yang Harus Anda Bayarkan: Rp.{hargaakhir}")
    cardqr()


# membuat kartu anggota dan qrcode
def cardqr():
    from PIL import Image, ImageDraw, ImageFont
    image = Image.new('RGB', (1000, 600), (66, 245, 179))  #1000, 6000 = pixel, 66... = warna canvas
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=45)
    (x, y) = (50, 50)
    message = "PROSUS SEVEN"
    company = message
    color = 'rgb(0, 0, 0)'  # color 0 0 0 = hitam
    font = ImageFont.truetype('arial.ttf', size=60)  # ukuran 60
    draw.text((x, y), message, fill=color, font=font)  # draw pada canvas x dan y dengan message = prosus seven FILL
    # adding an unique id number dari input user nanti
    (x, y) = (600, 70)
    # add id card siswa dari fungsi iduser
    idno = nomorid
    message = str('ID ' + str(idno))
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=40)
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (45, 200)
    # input nama di awal diproses
    message = datanama
    name = message
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), message, fill=color, font=font)
    # input jenis kelain di proses
    (x, y) = (45, 300)
    message = jeniskelamin
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (260, 300)
    message = umur
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    # input tempat tanggal lahir diproses
    (x, y) = (45, 400)
    message = ttl
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    # input kelas diproses
    (x, y) = (45, 500)
    message = kelas
    color = 'rgb(255, 0, 0)'  # red
    draw.text((x, y), message, fill=color, font=font)
    # save the edited image
    image.save(str(name) + '.png')
    img = qrcode.make(str(company) + str(idno) + str(name))  # this info. is added in QR code, also add other things
    img.save(str(idno) + '.bmp')
    # final proses
    til = Image.open(name + '.png')
    im = Image.open(str(idno) + '.bmp')  # 25x25
    til.paste(im, (550, 255))
    til.save(name + '.png')
    removebmp()
    print(('\n\nKartu Anggota anda berhasil dibuat dengan nama ' + name + '.png'))


# memnentukan kelas berdasarkan nilai
def penentuankelas():
    print(80 * '=')
    text = f"Anda Masuk Kelas {kelas}"
    print(text.center(75))
    print(80 * '=')
    print()
    print('\t\t\t==========B I O D A T A   D I R I==========\t\t\t')

def akun():
    print(80 * '=')
    text2 = "selamat bergabung"
    print(text2.center(75))
    print(f"""untuk saat ini akun anda adalah:
username: {nomorid}
password: {nomorid + datanama}
segera rubah password anda di dashboard""")

# membuat struk
def struk():
    print("")
    print("+" * 30)
    bimbel = "BIMBEL PROSUS SEVEN"
    judul = bimbel.center(30)
    print(judul)
    print("+" * 30)
    print("")
    bukti = "BUKTI PEMBAYARAN"
    buktibayar = bukti.center(30)
    print(buktibayar)
    garis = "-" * 20
    garisbawah = garis.center(30)
    print(garisbawah)
    print("Nama                   : %s" % datanama)
    print("ID Siswa               : %s" % nomorid)
    print("Tanggal Pembayaran     :", datetime.date.today())
    print("Nominal Pembayaran     : Rp. %d" % hargaakhir)
    akun()

#hapus file qr.bmp
def removebmp():
    if os.path.exists(f"{nomorid}.bmp"):
        os.remove(f"{nomorid}.bmp")
    else:
        pass

# program utama
pilihanawal = str()
while pilihanawal != "0":
    global kelas
    header()
    print()
    print('\t\t\t\t\t\t\t==SELAMAT DATANG==\t\t\t\t\t\t\t\t ')
    print()
    print('\t\tBimbel PROSUS SEVEN Siap Membantu Kamu Menuju Masa Depanmu!\t\t')
    print('\t\t\t\t\tPROSUS SEVEN dengan 7 Keunggulan:\t\t\t\t\t')
    print('\t\t\t1.Smart dan Profesional Tentor Lulusan PTN\t\t\t\t')
    print('\t\t\t2.Pertemuan 3x Seminggu, 2 Pelajaran @90 Menit\t\t\t\t')
    print('\t\t\t3.Modul dan Soal-Soal Persis Seperti UTBK Tahun-Tahun Lalu\t\t\t')
    print('\t\t\t4.Free konsultasi PR dan Tugas\t\t\t\t')
    print('\t\t\t5.TryOut dan Simulasi UTBK 2 Minggu Sekali\t\t\t')
    print('\t\t\t6.Ruang Kelas Nyaman dan Dibatasi Max 15 Murid/kelas\t\t\t')
    print('\t\t\t7.Konsultasi Penjurusan oleh Wali Kelas\t\t\t\t')
    print()
    print('\t\t\t\t\t\t'"BERSAMA 'SEVEN' MASUK 'PTN'!"'\t\t\t\t\t\t\t')
    print()
    print(80 * '+')
    print()
    print("Silahkan pilih salah satu menu di bawah ini, masukkan 0 untuk keluar dari program")
    pilihanawal = input("1. Informasi Umum \n2. Daftar Langsung \nMasukkan pilihan Anda (tuliskan nomor saja): ")
    print()
    print(80 * '+')
    print()
    if pilihanawal == "1":
        print('\t\t\t==========I N F O R M A S I   U M U M==========\t\t\t\t')
        pilihaninfo = input(
            "1. Informasi daftar hari les \n2. Informasi pembagian kelas berdasarkan nilai tes \n3. Informasi biaya les \nMasukkan pilihan anda (Tuliskan angka saja): ")
        if pilihaninfo == "1":
            print()
            print(80 * '+')
            print()
            print('\t\t\t==========INFORMASI DAFTAR HARI LES==========\t\t\t')
            print('PROSUS SEVEN memiliki 2 pilihan hari les:')
            print("1. Senin, Rabu, Jumat")
            print("2. Selasa, Kamis, Sabtu")
            time.sleep(5)
        elif pilihaninfo == "2":
            print(80 * '+')
            print()
            print('\t==========INFORMASI PEMBAGIAN KELAS BERDASARKAN HASIL TES==========\t\t')
            print('Pembagian kelas berdasarkan hasil tes:')
            print("1. Apabila nilai >=90 maka anda masuk ke kelas LULUS")
            print("2. Apabila nilai >=80 dan <90 maka anda masuk ke kelas GRADE A")
            print("3. Apabila nilai >=70 dan <80 maka anda masuk ke kelas GRADE B")
            print("4. Apabila nilai >=60 dan <70 maka anda masuk ke kelas GRADE C")
            print("NOTES : Apabila nilai anda tidak memenuhi syarat maka anda tidak bisa mengikuti kelas")
            time.sleep(5)
        elif pilihaninfo == "3":
            print(80 * '+')
            print()
            print('\t\t\t\t==========INFORMASI BIAYA LES==========\t\t\t\t')
            print('Biaya bimbingan belajar dikelompokkan menjadi 2 kategori yaitu PERSEMESTER dan PERTAHUN')
            print('Apabila memilih kategori PERSEMESTER maka biaya :')
            print(" 1. kelas LULUS = Rp.6.000.000 ")
            print(" 2. kelas GRADE A = Rp.7.500.000 ")
            print(" 3. kelas GRADE B = Rp.8.000.000 ")
            print(" 4. kelas GRADE C = Rp.8.500.000 ")
            print('Apabila memilih kategori PERTAHUN maka biaya :')
            print(" 1. kelas LULUS = Rp.11.000.000 ")
            print(" 2. kelas GRADE A = Rp.12.500.000 ")
            print(" 3. kelas GRADE B = Rp.13.000.000 ")
            print(" 4. kelas GRADE C = Rp.13.500.000 ")
            time.sleep(5)
        else:
            pass
    elif pilihanawal == "2":
        print('\t\t\t ==========D A F T A R   L A N G S U N G==========\t\t\t')
        datanama = input("Masukkan Nama Anda : ")
        datajurusan = input("Masukkan Jurusan Anda : ")
        datasma = input("Masukkan Asal SMA Anda : ")
        email = input("Email : ")
        nomorid = iduser()
        print()
        print(80 * '+')
        print()
        print('\t\t\t\t==========TEST PEMBAGIAN KELAS==========\t\t\t\t')
        print("Test Pembagian Kelas dalam Bimbel Prosus Seven adalah untuk menentukan kelas yang akan ")
        print("siswa dapatkan guna memaksimalkan kegiatan pembelajaran dalam Bimbel Prosus Seven.")
        print("Test hanya dapat berlangsung 1x dengan durasi 10 menit. Diharapkan siswa mengerjakannya")
        print("dengan sungguh-sungguh. ")
        print('\t\t\t\t\t\t\t-SELAMAT MENGERJAKAN-\t\t\t\t\t\t')
        print()
        header()
        from soal import score  # Mengimport File Soal

        print()
        print(80 * '=')
        print(f"NILAI ANDA ADALAH: {score}")
        print(80 * '=')
        print()
        if score >= 60:
            print(80 * '+')
            print('\t\t\t\t\t\t-Selamat Anda LOLOS!!-\t\t\t\t\t')
            print(80 * '+')
            print()
            maksimalinput = 3
            jumlahinput = 0
            while jumlahinput < maksimalinput:
                durasibimbel = input(
                    "Silakan pilih durasi belajar anda \n1. 1 semester \n2. 1 tahun \nMasukkan pilihan anda (tulis angka saja): ")
                jumlahinput += 1
                if durasibimbel != "1" and durasibimbel != "2":
                    print("mohon pilih salah satu, anda hanya boleh melakukan 3 kesalahan input!")
                elif durasibimbel == "1":
                    if score >= 90:
                        kelas = "LULUS"
                        harga = 6000000
                        penentuankelas()
                        inputdata()
                        struk()
                        break
                    elif 80 <= score < 90:
                        kelas = "GRADE A"
                        harga = 7500000
                        penentuankelas()
                        inputdata()
                        struk()
                        break
                    elif 70 <= score < 80:
                        kelas = "GRADE B"
                        harga = 8000000
                        penentuankelas()
                        inputdata()
                        break
                    elif 60 <= score < 70:
                        kelas = "GRADE C"
                        harga = 8500000
                        penentuankelas()
                        inputdata()
                        struk()
                        break
                    else:
                        pass
                elif durasibimbel == "2":
                    if score >= 90:
                        kelas = "LULUS"
                        harga = 11000000
                        penentuankelas()
                        inputdata()
                        struk()
                        break
                    elif 80 <= score < 90:
                        kelas = "GRADE A"
                        harga = 12500000
                        penentuankelas()
                        inputdata()
                        struk()
                        break
                    elif 70 <= score < 80:
                        kelas = "GRADE B"
                        harga = 13000000
                        penentuankelas()
                        inputdata()
                        struk()
                        break
                    elif 60 <= score < 70:
                        kelas = "GRADE C"
                        harga = 13500000
                        penentuankelas()
                        inputdata()
                        struk()
                        break
                    else:
                        pass
            sys.exit()

        else:
            print(80 * '=')
            print('\t\t\t\t\tMaaf Anda Tidak Lolos Test\t\t\t\t')
            print(80 * '=')
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                subject = f"Hai, {datanama}"
                body = "Tidak perlu sedih jika tidak lulus tes, stay tune email ini untuk mendapatkan promo untuk semester depan"
                msg = f"Subject: {subject}\n\n{body}"
                smtp.sendmail(EMAIL_ADDRESS, email, msg)
            sys.exit()