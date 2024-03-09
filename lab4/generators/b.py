def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())
even_nums = even_numbers(n)
print(*even_nums, sep=',')