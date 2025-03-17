import random  
import sys     

if len(sys.argv) != 4:
    sys.exit("wrong argument")  

trials = int(sys.argv[1]) 
days = int(sys.argv[2])    
people = int(sys.argv[3]) 

duplicate= 0 

for _ in range(trials):  
    birthdays = []  
    for _ in range(people):  
     	bday = random.randrange(days)
     	birthdays += bday