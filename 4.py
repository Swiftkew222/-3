from math import factorial
A = [x ** 2 for x in range(1, 11)]
print(A)
D = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
D1 = {d: X + 1 for X, d in enumerate(D)}
print(D1)
L = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
T = {l.lower() for l in L}
print(T)
N = [1, 3, 4, 87, 98, 15, 7, 4]
N1 = [n for n in N if n % 2 == 0]
print(N1)
F = {n: factorial(n) for n in range(1, 6)}
print(F)
