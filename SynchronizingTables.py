def SynchronizingTables(N, ids, salary):

    SortedIds = ids.copy()

    SortedSalary = salary.copy()

    SortedSalary.sort()
    
    SortedIds.sort()

    dictonary = {SortedIds[i]: SortedSalary[i] for i in range(N)}

    FinalSalary = []

    for i in range(N):

        FinalSalary.append(dictonary[ids[i]])

    return FinalSalary
