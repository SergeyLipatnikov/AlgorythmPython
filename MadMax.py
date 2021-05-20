def MadMax(N, Tele):

    Tele.sort()

    SortTele = Tele

    Max = max(SortTele)

    temp = SortTele[N//2]

    SortTele[N//2] = Max

    SortTele[N-1] = temp

    Forward = SortTele[0 : N//2+1]

    Reverse = SortTele[N//2+1 : N-1]

    Reverse.reverse()

    Final = Forward

    Final.extend(Reverse)

    Final.append(SortTele[N-1])

    return Final
     

    

print(MadMax(7,[120,1,35,48,243,187,16]))