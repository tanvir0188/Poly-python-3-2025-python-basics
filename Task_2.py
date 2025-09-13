mark=int(input('Enter the mark : '))
attendance=int(input('Enter Attendnce : '))

if mark>=90:
    print('Eligible')
elif mark >=80 and attendance>=75 :
    print('Eligible')

else:
    print('NOT Eligible')