##51 down to 1 by -2  *theprime
##varient of mounty python how many points above/ bewlow the line

import random
import time

def ratio_pra():
    inside = 0
    outside = 0
    total = 0
    while True:  
        x = random.uniform(0, 1)  
        y = random.uniform(0, 1)  

        if y <= x**2 :
            inside += 1   
        else :
        	outside += 1 
        total += 1
        ratio = (inside / outside if outside > 0 else float('inf') )   

        print(f"Iteration {total}: ratio = {ratio}")
  
ratio_pra ()