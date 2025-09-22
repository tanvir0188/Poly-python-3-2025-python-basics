n=int(input("Enter the number 1-10 : "))
for i in range(1,n+1):
    print(f"{'even' if i%2==0 else 'odd'} --->>> {i}" )