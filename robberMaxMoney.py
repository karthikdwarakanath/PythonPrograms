# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint
# stopping you from robbing each of them is that adjacent houses have security
#  system connected and it will automatically contact the police if two adjacent
#  houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each
#  house, determine the maximum amount of money you can rob tonight without
#  alerting the police.
#Array containing money in each house
#find the max money such that houses arent adjacent

#DP solution
#keep track of max of dp[i-1] and sum(dp[i-2], num[i-1]) and sum of
# house list = [4,9,6]
# n = 3

def maxMoney(houseList):
    if len(houseList) == 0:
        return 0
    if len(houseList) == 1:
        return houseList[0]
    if len(houseList) == 2:
        return max(houseList[0], houseList[1])
    dpMax = 0
    dp0 = 0
    dp1 = houseList[0]
    for i in range(2, len(houseList) + 1):
        dpMax = max(dp0 + houseList[i-1], dp1)
        dp0 = dp1
        dp1 = dpMax
    return dpMax

print maxMoney([4,9,6])
