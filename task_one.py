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
### Check numbers divisible by 7 but not 3
### Check numbers divisible by 3 but not 3
### Print odd numbers divisible by 7 but not 3
### Split digits the add sum of the digits
### Print numbers divisible by sum of digits
### Print numbers equal to the square of the sum of its digits


#### Code
# global variables
possible_numbers = range(1, 101)
odd_numbers = []
numbers_divisible_by_3_and_7 = []
numbers_divisible_by_7_but_not_3 = []

# conditions
for i in possible_numbers:
    if i % 2 != 0:
        # check for odd numbers
        odd_numbers.append(i)
        # print(odd_numbers)
    for i in odd_numbers:
        if i % 7 == 0 and i % 3 == 0:
            numbers_divisible_by_3_and_7.append(i)
            print(numbers_divisible_by_3_and_7)

