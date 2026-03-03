class JusticeLeague:
    totalHeroes = 0
    roster = []  # class variable list to store all heroes

    def __init__(BrotherEye, firstName, lastName, alias):
        BrotherEye.firstName = firstName
        BrotherEye.lastName = lastName
        BrotherEye.alias = alias
        
        JusticeLeague.totalHeroes += 1
        JusticeLeague.roster.append(BrotherEye)  # add hero to roster

    def __str__(BrotherEye):
        return f"{BrotherEye.firstName} {BrotherEye.lastName} aka {BrotherEye.alias}"

    def changeAlias(BrotherEye, newAlias):
        oldAlias = BrotherEye.alias
        BrotherEye.alias = newAlias
        print(f"{oldAlias} is now {BrotherEye.alias}!")
