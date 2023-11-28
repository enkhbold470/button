import time
import datetime
from time import monotonic
# import sys
start_time = monotonic()

def quiz():#prompt,response,timer)
    print("Your prompt is: ")
    prompt=input()
    answer="Damn"
    #timer=datetime.timedelta(10)
    if True:
        print("Make your selection.")
        response=input()
        #timer
        if response == answer:
            print ("Bunny!")
        else:
            print ("Sucker!")
    
quiz()
#print(f"Run time {monotonic() - start_time} seconds")