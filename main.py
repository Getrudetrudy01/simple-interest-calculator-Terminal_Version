#python program to calculate simple interest


princ_amount = float(input("Please Enter Principal Amount : "))
rate_of_interest = float(input(" Please Enter the Rate Of Interest : "))
time_period = float(input("Please Enter Time Period in Years : "))


simple_interest = (princ_amount*rate_of_interest*time_period) / 100

print("/nSimple Interest for Principal Amount {0} = {1}" .format(princ_amount, simple_interest))





P = float(input("Please Enter Principal Amount : "))
R = float(input(" Please Enter the Rate Of Interest : "))
T = float(input("Please Enter Time Period in Years : "))

simple_interest = (P*R*T) / 100

print("/nSimple Interest for Principal Amount {0} = {1}" .format(P, simple_interest))