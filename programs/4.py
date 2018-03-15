import time
from pprint import pprint

plist = list()

for int1 in range(900, 1000):
    for int2 in range(900, 1000):

        product = int1 * int2
        # product = 880088
        sproduct = str(product)
        plength = len(sproduct)
        l = list()

        rproduct = ""
        for i in range(len(sproduct)-1, -1, -1):
            rproduct += sproduct[i]

        if rproduct == sproduct:
            plist.append(product)
        #
        # print(l)
        # print(plist)
        # print("Loop No.", i+j)


        # time.sleep(1)



pprint(plist)
