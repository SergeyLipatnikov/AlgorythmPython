def WordSearch(lens, s, subs):

    FinalString = []
    s2 = ''
    SEPARATORS= " "

    for char in s:
        if char in SEPARATORS:
            if s2: FinalString.append(s2)
            s2=''
        else:
            s2+=char
    
    for i in range(len(FinalString)):

        if len(FinalString[i]) < 6:

            FinalString[i].join(FinalString[i+1])


    return FinalString

print(WordSearch(12, 'строка разбивается на набор строк через выравнивание по заданной ширине', 'строка'))