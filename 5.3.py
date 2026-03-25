import json
import random
import string
def c_password(length=12):
    A = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(A) for _ in range(length))
def c_user():
    N = ["DARTVAYDER"]
    name = random.choice(N)
    age = random.randint(18, 70)
    email = f"{name.lower()}@EXAMPLE.com"
    password = c_password()
    return {
        "name": name,
        "age": age,
        "email": email,
        "password": password
    }
user = c_user()
file_n = 'user.json'
with open(file_n, 'w') as f:
    json.dump(user, f, indent=4)
with open(file_n, 'r') as f:
    data = json.load(f)
print(json.dumps(data, indent=4))
