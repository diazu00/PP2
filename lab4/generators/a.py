def square_generator(N):
    for i in range(N):
        yield i**2

x = int(input())
for square in square_generator(x):
    print(square)