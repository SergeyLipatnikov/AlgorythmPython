def squirrel (N):

    nuts = 1

    for i in range(1, N+1):

        nuts *= i

    
    nuts = str(nuts)

    return int(nuts[0])
