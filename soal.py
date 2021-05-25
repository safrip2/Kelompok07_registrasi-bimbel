global score

q1 = """1. terdapat enam orang anak yang terdiri dari 3 laki lai dan 3 perempuan sedang duduk berjajar bersama, peluang 3 anak perempuan duduk berdampingan adalah...
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

q4 = """4. Untuk mengerjakan 1 unit rumah dibutuhkan waktu 36 hari dengan 12 tenaga kerja. Berapa waktu akan dihabiskan bila menggunakan 24 orang tenaga kerja?
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






questions = {q1: "c", q2: "c", q3: "", q4: "e", q5: "d", q6: "a", q7: "", q8: "", q9: "", q10: ""}
score = 0
for soal in questions:
    print(soal)
    ans = input("masukkan jawaban: ")
    if ans ==questions[soal]:
        score += 10
    else:
        score += 0

return score

