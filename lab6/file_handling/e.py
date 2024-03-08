lst = [i for i in input().split()]
filename = 'example.txt'
# Открытие файла для записи в режиме "w" (write)
with open(filename , 'w') as f:
    # Запись списка в файл
    for item in lst:
        f.write("%s\n" % item)