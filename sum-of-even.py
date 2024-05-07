integer_list = [2, 3,4, 6,7, 5]
def add_even(integers_list):
    even_numbers = []
    sum = 0

    # find all even values
    for i in integers_list:
        if i % 2 == 0:
            even_numbers.append(i)

    # sum all even values
    for i in even_numbers:
        sum += i
    return sum

print(add_even(integer_list))
