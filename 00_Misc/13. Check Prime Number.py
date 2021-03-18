#check if number is prime
i = int(input("Enter the number :"))

for j in range(2, i):
    if i % j == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

