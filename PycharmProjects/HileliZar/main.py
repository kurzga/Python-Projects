import random

def biased_die_roll(probabilities):
    return random.choices(range(1, len(probabilities)+1), probabilities)[0]
biased_probabilities = [0.1, 0.1, 0.1, 0.1, 0.2, 0.4, 0]
result = biased_die_roll(biased_probabilities)
print(f"hileli zar sonucu: {result}")
