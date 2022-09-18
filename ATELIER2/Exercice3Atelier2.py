L = [-1,5,19,-62,0,-5,4,9,13,-23]

def separer(L: list) -> list:
    LSEP = []
    for i in range(len(L)):
        if L[i] < 0:
            LSEP.append(L[i])

    for i in range(len(L)):
        if L[i] == 0:
            LSEP.append(L[i])
    
    for i in range(len(L)):
        if L[i] > 0:
            LSEP.append(L[i])
    
    return LSEP

print(separer(L))