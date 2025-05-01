selectAnother = "Y"
while selectAnother != "n" or selectAnother != "N":
    name = input("Enter employee name: ")
    positionSelect = int(input("Position(1-Manager, 2-Developer, 3-Analyst): "))
    hoursWorked = int(input("Enter hours worked: "))


    positionTitle = ""     # Determine position title
    if positionSelect == 1:
        positionTitle = "Position: Manager"
    if positionSelect == 2:
        positionTitle = "Position: Developer"
    if positionSelect == 3:
        positionTitle = "Position: Analyst"
    
    print(positionTitle)


    grossSalary = 0     # Calculate gross salary
    if positionSelect == 1:
        grossSalary = 50 * hoursWorked
    if positionSelect == 2:
        grossSalary = 40 * hoursWorked
    if positionSelect == 3:
        grossSalary = 35 * hoursWorked

    print("Salary Breakdown: ")
    print("Gross salary: ", grossSalary)

    taxDeduction = 0 # Calculate tax deduction
    if grossSalary > 50000:
        taxDeduction = grossSalary * 0.3
    elif grossSalary <= 50000 and grossSalary >= 30000:
        taxDeduction = grossSalary * 0.2
    elif grossSalary < 30000:
        taxDeduction = grossSalary * 0.1

    print("Tax Deduction: ", taxDeduction)

    takeHomeSalary = grossSalary - taxDeduction # Calculate take home salary
    print("Take home salary: ", takeHomeSalary)

    selectAnother = input("Do you want to enter another employee details? [Y/N]: ")

    if selectAnother == "n" or selectAnother == "N":
        break

print("Thank you for using the Employee Salary Calculation System!")
print("Goodbye!")