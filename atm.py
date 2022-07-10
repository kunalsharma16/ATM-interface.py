
import time
print("Welcome to scotia bank")
time.sleep(4)
print(" Loading.........")
time.sleep(3)
print("Please insert your card")
time.sleep(2)
print(" Pulling up your information")
time.sleep(1)
print(" Please enter your pin")
pin = "6862"
pin_input = input("pin")
if pin_input == pin :
   print ("***** Main Menu *****")
   print (" 1.Checking")
   print("  2.Savings")
   print (" 3.credit card")
   c = int(input("please select your option"))
   if c==1:
     print(" your aval bal in checking acc is $3500")
   elif c==2:
     print ("Your saving acc bal is $10,000")
   elif c==3:
     print("Your aval credit $500 \n bal due $500")
else :
    print (" pin is worng \n try again")
























