from typing import List


def main():
    arr = ["abcdx", "yfrq", "fw", "kr", "zyrn"]
    print(maxLength(arr))


def maxLength(arr: List[str]) -> int:
    arr = ClearArrayFromUnnecessaryWords(arr)
    arr.sort(key=len)
    intResult1 = CheckArray(arr)
    arr.sort(key=len, reverse=True)
    intResult2 = CheckArray(arr)

    if intResult1 > intResult2:
        return intResult1
    else:
        return intResult2


def checkStringForDuplicateLetters(strWord: str) -> bool:
    tempLetters = [i for i in strWord]
    if len(tempLetters) == 1:
        return False

    for index in range(len(tempLetters)):
        for secondIndex in range(index + 1, len(tempLetters)):
            if tempLetters[index] == tempLetters[secondIndex]:
                return True

    return False


def ClearArrayFromUnnecessaryWords(arr: List[str]) -> List[str]:
    for word in arr:
        if checkStringForDuplicateLetters(word) == True:
            arr.pop(word)

    return arr


def CheckArray(arr: List[str]) -> int:
    strResult = ""
    dictResult = {}
    print(set(arr))
    for index in range(len(arr)):
        strTempString = arr[index]
        tempDict = {}

        for secondIndex in range(index + 1, len(arr)):
            dictResult = dict.fromkeys(strTempString, 0)
            tempDict = dict.fromkeys(arr[secondIndex], 0)

            for key in tempDict.keys():
                if key in dictResult:
                    continue

            strTempString += arr[secondIndex]

        if strResult == "":
            strResult = strTempString

        if len(strResult) < len(strTempString):
            strResult = strTempString

    return len(strResult)


if __name__ == '__main__':
    main()
