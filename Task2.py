#search name
def searchName():
    names = []
    names_starting_with_A = []
    names_starting_with_user_input = []

    f = open("names.txt", "r")

    # store names in a list
    for each in f.read().splitlines():
        names.append(each)
    
    # # this search prints names that only starts with letter "A"
    # for name in names:
    #     if name[0] == 'A':
    #         names_starting_with_A.append(name)
    
    # print(names_starting_with_A)

    # this modified part first reads a letter from the user
    user_input = str(input('Enter text to search with: '))
    for name in names:
        if name[0:len(user_input)].upper() == user_input.upper():
            names_starting_with_user_input.append(name)

    # prints names starting with user input
    print('List of names starting with ' + user_input + ' are: ' + str(names_starting_with_user_input))
# searchName()

# function to extract an integer from a string
def integerFromString(yourString):
    integer = 0
    for word in yourString.split():
        if word.isdigit():
            integer = int(word)
    return integer

#search age
def searchAge():
    names = []
    names_where_age_is_5 = []
    names_where_age_is_user_input = []

    f = open("names.txt", "r")

    # store names in a list
    for each in f.read().splitlines():
        names.append(each)
    
    # # lines where age = 5
    # for name in names:
    #     if integerFromString(name) == 5:
    #         names_where_age_is_5.append(name)
    
    # print(names_where_age_is_5)

    # get lines where age = user input
    user_input = int(input('Enter search age: '))
    for name in names:
        if integerFromString(name) == user_input:
            names_where_age_is_user_input.append(name)
    
    print('Names where age = ' + str(user_input) + ' are: ' + str(names_where_age_is_user_input))
# searchAge()

def main():
    print('***You have two choices of search***')
    print('***1. Search by name****')
    print('***2. Search by age***')
    choice = input('***To proceed, Enter your search option below (Either 1 or 2): ')

    if choice == '1':
        searchName()
    elif choice == '2':
        searchAge()
    else:
        print('Warning! Invalid Choice!')

main()