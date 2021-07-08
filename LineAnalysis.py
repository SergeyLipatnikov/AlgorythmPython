def LineAnalysis(line):

    if line == '*':

        return True

    elif line == '**':

        return True

    elif line == '***':

        return True

    elif line == '*.*':

        return True

    else:

        count = 0

        string = ''

        for i in line:

            if i != '*':

                string += i

            else:

                count += 1

                string += i

            if count == 2:

                break

        Number = len(string)

        char = True
        
        for j in range(Number - 1,len(line),Number - 1):

            temp = line[j + 1 - Number:j+1]

            if temp != string:

                char = False

                break
        
        if char:

            return True

        else:

            return False