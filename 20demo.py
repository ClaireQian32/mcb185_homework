
person = 'Steve', 21, 57891.50 # name, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my) #call for individule values 

###########
i = 0
while i < 3:
    i = i + 1
    print('hey', i)   

for i in range(1, 10, 3): #start,stop,increment 
    print(i)
for i in range(0, 5): #increment=1
    print(i)
for i in range(5): #initial=0
    print(i)
    
basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing)
    
for i in range(len(basket)): #len returns the numer of things
    print(basket[i])  #use the range() function and numeric indices, output=thing
    
##Triangular
1   def triangular(n):
2       tri = 0
3       for i in range(n+1):
4           tri = tri + i
5       return tri

##factorial
1   def factorial(n):
2       if n == 0: return 1
3       fac = 1
4       for i in range(1, n + 1):
5           fac = fac * i
6       return fac

#poission
def poisson(n, k):
    return n**k * math.e**-n / factorial(k)
    
#nchoosek
def nchoosek(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
    
#euler
def euler(limit):
    e = 0
    for n in range(limit):
        e = e + 1 / factorial(n)
    return e
    
#is_prime
def is_prime(n):
    for den in range(2, n//2 +1):
        if n % den == 0: return False
    return True

#nilakantha
def nilakantha(limit):
    pi = 3
    for i in range(1, limit+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d
        else:          pi = pi + 4 / d
    return pi
    
########3
import random
    for i in range(3): #3 times
    print(random.randint(1, 6)) #randnum bw 1-6
    
random.seed(1) #set seed

# += increment -=decrement *=multiply 
