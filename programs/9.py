_sum = 1000
_limit = 1000

for a in range(1,_limit+1):
    for b in range(1,_limit+1):
        if a < b:
            both_squared = a**2 + b**2
            c = (both_squared**0.5)
            if (c.is_integer()):
                if ((a+b+c) == _sum):
                    print("Formula:", str(a)+"²", "+", str(b)+"²", "=", str(c)+"²")
                    print("Product:", str(a*b*c))
