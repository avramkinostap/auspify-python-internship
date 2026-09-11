import string
import random

print("Write password length")
length = int(input())
print("How many passwords to generate?")
times = int(input())

all_characters = string.ascii_letters + string.digits + string.punctuation


for j in range(times):
    password = ""
    for i in range(length):
        password += random.choice(all_characters)

    print(password)