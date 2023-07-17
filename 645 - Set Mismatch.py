from typing import List


def main():
    nums = [1, 5, 3, 2, 2, 7, 6, 4, 8, 9]
    print(findErrorNums(nums))


def findErrorNums(nums: List[int]) -> List[int]:
    dctList = {}
    nums.sort()
    foundDuplicate = 0
    for index in range(len(nums)):
        if nums[index] not in dctList:
            dctList[nums[index]] = index + 1 + foundDuplicate
        else:
            duplicateNum = nums[index]
            foundDuplicate = -1

    for index in range(len(nums)):
        if index + 1 not in dctList:
            missingNum = index + 1
            break

    return [duplicateNum, missingNum]


if __name__ == '__main__':
    main()
