
import pyttsx3

import time 
x=pyttsx3.init()
y= time.strftime(" %D ")
z=(time.strftime("%I""hours""%M""minutes"))
# checking code 
datetim_e = "sir The date is",y,"The time is ",z
print(y)
print(z)
x.say(datetim_e)
x.runAndWait()

