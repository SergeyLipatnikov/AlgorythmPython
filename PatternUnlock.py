def PatternUnlock(N, hits):

    layout = [[6,1,9],
              [5,2,8],
              [4,3,7]]

    First = []

    Second = []

    length = 0.0

    StrLength = ''

    for i in range(3):

            for j in range(3):

                if layout[i][j] == hits[0]:

                    First.append(i)
                    First.append(layout[i].index(hits[0]))

    for k in range (1, N):

        for i in range(3):

            for j in range(3):

                if layout[i][j] == hits[k]:
                    
                    Second.clear()
                    Second.append(i)
                    Second.append(layout[i].index(hits[k]))
        
        if First[0] == Second[0]:

            length += 1

        elif First[1] == Second[1]:

            length += 1

        else:

            length += round((1+1) ** (0.5), 6)

        First.clear()  
        First = Second.copy()

    temp = str(round(length,5))

    temp2 = temp.replace(".", "")

    StrLength = temp2.replace("0", "")

    return StrLength