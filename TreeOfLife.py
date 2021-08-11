def TreeOfLife(H, W, N, tree):

    StartTree = []

    for i in range(H):

        A = []

        StartTree.append(A)

        for j in range(W):

            if tree[i][j] == '.':

                StartTree[i].append(0)

            else:

                StartTree[i].append(1)

    for k in range(N):

        if k % 2 == 0:

            for i in range(H):

                for j in range(W):

                    StartTree[i][j] += 1
        
        else:

            for i in range(H):

                for j in range(W):

                    StartTree[i][j] += 1

            StartTree = CheckKill(H,W, StartTree)

    FinalTree = []

    for i in range(H):

        String = ''

        for j in range(W):

            if StartTree[i][j] == 0:

                String += '.'
            else:
                String += '+'
        
        FinalTree.append(String)

    return FinalTree

def CheckKill(H, W, Tree):

    KillTree = []

    for k in range(H):

        Temp =[]

        KillTree.append(Temp)

        for n in range(W):

            KillTree[k].append(0)

    for i in range(H):

        for j in range(W):

            if Tree[i][j] >= 3:

                KillTree[i][j] = 1

                if i == 0 and j == 0:
                    KillTree[i+1][j] = 1
                    KillTree[i][j+1] = 1
                elif i == H-1 and j == W-1:
                    KillTree[i-1][j] = 1
                    KillTree[i][j-1] = 1
                elif i == 0 and j == W-1:
                    KillTree[i+1][j] = 1
                    KillTree[i][j-1] = 1
                elif i == H-1 and j == 0:
                    KillTree[i-1][j] = 1
                    KillTree[i][j+1] = 1
                elif i == 0:
                    KillTree[i+1][j] = 1
                    KillTree[i][j-1] = 1
                    KillTree[i][j+1] = 1
                elif j == 0:
                    KillTree[i-1][j] = 1
                    KillTree[i+1][j] = 1
                    KillTree[i][j+1] = 1
                elif i == H-1:
                    KillTree[i-1][j] = 1
                    KillTree[i][j-1] = 1
                    KillTree[i][j+1] = 1
                elif j == W-1:
                    KillTree[i-1][j] = 1
                    KillTree[i+1][j] = 1
                    KillTree[i][j-1] = 1
                else:
                    KillTree[i-1][j] = 1
                    KillTree[i+1][j] = 1
                    KillTree[i][j-1] = 1
                    KillTree[i][j+1] = 1
    for m in range(H):

        for s in range(W):

            if KillTree[m][s] == 1:

                Tree[m][s] = 0

    return Tree