n = int(input("Enter a Number: "))

while n >= 0:
    n += n-1
    print(n)
    n -= 1
print(n)