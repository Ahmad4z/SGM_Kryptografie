import time
from math import ceil, sqrt
start_time = time.time()


def fermat_factors(N):
    z = int(ceil(sqrt(N)))
    if z * z == N:
        return [z, z]
    while True:
        x = z * z - N
        y = int(sqrt(x))
        if y * y == x:
            break
        else:
            z = z + 1
    return [z - y, z + y]


print(fermat_factors(187))
print("--- %s seconds ---" % (time.time() - start_time))
