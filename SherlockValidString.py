def SherlockValidString(s):

    Symbols ={}

    for Symbol in s:

        if len(Symbols) == 0:

            Symbols.update({Symbol:1})

        else:

            Check = list(Symbols.keys())

            count = 0

            for i in range(len(Check)):

                count += 1

                if Symbol == Check[i]: 

                    Symbols[Symbol] += 1
                
                elif count == len(Check):

                    Symbols.update({Symbol:1})

    UniqValues = list(set(Symbols.values()))

    UniqValues.sort()

    sorted_keys = Symbols.keys()

    if len(UniqValues) > 2:

        return False

    elif len(UniqValues) == 1:

        return True

    elif abs(UniqValues[0] - UniqValues[1]) > 1:

        return False
    
    else:

        temp1 = []
        temp2 = []

        n = 0

        for values in UniqValues:

            n += 1

            if n == 1:

                for check in sorted_keys:

                    if values == Symbols[check]:

                        temp1.append(check)
            else:

                for check in sorted_keys:

                    if values == Symbols[check]:

                        temp2.append(check)  

        if (len(temp1) >= 2) and (len(temp2) >= 2):

            return False

        else:

            return True