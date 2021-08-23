def white_walkers(village):

    return CheckWalkers(village,CheckSum(village,FindNumbers(village)))

def FindNumbers(String):

    Index =[]

    for i in range(len(String)):

        if String[i].isdigit():

            Index.append(i)

    return Index
    
def CheckSum(String, Index):

    RightPosition = []

    if len(Index) == 1:

        return []

    for i in range(len(Index)):

        temp = []

        for j in range(i+1,len(Index)):

            if int(String[Index[i]]) + int(String[Index[j]]) == 10:

                temp.append(Index[i])
                temp.append(Index[j])
                RightPosition.append(temp)
                temp = []
                break
            
    return RightPosition

def CheckWalkers(String, Sums):

    Check = False

    for i in range(len(Sums)):

        start = Sums[i][0] + 1
        stop = Sums[i][1]

        count = 0

        Check = False

        for j in range(start, stop):

            if String[j] == '=':

                count += 1

        if count == 3:

            Check = True

    if Check:

        return True

    else:

        return False