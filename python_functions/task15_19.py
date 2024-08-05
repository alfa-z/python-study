# Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF.
# To find the Kenya NHIF Rate using THIS LINK:  


def calc_gross_salary(a,b):
    gross_salary = a+b
    return gross_salary
basic_salary = int(input('Enter basic salary: '))
benefits = int(input('Enter benefits: '))
total = calc_gross_salary(basic_salary, benefits)
print(f'Your Gross Salary = {total}')


def calc_nhif(gross_salary):
    if gross_salary <= 5999:
        nhif = 150
    elif gross_salary >=6000 and gross_salary<=7999:
        nhif = 300
    elif gross_salary>=8000 and gross_salary<=11999:
        nhif =400
    elif gross_salary>=12000 and gross_salary<=14999:
        nhif = 500
    elif gross_salary>=15000 and gross_salary<=19999:
        nhif = 600
    elif gross_salary>=20000 and gross_salary <=24999:
        nhif = 750
    elif gross_salary>=25000 and gross_salary<=29999:
        nhif = 850
    elif gross_salary>=30000 and gross_salary<=34999:
        nhif = 900
    elif gross_salary>=35000 and gross_salary<=39999:
        nhif = 950
    elif gross_salary >=40000 and gross_salary<=44999:
        nhif = 1000
    elif gross_salary >=45000 and gross_salary <=49999:
        nhif = 1100
    elif gross_salary>=50000 and gross_salary<=59999:
        nhif = 1200
    elif gross_salary>=60000 and gross_salary<=69999:
        nhif = 1300
    elif gross_salary>=70000 and gross_salary<=79999:
        nhif = 14000
    elif gross_salary>=80000 and gross_salary<=89999:
        nhif = 1500
    elif gross_salary>=90000 and gross_salary<=99999:
        nhif =1600
    else:
        nhif = 1700
    return nhif
nhif = calc_nhif(total)
print(f'Your NHIF = {nhif}')


# TASK 16
# Continue with the program above, then use  the gross salary to find the NSSF.
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF.


def calc_nssf(gross_salary, rate =0.06):
    if gross_salary<=18000:
        nssf = rate*gross_salary
    else:
        nssf = rate*18000
    return nssf
NSSF = calc_nssf(total)
print(f'Your NSSF = {NSSF}')


# TASK 17
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015


def calc_nhdf(gross_salary):
    nhdf = 0.015 * gross_salary
    return(nhdf)
NHDF = calc_nhdf(total)
print(f'Your NHDF = {NHDF}')






# TASK 18
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF)


def calc_taxable_income(gross_salary, nssf, nhdf, nhif):
    taxable_income = gross_salary - (nssf+nhdf+nhif)
    return taxable_income
Taxable_Income = calc_taxable_income(total, NSSF, NHDF, nhif)
print(f'Your Taxable Income = {Taxable_Income}')






# TASK 19
# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK


def calc_payee(taxable_income, relief=2400):
    if taxable_income>=0 and taxable_income<=24000:
        payee = 0
    elif taxable_income>24000 and taxable_income<=32333:
        payee = (0.1*24000) + (0.25*(taxable_income-24000)) - relief
    elif taxable_income>32333 and taxable_income<=500000:
        payee = (0.1*24000) + (0.25*8333) + (0.30*(taxable_income-32333)) - relief
    elif taxable_income >500000 and taxable_income<=800000:
        payee = (0.1*24000) + (0.25*8333) + (0.3*467667) + (0.325*(taxable_income-50000)) - relief
    else:
        payee = (0.1*24000) + (0.25*8333) + (0.3*467667) + (0.325*300000) + (0.35*(taxable_income-800000)) - relief
    return payee
PAYEE = calc_payee(Taxable_Income)
print(f'Your PAYEE = {PAYEE}')




# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee-relief)


def calc_net_salary(gross_salary, nhif, nhdf, nssf, payee):
   
    net_salary = gross_salary - (nhif + nhdf + nssf + payee)
    return net_salary

Net = calc_net_salary(total, NSSF, nhif, NHDF, PAYEE)
print(f'Your Net Salary = {Net}')


#deploying code
#create repository  by pressing + then new 