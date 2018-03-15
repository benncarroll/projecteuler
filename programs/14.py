l = list()
r = dict()

lim = 1000000

for i in range(lim - lim//4, lim + 1):
    if i%2==0:
        continue
    else:
        l.append(i)

for num in l:
    chain = list()
    n = num
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        chain.append(n)
    r[num] = chain

longest = [1,1]
for entry in r:
    if len(r[entry]) > longest[1]:
        longest[0] = entry
        longest[1] = len(r[entry])

print(longest)
