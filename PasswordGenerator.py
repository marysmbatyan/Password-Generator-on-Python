#password generation function
def generate_password(length, chars):
    password = random.sample(chars, length)
    return password

#start
import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

#properties
count = int(input('Ведите количество генерируемых паролей:  '))
leng = int(input('Введите длину одного пароля:  '))
add_digits = input('Включать ли цифры? (yes / no):  ')
add_upper = input('Включать ли прописные буквы? (yes / no):  ')
add_lower = input('Включать ли строчные буквы? (yes / no):  ')
add_punctuation = input('Включать ли символы? (yes / no):  ')
exclude = input('Исключать ли неоднозначные символы il1Lo0O? (yes / no):  ')

if add_digits == 'yes':
    chars += digits
if add_upper == 'yes':
    chars += uppercase_letters
if add_lower == 'yes':
    chars += lowercase_letters
if add_punctuation == 'yes':
    chars += punctuation
if exclude == 'yes':
    for i in exclude:
        chars.replace(i, '')

#get password
for i in range(1, count + 1):
    print('Password', i, ': ', ''.join(generate_password(leng, chars)))
