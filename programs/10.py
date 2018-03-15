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
    if i%2==0:
        continue
    else:
        list_to_lim.append(i)

prime_list = list()
for i in range(2, int(lim**0.5) + 1):
    if checkPrime(i):
        prime_list.append(i)

for prime in prime_list:
    for num in list_to_lim:
        if num != prime:
            if num % prime == 0 :
                list_to_lim.remove(num)
                # print(len(list_to_lim))
    # print(len(list_to_lim))

_sum = 2
for i in list_to_lim:
    _sum += i

f = open("10_output.txt", "w+")

# print(list_to_lim, file=f)
print("Sum of all primes below " + str(lim) + ":", _sum, file=f)
print("Sum of all primes below " + str(lim) + ":", _sum)
