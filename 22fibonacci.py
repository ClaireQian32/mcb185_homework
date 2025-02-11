def fibonacci(n):
	a = 0
	b = 1
	for _ in range (n):
		print (a)
		temp = a 
		a = b 
		b = temp + a 
		
print (fibonacci(10))