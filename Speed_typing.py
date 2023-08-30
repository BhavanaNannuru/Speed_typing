from datetime import datetime as d
import random
import keyboard
import math
import time
import os, psutil
start=time.time() #returns number of seconds passed since epoch  Jan 1 1970  00:00:00
sentences=["welcome to the world of typing!","people like to prefer air conditioners in summer","swimming is the best joyful exercise to practice","adithi is exhausted due to lack of sleep last night","after a long time students got a chance to live a normal college life","junk food is one of the favourite food among every child","human brain can be able to think of thousand thoughts in a minute","floods are the worst thing to happen to the poor people","actors in America gets a lot of pay in the movie they act","spotify is the best music playing app I have come across","spending a quality time with your friends is the best therapy","children likes iice creams the most","as far as speed of execution is concerned","Typing speed project is done using python"]
opt = 1
try:
    while opt:
        i=random.randint(0,len(sentences)-1)
        print("Ready?")
        print(sentences[i])
        chk=keyboard.read_key()
        chk=keyboard.read_key()
        if chk:
            a = d.now() #returns current date and time
            ch = input()
            b = d.now()
            sec = (b-a).total_seconds() # Returns the total seconds in the specific duration given
            count=0
            if len(sentences[i])==len(ch):
                for j in range(0,len(sentences[i])):
                    if sentences[i][j]==ch[j]:
                        count+=1
                wpm = (((len(ch)/5)-(len(sentences[i])-count))/(sec/60))
                #wpm = (count*sec)/300
                print("Time taken:",sec)
                print("WPM:",math.trunc(wpm))
                print("Accuracy Percentage:",round((count*100)/len(sentences[i]),2))
            else:
                print("Try entering the correct Input!")
                    
            print("Wanna try again?")
            opt = int(input("1 or 0 : "))
except:
    print("Enter valid inputs only!")
end = time.time()
print("Ended in: ",round((end-start),3),"seconds")
print("Memory in MB:",psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2) #resident set size in bytes
