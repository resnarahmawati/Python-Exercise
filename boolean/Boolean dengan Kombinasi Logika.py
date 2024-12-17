# Kombinasi logika kompleks
def can_vote(age, is_registered):
    return age >= 18 and is_registered

print("Can vote (age 20, registered):", can_vote(20, True))
print("Can vote (age 16, registered):", can_vote(16, True))
