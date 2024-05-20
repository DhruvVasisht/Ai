def water_jug_dfs(capacity_jug1, capacity_jug2, target):
    stack = [(0, 0)]
    visited = set()

    def dfs(jug1, jug2):
        if (jug1, jug2) in visited:
            return False
        visited.add((jug1, jug2))
        if jug1 == target or jug2 == target:
            print("Solution found:", (jug1, jug2))
            return True
        actions = [
            (capacity_jug1, jug2),
            (jug1, capacity_jug2),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, capacity_jug2 - jug2), jug2 + min(jug1, capacity_jug2 - jug2)),
            (jug1 + min(jug2, capacity_jug1 - jug1), jug2 - min(jug2, capacity_jug1 - jug1))
        ]
        for action in actions:
            if dfs(*action):
                return True
        return False

    if not dfs(0, 0):
        print("Solution not found.")

capacity_jug1 = int(input("Enter capacity of jug 1: "))
capacity_jug2 = int(input("Enter capacity of jug 2: "))
target_amount = int(input("Enter target amount: "))
water_jug_dfs(capacity_jug1, capacity_jug2, target_amount)