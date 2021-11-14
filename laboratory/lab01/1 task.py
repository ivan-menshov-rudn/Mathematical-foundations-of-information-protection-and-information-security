slovr = 'авгдеёжзийклмнопрстуфхцчшщъыьэюя '
k = int(input('Введите ключ шифра: '))
user_string = str(input('Введите строку: '))
new_string = ''
for i in range(len(user_string)):
    f_index = slovr.find(user_string[i])
    new_string += slovr[(k+f_index) % len(slovr)]
print(f'Зашивровка:{new_string}')

new_string1 = ''
for i in range(len(new_string)):
    f_index = slovr.find(new_string[i])
    new_string1 += slovr[(f_index-k) % len(slovr)]
print(f'Расшивровка:{new_string1}')