import math

#User selects calculation option
calculation = input("This programme allows you to calculate interest on an investment or a bond, Please enter input word 'Investment' or 'Bond' to proceed").lower()

#If defination for calculation selection
if calculation == "investment":
# define calculation for investment
    invest_amount = float(input("Please input the initial capital you wish to invest"))
    invest_int_rate = float(input("Please input the % of interest of investment"))
    invest_years = int(input("Please input the investment term in years"))
    int_type = input("Input whether the account is on 'simple' or 'compound' interest").lower()

# Defining selection of simple and compound interest as well as formula for caalculating both
    if int_type == "simple":
        print("Simple interest formula will be used")
        Investment = invest_amount*(1+(invest_int_rate/100)*invest_years)
        print("The interest accumulated over {} will be{}".format(invest_years,Investment))
    elif int_type == "compound":
        print("Compound interest formula will be used")
        Investment = invest_amount* math.pow((1+(invest_int_rate/100)),invest_years)
        print("The interest accumulated over {} years will be{}".format(invest_years,Investment))
    else:
        print("Please input either simple or compound for calculation")

elif calculation == "bond":
# define calculation for bond
    bond_value = float(input("Please input the current value of the house"))
    bond_int_rate = float(input("Please input the % of interest of the bond"))
    bond_months = int(input("Please input the bond term in months"))
    monthly_rate = bond_int_rate/100/12
    Bond = (monthly_rate*bond_value)/(1-(1+(monthly_rate))**(-1*bond_months))
    print("The monthly repayment will be{}".format(Bond))

else:
    print("Invalid input. Please enter 'investment' or 'bond'.")