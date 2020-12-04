#!/usr/bin/env python3

# (Financial application: payroll) Write a program that reads the following infor-
# mation and prints a payroll statement:

#   Employee's name (e.g., Smith)
#   Number of hours worked in a week (e.g., 10)
#   Hourly pay rate (e.g., 9.75)
#   Federal tax withholding rate (e.g., 20%)
#   State tax withholding rate (e.g., 9%)

# A sample run is shown below:

#   Enter employee's name: Smith [Enter]
#   Enter number of hours worked in a week: 10 [Enter]
#   Enter hourly pay rate: 9.75 [Enter]
#   Enter federal tax withholding rate: 0.20 [Enter]
#   Enter state tax withholding rate: 0.09 [Enter]
#
#   Employee Name: Smith
#   Hours Worked: 10.0
#   Pay Rate: $9.75
#   Gross Pay: $97.5
#   Deductions:
#     Federal Withholding (20.0%): $19.5
#     State Withholding (9.0%): $8.77
#     Total Deduction: $28.27
#   Net Pay: $69.22

name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
rate = eval(input("Enter hourly pay rate: "))
pay = hours * rate
federalTaxRate = eval(input("Enter federal tax withholding rate: "))
federalTax = pay * federalTaxRate
stateTaxRate = eval(input("Enter state tax withholding rate: "))
stateTax = pay * stateTaxRate
deductions = federalTax + stateTax
netPay = pay - deductions

print()
print("Employee Name:", name)
print("Hours Worked:", format(hours, ".1f"))
print("Pay Rate: $" + format(rate, ".2f"))
print("Gross Pay: $" + str(pay))
print("Deductions:")
print("  Federal Withholding (" + format(federalTaxRate, ".1%") + "): $" + format(federalTax, ".1f"))
print("  State Withholding (" + format(stateTaxRate, ".1%") + "): $" + str(stateTax * 100 // 1 / 100))
print("  Total Deductions: $" + format(deductions, ".2f"))
print("Net Pay: $" + format(netPay, ".2f"))
