import re
for _ in range(int(input())):print("YES"if(re.match(r"^(100+1+|01)+$",input()))else"NO")
