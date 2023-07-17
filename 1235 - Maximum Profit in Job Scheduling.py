from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        tasks = len(startTime)

        timeline = []
        # list all actions
        for i in range(tasks):
            # if time is equal, end must be sorted first.
            # we will need to update maximums first
            timeline.append([startTime[i], 'start', i])
            timeline.append([endTime[i], 'end', i])

        # sort by time
        timeline.sort()

        # get all possible routes
        profits = [0]*tasks

        previousMax = 0
        for time, action, index in timeline:

            if action == 'start':   # add profit to the route
                profits[index] = profit[index] + previousMax
            else:                   # if route is finished, check if it beat maximum
                previousMax = max(profits[index], previousMax)

        return previousMax


if __name__ == '__main__':
    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]

    objSolution = Solution()
    objSolution.jobScheduling(startTime, endTime, profit)
