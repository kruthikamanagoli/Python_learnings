num = int(input('Enter the number: '))
first = 0
second = 1
for i in range(num):
    print(first)
    x = first
    first = second
    second = x + second