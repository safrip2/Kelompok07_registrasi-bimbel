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


questions = {q1: "c", q2: "", q3: "", q4: "", q6: "", q7: "", q8: "", q9: "", q10: ""}
score = 0
for soal in questions:
    print(soal)
    ans = input("masukkan jawaban: ")
    if ans ==questions[soal]:
        score += 10
    else:
        score += 0

return score

