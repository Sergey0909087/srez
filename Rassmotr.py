# # 1 zadanie
# print(input('Enter your str: ')[::-1])

# # 2 zadanie

# new_str = input('Enter your str: ')
# letters = 0
# numbers = 0
# for char in new_str:
#     if char.isalpha():
#         letters += 1
#     if char.isdigit():
#         numbers += 1
# print('letters:', letters, '\nNumbers:', numbers)

# 3 zadanie
# print(input('enter str: ').count(input('Enter symbol:  ')))

# some_str = input('Enter str: ')
# symbol = input('enter symbol: ')
# counter = 0
# for i in some_str:
#     if i == symbol:
#         counter += 1
# print('Количество подобных символов в строке:', counter)

# 4 zadanie
# print(input('Enter str: ').count(input('enter word: ')))

# 5 zadanie
some_str = input('Enter str: ')
find_word = input('Enter word to find: ')
replace_world = input('Enter word yo replace: ')
# new_str = ''
# find_index = some_str.find(find_word)
# if find_index != -1:
#     new_str += some_str[:find_index] + replace_world + some_str[find_index + len(find_word):]
# else:
#     print('Слово не найдено')
# print(new_str)

# print(some_str.replace(find_word, replace_world))
