pets = []


pet = {
    'animal type': 'parrot',
    'name': 'killer',
    'owner': 'mcqueen',
    'weight': 6,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'simba',
    'owner': 'scar',
    'weight': 20,
    'eats': 'cat food',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'chop',
    'owner': 'franklin',
    'weight': 37,
    'eats': 'dog food',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")