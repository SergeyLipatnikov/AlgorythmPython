def TransformTransform(A,N):

    k = 0

    Massive = Transform(Transform(A,N),len(Transform(A,N)))

    for i in range(len(Massive)):

        k += Massive[i]

    if k % 2 == 0:

        return True

    else:

        return False


def Transform(Array, N):

    B = []
    
    for i in range(N):

        for j in range(N-i):

            k=i+j

            if k == j:

                B.append(Array[j])

            else:

                Temp = Array[j:k+1]

                Temp.sort()

                B.append(Temp[len(Temp)-1])

    return B

print(TransformTransform([2,3,4,9,8,3],6))