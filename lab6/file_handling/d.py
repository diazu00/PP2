filename = "snake.txt"
with open(filename, "r") as file:
    cnt = 0
    for line in file:
        cnt += 1
print(cnt)