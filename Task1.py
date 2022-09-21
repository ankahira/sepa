numbers_divisible_by_7_and_3 = []
numbers_divisible_by_7_and_not_3 = []
odd_numbers_divisible_by_7_and_not_3 = []
numbers_divisible_by_sum_of_its_digits = []
numbers_equal_to_square_of_sum_of_its_digits = []

two_digit_and_above_numbers = []


# this function gets the sum of the digits of a number
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

    
# questions (a, b, and c)
for i in range (1, 101):
    # numbers divisible by 7 and 3
    if (i % 7 == 0) and (i % 3 == 0):
        numbers_divisible_by_7_and_3.append(i)
    
    # numbers divisible by 7 and not 3
    if (i % 7 == 0) and (i % 3 != 0):
        numbers_divisible_by_7_and_not_3.append(i)
    
    # odd numbers divisible by 7 and not 3
    if (i % 2 != 0):
        if (i % 7 == 0) and (i % 3 != 0):
            odd_numbers_divisible_by_7_and_not_3.append(i)
    
    # numbers divisible by sum of its digits
    if (i % getSum(i) == 0):
        numbers_divisible_by_sum_of_its_digits.append(i)
    
    # numbers equal to the square of sum of its digits
    if (i == (getSum(i)*getSum(i))):
        numbers_equal_to_square_of_sum_of_its_digits.append(i)


print('Numbers divisible by 7 and 3: ' + str(numbers_divisible_by_7_and_3))
print('Numbers divisible by 7 and not 3: ' + str(numbers_divisible_by_7_and_not_3))
print('Odd numbers divisible by 7 and not 3: ' + str(odd_numbers_divisible_by_7_and_not_3))
print('Numbers divisible by sum of its digits: ' + str(numbers_divisible_by_sum_of_its_digits))
print('Numbers equal to the square of sum of its digits: ' + str(numbers_equal_to_square_of_sum_of_its_digits))