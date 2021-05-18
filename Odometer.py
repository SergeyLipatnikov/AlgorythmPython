def odometer ( oksana ):

    distance = 0

    for i in range(len(oksana)):

        if (i % 2 == 0):

            speed = oksana[i]

        else:

            if (i == 1):

                time = oksana[i]

            else:

                time = oksana[i] - oksana[i-2]
            
            distance += speed * time

    return distance