#numb_1 = [[2, 4,1, 5], [2,10,12], [14, 16,20]]
#Check the even numbers in the list. The output should be like the following:
  #n is an even number.
  #n is an odd number

#and so on.

numb_1=[[2,4,1,5],[2,10,12],[14,16,20]]
for sublist in numb_1:
    for n in sublist:
        if n % 2 == 0:
            print(f"{n} is an even number")
        else:
            print(f"{n} is an odd number")





#even_numbers = [2,4,6,8]
#Write a try catch block to print the fifth indexed number. (hint: here the 5th index is invalid. 
#So we should get error for that. That's why you have write a try catch block)

even_numbers=[2,4,6,8]
    try:
        print(even_numbers[5])
    except IndexError as e:
        print("Error: Tried to access an index that does not exist")
       