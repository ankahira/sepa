# Question one
# Loop in range 1 to 100
## Condition
## Print numbers divisible by 7 and 3
## Print numbers divisible by 7 but not 3
## Print numbers divisible by 3 but not 7
## Print odd numbers divisible by 7 but not 3
## Print the numbers divisible by sum of its digits
## Print numbers equal to the square of the sum of its digits

### Pseudo code
### Define range of numbers
### Single out all possible odd numbers to eliminate numbers like 14
### Check numbers divisible by 7 and 3
### Check numbers divisible by 7 but not 3 add to empty set
### Check numbers divisible by 3 but not 7 in main arrayand add to empty set
### Print odd numbers divisible by 7 but not 3
### Split digits the add sum of the digits
### Print numbers divisible by sum of digits
### Print numbers equal to the square of the sum of its digits


#### Code
# global variables
possible_numbers = range(1, 101)
odd_numbers = set()
numbers_divisible_by_3_and_7 = set()
numbers_divisible_by_7_but_not_3 = set()
odd_numbers_divisible_by_7_but_not_3 = set()


# conditions
for i in possible_numbers:
    if i % 7 == 0 and i % 3 == 0:
        numbers_divisible_by_3_and_7.add(i)
# print(numbers_divisible_by_3_and_7)

for i in possible_numbers:
    if (i % 7 == 0) and (i % 3 != 0):
        numbers_divisible_by_7_but_not_3.add(i)
# print(numbers_divisible_by_7_but_not_3)

for i in possible_numbers:
    if i % 2 != 0:
        odd_numbers.add(i)
        # print(odd_numbers)
        for i in odd_numbers:
            if (i % 7 == 0) and (i % 3 !=0):
                odd_numbers_divisible_by_7_but_not_3.add(i)
# print(odd_numbers_divisible_by_7_but_not_3)

## function to split items in a number

def getItems(number):
    digits = []
    # Loop the number as a string
    for i in str(number):
        digits.append(int(i))
    # print(digits)
        if i in len(digits)< 1:
            print(digits.index(i))

getItems(number = input("Enter 2 digit number: "))


