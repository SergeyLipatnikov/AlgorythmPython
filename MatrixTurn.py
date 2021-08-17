def MatrixTurn(Matrix,M,N,T):

    count = 0

    String = ''

    String = CreateGorizontRightString(Matrix,String)
    String = CreateVerticalDownString(Matrix,M,N,String)
    String = CreateGorizontLeftString(Matrix,M,N,String)
    String = CreateVerticalUpString(Matrix,M,String)
    # while count < M // 2:

    #     String = ''

    #     String = CreateGorizontLeftString(Matrix,)


    #     count += 1

    return String

def TurnString(S,N, Symbol):

    final = S[N]

    for i in range(N):

        if i == N- 1:

            break

        else:

            S[i+1] = S[i]

    S[0] = Symbol

    return S, final

def CreateVerticalDownString(Array, M, N, String):

    for i in range(1,M-1):

        String += Array[i][N-1]

    return String

def CreateVerticalUpString(Array, M, String):

    for i in range(M-2,0,-1):

        String += Array[i][0]

    return String

def CreateGorizontRightString(Array, String):

    String += Array[0]

    return String

def CreateGorizontLeftString(Array, M, N, String):

    for i in range(N-1,-1,-1):

        String += Array[M-1][i]

    return String

print(MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3))