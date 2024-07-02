n = input()

func = []

for ch in n:
    
    if 65 <= ord(ch) <= 90:
        print(ch, end="")

    elif ch == "+" or ch == "-":

        if len(func) != 0:
            prev = func.pop()
            if prev == "*" or prev == "/":
                print(prev, end="")

                if len(func) != 0:
                    pprev = func.pop()
                    if pprev == "+" or pprev == "-":
                        print(pprev, end="")
                    else:
                        func.append(pprev)

            elif prev == "+" or prev == "-":
                print(prev, end="")
            else:
                func.append(prev)

        func.append(ch)

    elif ch == "*" or ch == "/":
        if len(func) != 0:
            prev = func.pop()
            if prev == "*" or prev == "/":
                print(prev, end="")
            else:
                func.append(prev)

        func.append(ch)
    
    elif ch == "(":
        func.append(ch)
    
    elif ch == ")":
        while len(func) != 0:
            prev = func.pop()
            if prev == "(":
                break
            print(prev, end="")

while len(func) != 0:
    prev = func.pop()
    print(prev, end="")
