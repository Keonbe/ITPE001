# Write a python program containing a function that will determine the number of lower&uppercase letters in a string.

def NumOfCase(inputUser):
    lower = 0
    higher = 0

    for i in inputUser:
        if i.islower():
            lower = lower + 1
        elif i.isupper():
            higher = higher + 1

    print ("Number of Uppercase Characters: ", lower, "\nNumber of Lowercase Characters: ", higher)

UserInput = input("Given String: ")
NumOfCase(UserInput)