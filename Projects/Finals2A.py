# Write a program containing a function[with parameter passing] that will ADD all the elements of a list. ELements of the list will be user input
# Sample: Given list example x = [1,2,3,4,5]
# Sum of elements = 15

def SumOfAllElements(GivenList):
    
    SumOfElements = 0
    for num in GivenList:
        SumOfElements += num
    return SumOfElements

userInput = input("Given list x = ")
GivenList = [int(x.strip()) for x in userInput.split(",")]
sumOfAll = SumOfAllElements(GivenList)
print("Sum of elements =", sumOfAll)
