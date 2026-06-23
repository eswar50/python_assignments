n= int(input("Enter a positive integer: "))

while n <= 0:

    print("please enter a positive integer.")
    n= int(input("Enter a positive integer: "))

total=0
num= 1

while num <= n:

    total += num
    num += 1

print("The sum of the first", total)