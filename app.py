import random

def generate_random_number():
    return random.randint(1, 100)
for _ in range(random.randint(1, 100)):
    print("Random number:", generate_random_number())