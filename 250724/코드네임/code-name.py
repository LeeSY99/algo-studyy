class person:
    def __init__(self, cn, s):
        self.codename = cn
        self.score = s

people = []
for _ in range(5):
    codename, score = input().split()
    people.append(person(codename, int(score)))

people.sort(key = lambda x: x.score)
print(people[0].codename, people[0].score)