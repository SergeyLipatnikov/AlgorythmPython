def Tankrush(H1,W1,S1,H2,W2,S2):

    pole = S1.split()

    tanks = S2.split()

    result = 0

    for i in range(H2):

        for j in range(H1):

            for k in range(len(pole[j]) - len(tanks[i]) + 1):

                char = True

                for n in range(len(tanks[i]) - 1, -1, -1):

                    if pole[j][k + n] != tanks[i][n]:

                        char = False

                        break

                if char is True:

                    if i == H2-1:

                        result +=1

                        break
                        
                    elif j == H1-1:

                        break 

                    else:

                        for l in range(i+1,H2):

                            for m in range(j+1,H1):

                                for k in range(len(pole[m]) - len(tanks[l]) + 1):

                                    char = True

                                    for n in range(len(tanks[l]) - 1, -1, -1):

                                        if pole[m][k + n] != tanks[l][n]:

                                            char = False

                                            break
                                    else:

                                        if char is True:

                                            result += 1

                                            continue
                                    
                                break

    if result == H2:

        return True

    else:

        return False

print(Tankrush(3, 4, '1234 2345 0237', 2, 2, '23 34 37'))