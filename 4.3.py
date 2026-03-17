def A(f):
    def B(*args, **kwargs):
        print(f"Функция calculate_area вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        r = f(*args, **kwargs)
        return r
    return B
@A
def calculate_area(length, width):
    return length * width
C = calculate_area(5, 15)
print(f"Площадь прямоугольника: {C}")
