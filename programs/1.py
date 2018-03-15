x = 0
l = list()
while (x < 1000):
    if (x % 3 == 0):
        l.append(x)
    elif (x % 5 == 0):
        l.append(x)
    x += 1

# print(l)
s = 0
for i in l:
    s += i

print(s)
