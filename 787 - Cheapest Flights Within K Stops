from math import inf


class Solution:
    def findCheapestPrice(
        self,
        number_of_cities: int,
        flights: list[list[int]],
        src: int,
        dst: int,
        max_stops: int,
    ) -> int:
        visited: dict = self.get_visited(number_of_cities)
        cities_mapping: dict = self.map_cities(flights)

        stack: list[tuple[int, int]] = [(0, src)]
        stops: int = 0

        while stack and stops <= max_stops:
            stack_size: int = len(stack)
            for _ in range(stack_size):

                road, current_city = stack.pop(0)

                if current_city not in cities_mapping:
                    continue

                for dest in cities_mapping[current_city]:
                    cost: int = cities_mapping[current_city][dest] + road

                    if cost >= visited[dest]:
                        continue
                    visited[dest] = cost

                    stack.append((cost, dest))

            stops += 1

        return visited[dst] if visited[dst] != inf else -1

    def map_cities(self, flights: list[list[int]]) -> dict:
        mapping: dict = {}
        for flight in flights:
            city, destination, travel_cost = flight

            if city in mapping:
                mapping[city][destination] = travel_cost
            else:
                mapping[city] = {destination: travel_cost}

        return mapping

    def get_visited(self, number_of_cities: int) -> dict:
        dct: dict = {}
        for i in range(number_of_cities):
            dct[i] = inf

        return dct


def main() -> int:
    sol: Solution = Solution()
    number_of_cities: int = 5
    flights: list[list[int]] = [
        [0, 1, 5],
        [1, 2, 5],
        [0, 3, 2],
        [3, 1, 2],
        [1, 4, 1],
        [4, 2, 1],
    ]
    source_city: int = 0
    destination_city: int = 2
    max_stops: int = 2

    result: int = sol.findCheapestPrice(
        number_of_cities=number_of_cities,
        flights=flights,
        src=source_city,
        dst=destination_city,
        max_stops=max_stops,
    )
    print(f"result: {result}")
    return result


if __name__ == "__main__":
    main()
