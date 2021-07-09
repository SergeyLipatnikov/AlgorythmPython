def MisterRobot(N, data):

    Steps = False

    count = 0

    while Steps != True:

        if data[count] < data[count+1]:

            count += 1

        else:

            if count == 0:

                temp = data[count:count+3]
            
            else:

                temp = data[count-1:count+2]

            for i in range(3):

                first = temp[1]

                second = temp[2]

                third = temp[0]

                temp[0] = first
                temp[1] = second
                temp[2] = third

                if first < second and second < third:

                    break

                elif i == 2:

                    return False
            
            data[count] = second
            data[count-1] = first
            data[count+1] = third

            count = 0

        if count == N - 1:
            
            return True