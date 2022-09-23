


def searchname():
    Infile = open("names.txt","r")
    for s in Infile:
        print (s)

def searchname():
    Infile = open("names.txt","r")
    for s in Infile:
        print (s[:-1]) 

searchname()            

def search_name():
    IniFile = open ("names.txt","r")
    for s in IniFile:
        if s[0] == "A":
                    
            print(s)

search_name()

# def search_name():
#     letter = input("enter letter: ")
#     IniFile = open ("names.txt","r")
#     for s in IniFile:
#         if s[0] == letter:
                    
#             print(s)
# search_name()  

def search_name():
    letter = input("enter letter: ").upper()
    IniFile = open ("names.txt","r")
    for s in IniFile:
        if s[0] == letter:
                    
            print(s)

search_name()   




def search_age():
    age = input("enter number: ")
    IniFile = open ("names.txt","r")
    for s in IniFile:
        if s[-1] == age:
                    
            print(s)

search_age()  

 
        
def main():
    print("use this code to search: 1 - search by name, 2 - search by number")

    code = input("number")

    if code == 1: 
        print("search by name") 

    elif code == 2:
        print("search by number")  

    

if __name__ == '__main__':

    main()         


