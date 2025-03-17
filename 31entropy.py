1   import sys
2   import math
3 #harvest words on the command line and turn them into probabilities.
4   probs = []   #set up a container for probability 
5   for arg in sys.argv[1:]:   #steps through each argument, but skip the first which is the command 
6       f = float(arg)  #convert arg into float number
7       if f <= 0 or f >= 1: sys.exit('error: not a probability')
8       probs.append(f) #add each floating point number into container [prob]
9
10  total = 0
11  for p in probs: total += p  #sum up each p in the containerinto one number total 
12  if not math.isclose(total, 1.0):  #check if the sum is close to 1 
13      sys.exit('error: probs must sum to 1.0')
14
15  h = 0  #initial entropy = 0
16  for p in probs:
17      h -= p * math.log2(p) #calculate entropy of each and subtracting each entropy in total entropy 
18
19  print(f'{h:.4f}')  #report final value in a f string , the .4f set the output to be 4 decimals 