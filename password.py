import random
chars="abcdefghijklmnopqrstuvwyz0123456789ABCDEFGHIJKLMNOPQRSTUVWYZ"
length=int(input("enter the length:"))
password=""

for a in range(length):
    password+=random.choice(chars)
print(password)
