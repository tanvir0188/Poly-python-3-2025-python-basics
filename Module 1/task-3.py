numb_1 = [[2, 4, 1, 5], [2, 10, 12], [14, 16, 20]]

for sublist in numb_1:
    for n in sublist:
        print(f"{n} is an even number" if n % 2 == 0 else f"{n} is an odd number")
