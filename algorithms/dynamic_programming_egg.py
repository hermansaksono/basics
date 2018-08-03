def get_min_num_trials(num_eggs, num_floors):
    if num_floors <= 1:
        return 1
    elif num_eggs <= 1:
        return num_floors
    else:
        min_trials = num_floors
        for i in range(1, num_floors + 1):                                   # O(k)
            egg_break = get_min_num_trials(num_eggs - 1, i - 1)              # O(n - 1 * k - c)
            egg_doesnt_break = get_min_num_trials(num_eggs, num_floors - i)  # O(n )
            num_trials = 1 + max(egg_break, egg_doesnt_break)
            min_trials = min(min_trials, num_trials)
        return min_trials


n_eggs = 2
k_floors = 100
print(get_min_num_trials(n_eggs, k_floors))

