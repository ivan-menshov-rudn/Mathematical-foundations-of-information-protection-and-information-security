# задаем пароль
password = str(input('Введите пароль:'))
# задаем фразу для шифрования
my_word = ''.join(str(input('Введите фразу:')).split())
# находим n
n = len(password)
# дополняем слово мусором по необходимости
if len(my_word)%n != 0:
    my_word += 'a'*(n-len(my_word) % n)
# находим порядок выписывания слов по паролю
password_sort = ''.join(sorted(password))
index_list = []
for i in range (len(password)):
    f_index = password.find(password_sort[i])
    index_list.append(f_index)
# записываем зашифрованное слово
new_word = ''
for i in index_list:
    for j in range(len(my_word)//n):
        new_word += my_word[j*n+i]
print(new_word)
