def triplets(n: int):
	for a in range (1, n):
		for b in range (a, n):
			c = ( a**2 + b**2 ) **0.5
			if c % 1 == 0 : 
				print (a, b, int(c))
		
		
print (triplets(100))
		