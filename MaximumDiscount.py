def MaximumDiscount(N, price):

    sale = 0

    Number = N // 3

    price.sort(reverse=True)

    for i in range(1,Number+1):

        sale += price[i*3-1]

    return sale
