def count_down(n):
    while n >= 0:
        yield n
        n -= 1

x = int(input())
for num in count_down(x):
    print(num)