score = int(input("โปรดใส่คะแนน : "))

grade = 0

if score >= 80:
    grade = 4.0
elif score >= 75 and score < 80:
    grade = 3.5
elif score >= 70 and score < 75:
    grade = 3.0
elif score >= 65 and score < 70:
    grade = 2.5
elif score >= 60 and score < 65:
    grade = 2.0
elif score >= 55 and score < 60:
    grade = 1.5
elif score >= 50 and score < 55:
    grade = 1.0
else: grade = 0

print("your grade is : " + str(grade))