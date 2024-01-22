"""
                        Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

i.e. how many days it took to get next high temperature from current day
 & mention those days in current day's index

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]

"""


def dailyTemperature(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stack_temp, stack_index = stack.pop()

            res[stack_index] = i - stack_index
        stack.append([temp, i])
        print(stack)  # current pair of temperature and index we are at
    return res


temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperature(temperatures))