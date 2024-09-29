my_dict = {'Nick': 1987, 'Leo': 1991, 'Anna': 1995}
my_dict.update({'Sara': 1989, 'Tom': 2001})
b = my_dict.pop('Anna')
print(my_dict)
print(my_dict.get('Leo'))
print(my_dict.get('Bill'))
print(b)

my_set = {5, 12, '10', True, 5, True}
my_set.discard(12)
my_set.add(False)
my_set.add(7)
print(my_set)