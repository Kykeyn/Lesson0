my_dict = {'Alex': 1996, 'Ivan': 1991, 'Kate': 2001}
print(my_dict)
print(my_dict.get('Ivan'))
print(my_dict.get('Boris'))
my_dict.update({'Anton': 1980,
                'Denis': 2005})
print(my_dict)
a = my_dict.pop('Alex')
print(a)
print(my_dict)
#
my_set = {1,2,2,'Sushi','Pizza',2.5,'Sushi',2.5,True,True,False}
print(my_set)
my_set.add(6)
my_set.add('Soda')
my_set.remove(1)
print(my_set)

