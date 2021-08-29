def Football(F,N):

    Check = F.copy()
    
    F.sort()

    if method1(Check,F,N)[0]:

        if checkIncrease(F, N):

            return True

    else:

        return False

def method1(List1,List2,N):

    Final = []

    for i in range(N):

        if List1[i] != List2[i]:

            Final.append(i)

    if len(Final) == 2:

        First = List2[Final[0]]

        List2[Final[0]] = List2[Final[1]]

        List2[Final[1]] = First

        return True, List2
    
    else:

        return False, List1

def method2(List1,List2,N):

    count = 0 

    for i in range(N-1,0):

        if List1[i] < List1[i-1]:

            count += 1

    if count > 2:

        return False

    else:

        return True

def checkIncrease(List,N):

    for i in range(N-1,0):

        if List[i]> List[i-1]:

            continue

        else:

            return False

    return True

print(Football([1,3,2],3))