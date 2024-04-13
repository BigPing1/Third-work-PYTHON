number = int(input("Enter a number to find out all even and odd numbers before it:\t"))

for i in range(2, number, 2):
    print(i)
print("These are all even\n")

for i in range(1, number, 2):
    print(i)
print("These are all odd")

if number % 2 == 0:
    print("\nYour number even")
else:
    print("\nYour number odd")