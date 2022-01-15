import math
import time
start_time = time.time()


def trial_factor(N):
    factors = {1, N}
    mvalue = int(math.sqrt(N))
    for i in range(2, mvalue + 1):
        if N % i == 0:
            factors.add(i)
            factors.add(N // i)

    return sorted(list(factors))


N = input("Bitte geben Sie N ein: ")

print(trial_factor(N))
print("--- %s seconds ---" % (time.time() - start_time))
