l = [1, 2]
x = 0

while x < 4000000:
    x = l[-1] + l[-2]
    l.append(x)

print(l)
print(x)

sum = 0

for i in l:
    if (i % 2 == 0):
        sum += i
    else:
        continue

print(sum)
