# string 
s = 'hello world'
print(s)
#operator
	 = assignment * repeat + concatenation >or<or== comparison

	len(s)	get the length of a string
	chr(n)	get the character whose ASCII value is n
	ord(c)	get the ASCII value of the character 

s.count(s1)	number of occurrences of s1 in s
s.endswith(s1)	True if s ends with s1
s.startswith(s1)	True if s starts with s1
s.upper()	uppercase version of s
s.lower()	lowercase version of s
s.rstrip()	strip characters from the right (spaces by default)
s.replace(a, b)	convert substring a to b

#format string
print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify

for nt in seq:
    print(nt, end='') #print everything on the same line
print()

#slice 
s = 'ABCDEFGHIJ'
print(s[0:5]) # print first 5 digits

print(s[0:8:2]) #[start, stop, step size] step size == -1 means revers string 

#put string into codon
dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(i, codon)
# container -> tuple
for i, nt in enumerate(nts):
    print(i, nt)
  #with two separate containers
  for nt, name in zip(nts, names):
    print(nt, name)
    
#list
Lists are similar to tuples except they are constructed with square brackets and their contents are mutable.
nts = ['A', 'T', 'C'] 
#or nts = list('A','T','C') do the same, but also able to convert strings into list
nts[2] = 'G' #change C to G (0,1,2)
print(nts)

nts.append('C') #add one more C to the end to the eng of list 

last = nts.pop()
print(last) #rule out and rm the last one in the list
#now the nts is only ATG
#when with index (ie. list.pop(1)it rules out the specific element)
#when in a loop it mimics LIFO 

#sort lists : all elements must have similar types (ex:int and floats)
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

#new name for list
nuclrotides = nts #makes the same list have two names
#make a copy 
newlist = nts.copy() #does not take arguments
    
#split and join
text = 'good day          to you'
words = text.split()
print(words)  #default split by any number of spaces
# for TSV or CSV, split on ','
    print(file.split(','))
    
s = '-'.join(aas) #connect with -, join tuple or list into a string
print(s)
s = ''.join(aas) #connect with space
print(s)

#searching 
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G')) #returns the index of first match (5)
print('index Z?', alph.index('Z')) #returns error if no match
#when not sure if smt exists in list or tuple
if thing in list: idx = list.index(thing)
#ex
fruits = ["apple", "banana", "cherry"]
thing = "banana"
if thing in fruits: 
    idx = fruits.index(thing)
    print(f"{thing} is at index {idx}")

-----------------
#minmax
1   def minmax(vals):
2       mini = vals[0]
3       maxi = vals[0]
4       for val in vals[1:]: #after the first
5           if val < mini: mini = val #comp val with mini, if true than replace
6           if val > maxi: maxi = val
7       return mini, maxi
    
#mean
1   def mean(vals):
2       total = 0
3       for val in vals: total += val #adds each val to total
4       return total / len(vals) #devide total with length of vals

#entropy 
import math
def entropy(probabilities):
    # Ensure probabilities are valid
    all_valid = True
    for p in probabilities:
        if p < 0 or p > 1:
            all_valid = False #must be, avoid for p=0 later
    if all_valid and math.isclose(sum(probabilities), 1.0):
        return -sum(p * math.log2(p) for p in probabilities if p > 0) #avoid p=0
    else:
        raise ValueError("Probabilities must be between 0 and 1 and sum to 1.")
# Example usage:
prob_dist = [0.5, 0.5]
print(entropy(prob_dist))  # Output: 1.0

#Kullback-Leibler distance, aka relative entropy, always non-negative
# measure how two prob set diverge from each other, it is not symmetric, so direction matters
def dkl(P, Q):
    total_p = 0
    total_q = 0
    for p, q in zip(P, Q):
        total_p += p
        total_q += q
    if total_p != 1 or total_q != 1: #if sum not equal to 1 
        print('not possible')("Both P and Q must be valid probability distributions (sum to 1).")

    d = 0
    for p, q in zip(P, Q):
        if p > 0 and q > 0:
            d += p * math.log2(p / q) 
    return d

p1 = [0.4, 0.3, 0.2, 0.1]
p2 = [0.1, 0.3, 0.4, 0.2]
print(dkl(p1, p2))
--------
#sys.argv 
python3 script.py 10 20 #apply function in script on 10 and 20

#compare
for i in range(0, len(list)):
	for j in range(X, len(list)):
	
X = 0: all combinations
X = i: half-matrix with diagonal
X = i+1: half-matrix without diagonal	
	
    
    