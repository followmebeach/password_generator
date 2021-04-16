import random

print('Генератор паролей | Trofimchuk27')
while True:
    chars = list('+-/*!&$#?=w@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    length = int(input('Укажите длину пароля?'+ "\n"))
    random.shuffle(chars)
    pasw = ''.join([random.choice(chars) for x in range(length)])
    print(f'Ваш сгенерированный пароль - {pasw}')
