global score
    q1 = """1. berapa hasil dari 1x1 
    a. 5
    b. 3
    c. 2"""

    questions = {q1: "a", q2: "b", q3: "c"}
    score = 0
    for soal in questions:
        print(soal)
        ans = input("masukkan jawaban: ")
        if ans ==questions[soal]:
            score += 10
        else:
            score += 0

    return score