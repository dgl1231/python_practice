i,k = 0,0

while i<9:
    if i<5:
        k=0
        while k<4-i:
            print("  ", end = "")
            k += 1
        k=0
        while k<i+1:
            print("\u2607",end="")
            k += 1
    
        
    print()
    i= i+1
