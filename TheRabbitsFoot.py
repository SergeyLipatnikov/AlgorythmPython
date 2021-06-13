def TheRabbitsFoot(s, encode):

    String =''

    FinalList =[]

    FinalString = ''

    if encode == True:

        for i in s:

            if i != ' ':

                String += i        

        lenght = len(String) ** 0.5

        min = int(lenght / 1)

        max = min + 1

        if min * max < len(String):

            min += 1

        StartPos = 0

        End = max

        i = 0

        for i in range(min):

            FinalList.append(String[StartPos:End])

            StartPos += max

            End += max

        Substring = ''

        FinalString = ''

        for j in range(max):

            for k in range(len(FinalList)):

                if j > len(FinalList[k]) - 1:

                    continue

                Substring += FinalList[k][j]

            if j == max - 1:

                FinalString += Substring

            else:
                                      
                FinalString += Substring + ' '

            Substring = ''

    else:

        for i in s:

            if i != ' ':

                String += i        

        lenght = len(String) ** 0.5

        min = int(lenght / 1)

        max = min + 1

        check = 0

        if min * max < len(String):

            check = len(String) - min * max

            min += 1

        else:

            check = min * max - len(String)

        End = max

        i = 0

        count = 1
        
        StartPos = 0

        Substring = ''

        NumberString = 1

        for i in range(min):

            CheckString = StartPos

            for k in range(max):
                
                if check < count:

                    if NumberString > len(String):

                        break

                    Substring += String[CheckString]

                    CheckString += max - 1

                    NumberString += 1

                    continue    

                count += 1

                Substring += String[CheckString]

                NumberString += 1

                CheckString += max
            
            FinalList.append(Substring)

            check -= 1

            if check < 0:

                check = 0

            Substring =''

            StartPos += 1

            count = 0

        for j in range(max):
                                  
            FinalString += FinalList[j]

    return FinalString