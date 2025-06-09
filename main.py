# cli interface
from algrothims import recursion

def StartMenu():
    print("welcome: select an option")
    option = int(input("1: recursion - factorial, merge sort, fibanacci"))
    if option  == 1:
        return RecursionOptions()
    else:
        print("error") # this shhould be an exception


# this i probaly the worst way of doing this but its for learning purposes only 
def RecursionOptions():
        number = int(input("enter a number to factor: "))
        if number:
            return print(recursion.factorial(n=number))
        else:
            print("eror")
        
        
 

if __name__== "__main__":
    StartMenu() 