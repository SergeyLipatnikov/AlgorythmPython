def ConquestCampaign (N, M, L, battalion):

    day = 1

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

        if (day == 1):

            for i in range(1,len(CheckBattalion),2):

                field[CheckBattalion[i-1]-1][CheckBattalion[i]-1] = 1                 

    return CheckBattalion, field

print(ConquestCampaign(3,4,6,[2,2,3,4,1,3,3,4, 2,2,1,3]))




    # for i in range(N):

    #     for j in range(M):

