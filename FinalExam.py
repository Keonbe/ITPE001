def position(positionslec):
        if (positionslec == 1):
               return ("Position: Manager")
        if positionslec == 2:
               return ("Position: Developer")
        if positionslec == 3:
               return ("Position: Analyst")
            
        
def positionSalary(positionslec, hoursWorked):
        salaryPosition = 0
        if positionslec == 1:
            salaryPosition = 50 * hoursWorked
        if positionslec == 2:
            salaryPosition = 40 * hoursWorked
        if positionslec == 3:
            salaryPosition = 35 * hoursWorked
        return salaryPosition
        
def taxDeduct(grossSalary):
        txDeduct = 0
        if grossSalary > 50000:
            txDeduct = grossSalary * 0.3
        if grossSalary <= 50000 or grossSalary >= 50000:
            txDeduct = grossSalary * 0.2
        if grossSalary < 30000:
            txDeduct = grossSalary * 0.1
            return txDeduct
            
def takehomemSalary(grossSalary, taxDeduction):
    TakeHomesalary = grossSalary - taxDeduction
    return TakeHomesalary

selecAnother = "Y"
while selecAnother != "n" or selecAnother != "N":
    name = input("Enter employee name: ")
    positionslec = int(input("Position(1-Manager, 2-Developer, 3-Analyst): "))
    position(positionslec)
    print(position(positionslec))
    hoursWorked = int(input("Enter hours worked: "))
    
    print("Salary Breakdown: ")
    grossSalary = positionSalary(positionslec, hoursWorked) #not working
    print("Gross salary: ", grossSalary) #dont use "positionSalary" or the function itself rather the var, better var naming
    taxDeduction = taxDeduct(grossSalary)
    print("Tax Deduction: ", taxDeduction)
    print("Take home salary: ", takehomemSalary(grossSalary, taxDeduction))
    selecAnother = input("Do you want to enter another employee details? [Y/N]: ")
    
    if selecAnother == "n" or selecAnother == "N":
        break

print("Thank you for using the Employee Salary Calculation System!")
print("Goodbye!")