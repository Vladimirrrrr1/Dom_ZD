
def get_multiplied_digits(namber):
    str_namber = str(namber)
    first = int(str_namber[0])
    if first == 0:
        first = 1
    if len(str_namber) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_namber[1:]))


result = get_multiplied_digits(input('chislo :'))
print(result)
