import sys
import  random

text = " ".join(sys.argv[1:]) #joining argument into a string
output = "" #creat a container for output

for character in text: #step through text
	if random.random() < 0.5 :
		output += character.upper() #adding the upper letter to 
	else: output += character.lower()
	
print(output)