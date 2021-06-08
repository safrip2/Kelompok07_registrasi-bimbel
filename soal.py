global score
import time
score = 0
print("""untuk menjawab ketik a, b, c, d, atau e lalu tekan enter
anda hanya diberi waktu 10 menit untuk menjawab soal""")
time.sleep(10)
durasi = 600
start_time = time.time()
print("\n")
q1 = """1. Terdapat enam orang anak yang terdiri dari 3 laki laki dan 3 perempuan sedang duduk berjajar bersama, 
peluang 3 anak perempuan duduk berdampingan adalah...
a. 1/60 
b. 1/30
c. 1/15
d. 1/20
e. 1/10"""

q2 = """2. Hitulah hasil 1 + 3 + 5 + …. + 99
a. 1800
b. 2400
c. 2500
d. 2800
e. 2300"""

q3 = """3. cot 105° tan 15° = ...
a. -7 + 4√3
b. 7 + 4√3
c. 7 - 4√3
d. -7 - 4√3
e. -7 + 2√3"""

q4 = """4. Untuk mengerjakan 1 unit rumah dibutuhkan waktu 36 hari dengan 12 tenaga kerja. 
Berapa waktu akan dihabiskan bila menggunakan 24 orang tenaga kerja?
a. 14 Hari 
b. 15 Hari 
c. 16 Hari 
d. 17 Hari 
e. 18 Hari"""

q5 = """5. 40% dari a sama dengan b. JIka b adalah 16,67% dari 48, maka a +b =
a. 8
b. 14
c. 24
d. 28
e. 36"""

q6 = """"6. Jika p = 4 √12 dan q = 3 √54 maka p + q = …
a. 8 √3 + 9 √6 
b. 8 √6 + 9 √3 
c. 9 √3 + 8 √6 
d. 3 √8 + 9 √6 
e. 6 √3 + 9 √8"""

q7 = """7. Jika x+y = 100 dan x/y = 1/9, maka y-x =
a. 20
b. 30
c. 50
d. 60
e. 80"""

q8 = """8. Jika 5p/q = 5 maka q/(5p-q) =
a. 12,5%
b. 16,7%
c. 25%
d. 33%
e. 40%"""

q9 = """9. Hitung panjang diagonal ruang dari sebuah kubus dengan panjang  rusuk 7 cm =
a. 7√3 cm
b. 6√3 cm
c. 3√3 cm
d. 9√3 cm
e. 12√3 cm"""

q10 = """10.  Perbandingan uang saku riri dan rara adalah 3 : 2, jika uang riri dan uang rara berjumlah Rp150.000,00. 
Berapakah masing-masing uang riri dan rara?
a. Rp80.000,00 dan Rp60.000,00
b. Rp90.000,00 dan Rp60.000,00
c. Rp90.000,00 dan Rp70.000,00
d. Rp100.000,00 dan Rp80.000,00
e. Rp100.000,00 dan Rp90.000,00"""

questions = {q1: "c", q2: "c", q3: "a", q4: "e", q5: "d", q6: "a", q7: "e", q8: "c", q9: "a", q10: "b"}
for soal in questions:
    print(soal)
    ans = input("masukkan jawaban: ")
    end_time = time.time() - start_time
    if end_time >= durasi:
        break
    if ans ==questions[soal]:
        score += 10
    else:
        score += 0


