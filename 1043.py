n, m = map(int, input().split())
realnum = input()
vertex = []
for _ in range(m):
    party = list(map(int, input().split())) 
    vertex.append(party[1:])

if realnum == "0":
    print(m)

else:
    arr = list(map(int, realnum.split())) 
    known = arr[1:]

    knownidx = 0
    while knownidx != len(known):
        knownpeep = known[knownidx]

        idx = 0
        while idx != len(vertex):
            target = vertex[idx]

            if knownpeep in target:
                for t in target:
                    if t not in known:
                        known.append(t)

                del vertex[idx]
            else:    
                idx += 1
        
        knownidx += 1
    
    print(len(vertex))

