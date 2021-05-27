def WordSearch(lens, s, subs):

    FinalString = []
    String = list(s)
    StartStr = []
    Startsubspos = 0
    Subsstr_len = lens
    s2 = ''

    for i in range(len(String)):
        
        if String[i] == ' ': #and len(s2) > 6:
            s2.join(String[Startsubspos : i])

            FinalString.append(s2)

            Startsubspos = i+1

            s2 = '' 


        
    return FinalString

print(WordSearch(12, 'строка разбивается на набор строк через выравнивание по заданной ширине', 'строка'))