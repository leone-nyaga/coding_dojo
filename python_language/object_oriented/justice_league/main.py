from justice_league import JusticeLeague

hero1 = JusticeLeague("Bruce", "Wayne", "Batman")
hero2 = JusticeLeague("Clark", "Kent", "Superman")
hero3 = JusticeLeague("Diana", "Prince", "Wonder Woman")

print("Total heroes:", JusticeLeague.totalHeroes)

print("\nLeague Roster:")
for hero in JusticeLeague.roster:
    print(hero)
