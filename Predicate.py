def prep_logic(predicate):
    parts = [part.strip() for part in predicate.split('(')]
    predicate_name = parts[0]
    arguments = parts[1].strip(')').split(',')
    proposition = predicate_name + " " + " ".join([arg.strip()[0].upper() + str(index) for index, arg in enumerate(arguments)])

    return proposition
predicate = "loves(student, coding)"
proposition = prep_logic(predicate)
print("Predicate:", predicate)
print("Proposition:", proposition)