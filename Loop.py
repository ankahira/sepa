num_divisibly_by_3_7= []
nums_divisible_by_7_and_not_3 = []
odd_nums_divisible_by_7_and_not_3 = []
nums_divisible_by_sum_of_its_digits = []
num_equal_to_the_square_of_sum_of_its_digits = []

two_digit_and_above_numbers = []


# function for the sum of the digits of a number
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

    
#assign range
for i in range (1, 100):
    
    # numbers that are divisible by 7 and 3
    if (i % 7 == 0) and (i % 3 == 0):
       num_divisibly_by_3_7.append(i)
    
    # numbers that are divisible by 7 and not 3
    if (i % 7 == 0) and (i % 3 != 0):
        nums_divisible_by_7_and_not_3.append(i)
    
    # odd numbers that are divisible by 7 and not 3
    if (i % 2 != 0):
        if (i % 7 == 0) and (i % 3 != 0):
            odd_nums_divisible_by_7_and_not_3.append(i)
    
    # numbers that are divisible by sum of its digits
    if (i % getSum(i) == 0):
        nums_divisible_by_sum_of_its_digits.append(i)
    
    # numbers that are equal to the square of sum of its digits
    if (i == (getSum(i)*getSum(i))):
        num_equal_to_the_square_of_sum_of_its_digits.append(i)


print('for numbers in range 1 to 100,Numbers divisible by 7 and 3 : ' + str(num_divisibly_by_3_7))
print('for numbers in range 1 to 100,Numbers divisible by 7 and not 3: ' + str(nums_divisible_by_7_and_not_3))
print('for numbers in range 1 to 100,Odd numbers divisible by 7 and not 3: ' + str(odd_nums_divisible_by_7_and_not_3))
print('for numbers in range 1 to 100,Numbers divisible by sum of its digits: ' + str(nums_divisible_by_sum_of_its_digits))
print('for numbers in range 1 to 100,Numbers equal to the square of sum of its digits: ' + str(num_equal_to_the_square_of_sum_of_its_digits))
