while True:
    n = input()
    if n == "0": break

    p = True
    i=0
    while i<=len(n)/2:
        if n[i] != n[len(n)-i-1]:
            p = False
            break
        i += 1
        
    print("yes" if p else "no")  
