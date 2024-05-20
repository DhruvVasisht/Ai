from collections import deque

def bfs(start_state, jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        curr_state, path = queue.popleft()
        jug1, jug2 = curr_state

        if jug1 == target or jug2 == target:
            return path + [curr_state]

        visited.add(curr_state)

        actions = [
            (jug1_capacity, jug2),
            (jug1, jug2_capacity),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))
        ]

        for action in actions:
            new_state = action
            if new_state not in visited:
                queue.append((new_state, path + [curr_state]))

    return None

def water_jug_bfs():
    jug1_capacity = int(input("Enter the capacity of jug 1: "))
    jug2_capacity = int(input("Enter the capacity of jug 2: "))
    target_amount = int(input("Enter the target amount of water: "))

    start_state = (0, 0)

    result = bfs(start_state, jug1_capacity, jug2_capacity, target_amount)
    if result:
        print("Target amount can be achieved!")
        print("Steps to achieve the target:")
        for state in result:
            print(state)
    else:
        print("Target amount cannot be achieved.")

if __name__ == "__main__":
    water_jug_bfs()