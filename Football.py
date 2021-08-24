def Football(F,N):

    Check = F.copy()
    
    F.sort()

    return method2(Check,F,N)

def method1(List1,List2,N):

    Final = []

    for i in range(N):

        if List1[i] != List2[i]:

            Final.append(i)

    if len(Final) == 2:

        return True
    
    else:

        return False

def method2(List1,List2,N):

    count = 0 

    for i in range(N-1,0):

        if List1[i] > List1[i-1]:

            count += 1

    if count > 2:

        return False

    else:

        return True

print(Football([9,5,3,7,1],5))