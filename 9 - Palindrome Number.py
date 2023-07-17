from typing import List


def main():
    testVal = -121
    return testVal == ModIntXD(testVal)

    if str(testVal) == ReverseInt(testVal):
        return True
    else:
        return False


def ReverseInt(intNum: int) -> str:
    arr = []
    strVal = ""
    for i in (str(intNum)):
        arr.append(i)

    for index in range(len(arr)-1, -1, -1):
        strVal += arr[index]

    return strVal


def ReverseNumber(intNum: int):
    intResult = 0
    while True:
        if intResult == 0:
            intResult = intNum % 10
            intNum -= intNum % 10
            intNum = intNum/10
        else:
            if intNum > 0:
                intResult = intResult * 10
                intResult += intNum % 10
                intNum -= intNum % 10
                intNum = intNum/10
            else:
                return intResult


if __name__ == '__main__':
    main()
