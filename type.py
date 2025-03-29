import random
import time
sentences=[
    "I'm the smartest one.",
    "She thinks python is fun.",
    "I love coding.",
    "Coding is fun.",
    "I like to learn AI.",
    "The weather is cloudy.",
    "I like to sleep.",
    "She is so funny."
]

attempts=3
limit=15
print("it's a typing game,\n you've 15 sec to type !!")
input("press ENTER to start:")
while attempts>0:
   sentence=random.choice(sentences)
   
    
   start_time=time.time()
   type=input(f"{sentence} \n Enetr the sentence")
   end_time=time.time()
   min=end_time-start_time

   if min>=limit:
    print("your 15 seconds ends!!")
 
    break
   elif type.lower()==sentence.lower():
      
      print(f"well done!it took {min:.0f} seconds.")
      break
   else:
      attempts-=1
      if attempts==0:
         print("Game over!you lost.")
         break
      else:
         print(f"incorrect,you've {attempts} chances.")
