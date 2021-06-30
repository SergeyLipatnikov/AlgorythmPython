def TankRush(H1,W1,S1,H2,W2,S2):

    pole = S1.split()

    tanks = S2.split()

    result = 0

    i,j = 0,0

    while i < H2:

        while j < H1:

            for k in range(len(pole[j]) - len(tanks[i]) + 1):

                char = True

                for n in range(len(tanks[i]) - 1, -1, -1):

                    if pole[j][k + n] != tanks[i][n]:

                        char = False

                        break

                if char is True:

                    if i == H2-1:

                        result +=1

                        i += 1

                        j += 1

                        if result == H2:

                            return True

                        else:

                            return False

                    else:

                        for k in range(len(pole[j+1]) - len(tanks[i+1]) + 1):

                            char = True

                            for n in range(len(tanks[i+1]) - 1, -1, -1):

                                if pole[j+1][k + n] != tanks[i+1][n]:

                                    char = False

                                    break

                            if char is True:

                                result += 1

                                i += 1

                                break
                        
            j += 1
        
        i += 1

        j = 0
                    
    if result == H2:

        return True

    else:

        return False