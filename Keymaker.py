def Keymaker(k):

    String = ''

    Array = []

    for i in range(k):

        Array.append(False)

    Array = KeymasterWork(Array,k)

    return String, Array

def KeymasterWork(Array, N):

    for i in range(N):

        if i == 0:

            Array = FirstIteration(Array,N)

        else :

            Temp = i

            Array = Iteration(Array,Temp)

    return Array

def FirstIteration(Array,N):

    for i in range(N):

        Array[i] = not(Array[i])

    return Array

def Iteration(Array,i):

    print(Array[i::i+1])

    # Array[i::i+1] = not(Array[i::i+1])

    # return Array

print(Keymaker(6))

# Array = [0,0,0,1]

# print(Array[1::2])