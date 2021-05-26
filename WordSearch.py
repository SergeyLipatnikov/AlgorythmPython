def WordSearch(lens, s, subs):

    FinalString = []
    StartStr = []
    Startsubspos = 0
    Subsstr_len = lens

    for i in range(len(s)):
        s2 = ''
        for i in range(Startsubspos,Subsstr_len):

            if s[i] != ' ' and len(s2) > 6:
                s2.append(s[i])

        FinalString.append(s2)   
        
    return FinalString

print(WordSearch(12, 'строка разбивается на набор строк через выравнивание по заданной ширине', 'строка'))