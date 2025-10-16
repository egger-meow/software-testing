total_credit = 0.0
total_score = 0.0

while True:
    try:
        score, credit = input("Enter score and credit: ").split()
        if score == "q":
            break
        total_credit += float(credit)
        total_score += float(score) * float(credit)
    except ValueError:
        break
    
print("Total credit: ", total_credit)
print("GPA: ", total_score / total_credit)
