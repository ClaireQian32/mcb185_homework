import random

def roll(n=1 , dc:int, adv = 'norm'): #roll (time, dc, adv = norm/adv/dadv )
    rolls = [random.randint(1, 20) for _ in range(n)]  # stores in a list
    print (f '{rolls}') 
    if adv == 'norm':
        if max(rolls) >= dc: print('Success')
        else: print('Fail')
    elif adv == 'adv':
        if max(rolls) >= dc: print('Success')  # Advantage: take the higher roll
        else: print('Fail')
    elif adv == 'dadv':
        if min(rolls) >= dc: print('Success')  # Disadvantage: take the lower roll
        else: print('Fail')
    else: print("invalid")

print (roll(4, 10, dadv))
	

			
			
		
	
		
	