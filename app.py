import random
import cowsay

def generate_random_number():
    return random.randint(1, 100)

for _ in range(random.randint(1, 100)):
    print("Generating random numbers")
    print("Random number:", generate_random_number())
cowsay.cow("Cow Test!")
cowsay.cow(generate_random_number())