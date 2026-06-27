
import pyttsx3

import time 
x=pyttsx3.init()
y= time.strftime(" %D ")
z=(time.strftime("%H""hours""%M""minutes"))
# checking code 
datetim_e = "sir The date is",y,"The time is ",z
print(y)
print(z)
x.say(datetim_e)
x.runAndWait()
# x = int(input( "Enter your no.."))
# match x:
#     case 0:
#        print("the value is zero")
#     case x if x <=20:
#         print(" less than 20")
#     case _:
#         print("it is not zero or less than equal to  20")
