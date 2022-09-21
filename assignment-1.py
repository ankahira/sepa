def d_seven_and_three():
    acc = 1
    while acc <= 100:
        if (acc % 3 != 0) or (acc % 7 != 0):
            acc += 1
            continue
        elif (acc % 3 == 0) or (acc % 7 != 0):
            print(acc)
            acc += 1


def d_seven_not_three():
    acc = 1
    while acc <= 100:
        if acc % 7 != 0:
            acc += 1
            continue
        elif (acc % 3 != 0) or (acc % 7 == 0):
            print(acc)
            acc += 1


def d_seven_not_three_odd():
    acc = 1
    while acc <= 100:
        if (acc % 2 == 0) or acc % 7 != 0:
            acc += 1
            continue
        elif (acc % 3 != 0) or (acc % 7 == 0):
            print(acc)
            acc += 1


def d_sum():
    acc = 1
    sum = 0
    while acc <= 100:
        if acc <= 9:
            acc += 1
            continue
        else:
            str_num = str(acc)
            for s in str_num:
                sum += int(s)
            if acc % sum == 0:
                print(acc)
            acc += 1
            sum = 0


def e_square_sum():
    acc = 1
    sum = 0
    while acc <= 100:
        if acc <= 9:
            acc += 1
            continue
        else:
            str_num = str(acc)
            for s in str_num:
                sum += int(s)
            if(sum ** 2) == acc:
                print(acc)
            acc += 1
            sum = 0


def choices():
    choice = input("""
This program loops from 1 to 100. 
Choose between 1 - 5 to check the conditions:
1: Print the numbers that are divisible by 7 and 3
2: Print the numbers that are divisible by 7 but not 3
3: Print the ODD numbers divisible by 7 but not 3
4: Print the numbers that are divisible by the sum of its digits
5: Print the numbers that are equal to the square of the sum of its digits
Q: quit
    """).lower()
    program(choice)


def program(ch):
    while True:
        if ch == "1":
            d_seven_and_three()
            choices()
        elif ch == "2":
            d_seven_not_three()
            choices()
        elif ch == "3":
            d_seven_not_three_odd()
            choices()
        elif ch == "4":
            d_sum()
            choices()
        elif ch == "5":
            e_square_sum()
            choices()
        elif ch == "q":
            print("Program ended")
            quit()
        else:
            print("Please enter the correct option:")
            choices()


choices()

