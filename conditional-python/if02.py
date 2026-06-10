marks = int (input("enter your marks here: "))
if marks >= 90:
    grade="A+"
elif marks >= 85:
    grade="B+"
elif marks >= 75:
    grade="C+"
elif marks >= 65:
    grade="d+"
else:
    grade="fail"
print("Grade  : ",grade)


