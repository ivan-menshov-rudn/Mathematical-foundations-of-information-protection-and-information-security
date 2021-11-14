slovr ='абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
mix_slovr = slovr[::-1]
user_string = str(input('Введите строку: '))
new_string = ''
for i in range(len(user_string)):
    f_index = slovr.find(user_string[i])
    new_string += mix_slovr[f_index]
print('Зашивровка:', new_string)
new_string1 = ''
for i in range(len(new_string)):
    f_index = mix_slovr.find(new_string[i])
    new_string1 += slovr[f_index]
print('Расшифровка ', new_string1)
