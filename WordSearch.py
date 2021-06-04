def WordSearch(lens, s, subs):

    FinalString = []
    Temp = []
    Startpos = 0
    Endpos = 0
    count = 0

    for i in s:

        if count == len(s) - 1:

            FinalString.append(s[Startpos:count+1])

        else:

            Temp.append(s[Startpos::lens])

            for j in Temp:

                if j == ' ':

                    Endpos += s[Startpos:].index(i)

                    FinalString.append(s[Startpos:Endpos])

                    Startpos = count + 1

                    Endpos += 1
        
        count += 1

    # for i in s:

    #     if count == len(s) - 1:

    #         FinalString.append(s[Startpos:count+1])

    #     else:

    #         if i == ' ':

    #             Endpos += s[Startpos:].index(i)

    #             FinalString.append(s[Startpos:Endpos])

    #             Startpos = count + 1

    #             Endpos += 1
        
    #     count += 1

    # j= 0 
    
    # while j < len(FinalString):

    #     if len(FinalString[j]) < lens//2:

    #         temp = FinalString[j]

    #         FinalString[j] = ' '
            
    #         temp = temp + ' ' + FinalString[j+1]
            
    #         FinalString[j] = temp

    #         j += 1

    #     j += 1

    return FinalString

print(WordSearch(12, 'строка разбивается на набор строк через выравнивание по заданной ширине', 'строка'))