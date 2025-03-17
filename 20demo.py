
person = 'Steve', 21, 57891.50 # name, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my) #call for individule values (known results will have 2 values )

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
    
########
import random
    for i in range(3): #3 times
    print(random.randint(1, 6)) #randnum bw 1-6
    
random.seed(1) #set seed
print(random.random())
print(random.random())

# += increment -=decrement *=multiply 
###########
import time

def estimate_pi():
    pi_estimate = 0
    denominator = 1
    sign = 1  # Alternates between +1 and -1
    iterations = 0

    while True:  # Infinite loop
        pi_estimate += sign * (1 / denominator)
        denominator += 2
        sign *= -1  # Flip sign for next term
        iterations += 1

        print(f"Iteration {iterations}: π ≈ {pi_estimate * 4}")
        time.sleep(0.1)  # Small delay for readability

estimate_pi()
#########
import random
import time

def estimate_pi():
    inside_circle = 0
    total_points = 0

    while True:  # Infinite loop
        x = random.uniform(0, 1)  # Random x between 0 and 1
        y = random.uniform(0, 1)  # Random y between 0 and 1
        distance = x**2 + y**2  # Squared distance from origin

        if distance <= 1:
            inside_circle += 1  # Point is inside the quarter circle
        
        total_points += 1
        pi_estimate = (inside_circle / total_points) * 4  # Estimate π

        print(f"Iteration {total_points}: π ≈ {pi_estimate}")
        time.sleep(0.1)  # Small delay for readability

try:
    estimate_pi()
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
#####
import random

def roll_3d6():
    """Roll 3 six-sided dice."""
    return sum(random.randint(1, 6) for _ in range(3))

def roll_3d6r1():
    """Roll 3 six-sided dice, but re-roll any 1s."""
    return sum(random.randint(2, 6) if x == 1 else x for x in [random.randint(1, 6) for _ in range(3)])

def roll_3d6x2():
    """Roll pairs of six-sided dice 3 times, taking the maximum of each pair."""
    return sum(max(random.randint(1, 6), random.randint(1, 6)) for _ in range(3))

def roll_4d6d1():
    """Roll 4 six-sided dice, dropping the lowest die roll."""
    rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(rolls)[1:])  # Drop the lowest roll

def average_stat(roll_function, trials=100000):
    """Calculate the average stat value over many trials."""
    return sum(roll_function() for _ in range(trials)) / trials

# Run simulations
trials = 100000
print(f"Average stat for 3D6:    {average_stat(roll_3d6, trials):.2f}")
print(f"Average stat for 3D6r1:  {average_stat(roll_3d6r1, trials):.2f}")
print(f"Average stat for 3D6x2:  {average_stat(roll_3d6x2, trials):.2f}")
print(f"Average stat for 4D6d1:  {average_stat(roll_4d6d1, trials):.2f}")

