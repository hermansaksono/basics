import random

# Configuration
total_fruits = 1000
apple_percent = 56.0
banana_percent = 44.0

# Creating the population
apples = [0] * int(apple_percent * total_fruits)  # Apple population
bananas = [1] * int(banana_percent * total_fruits)  # Banana population

apples_plus_bananas = apples + bananas
random.shuffle(apples_plus_bananas)


# Creating the samples
num_samples = 200
random_picks = [i for i in range(0, total_fruits)]
random.shuffle(random_picks)
samples_to_be_picked = random_picks[0:num_samples]


# Sampling the fruits
apples_sampled = 0
bananas_sampled = 0

for i in samples_to_be_picked:
    if apples_plus_bananas[i] == 0:
        apples_sampled += 1
    if apples_plus_bananas[i] == 1:
        bananas_sampled += 1

apple_samples_percent = round(apples_sampled/float(num_samples), 2)
banana_samples_percent = round(bananas_sampled/float(num_samples), 2)


# Output the result
print("Apples percent: " + str(apple_samples_percent) + "%")
print("Bananas percent: " + str(banana_samples_percent) + "%")
