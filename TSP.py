def tsp(c):
    global cost
    minimum = float('inf')
    nearest_city = float('inf')
    for count in range(limit):
        if matrix[c][count] != 0 and visited_cities[count] == 0:
            if matrix[c][count] < minimum:
                minimum = matrix[c][count]
                nearest_city = count
                
    if minimum != float('inf'):
        cost += minimum 
    return nearest_city

def minimum_cost(city):
    global cost
    visited_cities[city] = 1
    print(city + 1, end=' ')
    nearest_city = tsp(city)
    if nearest_city == float('inf'):
        nearest_city = 0
        print(nearest_city + 1, end='')
        cost = cost + matrix[city][nearest_city]
        return
    minimum_cost(nearest_city)


limit = int(input("Enter Total Number of elements:\t"))
matrix = []
visited_cities = [0] * limit 
cost = 0

print("\nEnter Cost Matrix")
for i in range(limit):
    print(f"\nEnter {limit} Elements in Row[{i + 1}]")
    row = list(map(int, input().split()))
    matrix.append(row)

print("\nEntered Cost Matrix")
for i in range(limit):
    print()
    for j in range(limit):
        print(matrix[i][j], end=' ')

print("\n\nPath:\t", end='')
minimum_cost(0)
print("\n\nMinimum Cost: \t",cost)