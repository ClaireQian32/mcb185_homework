def calculate_tm(a, c, g, t):
    total_bases = a + c + g + t

    if total_bases <= 13:
        tm = (a + t) * 2 + (g + c) * 4
    else:
        tm = 64.9 + 41 * (g + c - 16.4) / total_bases
    
    return tm
    
print (calculate_tm(3,4,5,5)) 

