from collections import deque

def waterjug(capacity_A, capacity_B, target):
    queue = deque()
    visited = set()
    initial_state = (0, 0)
    queue.append((initial_state, []))
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()
        a, b = current_state

    
        if a == target or b == target:
            print("Solution found!")
            print("Steps to reach the solution:")
            for step, (a_amount, b_amount) in zip(
                path, path_to_states(path, capacity_A, capacity_B)
            ):
                print(step, "- Jug A:", a_amount, "Jug B:", b_amount)
            return True


        actions = [
            ("Fill A", (capacity_A, b)),
            ("Fill B", (a, capacity_B)),
            ("Empty A", (0, b)),
            ("Empty B", (a, 0)),
            ("Pour A to B", (max(0, a - (capacity_B - b)), min(b + a, capacity_B))),
            ("Pour B to A", (min(a + b, capacity_A), max(0, b - (capacity_A - a)))),
        ]

        for action_name, next_state in actions:
            if next_state not in visited:
                queue.append((next_state, path + [action_name]))
                visited.add(next_state)

    
    print("No solution found!")
    return False


def path_to_states(path, capacity_A, capacity_B):
    states = [(0, 0)]
    for action in path:
        prev_a, prev_b = states[-1]
        if action == "Fill A":
            states.append((capacity_A, prev_b))
        elif action == "Fill B":
            states.append((prev_a, capacity_B))
        elif action == "Empty A":
            states.append((0, prev_b))
        elif action == "Empty B":
            states.append((prev_a, 0))
        elif action == "Pour A to B":
            a_to_b = min(prev_a, capacity_B - prev_b)
            states.append((prev_a - a_to_b, prev_b + a_to_b))
        elif action == "Pour B to A":
            b_to_a = min(prev_b, capacity_A - prev_a)
            states.append((prev_a + b_to_a, prev_b - b_to_a))
    return states[1:]


jug_A_capacity = int(input("Enter capacity of Jug A: "))
jug_B_capacity = int(input("Enter capacity of Jug B: "))
target_amount = int(input("Enter the target amount: "))

waterjug(jug_A_capacity, jug_B_capacity, target_amount)