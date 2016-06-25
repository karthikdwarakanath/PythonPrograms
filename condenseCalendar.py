#[(1,3), (2,5)] gives [(1,5)]
#end time of one slot is less or equal to start time of another slot
#once condensed, the two slots can be replace with 1 slot.
#brute force would be to check every two slots and if condition is met,
#they can be replaced with 1 condensed slot
#edge cases end time of 1 == start time of second
#start and end time of one meeting is within the start and end times of another
#sort the array using the start times of the meetings
def condenseCal(inputList):
    mergedList = []
    sortedList = sorted(inputList, key=lambda x: x[0])
    mergedList.append(sortedList[0])
    for index, item in enumerate(sortedList[1:]):
        itemToMerge = mergedList.pop()
        if item[0] <= itemToMerge[1]:
            mergedList.append((itemToMerge[0], max(itemToMerge[1], item[1])))
        else:
            mergedList.append(itemToMerge)
            mergedList.append(item)
    return mergedList

print condenseCal([(1,2), (3,4), (4,10), (6,9), (2,5)])
print condenseCal([(1,3), (2,4)])
print condenseCal([(1,5), (5,6)])
