# Nested if statements
print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
type = input("Please type in one these types: 1-Scalene | 2-Equilateral | 3-Isosceles\n").lower()

if type=='scalene':
    print("All sides are different")
    question = input('\n Would you like to see a famous scalene? -yes OR -no ==> ').lower()
    if question == 'yes':
        print('Famous scalene triangle: 3, 4, 5')
elif type=='equilateral':
    print('All sides are equal')
elif type=='isosceles':
    print("Two sides are the same")
else:
    print("Not a valid answere")

print('Bye!')