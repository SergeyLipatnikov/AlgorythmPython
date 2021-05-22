def MadMax(N, Tele):

    Tele.sort()

    Final = []

    Max = max(Tele)

    temp = Tele[N//2]

    Tele[N//2] = Max

    Tele[N-1] = temp

    Forward = Tele[0 : N//2+1]

    Reverse = Tele[N//2+1 : N-1]

    Reverse.reverse()

    Final.extend(Forward)

    Final.extend(Reverse)

    if len(Tele) > 1:

        Final.append(Tele[N-1])

    return Final
