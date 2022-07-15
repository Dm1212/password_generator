import random

low_case = list('abcdefghiklmnopqrstvwxyz')
upper_case = list('ABCDEFGHIKLMNOPQRSTUVWXYZ')
number = list('0123456789')
special_simbols = ['!','"','#','$','%','&','(',')','*','+','-','.','/',':',';','<','=','>','?','@','[','^','_','|','~']

password = []

z = int(input('Введите какое количество символов будет в пароле: '))

while len(password) < z:
    
    password.append(random.choice(low_case))
    password.append(random.choice(upper_case))
    password.append(random.choice(number))
    password.append(random.choice(special_simbols))

random.shuffle(password)
password = ''.join(password)
print(password)