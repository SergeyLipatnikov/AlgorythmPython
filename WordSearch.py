def WordSearch(lens, s, subs):

    FinalString = []
    Temp = ''
    Startpos = 0
    Endpos = lens
    sublenght = len(s)//(lens//2)
    Result =[]

    for i in range(sublenght):

        Temp += s[Startpos:Endpos]

        if Endpos >= len(s):

            FinalString.append(s[Startpos:Endpos])

            break
                
        for j in range(len(Temp)):

            if Temp[j] == ' ':

                if j < lens//2:

                    continue

                SubEndpos = j

                FinalString.append(Temp[:SubEndpos])

                Temp = ''

                Startpos += SubEndpos + 1
                
                Endpos += SubEndpos + 1

                break

            elif j == len(Temp) -1:

                FinalString.append(Temp.lstrip())

                Startpos += lens 
                
                Endpos += lens 

                Temp = ''
    i = 0

    j = 0
    
    for k in range(len(FinalString)):

        if FinalString[k].find(' ') > - 1:

            count = FinalString[k].index(' ')

            Temp = FinalString[k][:count]

            if Temp == subs:

                Result.append(True)

            else:

                Temp = FinalString[k][count + 1:]

                if Temp == subs:

                    Result.append(True)

                else:

                    Result.append(False)                
        
        elif len(FinalString[k]) != len(subs):

            Result.append(False)

        else:

            Temp = FinalString[k]

            if Temp == subs:

                Result.append(True)

            else:

                Result.append(False)  


    return FinalString, Result
