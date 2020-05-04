x=int(input("Enter a number:"))#User inputs number

for i in range(2,x-1): #loop from 2 to number before number entered
        if(x % i) == 0: #check if there are factors other than 1, itself
            print("Not a prime number.")
            break

if (x == 1):
    print("Not a prime number.")

else:
    print("A prime number.")



