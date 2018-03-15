from datetime import datetime
import time


def mt():
    dt = datetime.now() - start_times[-1]
    ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
    return ms


start_times = list()

# Prime function can solve all primes under 1mil in under a second
# made by me woo


def checkPrime(a):
    # start_times.append(datetime.now())
    i = 1
    while i < (a - 1):
        i += 1
        if a % i == 0:
            return False
    return True


def test():
    d = input("Pick number: ")
    while d:
        print(checkPrime(int(d)))
        # print("Completed in", round(mt()/1000,2), "seconds")
        d = input("Pick number: ")


def findTwoFactors(a):
    i = 1
    while i < (a - 1):
        i += 1
        if a % i == 0:
            return [a // i, i]
    return [a]


l = list()


def findPrimeFactors(a):
    l = [[a, False]]
    nprimes = 0
    toAdd = list()
    while True:

        # Debug
        # print("l:     ",l)
        # print("toAdd: ", toAdd)
        # print("npri:  ", nprimes)

        # Add new splits from previous run
        for i in toAdd:
            l.append(i)
        toAdd = list()

        # Check if all are prime
        nprimes = 0
        for i in l:
            if checkPrime(i[0]):
                i[1] = True
                nprimes += 1
        if nprimes == len(l):
            break

        # Break down numbers
        for i in l:
            if i[1] != True:
                for j in findTwoFactors(i[0]):
                    toAdd.append([j, False])
                l.remove(i)

    s = ""
    s2 = ""
    r = "\n"
    if len(l) > 1:
        f = list()
        for i in sorted(l):
            f.append(str(i[0]))
        s = "|| The prime factors of " + str(a) + " are: " + str(", ".join(f)) + " ||"
        s2 = "\n|| " + str(" x ".join(f)) + " = " + str(a)
        s2 = s2 + " " * (len(s) - len(s2) - 1) + "||"
    else:
        s = "|| " + str(a) + " is a prime number."

    buffer = "-" * (max(len(s), len(s2)) - 1)

    return buffer + r + s + s2 + r + buffer


u = input("\n\nEnter number to find prime factors: ")
while u:
    try:
        print("\n" + findPrimeFactors(int(u)))
    except ValueError as e:
        print("Invalid entry. Please enter an integer.")

    u = input("\nEnter number to find prime factors: ")
