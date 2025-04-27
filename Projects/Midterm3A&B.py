print("Program 1:")
#Write a program if the given year is a LEAP year or not
# Conditions: Check if year is / by 400; Check if year is / by 4 and not by 100; Print "LEAP YEAR! or "NOT LEAP YEAR"

year = int(input("Enter year: "))
if year % 400 == 0 or year % 4 == 0:
    print("LEAP YEAR")
else:
    print("NOT LEAP YEAR")
#NOTE: REMEMBER OPERATORS

###-----
print("Program 2:")
#Write a program compute student average for semester with subj: Eng, Reed, PE, Alg, & ComProg
#Each subject ask for subject grade, display remark after computation
# GPA           Remark
# 81-90         Very Satisfactory
# 71-80         Satisfactory
# 60-70         Fair
# Below 60      Poor

eng = int(input("Enter grade for English: "))
reed = int(input("Enter grade for Religious Education: "))
pe = int(input("Enter grade for Physical Education: "))
alg = int(input("Enter grade for Algebra: "))
comprog = int(input("Enter grade for Computer Programming: "))

avgGrade = (eng+  reed + pe + alg + comprog) / 5

if avgGrade >= 91 and avgGrade <= 100:
    print("Outstanding")
elif avgGrade >= 81 and avgGrade <= 90:
    print("Very Satisfactory")
elif avgGrade >= 71 and avgGrade <= 80:
    print("Satisfactory")
elif avgGrade >= 60 and avgGrade <= 70:
    print("Fair")
else:
    print(avgGrade,"Poor")
#USE "and" or "or" logical and not && or ||
