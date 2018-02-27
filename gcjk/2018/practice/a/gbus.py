def is_city_in_route(city_id, bus_start, bus_end):
    return bus_start <= city_id <= bus_end


def main():
    for T in range(1, int(input()) + 1):
        cities = []
        N = int(input())
        buses = input().split(' ')
        P = int(input())
        for p in range(P):
            city_id = int(input())
            passing_bus_count = 0
            for n in range(N):
                bus_start = int(buses[2 * n])
                bus_end = int(buses[2 * n + 1])
                if is_city_in_route(city_id, bus_start, bus_end):
                    passing_bus_count += 1
            cities.append(str(passing_bus_count))
        print('Case #{}: {}'.format(T, ' '.join(cities)))
        input()


if __name__ == '__main__':
    main()
