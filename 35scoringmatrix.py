import sys 

if len(sys.argv) != 4:
    sys.exit(f"wrong argument")  
    
alphabet = sys.argv[1]  
match_score = int(sys.argv[2])  
mismatch_score = int(sys.argv[3])  

print(f"   {'  '.join(alphabet)}")

for char1 in alphabet:
    row = [f"{match_score:2}" if char1 == char2 else f"{mismatch_score:2}" for char2 in alphabet]
    print(f"{char1} {' '.join(row)}")