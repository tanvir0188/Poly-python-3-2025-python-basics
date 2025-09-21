

numb_1=[[2,4,1,5],[2,10,12],[14,16,20]]
for sublist in numb_1:
    for n in sublist:
        if n % 2 == 0:
            print(f"{n} is an even number")
        else:
            print(f"{n} is an odd number")


 

even_numbers=[2,4,6,8]
    try:
        print(even_numbers[5])
    except IndexError as e:
        print("Error: Tried to access an index that does not exist")