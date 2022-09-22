def search_name():
    IniFile = open ("names.txt","r")
    for s in IniFile:
        if s[0] == "A":
                    
            print(s)

search_name()

def search_name():
    letter = input("enter letter: ")
    IniFile = open ("names.txt","r")
    for s in IniFile:
        if s[0] == letter:
                    
            print(s)

search_name()    

# def search_name():
#     IniFile = open ("names.txt","r")
#     for s in IniFile:
    
                    
#             print(s[:-1])

# search_name()  


def search_age():
    age = input("enter number: ")
    IniFile = open ("names.txt","r")
    for s in IniFile:
        if s[0] == age:
                    
            print(s)

search_age()    

