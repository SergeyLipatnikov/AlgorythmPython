def MassVote(N, Votes):

    result = ''

    candidate = {a: Votes[a-1] for a in range(1,N+1)}

    Votes.sort()

    SummVotes = 0

    for i in range(N):

        SummVotes += Votes[i]

    if Votes[N-1] == Votes[N-2]:

        return "no winner"

    else:

        if round(Votes[N-1]/SummVotes*100, 3) > 50:

            for Number, Values in candidate.items():

                if Votes[N-1] == Values:

                    return "majority winner " + str(Number)
        
        elif round(Votes[N-1]/SummVotes*100, 3) <= 50:

            for Number, Values in candidate.items():

                if Votes[N-1] == Values:

                    return "minority winner " + str(Number)