def SumOfThe(N,data):

    Checkresult = False

    count = 1

    sum = 0

    data.sort()

    while Checkresult != True:

        First = data[0]

        for i in range(1,N):

            sum += data[i]

        if First == sum:

            return First
        
        else:

            Temp = First

            data[0] = data[count]

            data[count] = Temp

            sum = 0

            count += 1     

    return False       