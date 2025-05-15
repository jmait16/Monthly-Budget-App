print("Let's Calculate your monthly budget.")

#inputting income before tax
while True:
    try:
        income = (float(input("Enter your yearly income: ")))/12
        break
    except ValueError:
            print("Please enter a valid number, make sure no \"$\"")

#state income tax rate dictionary (TO BE CHANGED IN FUTURE)
state_income_taxes = dict(
    AL = 0.95, AK = 1, AZ = 0.975, AR = 0.956, CA = 0.867, CO = 0.9575, CT = 0.9301, DE = 0.934, DC = 0.8925, FL = 1, GA = 0.9451,
    HI = 0.89, ID = 0.942, IL = 0.9505, IN = 0.9695, IA = 0.943, KS = 0.943, KY = 0.96, LA = 0.9575, ME = 0.9285, MD = 0.9425, MA = 0.91,
    MI = 0.9575, MN = 0.9015, MS = 0.953, MO = 0.952, MT = 0.941, NE = 0.9416, NV = 1, NH = 1, NJ = 0.8925, NM = 0.941, NY = 0.891,
    NC = 0.955, ND = 0.975, OH = 0.965, OK = 0.9525, OR = 0.901, PA = 0.9693, RI = 0.9401, SC = 0.937, SD = 1, TN = 1, TX = 1,
    UT = 0.9535, VT = 0.9125, VA = 0.9425, WA = 1, WV = 0.9488, WI = 0.9235, WY = 1,
)

#Inputting state for state income tax
while True:
    user_state = input("Which state do you live in? (Write state abbreviation; ex: ME, NH, MA): ")
    if user_state in state_income_taxes:
        state_income_tax = 1-state_income_taxes[user_state]
        break
    else:
        print("Invalid state abbreviation, Please try again.")

#defining expense-calculation function
def exp(exp_name):
    while True:
        try:
            expense = float(input("Enter your monthly " + exp_name +  " expense: "))
            return expense
        except ValueError:
            print("Please enter a valid number, make sure no \"$\"")

#inputting rent/home expense
rent_expense = exp("rent/mortgage")

#inputting food expense
food_expense = exp("food")

#inputting transportation expense
transportation_expense = exp("transportation (ex: Gas, uber, car payments)")

#inputting fun/personal expense
fun_expense = exp("fun")

#inputting utilities expense
utilities_expense = exp("utilities (ex: electricity, water, wifi, phone)")

#inputting insurance expense
insurance_expense = exp("insurance")

#inputting debt expense
debt_expense = exp("debt")

#inputting education expense
education_expense = exp("education (ex: books, courses)")

#inputting misc expense
miscellaneous_expense = exp("miscellaneous")

#Federal income tax calculation
if income < 967:
    FIT = income*0.1
elif income < 3929:
    FIT = (967*0.1)+((income-967)*0.12)
elif income < 8377:
    FIT = (967*0.1)+((3929-967)*0.12)+((income-3929)*0.22)
elif income < 15996:
    FIT = (967*0.1)+((3929-967)*0.12)+((8377-3929)*0.22)+((income-8377)*0.24)
elif income < 20310:
    FIT = (967*0.1)+((3929-967)*0.12)+((8377-3929)*0.22)+((15996-8377)*0.24)+((income-15996)*0.32)
elif income < 50779:
    FIT = (967*0.1)+((3929-967)*0.12)+((8377-3929)*0.22)+((15996-8377)*0.24)+((20310-15996)*0.32)+((income-20310)*0.35)
else:
    FIT = (967*0.1)+((3929-967)*0.12)+((8377-3929)*0.22)+((15996-8377)*0.24)+((20310-15996)*0.32)+((50779-20310)*0.35)+((income-50779)*0.37)

#calculating total variables
SIT = state_income_tax*income
expenses = rent_expense+food_expense+fun_expense+transportation_expense+utilities_expense+insurance_expense+debt_expense+education_expense+miscellaneous_expense
leftover = (income-expenses-SIT-FIT)

#rounding variables
income = round(income, 2)
expenses = round(expenses, 2)
leftover = round(leftover, 2)
SIT = round(SIT, 2)
FIT = round(FIT, 2)

#creating space
print()
print()

#printing general summary
print("GENERAL MONTHLY SUMMARY:")
print()
print("Your monthly income is: $" + str(income))
print("Your federal income tax is: $" + str(FIT))
print("Your state income tax is: $" + str(SIT))
print("Your total monthly expenses are: $" + str(expenses))

#leftover analysis
if leftover < 0:
    print("Your deficit is: $" + str(leftover))
    print("Consult the below \"Expense Summary\" to achieve positive surplus.")
elif leftover == 0:
    print("You have no surplus.")
else:
    print("Your surplus is: $" + str(leftover))
    print("Congrats, you have positive surplus!")
print()

#rounding individual expenses
rent_expense = round(rent_expense, 2)
food_expense = round(food_expense, 2)
transportation_expense = round(transportation_expense, 2)
fun_expense = round(fun_expense, 2)
utilities_expense = round(utilities_expense, 2)
insurance_expense = round(insurance_expense, 2)
debt_expense = round(debt_expense, 2)
education_expense = round(education_expense, 2)
miscellaneous_expense = round(miscellaneous_expense, 2)

#printing expense summary
print("MONTHLY EXPENSE SUMMARY:")
print()
print("Your monthly rent expense is: $" + str(rent_expense))
print("Your monthly food expense is: $" + str(food_expense))
print("Your monthly transportation expense is: $" + str(transportation_expense))
print("Your monthly fun expense is: $" + str(fun_expense))
print("Your monthly utilities expense is: $" + str(utilities_expense))
print("Your monthly insurance expense is: $" + str(insurance_expense))
print("Your monthly debt expense is: $" + str(debt_expense))
print("Your monthly education expense is: $" + str(education_expense))
print("Your monthly miscellaneous expense is: $" + str(miscellaneous_expense))
print("YOUR TOTAL MONTHLY EXPENSES: $" + str(expenses))

#asterisk
print()
print()
print()
print()
print("*These values are a great ESTIMATION for budgeting your month")


