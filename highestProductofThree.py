def findHighestThreeProduct(inputList):
    if len(inputList) < 3:
        raise IndexError('Input List should be atleast three integers long')
    highestThreeProduct = inputList[0] * inputList[1] * inputList[2]
    highestTwoProduct = inputList[0] * inputList[1]
    lowestTwoProduct = inputList[0] * inputList[1]
    highest = max(inputList[0], inputList[1])
    lowest = min(inputList[0], inputList[1])
    for index, item in enumerate(inputList):
        if index < 2:
            continue
        highestThreeProduct = max(highestThreeProduct, item * highestTwoProduct, item * lowestTwoProduct)
        highestTwoProduct = max(highestTwoProduct, item * highest, item * lowest)
        lowestTwoProduct = min(lowestTwoProduct, item * lowest, item * highest)
        highest = max(item, highest, lowest)
        lowest = min(item, lowest, highest)
    return highestThreeProduct


print findHighestThreeProduct([-1,-2,-3,4,5])
print findHighestThreeProduct([3,4,5,6,7,8,9])
print findHighestThreeProduct([-2,-3,-4,-5,-6,3])
