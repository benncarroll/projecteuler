from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))


def findFactors(num):
    n = int(num)
    l = list()
    if n % 2 == 0:
        for i in range(1,n+1):
            if n % i == 0:
                l.append(i)
    else:
        for i in range(1, n+1, 2):
            if n % i == 0:
                l.append(i)
    return l

def generateTriangleNum(up_to):
    n = 0
    for i in range(1, up_to+1):
        n+=i
    return n

divisor_list = list()
tri_num_count = 12372
tri_num = 0

while len(divisor_list) <= 500:
    tri_num_count += 1
    tri_num = generateTriangleNum(tri_num_count)
    if not tri_num % 10 == 0:
        continue
    divisor_list = factors(tri_num)
    print(tri_num, " "*(15-len(str(tri_num))), len(divisor_list), " "*(5-len(str(len(divisor_list)))), tri_num_count)

print(tri_num, len(divisor_list))
