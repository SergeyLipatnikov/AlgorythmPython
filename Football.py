def Football(F,N):

    Check = F.copy()
    
    F.sort()

    First = method1(F,Check,N)

    if First[0]:

        if checkIncrease(First[1],N):

            return True

        else: 

            return False 

    Second = method2(Check,N)

    if Second[0]:

        if checkIncrease(Second[1],N):

            return True

        else: 

            return False

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

def method2(List,N):

    indexFirst = []

    for i in range(N-1):

        if i == 0:

            if List[i] > List[i+1]:

                indexFirst.append(i)

        elif List[i] > List[i+1]:

            indexFirst.append(i)

        else:

            break
            
    if len(indexFirst) == 0:

        return False, List
    
    else:

        indexFirst.append(indexFirst[len(indexFirst)-1]+1)

    Substring = List[indexFirst[0]:indexFirst[len(indexFirst)-1]+1]

    Substring.reverse()

    for i in range(len(Substring)):

        List[indexFirst[i]] = Substring[i]

    if checkIncrease(List,N):

        return True, List

    else: 

        return False, List

def checkIncrease(List,N):

    for i in range(N-1):

        if List[i]< List[i+1]:

            continue

        else:

            return False

    return True