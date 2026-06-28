import pyttsx3
import time
k= pyttsx3.init()
d="hello"
x= float(time.strftime("%H"".""%M"))
# x=int(input("Time: "))
if( x<12.00):
   t=("Good morning sir!!")
elif( x<16.00):
   t=("Good afternoon Sir!!")
elif( x<20.00):
     t=("Good evening Sir!!")
else:
    t=("Good Night SIR!!")



w = t + ", the time is " + str(x) + " minutes" 

k.say(w)
k.runAndWait()
