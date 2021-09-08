def Keymaker(k):

    String = ''

    Array = []

    for i in range(k):

        Array.append(False)

    Array = KeymasterWork(Array,k)

    String = StringInterpritation(String,Array,k)

    Check = Delitel(k)

    return String, Check

def KeymasterWork(Array, N):

    for i in range(N):

        if i == 0:

            Array = FirstIteration(Array,N)

        else :

            Temp = i

            Array = Iteration(Array,Temp,N)

    return Array

def FirstIteration(Array,N):

    for i in range(N):

        Array[i] = not(Array[i])

    return Array

def Iteration(Array,i,N):

    for k in range(i,N,i+1):

        Array[k] = not(Array[k])

    return Array

def StringInterpritation(String,Array, N):

    for i in range(N):

        if Array[i]:

            String += '1'
        else:

            String += '0'

    return String

def Delitel(k):

    Array = []

    for i in range(k - 1, 1, -1):

        if (k % i == 0):

            Array.append(i)

    Len = len(Array)

    return Array,Len


print(Keymaker(126))