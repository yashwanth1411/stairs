def count_ways_to_climb_stairs(steps):
    if steps <= 2:
        return steps

    # Initialize an array to store the number of ways to reach each step
    ways = [0] * (steps + 1)

    # Base cases
    ways[1] = 1
    ways[2] = 2

    # Fill the array using a recurrence relation
    for i in range(3, steps + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[steps]


num_steps = int(input())

result = count_ways_to_climb_stairs(num_steps) 
  

print(result)
