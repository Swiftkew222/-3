import random
import string
from pathlib import Path
def g_name(length=8):
    A = string.ascii_letters + string.digits
    name = ''.join(random.choice(A) for _ in range(length))
    return name + '.txt'
def c_files(B, count=10):
    B1 = Path(B)
    B1.mkdir(A1=True, B2=True)
    l_files = []
    for _ in range(count):
        name = g_name()
        file_path = B1 / name
        file_path.touch()
        l_files.append(str(file_path.resolve()))
    return l_files
B_name = 'random_files'
files = c_files(B_name)
for file in files:
    print(file)
