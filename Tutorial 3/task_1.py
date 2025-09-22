numb_1 = [[2, 4, 1, 5], [2, 10, 12], [14, 16, 20]]

for sub_list in numb_1:       
    for n in sub_list:    
        if n % 2 == 0:
            print(n, "is an even number.")
        else:
            print(n, "is an odd number.")
