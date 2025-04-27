##Midterm2_Activity1

##Write a program that will accept the hours worked and hourly rate of an employee.
##Display GROSS INCOME
##Deductions include TAX 10% of Gross Income and COMPANY CONTRIBUTION 5% Gross income.
##Display the TOTAL DEDUCTION and the NET INCOME after all deductions.

print("Enter Hours Worked: ")
hoursWorked = input()
print("Enter Hourly Rate: ")
hourlyRate = input()

grossIncome = int(hoursWorked) * int(hourlyRate)
print("\nGROSS INCOME: ", grossIncome) ##use "," instead of "+" - different syntax to concat different datatypes
totalDeduction  = (0.10 * grossIncome) + (0.05 * grossIncome) ## tax & company respectively
netIncome = grossIncome - totalDeduction
print("Total Deduction: ", totalDeduction,  "\nNet Income: ",  netIncome) ##same as line 13