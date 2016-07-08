#meeting intervals where everybody is free
#[(8,10), (11,12), (12,2), (3,4)]
#[(8,9), (10,11), (11,1), (3,4)]
#The above should return (2,3)
#The way to solve in optimized way
#Create an array from the first start time of all the employee start time
#Lets say 8 am
#The array units is 1 hour
#each element translates to 8 + i where i is the index of the array
#For every start time we add one to the (time - 8)
#for every end time, we subtract one to the (time - 8)

def findInterval(intervalList):
    endMaxTime = 16
    minTime = 8
    intervalArr = [0] * (endMaxTime - minTime + 1)
    for person in intervalList:
        for times in person:
            index1 = times[0] - minTime
            index2 = times[1] - minTime
            # print index1, index2
            intervalArr[index1] += 1
            intervalArr[index2] -= 1
    intervalStart = -1
    intervalEnd = -1
    sum = 0
    for i in range(len(intervalArr)):
        sum += intervalArr[i]
        if sum == 0 and intervalStart < 0:
            intervalStart = i
            intervalEnd = i+1
        elif sum == 0 and intervalStart >= 0 and (i+1 < endMaxTime - i+1):
            intervalEnd = i+1
    return intervalStart+8, intervalEnd+8


print findInterval([[(8,10), (11,12), (12,14), (15,16)], [(8,9), (10,11), (11,13), (15,16)]])
