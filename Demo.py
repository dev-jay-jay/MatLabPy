first = input('Enter the first number: ')
second = input('Enter the second number: ')
third = input('Enter the third number: ')

if first > second and first > third:
    print(first, ' is the greatest number')
elif second > first and second > third:
    print(second, ' is the greatest number')
else:
    print(third, ' is the greatest number')

if first < second and first < third:
    print(first, ' is the smallest number')
elif second < first and second < third:
    print(second, ' is the smallest number')
else:
    print(third, ' is the smallest number')
