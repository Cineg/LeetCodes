class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()

        res: int = 0
        idx: int = 0

        while idx < len(students):
            res += abs(seats[idx] - students[idx])
            idx += 1

        return res
