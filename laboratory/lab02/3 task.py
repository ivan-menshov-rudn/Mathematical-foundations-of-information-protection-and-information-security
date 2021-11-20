# задаем 1 шифр цезаря
slovr = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# задаем пароль
pasword = str(input('Введите пароль: ')).lower()
# задаем фразу для шифрования
word = str(input('Введите фразу для шифрования: ')).lower()
# растягиваем пароль
k = (len(word) % len(pasword))
pasword_len = '' + pasword * (len(word) // len(pasword)) + pasword[:k]
print(word, pasword_len, sep='\n')
# создаем квадрат вижинера
slovr_visinera = []
slovr_i = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for i in range(len(slovr)):
    slovr_visinera.append(slovr_i)
    new = slovr_i[1:] + slovr_i[0]
    slovr_i = new
print("Квадрат вижинера:", slovr_visinera)
# шифруем сообщение
message = ''
for i in range(len(word)):
    f_index1 = slovr.find(word[i])
    f_index2 = slovr.find(pasword_len[i])
    message += slovr_visinera[f_index1][f_index2]
print(f'Защифрованное сообщение: {message}')
