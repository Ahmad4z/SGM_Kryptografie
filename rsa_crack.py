import time
import math

start_time = time.time()
# Um P und Q zu ermitteln wird hierbei als Beispiel die Probedivision genommen, aber hier kann man auch die Faktorisierungsmethode von Fermat nehmen.
def trial_factor(N):
    factors = {1, N}
    mvalue = int(math.sqrt(N))
    for i in range(2, mvalue + 1):
        if N % i == 0:
            factors.add(i)
            factors.add(N // i)

    return sorted(list(factors))

N = input("Bitte geben Sie N ein: ")
fn = N
fact = trial_factor(N)
print "Factors"
print "------"


def sub(num1, num2):
    return num1, num2


for N in fact:
    print str(int(N))

def extended_euclidean_algorithm(a, b):
    # This function implements the extended Euclidean algorithm and runs in 0(log b) in the worst case.
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse_of(n, p):
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd
    if gcd != 1:
        # Ether n is 0 or p is not a prime number
        raise ValueError(
            '{} has no multiplicative inverse'
            'modulo {}'.format(n, p))
    else:
        return x % p


e = input("Bitte geben Sie e ein: ")

p = fact[1]
q = fact[2]
cipher = input("Bitte geben Sie die verschluesselte Nachricht ein: ")
PHI = (p - 1) * (q - 1)

d = inverse_of(e, PHI)
print "The decription key is: ", d

plainTex = pow(cipher, d, fn)

print "The plaintext is: ", plainTex
print("--- %s seconds ---" % (time.time() - start_time))
