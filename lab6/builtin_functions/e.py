def all_true(tp):
    return all(tp)  #Функция all()принимает итерируемый объект и возвращает значение, Trueесли все элементы в итерируемом объекте равны True, и Falseв противном случае.

tp = (bool(i) for i in input().split())
print(all_true(tp))