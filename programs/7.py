# Using Sieve of Eratosthenes method

def checkPrime(a):
    # start_times.append(datetime.now())
    i = 1
    while i < (a - 1):
        i += 1
        if a % i == 0:
            return False
    return True

lim = int(input("Choose integer: "))
list_to_lim = list()
for i in range(2, lim + 1):
    list_to_lim.append(i)

prime_list = list()
for i in range(2, int(lim**0.5) + 1):
    if checkPrime(i):
        prime_list.append(i)

for prime in prime_list:
    for num in list_to_lim:
        if num % prime == 0 and num != prime:
            list_to_lim.remove(num)

# print("Primes:", len(list_to_lim))

if len(list_to_lim) >= 10000:
    print(list_to_lim[10000:1000])

# print(list_to_lim)
