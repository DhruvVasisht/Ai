def prop_logic(predicate):
    parts = [part.strip() for part in predicate.split('(')]
    predicate_name = parts[0]
    arguments = parts[1].strip(')').split(',')
    proposition = predicate_name + " " + " ".join([arg.strip()[0].upper() + str(index) for index, arg in enumerate(arguments)])

    return proposition

user_input = input("Enter a predicate (e.g., 'loves(student, coding)'): ")
proposition = prop_logic(user_input)
print("Predicate:", user_input)
print("Proposition:", proposition)
