def MatrixTurn(Matrix,M,N,T):

    MatrixArray = CreateMatrixArray(Matrix)

    for i in range(T):
        
        count = 0
        
        SubStrings = []

        while count < M // 2:

            String = []

            String = CreateSubString(MatrixArray,M,N,String,count)

            String = TurnString(String, M, N, count)

            SubStrings.append(String)

            MatrixArray= ChangeSubString(MatrixArray, M, N, SubStrings,count)

            count += 1

    return ReturnArray(Matrix,MatrixArray)

def TurnString(S, M, N, count):

    if M == N and (M // 2 -1 ==count):

        start = S[len(S)-1][len(S[len(S)-1])-1]

        for i in range(len(S)-1,-1,-2):

            end = S[i-2][len(S[i-2])-1]

            for j in range(len(S[i])-1,-1,-1):

                S[i][j] = S[i][j-1]

            S[i][0]= end

        S[1][0] = start
    
    else:

        start = S[len(S)-1][len(S[len(S)-1])-1]

        for i in range(len(S)-1,-1,-1):

            end = S[i-1][len(S[i-1])-1]

            for j in range(len(S[i])-1,-1,-1):

                S[i][j] = S[i][j-1]

            S[i][0]= end

        S[0][0] = start

    return S

def CreateVerticalDownString(Array, M, N, String,count):

    temp = []

    for i in range(0+count,M-count):

        temp.append(Array[i][N-1-count])

    String.append(temp)

    return String

def CreateVerticalUpString(Array, M, String,count):

    temp = []

    for i in range(M-1-count,-1+count,-1):

        temp.append(Array[i][0+count])

    String.append(temp)

    return String

def CreateGorizontRightString(Array,N,String,count):

    temp = []

    for i in range(1+count,N-1-count):

        temp.append(Array[0+count][i])

    String.append(temp)

    return String

def CreateGorizontLeftString(Array, M, N, String,count):

    temp = []

    for i in range(N-2-count,0+count,-1):

        temp.append(Array[M-1-count][i])

    String.append(temp)

    return String

def CreateSubString(Array, M, N, String,count):

    String = CreateGorizontRightString(Array,N,String,count)
    String = CreateVerticalDownString(Array,M,N,String,count)
    String = CreateGorizontLeftString(Array,M,N,String,count)
    String = CreateVerticalUpString(Array,M,String,count)

    return String

def CreateMatrixArray(MatrixString):

    MatrixArray= []

    for i in range(len(MatrixString)):

        MatrixArray.append(list(MatrixString[i]))

    return MatrixArray

def ChangeGorizontRightString(Array,N,SubArray,count):

    for i in range(1+count,N-1-count):

        Array[0+count][i] = SubArray[count][0][i-1-count]

    return Array

def ChangeVerticalDownString(Array, M, N, SubArray,count):

    for i in range(0+count,M-count):

        Array[i][N-1-count] = SubArray[count][1][i-count]

    return Array

def ChangeGorizontLeftString(Array, M, N, SubArray,count):

    for i in range(N-2-count,0+count,-1):

        Array[M-1-count][i] = SubArray[count][2][N-2-count-i]

    return Array

def ChangeVerticalUpString(Array, M, SubArray,count):

    for i in range(M-1-count,-1+count,-1):

        Array[i][0+count] = SubArray[count][3][M-1-count-i]

    return Array

def ChangeSubString(Array, M, N, SubArray,count):

    Array = ChangeGorizontRightString(Array,N,SubArray,count)
    Array = ChangeVerticalDownString(Array,M,N,SubArray,count)
    Array = ChangeGorizontLeftString(Array,M,N,SubArray,count)
    Array = ChangeVerticalUpString(Array,M,SubArray,count)

    return Array

def ReturnArray(Array, turnArray):

    for i in range(len(Array)):

        Array[i]=''.join(turnArray[i])

    return Array