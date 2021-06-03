def WordSearch(lens, s, subs):

    FinalString = []
    s2 = ''
    SEPARATORS= " \n"

    if len(s) > 0 and s[0] != ' ':
        word_count = 1
        for i in range(len(s)-1):

            # пары символов "пробел+следующий не пробел" считаем как слово
            if s[i] == ' ' and s[i+1] != ' ':
                
                word_count += 1

    for i in range(len(s)-1):

        # пары символов "пробел+следующий не пробел" считаем как слово
        if s[i] == ' ' and s[i+1] != ' ':
            
            word_count += 1
    
    for i in range(len(FinalString)):

        if len(FinalString[i]) < 6:

            FinalString[i].join(FinalString[i+1])


    return FinalString

print(WordSearch(12, 'строка разбивается на набор строк через выравнивание по заданной ширине', 'строка'))