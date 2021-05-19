def ConquestCampaign (N, M, L, battalion):

    day = 0

    CheckBattalion = [battalion[0],battalion[1]]

    if (L > 1):

        for i in range(3,L*2,2):

            uni = True

            for j in range(1,len(CheckBattalion),2):

                if ((battalion[i-1] == CheckBattalion[j-1]) and (battalion[i] == CheckBattalion[j])):

                    uni = False

                    break
            
            if (uni):
            
                CheckBattalion.append(battalion[i-1])
                CheckBattalion.append(battalion[i])

    field = []

    for i in range(N):

        field.append([0]* M)


    
    CheckField = False

    while (CheckField != True):

        if (day == 0):

            for i in range(1,len(CheckBattalion),2):

                field[CheckBattalion[i-1]-1][CheckBattalion[i]-1] = 1                 

            day += 1
        
        else:

            TempFieldBattalion = []

            for i in range(N):
                for j in range(M):
                    if (field[i][j] == 1):
                        TempFieldBattalion.append(i)
                        TempFieldBattalion.append(j)
            
            if len(TempFieldBattalion) == N*M*2:

                CheckField = True

                break

            else:

                for i in range(1,len(TempFieldBattalion),2):

                    if TempFieldBattalion[i] == 0 and TempFieldBattalion[i-1] == 0:

                        field[TempFieldBattalion[i - 1] + 1][TempFieldBattalion[i]] = 1
                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] + 1] = 1
                    
                    elif TempFieldBattalion[i] == 0 and TempFieldBattalion[i-1] == N-1:

                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] + 1] = 1
                        field[TempFieldBattalion[i - 1] - 1][TempFieldBattalion[i]] = 1
                    
                    elif TempFieldBattalion[i] == M-1 and TempFieldBattalion[i-1] == 0:

                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] - 1] = 1
                        field[TempFieldBattalion[i - 1] + 1][TempFieldBattalion[i]] = 1

                    elif TempFieldBattalion[i] == M-1 and TempFieldBattalion[i-1] == N-1:

                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] - 1] = 1
                        field[TempFieldBattalion[i - 1] - 1][TempFieldBattalion[i]] = 1
                    
                    elif TempFieldBattalion[i] == 0:

                        field[TempFieldBattalion[i - 1] + 1][TempFieldBattalion[i]] = 1
                        field[TempFieldBattalion[i - 1] - 1][TempFieldBattalion[i]] = 1
                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] + 1] = 1

                    elif TempFieldBattalion[i] == M-1:

                        field[TempFieldBattalion[i - 1] - 1][TempFieldBattalion[i]] = 1
                        field[TempFieldBattalion[i - 1] + 1][TempFieldBattalion[i]] = 1
                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] - 1] = 1

                    elif TempFieldBattalion[i-1] == 0:

                        field[TempFieldBattalion[i - 1] + 1][TempFieldBattalion[i]] = 1
                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] + 1] = 1
                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] - 1] = 1

                    elif TempFieldBattalion[i-1] == N-1:

                        field[TempFieldBattalion[i - 1] - 1][TempFieldBattalion[i]] = 1
                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] + 1] = 1
                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] - 1] = 1

                    else:

                        field[TempFieldBattalion[i - 1] - 1][TempFieldBattalion[i]] = 1
                        field[TempFieldBattalion[i - 1] + 1][TempFieldBattalion[i]] = 1 
                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] + 1] = 1 
                        field[TempFieldBattalion[i - 1]][TempFieldBattalion[i] - 1] = 1

            day += 1

    return day

