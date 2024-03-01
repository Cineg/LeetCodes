class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:
        students: int = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                students += 1

        return students
