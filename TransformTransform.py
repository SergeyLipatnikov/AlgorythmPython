def TransformTransform(A,N):

    return Transform(A,N)

    # if k % 2 == 0:

    #     return True

    # else:

    #     return True


def Transform(Array, N):

    B = []

    for i in range(N-1):

        for j in range(N-1-i):

            k=i+j

            if k == j:

                B.append(Array[j])

            else:

                Temp = Array[j:k].sort()

                print(Temp)

                B.append(Array[len(Array[j:k])-1])

    return B

print(TransformTransform([3,2,5,4,8,7],6))