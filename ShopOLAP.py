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

    sorted_keys = sorted(lists, key=lambda x:x[1], reverse=True)

    for w in sorted_keys:

        FinalList.append(w + ' ' + str(lists[w]))

    return FinalList, UniqValues, sorted_keys

print(ShopOLAP(5,['dress1 5','handbug32 3','dress2 3','handbug23 2','handbug128 4']))