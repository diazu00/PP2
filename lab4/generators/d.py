def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

x = int(input())
y = int(input())
for square in squares(x, y):
    print(square)