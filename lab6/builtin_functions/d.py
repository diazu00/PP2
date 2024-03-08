import time
import math

a = int(input())
b = int(input()) #Ожидайте заданное количество миллисекунд

time.sleep(b / 1000) #Ожидание заданного количество миллисекунд

result = math.sqrt(a)
print(result)