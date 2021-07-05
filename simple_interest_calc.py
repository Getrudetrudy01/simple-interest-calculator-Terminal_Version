
#python code for calculating simple interest,ptincipal, time period and rate of time when either of them is given.

#rate_of_interest = "R"
#time_period = "T"
#simple_interest = "I"
from Cal_Engine import cal_principal
from Cal_Engine import cal_rate
A = 100
# P = "principal_amount"
# T = "time_period"
# R = "rate_of_interest"
# I = "simple_interest"

#class parameter:
# P = (I*A)/(R*T)
# R = (I*A)/P*T
# T = (I*A)/P*R
# I = (P*R*T)/A


prompt = input("Please What Do You Want To Find?\n (a) P\n  (b) R\n (c) T\n (d) I\n\n : " )

if prompt == "a":
       R = float(input("Please Enter the Rate Of Interest : "))
       I = float(input("Please Enter the Simple Interest : "))
       T = float(input("Please Enter Time Period In Years : "))

       print(int(cal_principal(A,I,R,T)))
elif prompt == "b":
         I = float(input("Please Enter the Simple Interest : "))
         T = float(input("Please Enter Time Period In Years : "))
         P = float(input("Please Enter Principal Amount : "))
         print(cal_rate(P,A,T,I))
elif prompt == "c":
         P = float(input("Please Enter Principal Amount : "))
         I = float(input("Please Enter the Simple Interest : "))
         R = float(input("Please Enter the Rate Of Interest : "))
         T = (I * A) / P * R
         print(T)
elif prompt == "d":
         P = float(input("Please Enter Principal Amount : "))
         R = float(input(" Please Enter the Rate Of Interest : "))
         T = float(input("Please Enter Time Period in Years : "))
         I = (P * R * T) / A
         print(I)
else:
    print("Invalid")