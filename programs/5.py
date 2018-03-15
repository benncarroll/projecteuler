# Elapsed Time: 13 minutes and 39 seconds.
#
# 20: 232792560


import datetime

start = datetime.datetime.now()
x = 0
lim = int(input("Choose integer: "))
while True:
    x += 1
    dcount = 0
    for i in range(2, lim + 1):
        if x % i == 0:
            dcount += 1
    if dcount >= lim-1:
        print(x)
        break
    if x % 1000000 == 0:
        t = datetime.datetime.now() - start
        tim = divmod(t.days * 86400 + t.seconds, 60)
        form = str(tim[0]) + " minutes and " + str(tim[1]) + " seconds.\n"
        print("Milestone: " + str(x//1000000) + " mil")
        print("Elapsed Time:", form)
