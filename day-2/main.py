import sys
from modules.EmployeeBot import *

#Author: Kyle Yap 

def main():

    #Check argumments passed
    if len(sys.argv) != 4:
        print('Usage:')
        print(f'{sys.argv[0]} <first_name> <last_name> <no_of_years>')
        quit();
    
    #Instantiate Class
    emp1=EmployeeBot(sys.argv[1],sys.argv[2],sys.argv[3])
    emp1.greet()

#Main method good convention
if __name__ == '__main__':
    main()
else:
    quit()