def searchname():
    infile = open("./names.txt", "r")
    input_char = input('Add the first 2 characters for searching the name: ')
    if len(input_char) < 2 or len(input_char) > 2:
        print('Please only input 2 characters')
        searchname()
    elif len(input_char) == 2:
        char = input_char[0].upper() + input_char[1].lower()

    for s in infile:
        if s[0:2] == char:
            print(s)
    infile.close()
    main()


def searchAge():
    try:
        input_age = int(input('Add the age: '))
    except ValueError:
        print("Please enter a number!")
        searchAge()
    children = []
    infile = open("./names.txt", "r")
    for s in infile:
        children.append(s.replace('\n', ''))
    for child in children:
        if str(input_age) in child:
            print(child)
    infile.close()
    main()


def main():
    choice = input("""
1. Search with name
2. Search with age
Q. quit
    """).lower()
    while True:
        if choice == '1':
            searchname()
        elif choice == '2':
            searchAge()
        elif choice == 'q':
            quit()
        else:
            print('Please enter the correct choice')


main()

