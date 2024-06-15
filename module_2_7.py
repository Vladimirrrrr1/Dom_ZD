def print_params(a=1, b='vova', c=True):
    print(a, b, c)
values_list = [1, 'vova', True]
values_dict = {'a': 1, 'b': 'vova', 'c': True}
values_list_2 = [12.5, 'vova']
print_params()
print_params(2, 'denis', False)
print_params(b=25)
print_params(c=[1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)