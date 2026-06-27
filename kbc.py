# amitabh sir ke lie module 
import pyttsx3
amitabh=pyttsx3.init()
amitabh.setProperty('rate',150)

#question and answers variable 
question= ("what  is Indias national flower?","who is our national bird?","who is our national animal? ","what  is our national fruit ? ", "is apple is a indian brand ?")
ans =("lotus","peacock","tiger","mango","no")
amitabh.say("welcome to game  so one by one all question will come at your screen and you have to type thier answer")
amitabh.runAndWait()
score = 0

#automatic loop 
for i in range(len(question)):
    print("Question no.",(i+1),":",question[i])
    answer=input("answer:").lower().strip()
    if ans==ans[i]:
        print("correct answer")
        score += 1000
    else:
        print("wrong answer")
        print("correct answer is:",ans[i])

scores=("your score is :",score)
amitabh.say(scores)
amitabh.runAndWait()
#ok tested 