def generate_7():
    for i in range(10,100):
        if '7' in str(i):
           yield i
for number in generate_7():
 print(number, end=' ')