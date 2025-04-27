def position(positionSelect):
    if positionSelect == 1:
        return "Position: Manager"
    if positionSelect == 2:
        return "Position: Developer"
    if positionSelect == 3:
        return "Position: Analyst"

def positionSalary(positionSelect, hoursWorked):
    salaryPosition = 0
    if positionSelect == 1:
        salaryPosition = 50 * hoursWorked
    if positionSelect == 2:
        salaryPosition = 40 * hoursWorked
    if positionSelect == 3:
        salaryPosition = 35 * hoursWorked
        return salaryPosition
        
def taxDeduct(grossSalary):
    taxDeduct = 0
    if grossSalary > 50000:
        taxDeduct = grossSalary * 0.3
    if grossSalary <= 50000 or grossSalary >= 50000:
        taxDeduct = grossSalary * 0.2
    if grossSalary < 30000:
        taxDeduct = grossSalary * 0.1
        return taxDeduct

def takehomeSalary(grossSalary, taxDeduction):
    TakeHomesalary = grossSalary - taxDeduction
    return TakeHomesalary

selectAnother = "Y"
while selectAnother != "n" or selectAnother != "N":
    name = input("Enter employee name: ")
    positionSelect = int(input("Position(1-Manager, 2-Developer, 3-Analyst): "))
    position(positionSelect)
    print(position(positionSelect))
    hoursWorked = int(input("Enter hours worked: "))


    print("Salary Breakdown: ")
    grossSalary = positionSalary(positionSelect, hoursWorked)
    print("Gross salary: ", grossSalary)
    taxDeduction = taxDeduct(grossSalary)
    print("Tax Deduction: ", taxDeduction)
    print("Take home salary: ", takehomeSalary(grossSalary, taxDeduction))
    selectAnother = input("Do you want to enter another employee details? [Y/N]: ")


    if selectAnother == "n" or selectAnother == "N":
        break

print("Thank you for using the Employee Salary Calculation System!")
print("Goodbye!")
