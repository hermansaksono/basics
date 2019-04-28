import random

total_fruits = 1000
apple_percent = 56.0
banana_percent = 44.0

apples = [0] * int(apple_percent * total_fruits)
bananas = [1] * int(banana_percent * total_fruits)

apples_plus_bananas = apples + bananas
random.shuffle(apples_plus_bananas)

random_picks = [i for i in range(0, total_fruits)]
random.shuffle(random_picks)

num_samples = 200

apples_sampled = 0
bananas_sampled = 0

for i in random_picks[0:num_samples]:
    if apples_plus_bananas[i] == 0:
        apples_sampled += 1
    if apples_plus_bananas[i] == 1:
        bananas_sampled += 1

apple_samples_percent = round(apples_sampled/float(num_samples), 2)
banana_samples_percent = round(bananas_sampled/float(num_samples), 2)

print("Apples percent: " + str(apple_samples_percent) + "%")
print("Bananas percent: " + str(banana_samples_percent) + "%")