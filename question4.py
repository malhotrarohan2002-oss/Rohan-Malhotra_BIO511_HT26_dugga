import random

results = {
    "Alice" :0,
    "Bob": 0,
    "Draw": 0

}
for game in range(20):
    alice = random.randint(1,6)
    bob = random.randint(1,6)

    if alice > bob:
        results["Alice"]+=1
    elif bob > alice:
        results["Bob"]+=1
    else:
        results["Draw"]+=1
print(results)
