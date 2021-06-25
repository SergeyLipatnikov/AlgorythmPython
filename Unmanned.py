def Unmanned(L, N, track):

    result = 0

    for i in range(N):

        if i == 0:

            result += track[i][0]

            if result > track[i][1]:

                continue
            
            else:
                
                result += (track[i][1] - result)

                continue

        else:

            result += track[i][0] - track[i-1][0]

        if (result // (track[i][1] + track[i][2])) > 0:

            Signal =  result - ((result // (track[i][1] + track[i][2])) * (track[i][1] + track[i][2]))

            if Signal > track[i][1]:

                continue

            else:

                result += (track[i][1] - Signal)                

        
        else:

            result += track[i][1]

    result += L - track[i][0]

    return result