#Create aan array of the size of the amount + 1
#for each denominations, calculate how many ways to achieve
#each amount in the array
#subsequent denominations are additions on top of exisiting ways
#return the findwaysfromCents[amount] to get the number of ways to get the amount
def findWaysDenominations(amount, denominations):
    findwaysfromCents = [0] * (amount + 1)
    findwaysfromCents[0] = 1
    for coin in denominations:
        for higherAmt in range(coin, amount + 1):
            higherAmtRem = higherAmt - coin
            findwaysfromCents[higherAmt] += findwaysfromCents[higherAmtRem]
    return findwaysfromCents[amount]

print findWaysDenominations(5, [1,3,5])
