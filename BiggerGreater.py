def BiggerGreater(input):

    AllVariant = []

    FinalVariant = []
    Word = list(input)
    permutation = list(range(len(input)))
    direction = [-1]*len(input)
    mobile_element_index = find_max_mobile_element(permutation, direction)
    while mobile_element_index != -1:
        temp =[]
        mobile_element = permutation[mobile_element_index]
        next_index = mobile_element_index + direction[mobile_element_index]
        swap_element(permutation, direction, mobile_element_index, next_index)
        change_direction(permutation, direction, mobile_element)
        for i in range(len(permutation)):
            temp.append(Word[permutation[i]])            
        String = ''.join(temp)
        AllVariant.append(String)
        mobile_element_index = find_max_mobile_element(permutation, direction)

    AllVariant.sort()

    for k in range(len(AllVariant)):

        if input < AllVariant[k]:

            FinalVariant.append(AllVariant[k])

    if len(FinalVariant) == 0:

        return ''

    FinalVariant.sort()

    return FinalVariant[0]


def find_max_mobile_element(permutation, direction):
    index = -1
    for i in range(len(permutation)):
        next_element_index = i + direction[i]
        if next_element_index >= 0 and next_element_index < len(permutation):
            if permutation[i] > permutation[next_element_index]:
                if index == -1:
                    index = i
                else:
                    if permutation[i] > permutation[index]:
                        index = i
    return index


def change_direction(permutation, direction, mobile_element):
    for i in range(len(permutation)):
        if permutation[i] > mobile_element:
            direction[i] = direction[i]*(-1)


def swap_element(permutation, direction, i, j):
    permutation[i], permutation[j] = permutation[j], permutation[i]
    direction[i], direction[j] = direction[j], direction[i]
