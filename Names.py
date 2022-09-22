
# function to search name with letters starting with a

def searchnamee():
    infile = open("names.txt", "r")
    for s in infile:
        if s.startswith("A"):
            print(s)


searchnamee()

#function  that reads a letter from user and prints name starting with the letter

def searchname():
    letter=input("enter the letter (s): ")
    names=[]
    for line in open("names.txt", 'r'):
        if line.lower().startswith(letter.lower()):
            words=line.split()
            names.append(words)
            
    print(names)



#function that searches age from user
    
def searchage():
    user_age=input("enter the age (s): ")
    ages=[]
    
    for line in open("names.txt", 'r'):
        if  str(user_age) in line:
            ages=line.split()
            ages.append(ages)
            
    print(ages)

#main function 

if __name__=="__main__":
    choice=int(input("press 1 to search for name or 2 to search for age: "))
    if choice==1:
        searchname()
    elif choice==2:
        searchage()
    else:
        print("invalid choice ")

#
