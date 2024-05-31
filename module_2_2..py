first = int(input())
third = int(input())
second = int(input())

if first == third and second:
    print(0)
elif first == second or third == first:
    print(2)
else:
    print(0)
