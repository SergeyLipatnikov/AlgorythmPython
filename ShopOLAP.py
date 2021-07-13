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

    UniqValues.sort(reverse=True)

    sorted_keys = lists.keys()

    for values in UniqValues:

        temp ={}

        for check in sorted_keys:

            if values == lists[check]:

                temp.update({check: values})

        Finalappend = list(temp.keys())

        Finalappend.sort()

        for w in Finalappend:

            FinalList.append(w + ' ' + str(lists[w]))

    return FinalList