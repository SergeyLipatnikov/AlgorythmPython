def ShopOLAP(N,items):

    FinalList = []

    lists = {}

    for i in range(N):

        temp = items[i].split()

        if lists.get(temp[0]) != None:

            lists[temp[0]] += int(temp[1])

        else:

            lists.update({temp[0]: int(temp[1])})

    UniqValues = list(set(lists.values()))

    sorted_keys = sorted(lists, key=UniqValues.sort(reverse=True))

    for w in sorted_keys:

        FinalList.append(w + ' ' + str(lists[w]))

    return FinalList