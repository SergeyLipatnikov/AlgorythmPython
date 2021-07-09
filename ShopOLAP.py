def ShopOLAP(N,items):

    FinalList = []

    lists = {}

    for i in range(N):

        temp = items[i].split()

        if lists.get(temp[0]) != None:

            lists[temp[0]] += int(temp[1])

        else:

            lists.update({temp[0]: int(temp[1])})

    list_keys = list(lists.keys())

    list_keys.sort()

    for i in list_keys:

        FinalList.append(i+ ' ' + str(lists[i]))

    return FinalList