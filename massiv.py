#len() # vozraschaet kolichestvo elementov interiruemogo obekta
# my_list = [1, 2, 3, 4, 5, 'string' ]
# if 'string' in my_list:
#     print('YES')

# for i in my_list:
#     print(i)

# print(type(my_list))

# int()
# float()
# str()

#sposob sozdaniya spiskov
# category = ['Drama', 'Comedy', 'Horor', 'Fantasy', 12345, 12345, 124.345, [1, 2, 3, 4, 5, [12354, 'hello']]]
# courses = list(('Math', 'Algoritms', 'Databases'))
# print(category)
# print(courses)

# #Sozdanie pystogo spiska
# list_1 = []
# list_2 = list()
# print(list_1)
# print(list_2)

# print(category)
# print(category[-1])
# print(category[-1][-1])
# print(category[-1][-1][1][2])

some_str = 'hello world my neme is oleg'
print(some_str)
new_list = list(list(some_str))
new_list[5] = 'aboba'
print(new_list)
print(' '.join(new_list)) #obedinit elements spiska v stroky
print(some_str.split()) # razbit stroku na otdelnie elenets - slova
