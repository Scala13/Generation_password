import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
zapros = int(input("Какая длина пароля вам нужна?"))
parol = ""
for i in range (zapros):
    parol += random.choice(symbols)
print("Ваш пароль:", parol)
