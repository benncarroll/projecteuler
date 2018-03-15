lim = int(input("Choose integer: "))
list_to_lim = list()
for i in range(1, lim + 1):
    list_to_lim.append(i)

# Sum of sqaures
sum_of_squares = 0

for i in list_to_lim:
    sum_of_squares += i**2

# Square of sum
square_of_sum = 0
sum_of_nums = 0

for i in list_to_lim:
    sum_of_nums += i
square_of_sum = sum_of_nums**2

difference = square_of_sum - sum_of_squares

print(difference)
