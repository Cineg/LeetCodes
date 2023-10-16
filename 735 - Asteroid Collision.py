class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        i: int = 1

        if len(asteroids) == 0:
            return asteroids
        
        while True:
            if len(asteroids) == 0:
                return asteroids
            
            if i < 1:
                i = 1
            
            if i >= len(asteroids):
                break

            if asteroids[i-1] >= 0 and asteroids[i] < 0:
                if abs(asteroids[i-1]) > abs(asteroids[i]):
                    asteroids.pop(i)
                    i -= 1

                elif abs(asteroids[i-1]) < abs(asteroids[i]):
                    asteroids.pop(i-1)
                    i -= 1

                elif abs(asteroids[i-1]) == abs(asteroids[i]):
                    asteroids.pop(i)
                    asteroids.pop(i-1)
                    i -= 2

            else:
                i += 1

        return asteroids

def main() -> None:
    sol = Solution()
    print(sol.asteroidCollision([8,-8]))


if __name__ == "__main__":
    main()