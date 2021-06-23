def UFO(N, data, octal):

    result = []

    if octal:

        for i in range(N):

            temp = str(data[i])

            result.append(int(temp,8))
    
    else:

        for i in range(N):

            temp = str(data[i])

            result.append(int(temp,16))


    return result