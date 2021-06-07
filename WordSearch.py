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

        if len(FinalString[k] == len(subs)):

            print('kek')

        elif FinalString[k].isspace():

            count = FinalString[k].index(' ')

            Temp = FinalString[k][:count]

            for i in range(len(Temp) - len(subs) + 1):

                char = True

                for j in range(len(subs) - 1, -1, -1):

                    if FinalString[k][i + j] != subs[j]:

                        char = False

                        break

                if char is True:

                    Result.append(True)

        Result.append(False)

    return FinalString, Result

print(WordSearch(12, 'строка разбивается на набор строк через выравнивание по заданной ширине rtr kek privetik', 'строк'))